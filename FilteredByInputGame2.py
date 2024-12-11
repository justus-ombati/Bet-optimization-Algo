import random
from itertools import product

def filter_outcomes_by_position(outcomes, user_input, position):
    """
    Filters outcomes where the value at a specific position matches the user's input.

    Args:
        outcomes (list): List of possible outcomes.
        user_input (str): User's prediction for the specific position.
        position (int): The position to filter by (0 for first, 1 for second, etc.).

    Returns:
        list: Filtered outcomes matching the user's input at the given position.
    """
    return [outcome for outcome in outcomes if outcome[position] == user_input]

def narrow_down_to_3_outcomes(filtered_outcomes):
    """
    Narrows a list of outcomes to 3 with balanced diversity.

    Args:
        filtered_outcomes (list): List of filtered outcomes.

    Returns:
        list: A list of 3 outcomes.
    """
    # Step 1: Shuffle to ensure randomness
    random.shuffle(filtered_outcomes)

    # Step 2: Split into groups based on the last value
    last_value_groups = {}
    for outcome in filtered_outcomes:
        key = outcome[2]  # Group outcomes by the last value
        if key not in last_value_groups:
            last_value_groups[key] = []
        last_value_groups[key].append(outcome)

    # Step 3: Pick one outcome from different groups (if possible)
    result = []
    for group in last_value_groups.values():
        if group:
            result.append(group[0])  # Pick the first outcome from each group
        if len(result) == 3:
            break

    # Final fallback: random selection if less than 3 unique groups exist
    while len(result) < 3:
        remaining = set(filtered_outcomes) - set(result)
        result.append(random.choice(list(remaining)))

    return result[:3]

def main():
    # Generate all possible outcomes for 3 games
    outcomes_list = [''.join(outcome) for outcome in product("HDA", repeat=3)]
    print("All possible outcomes (27):")
    print(outcomes_list)

    # Step 1: User input for the first game
    while True:
        user_input_game1 = input("Enter your prediction for the first game (H/D/A): ").strip().upper()
        if user_input_game1 in {"H", "D", "A"}:
            break
        else:
            print("Invalid input! Please enter H, D, or A.")

    # Filter outcomes based on the first game prediction
    filtered_outcomes_game1 = filter_outcomes_by_position(outcomes_list, user_input_game1, position=0)
    print(f"\nFiltered outcomes that start with '{user_input_game1}':")
    print(filtered_outcomes_game1)

    # Narrow down to 3 outcomes
    narrowed_outcomes_game1 = narrow_down_to_3_outcomes(filtered_outcomes_game1)
    print("\nExpert narrowed outcomes after Game 1:")
    for idx, outcome in enumerate(narrowed_outcomes_game1, 1):
        print(f"{idx}. {outcome}")

    # Step 2: User input for the second game
    while True:
        user_input_game2 = input("\nEnter your prediction for the second game (H/D/A): ").strip().upper()
        if user_input_game2 in {"H", "D", "A"}:
            break
        else:
            print("Invalid input! Please enter H, D, or A.")

    # Pull all 9 outcomes with the same middle value as the user input
    filtered_outcomes_game2 = filter_outcomes_by_position(outcomes_list, user_input_game2, position=1)
    print(f"\nFiltered outcomes with '{user_input_game2}' as the middle value:")
    print(filtered_outcomes_game2)

    # Narrow down to 3 outcomes again
    narrowed_outcomes_game2 = narrow_down_to_3_outcomes(filtered_outcomes_game2)
    print("\nExpert narrowed outcomes after Game 2:")
    for idx, outcome in enumerate(narrowed_outcomes_game2, 1):
        print(f"{idx}. {outcome}")

if __name__ == "__main__":
    main()
