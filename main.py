import pandas as pd
# Set variable to read the csv file
football_data = pd.read_csv("cfb.csv")

# Checks to make sure the user inputs a valid season
while True:
    try:
        season = int(input("Enter a season to analyze: "))
        season_data = football_data.loc[football_data["Season"] == season]
        
        if not season_data.empty:
            break  # Valid number AND season exists in CSV, so exit the loop
        else:
            print("Sorry, that season was not found.")
    except ValueError:
        print("Invalid input. Please enter numbers only (e.g., 2022).")

# Creates a dictionary for the 4 win categories
win_categories = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": []
}
# Goes down the list and adds each team into the 4 categories of wins
for i, row in season_data.iterrows():
    if row["Win"] >= 10:
        win_categories["10 or more wins"].append(row["Team"])
    elif row["Win"] >= 8:
        win_categories["8-9 wins"].append(row["Team"])
    elif row["Win"] >= 6:
        win_categories["6-7 wins"].append(row["Team"])
    else:
        win_categories["Fewer than 6 wins"].append(row["Team"])
# Displays results
print("College Football Results for", season)

for category, teams in win_categories.items():
    print(category + ":")
    for team in teams:
        print(team)
    print()