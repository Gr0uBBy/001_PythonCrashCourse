alien_0 = {
    "color": "green",
    "points": 5,
}

print(alien_0["color"])
print(alien_0["points"])

print(f"Great! You have just earned {alien_0['points']} points!")

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

print(f"Alien color is {alien_0['color']}.")
alien_0["color"] = "yellow"
print(f"Now alien color is {alien_0['color']}.")

# /alien_0["speed"] = "medium"
alien_0["speed"] = "fast"

print(
    f"Alien origonal coordinates (X:{alien_0['x_position']}, Y:{alien_0['y_position']})"
)

if alien_0["speed"] == "slow":
    x_incremnet = 1
elif alien_0["speed"] == "medium":
    x_incremnet = 2
elif alien_0["speed"] == "fast":
    x_incremnet = 3

alien_0["x_position"] += x_incremnet

print(
    f"Alien new coordinates are: (X:{alien_0['x_position']}, Y:{alien_0['y_position']})"
)

print(alien_0)

del alien_0["points"]

print(alien_0)
