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

def settle_event():
    print("=" * 35)
    print("SETTLE EVENT".center(35))
    print("=" * 35)

    event_name = input("Event Name: ")
    team_1_goals = int(input("Team 1 Goals: "))
    team_2_goals = int(input("Team 2 Goals: "))
    qualified_team = input("Qualified Team: ")
    total_goals = team_1_goals + team_2_goals

    rows = []

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["event_name"].lower() == event_name.lower():
                row["status"] = "Complete"
                row["team_1_goals"] = team_1_goals
                row["team_2_goals"] = team_2_goals
                if team_1_goals > team_2_goals:
                    winner = row["event_name"].split(" v ")[0]
                elif team_2_goals > team_1_goals:
                    winner = row["event_name"].split(" v ")[1]
                else:
                    winner = "Draw"
                    
                if row["market"].lower() == "full time result":
                    if row["selection"].lower() == winner.lower():
                        row["selection_result"] = "Win"
                    else:
                        row["selection_result"] = "Lose"

                if row["market"].lower() == "double chance":
                    if winner.lower() in row["selection"].lower():
                        row["selection_result"] = "Win"
                    else:
                        row["selection_result"] = "Lose"

                if row["market"].lower() == "btts":
                    if team_1_goals > 0 and team_2_goals > 0:
                        btts_result = "Yes"
                    else:
                        btts_result = "No"

                    if row["selection"].lower() == btts_result.lower():
                        row["selection_result"] = "Win"
                    else:
                        row["selection_result"] = "Lose"        

                if row["market"].lower() == "goals over/under":
                    selection = row["selection"]
                    parts = selection.split()
                    direction = parts[0].lower()
                    line = float(parts[1])
                    if direction == "over":
                        if total_goals > line:
                            row["selection_result"] = "Win"
                        else:
                            row["selection_result"] = "Lose"
                    else:
                        if total_goals < line:
                            row["selection_result"] = "Win"
                        else:
                            row["selection_result"] = "Lose"

                if row["market"].lower() == "to qualify":
                    if row["selection"].lower() == qualified_team.lower():
                        row["selection_result"] = "Win"
                    else:
                        row["selection_result"] = "Lose"

                if row["market"].lower() == "correct score":
                    predicted_score = row["selection"].strip()
                    actual_score = f"{team_1_goals}-{team_2_goals}"

                    if predicted_score == actual_score:
                        row["selection_result"] = "Win"
                    else:
                        row["selection_result"] = "Loss"                                        


            rows.append(row)

    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

        print()
        print("✅ Event settled successfully.")            

    print()
    print("Result Entered")
    print("-" * 35)
    print(f"Event: {event_name}")
    print(f"Score: {team_1_goals}-{team_2_goals}")                

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

def main_menu():
    print("=" * 35)
    print("DATA TRACKER".center(35))
    print("=" * 35)
    print("1. Add Event Data")
    print("2. Settle Event")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_event_data()
    elif choice == "2":
        settle_event()
    elif choice == "3":
        print("Exiting Data Tracker.")
    else:
        print("Invalid option.")

main_menu()                        
