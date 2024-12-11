
from itertools import product

def generate_outcomes_and_calculate_odds(odds_map):
        
        """
    Generates all possible outcomes for 3 games and calculates the combined odds for each outcome.
    
    Args:
        odds_map (dict): A dictionary containing odds for Home ('H'), Draw ('D'), and Away ('A').
                         Example: {"H": 2.5, "D": 2.7, "A": 3.0}
                         
    Returns:
        list: A list of dictionaries where each dictionary represents an outcome and its combined odds.
    """
        outcomes = list(product("HDA", repeat=3)) # Cartesian product of ['H', 'D', 'A'] repeated 3 times
        results = []

        for idx, outcome in enumerate(outcomes, start=1):
                outcome_str = ''.join(outcome) # Convert tuple to string e.g., ('H', 'D', 'A') -> "HDA"
                combined_odds = odds_map[outcome[0]] * odds_map[outcome[1]] * odds_map[outcome[2]]

                results.append({
                        "Outcome": f"{idx}. {outcome_str}",
                        "Combined Odds": round(combined_odds, 2) # Round to 2 decimal places
                })

        return results
# Example odds mapping
odds_example = {"H": 2.5, "D": 2.7, "A": 3.0}

outcomes_with_odds = generate_outcomes_and_calculate_odds(odds_example)

for outcome in outcomes_with_odds:
        print(outcome)