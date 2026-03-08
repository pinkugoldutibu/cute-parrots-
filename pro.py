class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
blu = parrot("blu",3)
woo = parrot("woo",2)
print(blu.species)
print(woo.species)
print(blu.name, blu.age)
print(woo.name, woo.age)