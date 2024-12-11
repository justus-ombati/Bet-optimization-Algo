import random
from itertools import product

def filter_outcomes_by_first_prediction(outcomes, user_input):
    """
    Filters outcomes that start with the user's prediction for the first game.

    Args:
        outcomes (list): List of all possible outcomes.
        user_input (str): User's prediction for the first game ("H", "D", or "A").
    
    Returns:
        list: Filtered outcomes that start with the user's input.
    """
    return [outcome for outcome in outcomes if outcome[0] == user_input]

def narrow_down_to_3_outcomes(filtered_outcomes):
    """
    Narrows a list of outcomes to 3 with balanced diversity.

    Args:
        filtered_outcomes (list): List of filtered outcomes.

    Returns:
        list: A list of 3 outcomes.
    """
    # Step 1: Split outcomes into groups based on the middle and last values
    grouped = {"middle_variation": [], "last_variation": []}

    for outcome in filtered_outcomes:
        # Add outcomes where the middle character varies
        if outcome[1] != outcome[2]:
            grouped["middle_variation"].append(outcome)
        else:
            grouped["last_variation"].append(outcome)

    # Step 2: Select outcomes ensuring variation in both positions
    result = []

    # Ensure diversity by picking from different groups
    if len(grouped["middle_variation"]) >= 2:
        result.extend(random.sample(grouped["middle_variation"], 2))
    elif grouped["middle_variation"]:
        result.append(grouped["middle_variation"][0])

    if len(grouped["last_variation"]) >= 1:
        result.append(random.choice(grouped["last_variation"]))
    elif grouped["last_variation"]:
        result.append(grouped["last_variation"][0])

    # Final fallback: random selection if no diversity groups are found
    while len(result) < 3:
        remaining = set(filtered_outcomes) - set(result)
        result.append(random.choice(list(remaining)))

    return result[:3]

def main():
    # Generate all possible outcomes for 3 games
    outcomes_list = [''.join(outcome) for outcome in product("HDA", repeat=3)]
    print("All possible outcomes (27):")
    print(outcomes_list)

    # Step 1: Get user's prediction for the first game
    while True:
        user_input = input("Enter your prediction for the first game (H/D/A): ").strip().upper()
        if user_input in {"H", "D", "A"}:
            break
        else:
            print("Invalid input! Please enter H, D, or A.")

    # Filter outcomes based on the first prediction
    filtered_outcomes = filter_outcomes_by_first_prediction(outcomes_list, user_input)
    print(f"\nFiltered outcomes that start with '{user_input}':")
    print(filtered_outcomes)

    # Narrow down to 3 outcomes using the expert technique
    narrowed_outcomes = narrow_down_to_3_outcomes(filtered_outcomes)
    print("\nExpert narrowed outcomes (3 outcomes):")
    for idx, outcome in enumerate(narrowed_outcomes, 1):
        print(f"{idx}. {outcome}")

if __name__ == "__main__":
    main()
