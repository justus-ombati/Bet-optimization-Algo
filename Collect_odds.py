def collect_game_odds():

    games_data = []

    for i in range(1, 4):
        print(f"Enter details for the Game {i}: ")
        game_name = input ("Game Name (eg. Man C v Che): ")

        try:
            home_odds = float(input("Home team odds: "))
            draw_odds = float(input("Draw odds: "))
            away_odds = float(input("Away team odds: "))

        except ValueError:
            print ("Please enter valid numeric values for odds")
            continue
        game_data = {
            "Game Name": game_name,
            "Home Odds": home_odds,
            "Draw Odds": draw_odds,
            "Away Odds": away_odds
        }

        games_data.append(game_data)

    return games_data

collected_odds = collect_game_odds()

print (collected_odds)