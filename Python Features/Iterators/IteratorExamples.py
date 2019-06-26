import random

class StrangeAnimalZoo:
    def __init__(self, nameList):
        print("This is a strange ZOOOOOOOO")
        print("If you want another animal, we will give you the animal in the magical order!")
        self.nameList = nameList

    def __next__(self):
        nextAnimalIndex = random.randint(0, len(self.nameList) - 1)
        print(self.nameList.pop(nextAnimalIndex))

# Length of iterator is unknown until you iterate through it.
animals = ["rabbit", "monkey", "pig", "elephant", "dog", "chimpanzee", "crocodile", "kangaroo", "koala"]
myNormalZoo = iter(animals)
print("This is a normal ZOOOOOOO")
while(True):
    # How to use next() for iterator if you don't know the length of the iterator -> give a default state
    animal = next(myNormalZoo, None)
    if animal is None:
        break
    print(animal)

enigmaZoo = StrangeAnimalZoo(animals)
while(len(enigmaZoo.nameList) > 0):
    # next will call __next__ function
    next(enigmaZoo)