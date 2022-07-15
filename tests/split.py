unyarned = yarning.split("\n")


with open("unyarned.txt", "w") as f:
    for i in unyarned:
        f.write(i + "\n")
