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

def get_kelly_recommendation(kelly):
    if kelly <= 0:
        return "No bet"
    elif kelly > 0.20:
        return "Half Kelly recommended"
    elif kelly > 0.10:
        return "Half or Quarter Kelly recommended"
    else:
        return "Full Kelly is reasonable"
    
def get_risk_rating(kelly):
    if kelly <= 0:
        return "No Bet ⚪"
    elif kelly < 0.05:
        return "Very Low 🟢"
    elif kelly < 0.10:
        return "Low 🟢"
    elif kelly < 0.20:
        return "Moderate 🟡"
    elif kelly <0.35:
        return "High 🟠"
    else:
        return "Very High 🔴"

def calculate_confidence_score(expected_value, kelly):
    score = 50

    if expected_value > 0:
        score += expected_value * 100
    else:
        score += expected_value * 200

    if kelly > 0.35:
        score -= 15
    elif kelly > 0.20:
        score -= 5

    if score > 100:
        score = 100
    elif score < 0:
        score = 0

    return score                        
    
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
        half_kelly = kelly / 2
        quarter_kelly = kelly / 4
        recommendation = get_kelly_recommendation(kelly)
        expected_value = calculate_ev(decimal_odds, probability)
        confidence_score = calculate_confidence_score(expected_value, kelly)
        risk = get_risk_rating(kelly)
        
        print_results()
        print(f"Decimal odds: {decimal_odds:.2f}")
        print(f"Probability: {probability:.2f}%")
        print(f"Full Kelly: {kelly * 100:.2f}% of bankroll")
        print(f"Half Kelly: {half_kelly * 100:.2f}% of bankroll")
        print(f"Quarter Kelly: {quarter_kelly * 100:.2f}% of bankroll")
        print(f"Recommendation: {recommendation}")
        print(f"Risk Rating: {risk}")
        print(f"Confidence Score: {confidence_score:.0f}/100")

        answer = input("Run another calculation? (y/n): ")

def bet_analyser():
    answer = "y"

    while answer == "y":
        print_header("Bet Analyser")

        decimal_odds = get_valid_decimal_odds()
        probability = get_valid_probability()

        implied_probability = calculate_probability(decimal_odds)
        fair_odds = probability_to_decimal_odds(probability)
        expected_value = calculate_ev(decimal_odds, probability)
        kelly = calculate_kelly(decimal_odds, probability)
        half_kelly = kelly / 2
        quarter_kelly = kelly / 4
        recommendation = get_kelly_recommendation(kelly)
        risk = get_risk_rating(kelly)
        confidence_score = calculate_confidence_score(expected_value, kelly)
        print()
        print("=" * 35)
        print(f"{'BET ANALYSIS':^35}")
        print("=" * 35)      
        print("📈 Market")
        print("-" * 35)      
        print(f"Bookmaker Odds:      {decimal_odds:.2f}")
        print(f"Implied Probability: {implied_probability * 100:.2f}%")
        print()
        print("🧠 Your Model")
        print("-" * 35)
        print(f"Model Probability:   {probability:.2f}%")
        print(f"Fair Odds:           {fair_odds:.2f}")
        if expected_value >= 0:
            print(f"Expected Value:      +{expected_value * 100:.2f}%")
        else:    
            print(f"Expected Value:      {expected_value * 100:.2f}%")
        print()    
        print("💰 Staking")
        print("-" * 35)
        print(f"Full Kelly:          {kelly * 100:.2f}% of bankroll")
        print(f"Half Kelly:          {half_kelly * 100:.2f}% of bankroll")
        print(f"Quarter Kelly:       {quarter_kelly * 100:.2f}% of bankroll")
        print()
        print("🎯 Assessment")
        print("-" * 35)
        print(f"Recommendation:      {recommendation}")
        print(f"Risk:                {risk}")
        if confidence_score >= 80:
            print(f"Confidence:         ⭐⭐⭐⭐⭐ {confidence_score:.0f}/100")
        elif confidence_score >= 65:
            print(f"Confidence:         ⭐⭐⭐⭐ {confidence_score:.0f}/100")
        elif confidence_score >= 50:
            print(f"Confidence:         ⭐⭐⭐ {confidence_score:.0f}/100")
        elif confidence_score >= 35:
            print(f"Confidence:         ⭐⭐ {confidence_score:.0f}/100")
        else:
            print(f"Confidence:         ⭐ {confidence_score:.0f}/100")            
        print()
        print("Verdict")
        print("-" * 35)
        if expected_value > 0:
            print("Verdict: ✅ Value Bet")
        else:
            print("Verdict: ❌ No Value")
        print()    
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

        print("1. Bet Analyser")
        print("2. Odds Converter")
        print("3. Probability Calculator")
        print("4. EV Calculator")
        print("5. Fair Odds Calculator")
        print("6. Kelly Calculator")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            bet_analyser()

        elif choice == "2":
            odds_converter()

        elif choice == "3":
            probability_calculator()

        elif choice == "4":
            ev_calculator()

        elif choice == "5":
            fair_odds_calculator()                 

        elif choice == "6":
            kelly_calculator()

        elif choice == "7":
            running = "n"    

        else:
            print("Invalid option. Please choose a valid number.")     


        print("Thanks for using Hazalytics!")

        print("Good luck!")

print_startup()
main_menu()