print("Welcome to the choose your own adventure game!")
name = input("What's your name? ")
age = int(input("How old are you? "))
print(f'Hello {name.capitalize()}. You are {age} years old')

is_older = age >= 18
health = 10

if is_older:
  print("You are man enough to play")
  wants_to_play = input("Do you want to play? (yes | no ) ").lower()
else:
  print("Come back later when you are man enough kid!")

if wants_to_play == "yes":
  print("Let's play")

  print(f'You are starting with {health} hp')
  direction = input("Do you want to go left or right? ").lower()
  if direction == "right":
    health = health - 10
    print(
      f"You walk past a camp of bandits and you are striped of all your possession and has {health} hp health left and you die!"
    )
  elif direction == "left":
    print("You saw a village")
    ans = input(
      "Do you enter the village or continue your way (Enter/Continue").lower()

    if ans == "enter":
      print("You meet a swordmaster and become his apprentice")
      print("You become rich. You win")
    elif ans == "continue":
      print("During your journey, you suffer from dehydration and lose health")
      health -= 2
      print(f'Your health is {health} hp')
      ans = input(
        "Ahead, you noticed an oasis and a palace. Which do you go to? (oasis/palace) "
      )

      if ans == "palace":
        health -= 3
        print(
          "You were captured by the guards and sent to the dungeons for 3 days. As a result, you starve and lose health"
        )
        if health <= 0:
          print(f'You now have {health} and you lost the game')
        else:
          print(
            f"You were released from the dungeon and later on become the advisor of the king. Your health is {health}. You win"
          )
        print(f"Your health is {health} hp")
      elif ans == "oasis":
        print("The oasis was a mirage. You die in the desert from dehydration")
        health = 0
        print(f'You now have {health} and you lost the game')
    else:
      "Invalid. Goodbye!"
  else:
    print("invalid command")
elif wants_to_play == "no":
  print("Goodbye!")
else:
  print("Wrong command. Enter either yes or no please!")
