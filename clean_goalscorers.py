import pandas as pd

# Load your data
data = pd.read_csv("goalscorers.csv")

official_tournaments = [
    "FIFA World Cup",
    "Copa América",
    "African Cup of Nations",
    "AFC Asian Cup",
    "UEFA Euro",
    "CONCACAF Championship",
    "Oceania Nations Cup",
    "Intercontinental Cup",
    "UEFA Nations League",
    "Arab Cup",
    "COSAFA Cup",
    "Gold Cup",
    "Asian Games",
    "Olympic Games"
]

qualification_tournaments = [
    'FIFA World Cup qualification',
    'AFC Asian Cup qualification',
    'UEFA Euro qualification',
    'African Cup of Nations qualification',
    'CONCACAF Championship qualification',
    'Arab Cup qualification',
    'Oceania Nations Cup qualification',
    'COSAFA Cup qualification',
    'Gold Cup qualification',
    'Africa Cup of Nations qualification',
    'Copa América qualification',
    'CONCACAF Nations League qualification',
]

def tournament_type(tournament):
    if tournament in official_tournaments:
        return 'official'
    elif tournament in qualification_tournaments:
        return 'qualification'
    else:
        return 'friendly'

# Apply the function to create the new column
data['tournament_type'] = data['tournament'].apply(tournament_type)

# Display the updated DataFrame
# print(data.head())

data.to_csv("converted_goalscorers.csv", index=False)
