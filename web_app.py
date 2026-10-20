
from flask import Flask, render_template, request

app = Flask(__name__)

# Approximate nutrition values for common foods.
# Calories, protein, carbs and fat are for the portion listed.
FOODS = {
    "oats": {
        "name": "Oats", "qty": 50, "unit": "g",
        "kcal": 195, "protein": 8.5, "carbs": 33.2, "fat": 3.5
    },
    "milk": {
        "name": "Milk", "qty": 250, "unit": "ml",
        "kcal": 153, "protein": 8, "carbs": 12, "fat": 8
    },
    "banana": {
        "name": "Banana", "qty": 120, "unit": "g",
        "kcal": 107, "protein": 1.3, "carbs": 27.5, "fat": 0.4
    },
    "eggs": {
        "name": "Eggs", "qty": 2, "unit": "eggs",
        "kcal": 144, "protein": 12.6, "carbs": 0.7, "fat": 9.6
    },
    "rice": {
        "name": "Cooked rice", "qty": 200, "unit": "g",
        "kcal": 260, "protein": 5.4, "carbs": 56, "fat": 0.6
    },
    "dal": {
        "name": "Cooked dal", "qty": 200, "unit": "g",
        "kcal": 230, "protein": 14, "carbs": 36, "fat": 2
    },
    "chicken": {
        "name": "Cooked chicken", "qty": 120, "unit": "g",
        "kcal": 198, "protein": 37, "carbs": 0, "fat": 4.3
    },
    "roti": {
        "name": "Roti (whole-wheat flour)", "qty": 60,
        "unit": "g flour", "kcal": 204, "protein": 7,
        "carbs": 43, "fat": 1.5
    },
    "vegetables": {
        "name": "Cooked vegetables", "qty": 150, "unit": "g",
        "kcal": 90, "protein": 3, "carbs": 15, "fat": 2
    },
    "curd": {
        "name": "Plain curd", "qty": 150, "unit": "g",
        "kcal": 92, "protein": 5.3, "carbs": 7, "fat": 4.5
    },
    "peanuts": {
        "name": "Peanuts", "qty": 15, "unit": "g",
        "kcal": 85, "protein": 3.9, "carbs": 2.4, "fat": 7.4
    },
    "paneer": {
        "name": "Paneer", "qty": 80, "unit": "g",
        "kcal": 212, "protein": 14.4, "carbs": 2.4, "fat": 16
    },
    "apple": {
        "name": "Apple", "qty": 150, "unit": "g",
        "kcal": 78, "protein": 0.4, "carbs": 20.5, "fat": 0.3
    },
    "chickpeas": {
        "name": "Boiled chickpeas", "qty": 100, "unit": "g",
        "kcal": 164, "protein": 8.9, "carbs": 27.4, "fat": 2.6
    }
}

# Different meal choices for each goal.
MEALS = {
    "gain": [
        ("Breakfast", ["oats", "milk", "banana", "eggs"]),
        ("Lunch", ["rice", "dal", "chicken", "vegetables"]),
        ("Evening snack", ["curd", "peanuts", "banana"]),
        ("Dinner", ["roti", "paneer", "dal", "vegetables"])
    ],
    "lose": [
        ("Breakfast", ["oats", "milk", "eggs"]),
        ("Lunch", ["rice", "dal", "chicken", "vegetables"]),
        ("Evening snack", ["curd", "apple"]),
        ("Dinner", ["roti", "paneer", "vegetables"])
    ],
    "maintain": [
        ("Breakfast", ["oats", "milk", "banana", "eggs"]),
        ("Lunch", ["rice", "dal", "chicken", "vegetables"]),
        ("Evening snack", ["curd", "peanuts"]),
        ("Dinner", ["roti", "paneer", "vegetables"])
    ]
}


def make_diet_plan(goal, calorie_target):
    """Create a portion-based example plan near the calorie target."""
    selected_meals = MEALS[goal]

    base_calories = sum(
        FOODS[key]["kcal"]
        for _, food_keys in selected_meals
        for key in food_keys
    )

    # Keep portion scaling within a moderate range.
    factor = calorie_target / base_calories if base_calories else 1
    factor = max(0.75, min(1.35, factor))

    diet_plan = []
    totals = {
        "calories": 0,
        "protein": 0.0,
        "carbs": 0.0,
        "fat": 0.0
    }

    for meal_name, food_keys in selected_meals:
        items = []

        for key in food_keys:
            food = FOODS[key]

            if food["unit"] == "eggs":
                quantity = max(1, round(food["qty"] * factor))
            else:
                quantity = max(
                    5, round(food["qty"] * factor / 5) * 5
                )

            actual_factor = quantity / food["qty"]

            item = {
                "name": food["name"],
                "quantity": quantity,
                "unit": food["unit"],
                "calories": round(food["kcal"] * actual_factor),
                "protein": round(food["protein"] * actual_factor, 1),
                "carbs": round(food["carbs"] * actual_factor, 1),
                "fat": round(food["fat"] * actual_factor, 1)
            }

            items.append(item)
            totals["calories"] += item["calories"]
            totals["protein"] += item["protein"]
            totals["carbs"] += item["carbs"]
            totals["fat"] += item["fat"]

        diet_plan.append({
            "name": meal_name,
            "items": items
        })

    totals["protein"] = round(totals["protein"], 1)
    totals["carbs"] = round(totals["carbs"], 1)
    totals["fat"] = round(totals["fat"], 1)

    return diet_plan, totals


@app.route("/")
def home():
    return render_template("index.html", error=None)


@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        name = request.form.get("name", "").strip()
        age = int(request.form["age"])
        gender = request.form["gender"]
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        activity = float(request.form["activity"])
        goal = request.form["goal"]

        # Validate user input.
        if not name:
            raise ValueError("Please enter your name.")

        if not 1 <= age <= 120:
            raise ValueError("Please enter a valid age.")

        if not 20 <= weight <= 500:
            raise ValueError("Please enter a valid weight in kg.")

        if not 80 <= height <= 250:
            raise ValueError("Please enter a valid height in cm.")

        if gender not in ("male", "female"):
            raise ValueError("Please select a valid option.")

        if activity not in (1.2, 1.375, 1.55, 1.725, 1.9):
            raise ValueError("Please select an activity level.")

        if goal not in MEALS:
            raise ValueError("Please select a goal.")

        # BMI calculation.
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity range"

        # BMR: Mifflin-St Jeor equation.
        if gender == "male":
            bmr = (
                10 * weight + 6.25 * height
                - 5 * age + 5
            )
        else:
            bmr = (
                10 * weight + 6.25 * height
                - 5 * age - 161
            )

        # Estimated daily maintenance calories.
        maintenance = bmr * activity

        # Simple calorie adjustments for the chosen goal.
        if goal == "lose":
            target_calories = maintenance - 300
        elif goal == "gain":
            target_calories = maintenance + 250
        else:
            target_calories = maintenance

        target_calories = max(target_calories, 1200)

        # Example macro split: 25% protein, 45% carbs, 30% fat.
        protein = target_calories * 0.25 / 4
        carbs = target_calories * 0.45 / 4
        fats = target_calories * 0.30 / 9

        # Build the portion-based meal plan.
        diet_plan, diet_totals = make_diet_plan(
            goal, target_calories
        )

        return render_template(
            "result.html",
            name=name,
            age=age,
            bmi=round(bmi, 1),
            category=category,
            bmr=round(bmr),
            maintenance=round(maintenance),
            target_calories=round(target_calories),
            protein=round(protein),
            carbs=round(carbs),
            fats=round(fats),
            diet_plan=diet_plan,
            diet_totals=diet_totals,
            goal=goal
        )

    except (ValueError, KeyError) as error:
        return render_template(
            "index.html", error=str(error)
        ), 400


if __name__ == "__main__":
    app.run(debug=True)
