import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, font
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from openai import OpenAI

# --- OpenAI Client ---
client = OpenAI(api_key="#####") # Replace ##### with your actual API key

# --- Functions ---
def calculate_calories(weight, height, age, sex="male", activity="light"):
    if weight <= 0 or height <= 0 or age <= 0:
        raise ValueError("Weight, height, and age must be positive numbers.")
    if sex.lower() == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    factors = {"sedentary": 1.2, "light": 1.375, "moderate": 1.55, "intense": 1.725}
    return round(bmr * factors.get(activity.lower(), 1.2), 0)

def generate_menu(calories, ingredients, preferences):
    prompt = f"""
    I am a college student living alone.
    I need a weekly meal plan with simple recipes (max 15 min each).
    I have these ingredients: {ingredients}.
    My daily target is {calories} kcal.
    My preferences/restrictions: {preferences}.
    Return 7 days with breakfast, lunch, dinner, and a shopping list.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

def export_pdf(text, filename="meal_plan.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    story = []

    for paragraph in text.split("\n"):
        if paragraph.strip():
            story.append(Paragraph(paragraph, styles["Normal"]))
            story.append(Spacer(1, 12))
    doc.build(story)

    # Open PDF automatically
    if os.name == "posix":  # Mac / Linux
        os.system(f"open {filename}")
    elif os.name == "nt":  # Windows
        os.startfile(filename)

def validate_fields():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        if weight <= 0 or height <= 0 or age <= 0:
            return False
        if not ingredients_text.get("1.0", tk.END).strip():
            return False
        if not preferences_text.get("1.0", tk.END).strip():
            return False
    except:
        return False
    return True

def on_generate():
    if not validate_fields():
        messagebox.showwarning("Incomplete/Invalid Data", "Please fill all fields with valid information.")
        return

    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = int(age_entry.get())
    sex = sex_var.get()
    activity = activity_var.get()
    ingredients = ingredients_text.get("1.0", tk.END).strip()
    preferences = preferences_text.get("1.0", tk.END).strip()

    calories = calculate_calories(weight, height, age, sex, activity)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Daily target calories: {calories} kcal\n\nGenerating menu...")
    output_text.config(state=tk.DISABLED)
    window.update()

    try:
        menu = generate_menu(calories, ingredients, preferences)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, menu)
        output_text.config(state=tk.DISABLED)
        export_pdf(menu)
        messagebox.showinfo("Success", "PDF generated and opened!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- GUI ---
window = tk.Tk()
window.title("Meal Plan Generator")
window.geometry("820x780")
window.configure(bg="#1e1e1e")  # Dark background

# Fonts
title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
text_font = font.Font(family="Helvetica", size=11)

frame = tk.Frame(window, bg="#1e1e1e", padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

def create_label(master, text, row, col):
    lbl = tk.Label(master, text=text, font=label_font, bg="#1e1e1e", fg="#ffffff")
    lbl.grid(row=row, column=col, sticky="w", pady=5)
    return lbl

def create_entry(master, row, col):
    entry = tk.Entry(master, font=text_font, relief="solid", bd=1, bg="#2e2e2e", fg="#ffffff", insertbackground="white")
    entry.grid(row=row, column=col, sticky="ew", pady=5)
    return entry

weight_entry = create_entry(frame, 0, 1)
create_label(frame, "Weight (kg):", 0, 0)

height_entry = create_entry(frame, 1, 1)
create_label(frame, "Height (cm):", 1, 0)

age_entry = create_entry(frame, 2, 1)
create_label(frame, "Age:", 2, 0)

# Sex
sex_var = tk.StringVar(value="male")
sex_menu = tk.OptionMenu(frame, sex_var, "male", "female")
sex_menu.config(font=text_font, bg="#2e2e2e", fg="#ffffff", relief="solid", bd=1)
sex_menu["menu"].config(bg="#2e2e2e", fg="#ffffff")
sex_menu.grid(row=3, column=1, sticky="ew", pady=5)
create_label(frame, "Sex:", 3, 0)

# Activity
activity_var = tk.StringVar(value="light")
activity_menu = tk.OptionMenu(frame, activity_var, "sedentary", "light", "moderate", "intense")
activity_menu.config(font=text_font, bg="#2e2e2e", fg="#ffffff", relief="solid", bd=1)
activity_menu["menu"].config(bg="#2e2e2e", fg="#ffffff")
activity_menu.grid(row=4, column=1, sticky="ew", pady=5)
create_label(frame, "Activity Level:", 4, 0)

# Ingredients
create_label(frame, "Ingredients (comma separated):", 5, 0)
ingredients_text = scrolledtext.ScrolledText(frame, width=50, height=6, font=text_font, bg="#2e2e2e", fg="#ffffff", relief="solid", bd=1, insertbackground="white")
ingredients_text.grid(row=5, column=1, sticky="ew", pady=5)

# Preferences / Restrictions
create_label(frame, "Preferences / Restrictions:", 6, 0)
preferences_text = scrolledtext.ScrolledText(frame, width=50, height=6, font=text_font, bg="#2e2e2e", fg="#ffffff", relief="solid", bd=1, insertbackground="white")
preferences_text.grid(row=6, column=1, sticky="ew", pady=5)

# Output
create_label(frame, "Generated Meal Plan:", 7, 0)
output_text = scrolledtext.ScrolledText(frame, width=90, height=20, font=text_font, bg="#2a2a2a", fg="#ffffff", relief="solid", bd=1, state=tk.DISABLED)
output_text.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=10)

# Generate Button
def on_enter(e):
    generate_btn['bg'] = '#ffa500'
def on_leave(e):
    generate_btn['bg'] = '#ffb84d'

generate_btn = tk.Button(frame, text="Generate Meal Plan", font=title_font, bg="#ffb84d", fg="#000000",
                         activebackground="#ffa500", activeforeground="#000000", command=on_generate,
                         relief="flat", bd=2)
generate_btn.grid(row=8, column=0, columnspan=2, pady=15, ipadx=15, ipady=8)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

# Make columns expand
frame.columnconfigure(1, weight=1)
frame.rowconfigure(7, weight=1)

window.mainloop()
