alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "blue", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []
print("Clearing the list of aliens")

for alien in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")
print(f"The total number of created aliens is {len(aliens)}")

for alien in aliens[:3]:
    # alien = {"color": "yellow", "points": 10, "speed": "medium"}
    alien["color"] = "yellow"
    alien["points"] = 10
    alien["speed"] = "medium"

for alien in aliens[:5]:
    print(alien)

print("...")
print(f"The total number of created aliens is {len(aliens)}")
