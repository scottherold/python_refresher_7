from player import Player

scott = Player("Scott")

print(scott.name)
print(scott.lives)
scott.lives -= 1
print(scott)

scott.lives -= 1
print(scott)

scott.lives -= 1
print(scott)

scott.lives -= 1
print(scott)

scott._lives = 9
print(scott)

scott.level = 2
print(scott)

scott.level += 5
print(scott)

scott.level = 3
print(scott)