import csv
import os
DATA_FILE = "data_tracker.csv"

FIELDNAMES = [
    "sport",
    "competition",
    "event_name",
    "event_date",
    "neutral_venue",
    "market",
    "selection",
    "odds",
    "status",
    "selection_result",
    "team_1_goals",
    "team_2_goals",
]

def save_selection(row):
    file_exists = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)    

def add_event_data():

    print("=" * 35)
    print("ADD EVENT DATA".center(35))
    print("=" * 35)

    sport = input("Sport: ").lower()

    if sport == "football":
        competition = input("Competition: ")
        if competition.lower() == "premier league":
            neutral_venue = "no"
            home_team = input("Home Team: ")
            away_team = input("Away Team: ")
            team_1 = home_team
            team_2 = away_team
            event_name = f"{team_1} v {team_2}"
            event_date = input("Date (DD/MM/YYYY): ")
        elif competition.lower() == "world cup":
            neutral_venue = input("Neutral Venue? (yes/no): ").lower()
            if neutral_venue == "no":
                home_team = input("Home Team: ")
                away_team = input("Away Team: ")
                team_1 = home_team
                team_2 = away_team
                event_name = f"{team_1} v {team_2}"
                event_date = input("Date (DD/MM/YYYY): ")
            else:
                team_1 = input("Team 1: ")
                team_2 = input("Team 2: ")
                event_name = f"{team_1} v {team_2}"
                event_date = input("Date: (DD/MM/YYYY): ")    

            print()
            print("Event Summary")
            print("-" * 35)
            print(f"Sport: {sport}")
            print(f"Competition: {competition}")
            print(f"Event: {event_name}")
            print(f"Date: {event_date}")
            print(f"Neutral Venue: {neutral_venue}")

            print()
            print("Selections")
            print("-" * 35)

            while True:

                market = input("Market: ")
                selection = input("Selection: ")
                odds = float(input("Odds: "))
                row = {
                    "sport": sport,
                    "competition": competition,
                    "event_name": event_name,
                    "event_date": event_date,
                    "neutral_venue": neutral_venue,
                    "market": market,
                    "selection": selection,
                    "odds": odds,
                    "status": "Pending",
                    "selection_result": "",
                    "team_1_goals": "",
                    "team_2_goals": "",
                }

                save_selection(row)

                print()
                print("Selection saved:")
                print("-" * 35)
                print(f"Market: {market}")
                print(f"Selection: {selection}")
                print(f"Odds: {odds:.2f}")
                print("Result: Pending")

                answer = input("\nAdd another selection? (y/n): ").lower()

                if answer != "y":
                    break                                

add_event_data()    
