
def animal_sounds():
  """
  Asks the user for an animal name and displays its sound.
  """
  animal_sounds = {
    "dog": "Woof!",
    "cat": "Meow!",
    "cow": "Moo!",
    "pig": "Oink!",
    "sheep": "Baa!",
  }
  while True:
    animal = input("Enter an animal name (or type 'quit' to exit): ").lower()
    if animal == 'quit':
      break
    if animal in animal_sounds:
      print(f"The {animal} says: {animal_sounds[animal]}")
    else:
      print("I don't know the sound of that animal. Try again!")
animal_sounds() 

