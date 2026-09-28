import csv
import tkinter as tk
from tkinter import scrolledtext

# Define a function to load recipes from a CSV file
def load_recipes(filename):
    """
    Load recipes from a CSV file and return a dictionary where the key is the dish name
    and the value is a dictionary with ingredients and instructions.
    """
    recipes = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dish = row['Dish'].strip().lower()
            recipes[dish] = {
                'Ingredients': row['Ingredients'].strip(),
                'Instructions': row['Instructions'].strip()
            }
    return recipes

# Define a function to get a recipe for a given dish
def get_recipe(dish, recipes):
    """
    Retrieve the recipe for the given dish from the recipes dictionary.
    If the dish is not found, return None.
    """
    return recipes.get(dish.lower())

# Define a function to interact with the user using GUI
def chatbot_gui():
    root = tk.Tk()
    root.title("Culinary Assistant Chatbot")
                         
    def process_user_input():
        
        user_input = entry.get()
        entry.delete(0, tk.END)  # Clear the input field

        if user_input.lower() == 'exit':
            response_text.insert(tk.END, "Goodbye! Happy cooking!\n")
            entry.config(state=tk.DISABLED)  # Disable input field
        else:
            recipe = get_recipe(user_input, recipes)
            if recipe:
                response_text.insert(tk.END, f"Recipe for {user_input.title()}:\n")
                response_text.insert(tk.END, f"Ingredients: {recipe['Ingredients']}\n")
                response_text.insert(tk.END, f"Instructions: {recipe['Instructions']}\n\n")
            else:
                response_text.insert(tk.END, f"Sorry, I don't have the recipe for {user_input}. Please try another dish.\n\n")
        prompt_user()
    # Entry for user input
    def prompt_user():
        response_text.insert(tk.END,"Please Enter The Name Of The Recipe You Would Like to Know:\n")
    
    
    entry = tk.Entry(root, width=60)
    entry.grid(row=0,column=0, padx=10, pady=10)

    # Button to submit user input
    submit_button = tk.Button(root, text="Submit", command=process_user_input)
    submit_button.grid(row=0,column=1, padx=5, pady=10)

    # Text area for bot responses
    response_text = scrolledtext.ScrolledText(root, width=125, height=100)
    response_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Initial message
    response_text.insert(tk.END, "Hello! I'm your Culinary Assistant. Ask me for a recipe and I'll provide it for you.\n")
    response_text.insert(tk.END, "Type 'exit' to end our conversation.\n\n")

    recipes = load_recipes('recipes.csv')
    prompt_user()

    root.mainloop()

# Run the chatbot GUI
if __name__ == "__main__":
    chatbot_gui()
