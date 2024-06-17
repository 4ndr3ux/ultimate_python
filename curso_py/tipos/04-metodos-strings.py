animal = " Sere la Cachorra            "
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title().strip())
print(animal.strip().upper())

print(animal.rstrip())
print(animal.find("Sere"))
print(animal.replace("Sere", "Luna"))
nuevo_animal = animal.replace("Sere", "Luna")

print(nuevo_animal.title())
print("Ser" in animal)
print(animal.find("S"))
print("Ser" not in animal)
