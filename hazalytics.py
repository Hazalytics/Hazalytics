APP_NAME = "HAZALYTICS"
VERSION = "v1.0.0"
TAGLINE = "Find The Edge"

def print_header(tool_name):
    print("=" * 35)
    print(f"{APP_NAME:^35}")
    print(f"{tool_name:^35}")
    print(f"{VERSION:^35}")
    print("=" * 35)

def print_results():
    print()
    print("Results")
    print("-" * 35)         

def calculate_probability(decimal_odds):
    return 1 / decimal_odds

def calculate_net_odds(decimal_odds):
    return decimal_odds - 1

def calculate_profit(decimal_odds, stake):
    return (decimal_odds - 1) * stake

def calculate_return(decimal_odds, stake):
    return decimal_odds * stake  

def probability_to_decimal(probability):
    return probability / 100

def probability_to_decimal_odds(probability):
    return 100 / probability

def calculate_ev(decimal_odds, probability):
    return (probability_to_decimal(probability) * decimal_odds) - 1

def get_ev_rating(expected_value):
    if expected_value > 0.20:
        return "⭐⭐⭐⭐⭐ Excellent value"
    elif expected_value > 0.10:
        return "⭐⭐⭐⭐ Strong value"
    elif expected_value > 0:
        return "⭐⭐⭐ Slight value"
    elif expected_value == 0:
        return "🤝 Fair price"
    else:
        return "❌ Negative EV"
    
def calculate_kelly(decimal_odds, probability):
    probability_decimal = probability_to_decimal(probability)
    net_odds = calculate_net_odds(decimal_odds)
    probability_of_losing_decimal = 1 - probability_decimal
    return ((net_odds * probability_decimal) - probability_of_losing_decimal) / net_odds
    
def get_valid_decimal_odds():
    while True:
        try:
            decimal_odds = float(input("Enter decimal odds: "))

            if decimal_odds <= 1:
                print("❌ Decimal odds must be greater than 1.")
            else:
                return decimal_odds

        except ValueError:
            print("❌ Please enter a valid number.")       

def get_valid_probability():
    while True:
        try:
            probability = float(input("Enter probability (%): "))

            if probability <= 0 or probability > 100:
                print("❌ Probability must be between 0% and 100%.")
            else:
                return probability
            
        except ValueError:
            print("❌ Please enter a valid number.")    

def get_valid_stake():
    while True:
        try:
            stake = float(input("Enter stake: £"))

            if stake <= 0:
                print("❌ Stake must be greater than £0.")
            else:
                return stake

        except ValueError:
            print("❌ Please enter a valid number.")    

def odds_converter():
    answer = "y"

    while answer == "y":
        print_header("Odds Converter")

        decimal_odds = get_valid_decimal_odds()
        stake = get_valid_stake()
        implied_probability = calculate_probability(decimal_odds)
        net_odds = calculate_net_odds(decimal_odds)
        profit = calculate_profit(decimal_odds, stake)
        total_return = calculate_return(decimal_odds, stake)

        print_results()
        print(f"Net odds: {net_odds:.2f}/1")
        print(f"Decimal odds: {decimal_odds:.2f}")
        print(f"Implied probability: {implied_probability * 100:.2f}%")
        print(f"Profit: £{profit:.2f}")
        print(f"Total return: £{total_return:.2f}")

        answer = input("Run another calculation? (y/n): ")

def probability_calculator():
    answer = "y"

    while answer == "y":
        print_header("Probability Calculator")

        probability = get_valid_probability()
        decimal_odds = probability_to_decimal_odds(probability)
        net_odds = calculate_net_odds(decimal_odds)

        print_results()
        print(f"Probability: {probability:.2f}%")
        print(f"Decimal odds: {decimal_odds:.2f}")
        print(f"Fractional odds: {net_odds:.2f}/1")

        answer = input("Run another calculation? (y/n): ")

def ev_calculator():
     answer = "y"

     while answer == "y":
        print("❌ Stake must be greater than £0.")
        print_header("EV Calculator")

        decimal_odds = get_valid_decimal_odds()   
        probability = get_valid_probability()
        expected_value = calculate_ev(decimal_odds, probability)
        fair_odds = probability_to_decimal_odds(probability)
        rating = get_ev_rating(expected_value)

        print_results()
        print(f"Probability: {probability:.2f}%")
        print(f"Fair odds: {fair_odds:.2f}")
        print(f"Decimal odds: {decimal_odds:.2f}")
        print(f"Expected value: {expected_value * 100:.2f}%")
        print(f"Rating: {rating}")

        answer = input("Run another calculation? (y/n): ")

def fair_odds_calculator():
     answer = "y"

     while answer == "y":
        print_header("Fair Odds Calculator")

        probability = get_valid_probability()
        fair_odds = probability_to_decimal_odds(probability)

        print_results()
        print(f"Probability: {probability:.2f}%")
        print(f"Fair odds: {fair_odds:.2f}")

        answer = input("Run another calculation? (y/n): ")

def kelly_calculator():
    answer = "y"

    while answer == "y":
        print_header("Kelly Calculator")

        decimal_odds = get_valid_decimal_odds()
        probability = get_valid_probability()
        kelly = calculate_kelly(decimal_odds, probability)

        print_results()
        print(f"Decimal odds: {decimal_odds:.2f}")
        print(f"Probability: {probability:.2f}%")
        print(f"Kelly stake: {kelly * 100:.2f}% of bankroll")

        answer = input("Run another calculation? (y/n): ")                

def print_startup():
    print("=" * 35)
    print(f"{APP_NAME:^35}")
    print(f"{TAGLINE:^35}")
    print(f"{VERSION:^35}")
    print("=" * 35)
    print()

def main_menu():
    running = "y"

    while running == "y":
        print_header("Main Menu")

        print("1. Odds Converter")
        print("2. Probability Calculator")
        print("3. EV Calculator")
        print("4. Fair Odds Calculator")
        print("5. Kelly Calculator")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            odds_converter()

        elif choice == "2":
            probability_calculator()

        elif choice == "3":
            ev_calculator()

        elif choice == "4":
            fair_odds_calculator()

        elif choice == "5":
            kelly_calculator()                 

        elif choice == "6":
            running = "n"

        else:
            print("Invalid option. Please choose a valid number.")     


        print("Thanks for using Hazalytics!")

        print("Good luck!")

print_startup()
main_menu()