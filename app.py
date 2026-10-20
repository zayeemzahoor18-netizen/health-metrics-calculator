

print("=" * 60)
print("HEALTH METRICS CALCULATOR")
print("=" * 60)

# User Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").strip().upper()

weight = int(input("Enter your weight (kg): "))
height_cm = int(input("Enter your height (cm): "))

# BMI Calculation
height_m = height_cm / 100
bmi = weight / (height_m ** 2)

# BMI Category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

    
    

# BMR Calculation
if gender == "M":
    bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
else:
    bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

# Activity Level
print("\nSelect Activity Level")
print("1. Sedentary (little or no exercise)")
print("2. Lightly Active (1-3 days/week)")
print("3. Moderately Active (3-5 days/week)")
print("4. Very Active (6-7 days/week)")
print("5. Extra Active (athlete or physical job)")

choice = int(input("Enter choice (1-5): "))

activity_factors = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
}

maintenance_calories = bmr * activity_factors.get(choice, 1.2)

# Calorie Targets
maintain = maintenance_calories
mild_loss = maintenance_calories - 250
weight_loss = maintenance_calories - 500
fast_loss = maintenance_calories - 750

mild_gain = maintenance_calories + 250
weight_gain = maintenance_calories + 500
fast_gain = maintenance_calories + 750

# Goal Selection Based on BMI
if bmi < 18.5:
    goal = "Weight Gain"
    target_calories = weight_gain
    advice = "Increase calorie intake and focus on protein-rich foods."

elif bmi < 25:
    goal = "Maintain Weight"
    target_calories = maintain
    advice = "Maintain a balanced diet and regular exercise."

else:
    goal = "Weight Loss"
    target_calories = weight_loss
    advice = "Reduce calorie intake and increase physical activity."

# Macronutrient Targets
protein = weight * 2.0      # grams
fat = weight * 0.8          # grams
carbs = (target_calories - (protein * 4 + fat * 9)) / 4

if carbs < 0:
    carbs = 0

    
# Ideal Weight Range (BMI-based)
ideal_min_weight = 18.5 * (height_m ** 2)
ideal_max_weight = 24.9 * (height_m ** 2)

# Single ideal weight (midpoint of healthy BMI range)
ideal_weight = (ideal_min_weight + ideal_max_weight) / 2


# Diet Plan
diet = f"""
BREAKFAST
• Oats: 80g
• Milk: 250ml
• Eggs: 3

LUNCH
• Rice: 200g cooked
• Chicken/Fish: 150g
• Vegetables: 150g

SNACK
• Yogurt: 200g
• Almonds: 20g

DINNER
• Rice: 150g cooked
• Chicken/Fish: 150g
• Salad: 150g

DAILY TARGETS
• Calories: {target_calories:.0f} kcal
• Protein: {protein:.0f} g
• Fat: {fat:.0f} g
• Carbs: {carbs:.0f} g
"""

# Output
print("\n" + "=" * 60)
print("                    HEALTH REPORT")
print("=" * 60)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Weight: {weight:.1f} kg")
print(f"Height: {height_cm:.1f} cm")

print("\n----- BMI ANALYSIS -----")
print(f"BMI: {bmi:.2f}")
print(f"Category: {category}")

print("\n----- CALORIE ANALYSIS -----")
print(f"BMR: {bmr:.0f} kcal/day")
print(f"Maintenance Calories: {maintain:.0f} kcal/day")


print("\n----- IDEAL WEIGHT -----")
print(f"Ideal Weight: {ideal_weight:.1f} kg")

print("\n----- CALORIE TARGETS -----")
print(f"Maintain Weight : {maintain:.0f} kcal/day")
print(f"Mild Weight Loss: {mild_loss:.0f} kcal/day")
print(f"Weight Loss     : {weight_loss:.0f} kcal/day")
print(f"Fast Weight Loss: {fast_loss:.0f} kcal/day")
print(f"Mild Weight Gain: {mild_gain:.0f} kcal/day")
print(f"Weight Gain     : {weight_gain:.0f} kcal/day")
print(f"Fast Weight Gain: {fast_gain:.0f} kcal/day")

print("\n----- RECOMMENDED GOAL -----")
print(goal)

print("\n----- HEALTH ADVICE -----")
print(advice)

print("\n----- PERSONALIZED DIET PLAN -----")
print(diet)


print("=" * 60)
print("Thank you for using Health Metrics Calculator!")
print("=" * 60)