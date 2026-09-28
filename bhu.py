import csv

def greet_user():
    print("Hello! I'm your culinary assistant. How can I help you today?")

def search_recipe(query):
    print(f"Searching for the recipe of {query}...")
    try:
        # Using a CSV file as the recipe database
        with open(r'recipes.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if query.lower() in row['Title'].lower():
                    # Printing the recipe information
                    print(f"Here is the recipe for {query}:\n")
                    print(f"Title: {row['Title']}")
                    print(f"Directions: {row['Directions']}")

                    # Loop through ingredients dynamically
                    for i in range(1, 20):  # Assuming a maximum of 19 ingredients
                        quantity_key = f"Quantity{i:02d}"
                        unit_key = f"Unit{i:02d}"
                        ingredient_key = f"Ingredient{i:02d}"

                        # Check if the keys are present in the row
                        if quantity_key in row and unit_key in row and ingredient_key in row:
                            # Print quantity, unit, and ingredient
                            print(f"{row[quantity_key]} {row[unit_key]} - {row[ingredient_key]}")

                    print(f"Category: {row['Category']}")
                    return

            print(f"Sorry, I couldn't find a recipe for {query}.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    greet_user()

    while True:
        user_input = input("What food would you like a recipe for? (Type 'exit' to quit): ").lower()

        if user_input == 'exit':
            print("Goodbye!")
            break

        search_recipe(user_input)

if __name__ == "__main__":
    main()
