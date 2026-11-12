import pandas as pd

football_data = pd.read_csv("cfb.csv")

season = int(input("Enter a season to analyze: "))

season_data = football_data.loc[football_data["Season"] == season]

while season_data.empty:
    print("Sorry, that season was not found.")
    season = int(input("Enter another season to analyze: "))
    season_data = football_data.loc[football_data["Season"] == season]

win_categories = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": []
}

for i, row in season_data.iterrows():
    if row["Win"] >= 10:
        win_categories["10 or more wins"].append(row["Team"])
    elif row["Win"] >= 8:
        win_categories["8-9 wins"].append(row["Team"])
    elif row["Win"] >= 6:
        win_categories["6-7 wins"].append(row["Team"])
    else:
        win_categories["Fewer than 6 wins"].append(row["Team"])

print("College Football Results for", season)

for category, teams in win_categories.items():
    print(category + ":")
    for team in teams:
        print(team)
    print()