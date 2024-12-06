spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# 1. Get names of the spicy foods
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# 2. Get the spiciest foods (heat_level > 5)
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. Print all spicy foods with a specific format
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# 4. Get a spicy food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no match is found

# 5. Print the spiciest foods (heat_level > 5) with a specific format
def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    for food in spiciest:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# 6. Get the average heat level of all spicy foods
def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)  # Using integer division to get an integer result

# 7. Add a new spicy food to the list
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
