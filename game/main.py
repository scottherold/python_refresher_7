from enemy import Enemy, Troll, Vampire

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

ugly_troll.take_damage(5)
another_troll.take_damage(10)
brother.take_damage(3)

print(ugly_troll)
print(another_troll)
print(brother)

print("=" * 60)

pierre = Vampire("Pierre")
vlad = Vampire("Vlad")
vamp = Vampire("Drac")

print("Creepy vampire - {}".format(pierre))
print("Evil vampire - {}".format(vlad))

# while vamp.alive:
#     vamp.take_damage(1)
#     print(vamp)