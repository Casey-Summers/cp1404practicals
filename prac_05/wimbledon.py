"""
Wimbledon stat tracker
Estimate: 70 minutes
Actual:   38 minutes
"""

FIELD_TITLES = 1
WINNING_COUNTRY_COLUMN = 1
WINNER_COLUMN = 2
FILENAME = "wimbledon.csv"


def main():
    """Program to find the amount of times a player has won Wimbledon and the winning countries."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        all_years_data = [line.strip() for line in in_file.readlines()]
        year_data = [year.split(",") for year in all_years_data[FIELD_TITLES:]]
        print("Wimbledon Champions:")
        winners = find_winners(year_data)
        players_to_wins = calculate_player_wins(winners)
        for players, wins in players_to_wins.items():
            print(f"{players}: {wins}")
        winning_countries = find_winning_countries(year_data)
        print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
        print(", ".join(winning_countries))


def find_winners(year_data):
    """Iterates through all year's corresponding winner's column and adds that index to a list."""
    winners = []
    for data_point in year_data:
        winners.append(data_point[WINNER_COLUMN])
    return winners


def calculate_player_wins(winners):
    """Calculates the total tournaments won by the player by searching through the list of winners for each year."""
    players_to_wins = {}
    for winner in winners:
        # If the player already exists in the list, it adds one to the key's corresponding value
        if winner in players_to_wins:
            players_to_wins[winner] += 1
        # If the player doesn't exist, the key is created and the value set to 1
        else:
            players_to_wins[winner] = 1
    return players_to_wins


def find_winning_countries(year_data):
    """Creates a list of winning countries that is then sorted and put into a unique set."""
    winning_countries = []
    for data_point in year_data:
        winning_countries.append(data_point[WINNING_COUNTRY_COLUMN])
    return sorted(set(winning_countries))


main()
