from itertools import product

def generate_outcomes_and_calculate_odds(odds_list):
    """
    Generates all possible outcomes for 3 games and calculates the combined odds for each outcome.

    Args:
        odds_list (list): A list of dictionaries containing odds for 'H', 'D', 'A' for each game.

    Returns:
        tuple: A tuple containing:
            - outcomes (list): A list of outcome strings (e.g., ['HHH', 'HHD', ...]).
            - combined_odds (list): A list of combined odds for each outcome.
    """
    outcomes = list(product("HDA", repeat=3))  # Generate outcomes as tuples
    outcome_strings = []
    combined_odds_list = []

    for outcome in outcomes:
        outcome_str = ''.join(outcome)  # Convert tuple to string e.g., ('H', 'D', 'A') -> "HDA"
        combined_odds = 1
        for i in range(3):  # Multiply odds for each game
            combined_odds *= odds_list[i][outcome[i]]
        
        outcome_strings.append(outcome_str)
        combined_odds_list.append(round(combined_odds, 2))

    return outcome_strings, combined_odds_list


def find_highest_and_lowest_odds(outcome_strings, combined_odds):
    """
    Finds the combined outcome with the highest and lowest odds from the given array.

    Args:
        outcome_strings (list): List of outcome strings (e.g., ['HHH', 'HHD', ...]).
        combined_odds (list): List of combined odds values.

    Returns:
        dict: A dictionary containing the highest and lowest odds with their respective outcomes.
    """
    max_value = max(combined_odds)
    min_value = min(combined_odds)

    max_index = combined_odds.index(max_value)
    min_index = combined_odds.index(min_value)

    result = {
        "Highest Odds": {"Outcome": outcome_strings[max_index], "Value": max_value},
        "Lowest Odds": {"Outcome": outcome_strings[min_index], "Value": min_value}
    }

    return result


def find_second_third_lowest_and_second_highest_odds(combined_odds, outcomes):
    """
    Finds the second and third lowest combined odds, and the second highest combined odds.
    
    Args:
        combined_odds (list): List of combined odds values.
        outcomes (list): List of outcomes corresponding to the combined odds.
    
    Returns:
        dict: A dictionary containing the second and third lowest odds, and the second highest odds with their outcomes.
    """
    # Sort combined odds with their indices
    sorted_indices = sorted(range(len(combined_odds)), key=lambda i: combined_odds[i])
    
    second_lowest_index = sorted_indices[1]  # Second lowest
    third_lowest_index = sorted_indices[2]   # Third lowest
    second_highest_index = sorted_indices[-2]  # Second highest
    
    result = {
        "Second Lowest Odds": {
            "Outcome": ''.join(outcomes[second_lowest_index]),
            "Value": combined_odds[second_lowest_index]
        },
        "Third Lowest Odds": {
            "Outcome": ''.join(outcomes[third_lowest_index]),
            "Value": combined_odds[third_lowest_index]
        },
        "Second Highest Odds": {
            "Outcome": ''.join(outcomes[second_highest_index]),
            "Value": combined_odds[second_highest_index]
        }
    }
    
    return result


# Example odds mapping for 3 games
odds_list = [
    {"H": 2.5, "D": 2.7, "A": 3.0},  # Game 1 odds
    {"H": 2.8, "D": 3.1, "A": 2.2},  # Game 2 odds
    {"H": 3.2, "D": 2.8, "A": 2.5}   # Game 3 odds
]

# Generate outcomes and combined odds
outcomes, combined_odds = generate_outcomes_and_calculate_odds(odds_list)

# Display all outcomes and combined odds
print("All Outcomes and Combined Odds:")
for i in range(len(outcomes)):
    print(f"{i+1}. {outcomes[i]} - {combined_odds[i]}")

# Find highest and lowest odds
extreme_odds = find_highest_and_lowest_odds(outcomes, combined_odds)
print("\nResults:")
print("Highest Odds:", extreme_odds["Highest Odds"])
print("Lowest Odds:", extreme_odds["Lowest Odds"])

# Find second and third lowest odds, and second highest odds
more_extreme_odds = find_second_third_lowest_and_second_highest_odds(combined_odds, outcomes)
print("\nSecond and Third Lowest, and Second Highest Odds:")
print("Second Lowest Odds:", more_extreme_odds["Second Lowest Odds"])
print("Third Lowest Odds:", more_extreme_odds["Third Lowest Odds"])
print("Second Highest Odds:", more_extreme_odds["Second Highest Odds"])
