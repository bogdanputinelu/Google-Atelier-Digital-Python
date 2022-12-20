players=[
    {
        "first_name": "Ion",
        "last_name": "Popescu",
        "varsta": 12
    },
    {
        "first_name": "Andreea",
        "last_name": "Popa",
        "varsta": 35
    },
    {
        "first_name": "Isabela",
        "last_name": "Enache",
        "varsta": 25
    }
]

sorted_players = sorted(players, key=lambda player: player["last_name"])
print(sorted_players)