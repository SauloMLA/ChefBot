🍽️ Meal Plan Generator
A Python desktop application that generates personalized weekly meal plans based on your nutritional needs, available ingredients, and dietary preferences using AI.

https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/OpenAI-GPT--4o--mini-green
https://img.shields.io/badge/GUI-Tkinter-orange

📋 Table of Contents
Features

Requirements

Installation

Configuration

Usage

How It Works

Troubleshooting

✨ Features
Calorie Calculation: Automatically calculates your daily calorie needs based on weight, height, age, sex, and activity level

AI-Powered Meal Plans: Generates weekly meal plans using OpenAI's GPT-4o-mini model

PDF Export: Automatically creates and opens a PDF version of your meal plan

Ingredient-Based: Creates recipes using ingredients you already have

Customizable: Accommodates dietary preferences and restrictions

User-Friendly GUI: Dark-themed interface built with Tkinter

🛠 Requirements
Python 3.8 or higher

OpenAI API key

Internet connection (for AI functionality)

📥 Installation
Step 1: Clone or Download the Repository
bash
# If using Git
git clone https://github.com/your-username/meal-plan-generator.git
cd meal-plan-generator

# Or simply download the script file to your computer
Step 2: Install Required Packages
bash
pip install openai tkinter reportlab python-dotenv
Note: tkinter usually comes pre-installed with Python. If you get errors, install it separately:

Windows: Usually included

Mac: brew install python-tk

Linux: sudo apt-get install python3-tk

🔧 Configuration
Step 1: Get Your OpenAI API Key
Go to OpenAI Platform

Sign up or log in to your account

Navigate to "API Keys"

Click "Create new secret key"

Copy your API key

Step 2: Set Up Environment Variables
Option A: Using .env file (Recommended)

Create a file named .env in the same directory as the script

Add your API key:

text
OPENAI_API_KEY=your_actual_api_key_here
Modify the code to use environment variables:

python
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
Option B: Direct replacement (Temporary)
Replace the API key in the code:

python
client = OpenAI(api_key="your_actual_api_key_here")  # Replace with your key
🚀 Usage
Running the Application
Navigate to the script directory:

bash
cd path/to/your/script
Run the script:

bash
python meal_plan_generator.py
Using the Application
Enter Your Personal Information:

Weight (in kilograms)

Height (in centimeters)

Age

Sex (Male/Female)

Activity Level (Sedentary/Light/Moderate/Intense)

Provide Available Ingredients:

List ingredients you have, separated by commas

Example: "chicken, rice, tomatoes, onions, pasta"

Specify Preferences/Restrictions:

Dietary preferences, allergies, or restrictions

Example: "vegetarian, no nuts, lactose intolerant"

Generate Meal Plan:

Click the "Generate Meal Plan" button

Wait for the AI to create your personalized weekly plan

The PDF will automatically open when ready

🧠 How It Works
Calorie Calculation
The app uses the Mifflin-St Jeor Equation to calculate your Basal Metabolic Rate (BMR), then adjusts for activity level:

Male: BMR = 88.362 + (13.397 × weight) + (4.799 × height) - (5.677 × age)

Female: BMR = 447.593 + (9.247 × weight) + (3.098 × height) - (4.330 × age)

AI Meal Generation
The application sends a structured prompt to OpenAI's GPT-4o-mini model including:

Your calculated calorie needs

Available ingredients

Dietary preferences

Request for simple recipes (15 minutes or less)

Output Includes
7-day meal plan (breakfast, lunch, dinner)

Simple, quick recipes

Shopping list for missing ingredients

PDF export with formatted layout

🐛 Troubleshooting
Common Issues
"API Key not found" Error

Ensure your API key is correctly set in the .env file or code

Verify the API key has sufficient credits

PDF won't open

Check if you have a PDF reader installed

The PDF is saved in the same directory as the script

Application crashes

Ensure all required packages are installed

Check your internet connection for AI features

GUI doesn't appear

Verify tkinter is properly installed

Try running with python3 instead of python

Getting Help
If you encounter issues:

Check that all dependencies are installed

Verify your OpenAI API key is valid and has credits

Ensure you're using Python 3.8 or higher

📝 Notes
Internet Required: The AI meal generation requires an active internet connection

API Costs: Using OpenAI's API may incur costs based on usage

Nutritional Accuracy: Calorie calculations are estimates; consult a professional for medical advice

Recipe Quality: Recipe quality depends on the specificity of your inputs

🔒 Security
Never commit API keys to version control

Use environment variables for sensitive information

Regularly rotate your API keys

Enjoy your personalized meal planning! 🍎🥦🍗