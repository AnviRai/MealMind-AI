import streamlit as st
from model import recommend_food

st.title("🍽️ AI Food Recommendation System")

st.write("Get personalized food recommendations based on your requirements.")

areas = [
    "Kamla Nagar",
    "South Ex",
    "Hauz Khaas",
    "CP",
    "Noida"
]

area = st.selectbox(
    "📍 Select your area",
    areas
)

# Number of people
people = st.number_input(
    "Number of People",
    min_value=1,
    max_value=20,
    value=2
)

# Meal type
meal_type = st.selectbox(
    "Select Meal Type",
    ["Breakfast", "Lunch", "Snacks", "Dinner"]
)

# Total budget
budget = st.number_input(
    "Total Budget (₹)",
    min_value=50,
    max_value=10000,
    value=500
)

# Calories per person
calories = st.number_input(
    "Preferred Calories per Person",
    min_value=100,
    max_value=1000,
    value=500
)

# Food preference
food_type = st.selectbox(
    "Food Preference",
    ["Vegetarian", "Non-Vegetarian"]
)

# Cuisine preference
cuisine = st.selectbox(
    "Cuisine Preference",
    [
        "Any Cuisine",
        "North Indian",
        "South Indian",
        "Chinese",
        "Italian"
    ]
)

if food_type == "Vegetarian":
    veg = 1
else:
    veg = 0

if st.button("Recommend Food"):

    budget_per_person = budget / people

    result = recommend_food(
        budget_per_person,
        calories,
        veg,
        cuisine,
        area,
        meal_type,
        people
    )

    st.subheader("Recommended Food 🍴")

    st.dataframe(result)

    st.write(f"**Meal:** {meal_type}")
    st.write(f"**People:** {people}")
    st.write(f"**Budget per person:** ₹{budget_per_person:.0f}")