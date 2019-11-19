# 3-4 page 46
People = ["Diana", "Cristina", "Sophie", "Ahria"]
for i in range(len(People)):
    print("I invite you to dinner, " + People[i] + ".")
print("")

# 3-5 page 46
print("Unfortunately Sophie can't come...")
print("")
People[2] = "Chloe"
for i in range(len(People)):
    print("I invite you to dinner, " + People[i] + ".")
print("")

# 3-6 page 46
print("We have found a bigger table for dinner!")
print("")
People.insert(0, "Sophia")
People.insert(int(len(People)/2), "Nanami")
People.insert(len(People), "Reem")
for i in range(len(People)):
    print("I invite you to dinner, " + People[i] + ".")
print("")

# 3-7 page 47
print("We can only invite two people...")
print("")
for i in range(len(People)-2,0,-1):
    print("Sorry " + People[i] + ", we don't have space for you...")
    People.pop(i)
print("")
length = len(People)
for i in range(len(People)):
    print("You're still invited " + People[i])
print("")
del People[1]
del People[0]
print(People)
print("")

# 3-8 page 50
Locations = ["Brisbane", "Maldives", "Norwich", "Canada", "Japan"]
for i in range(len(Locations)):
    print(Locations[i])
print("")
ELocations = sorted(Locations)
for i in range(len(Locations)):
    print(Locations[i])
print("")
E2Locations = sorted(Locations, reverse=True)
for i in range(len(Locations)):
    print(Locations[i])
print("")
reversed(Locations)
for i in range(len(Locations)):
    print(Locations[i])
print("")
Locations.reverse()
for i in range(len(Locations)):
    print(Locations[i])
print("")
Locations.sort()
for i in range(len(Locations)):
    print(Locations[i])
print("")
Locations.sort(reverse=True)
for i in range(len(Locations)):
    print(Locations[i])
print("")