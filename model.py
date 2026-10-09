import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load dataset
data = pd.read_csv("data/food_data.csv")


def recommend_food(budget, calories, veg, cuisine, area, meal_type, people):

    # -----------------------------
    # 1. Food preference filter
    # -----------------------------
    if veg == 1:
        filtered_data = data[data["veg"] == 1]
    else:
        filtered_data = data[data["veg"] == 0]

    # -----------------------------
    # 2. Area filter
    # -----------------------------
    filtered_data = filtered_data[
        filtered_data["area"] == area
    ]

    # -----------------------------
    # 3. Meal type filter
    # -----------------------------
    filtered_data = filtered_data[
        filtered_data["category"] == meal_type
    ]

    # -----------------------------
    # 4. Cuisine filter
    # -----------------------------
    if cuisine != "Any Cuisine":
        filtered_data = filtered_data[
            filtered_data["cuisine"] == cuisine
        ]

    # -----------------------------
    # 5. If nothing matches
    # -----------------------------
    if len(filtered_data) == 0:
        return pd.DataFrame(
            columns=[
                "name",
                "category",
                "price",
                "calories",
                "rating",
                "area",
                "restaurant",
                "cuisine"
            ]
        )

    # -----------------------------
    # 6. ML recommendation
    # -----------------------------
    features = ["price", "calories", "rating"]

    X = filtered_data[features]

    number = min(5, len(filtered_data))

    model = NearestNeighbors(
        n_neighbors=number,
        metric="euclidean"
    )

    model.fit(X)

    # User requirements
    user_input = [[budget, calories, 4.0]]

    distances, indexes = model.kneighbors(user_input)

    recommendations = filtered_data.iloc[indexes[0]]

    return recommendations[
        [
            "name",
            "category",
            "price",
            "calories",
            "rating",
            "area",
            "restaurant",
            "cuisine"
        ]
    ]