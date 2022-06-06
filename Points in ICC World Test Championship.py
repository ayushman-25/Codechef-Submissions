n1, n2, team = int(input()), int(input()), input()
if team not in ["AUS", "IND"]:
    print("Invalid input"); exit(0)
print(n1 + (10 if (team == "AUS") else 70))
print(n2 + (10 if (team == "IND") else 70))
