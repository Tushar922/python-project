
playing = True

while True:
  print("Welcome to The Mysterious Forest!")
  print("1. Enter the forest")
  print("2. Quit")
  choice = input("Enter your choice: ")

  if choice == "1":
    print("You step into the dense forest, sunlight filtering through the leaves.")
    print("A path winds ahead, leading deeper into the unknown.")
    print("1. Follow the path")
    print("2. Explore the nearby jungle")
    choice2 = input("Enter your choice: ")

    if choice2 =="2":
      print("returned to home")
      print("completed game")
      break
    if choice2 == "1":
      print("You follow the path, its twists and turns revealing strange plants and curious creatures.")
      print("Suddenly, you reach a crossroads... but strange creature are following")
      print("1. Go left")
      print("2. Go right")
      choice3 = input("Enter your choice: ")

      if choice3 == "1":
        print("u head to the cave")
        print("1. go inside cave")
        print("2. go back")
        choicec=input("enter ur choice:")
        if choicec=="2":
          print("game over \nThanks for playing")
          break
        if choicec=="1":
          print("this cave has some food")
          print("1. eat food in cave")
          print("2. carry food and eat it in a safe place")
          choicei=input("enter ur choice")
          if choicei=="1":
            print("game over killed by strange creature\nThanks for playing")
            break
          if choicei=="2":
            print("safe from that strange creature \nwhere should i go")
            print("1. go to blood village")
            print("2. go to magical tree and eat food")
            choiceop=input("Enter ur choice:")
            if choiceop=="1":
              print("game over killed by bloody creature\n Thanks for playing")
              break
            if choiceop=="2":
              print("game break")
      if choice3 == "2":
        print("u found monster")
        print("1.touch monster")
        print("2.ignite fire")
        choiceo=input("Enter ur choice:")
        if choiceo=="1":
          print("game over monster killed u")
          print("Thanks for playing")
          break
        if choiceo=="2":
          print("game over monster awake\nThanks for playing")
          break
    elif choice2 == "2":
      print('game over stepped into wild flower ')
      break   
  
  elif choice == "2":
    playing = False
    print("Thank you for playing!")

  
  else:
    print("Invalid choice. Please try again.")