import streamlit as st
import os
from google import genai
from google.genai import types

st.set_page_config(page_title="AI Cooking To-Do List", page_icon="🍳")

st.title("🍳 AI Cooking To-Do List")
st.write("Generate a personal cooking to-do list based on your day!")

# Initialize the GenAI client
# Assumes GEMINI_API_KEY is set in the environment variables
try:
    client = genai.Client()
except Exception as e:
    st.error(f"Error initializing client. Make sure GEMINI_API_KEY is set. Error: {e}")
    st.stop()

day_description = st.text_area("Describe your day", placeholder="e.g., I have back-to-back meetings until 5 PM, then I'm going to the gym for an hour. I want something healthy but quick.")
budget = st.number_input("Daily budget limit (₹)", min_value=0.0, value=2000.0, step=50.0)

system_instruction = """You are a helpful AI cooking assistant designed to provide an effortless, structured meal planning flow.
You must strictly output your response in exactly the following four sections, using these exact headings:

## 1. Breakfast/Lunch/Dinner plan
Provide a meal plan for breakfast, lunch, and dinner based on the user's schedule. Include the expected active prep time for each meal.

## 2. Grocery list
Provide a grocery list for the meals. 
CRITICAL: Format this list strictly as Markdown checkboxes (e.g., `- [ ] Item name - ₹X.XX`). Include localized estimated costs for each item next to it.

## 3. Substitutions
Provide smart ingredient alternatives to save money or time for the suggested meals.

## 4. Budget feasibility logic
Provide a mathematical verification detailing the total estimated cost of the grocery list. Compare it against the user's daily budget limit.
State clearly whether the total cost is strictly 'FEASIBLE' or 'OVER BUDGET' against their constraint.
"""

if st.button("Generate Cooking Plan"):
    if not day_description:
        st.warning("Please describe your day so we can plan your meals!")
    else:
        with st.spinner("Cooking up your plan..."):
            prompt = f"Here is my day: {day_description}\nMy daily budget limit is: ₹{budget}"
            
            try:
                response = client.models.generate_content(
                    model="gemini-3.1-high",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                    )
                )
                
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred while generating the plan: {e}")
