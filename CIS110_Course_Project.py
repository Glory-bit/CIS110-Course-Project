print(f"Hello there! Today we have a story about a hungry man. Let's see what happens to him.")
print(f"We have a few qustions for you before the story begins. Don't worry there are no wrong answers!")
print(f"After typing your answers make sure to press the enter key.")
input(f"\nPress the enter key to continue...")
keepPlaying = "yes"
while keepPlaying.lower() == "yes":
        print(f"\nLets answer some questions!")
        userName = input(f"\nWhat is the man's name? ")
        while len(userName) == 0:
            userName = input(f"Please name the man. ")
        yogurtType = input("what is the flavor of the yogurt?: ")
        while len(yogurtType) == 0:
            yogurtType = input(f"Please enter a flavor. ")
        pizzaType = input("What kind of pizza does the man have?: ")
        while len(pizzaType) == 0:
            pizzaType = input(f"Please give a type of pizza. ")
        manJob = input("Where does the man work?: ")
        while len(manJob) == 0:
            manJob = input(f"Please enter a workplace. ")
        jobTransport = input("How does the man get to work?: ")
        while len(jobTransport) == 0:
            jobTransport = input(f"Please enter how the man gets to work. ")
        print(f"Lets get this story started! ")
        input(f"\nPress the enter key to continue...")
        print(f"\nThis story begins in the very comfy bed of a man named {userName}. ")
        print(f"This morning {userName} is feeling hungry and decides to get out of bed to go to the kitchen. ")
        print(f"In the kitchen {userName} opens the fridge and sees some {yogurtType} yogurt. ")
        maneatYogurt = input(f"\nShould {userName} eat the {yogurtType} yogurt? Type yes or no: ")
        while len(maneatYogurt) ==0:
            maneatYogurt = input(f"Please Type yes or no: ")
        if maneatYogurt == "yes":
            print(f"\n{userName} grabs a spoon and eats the {yogurtType} yogurt. ")
            print(f"Right after finishing the yogurt the man sees the expiration date. ")
            print(f"This yogurt expired 3 days ago! It tasted fine though. ")
            print(f"{userName} thinks he shold be alright since the yogurt tasted fine! ")
        else:
            print(f"\n{userName} inspects the yogurt but sees it expired 3 days ago. ")
            print(f"Since the yogurt is expired the man does not eat the yogurt. ")
            print(f"After all he doesn't want to get sick from expired food right before work. ")
            print(f"\nThe man is still feeling hungry. ")
            input(f"\nPress the enter key to continue...")
            print(f"In the fridge is also some {pizzaType} pizza from the night before. ")
        maneatPizza = input(f"\nShould {userName} eat the leftover {pizzaType} pizza from last night? Type yes or no: ")
        while len(maneatPizza) == 0:
            maneatPizza = input(f"Please Type yes or no: ")
        if maneatPizza =="yes":
            print(f"\n{userName} grabs the pizza box and opens it up for a slice. ")
            print(f"The pizza still looks and smells fine. ")
            print(f"The pizza will make a great breakfast since its just from last night!  ")
            print(f"{userName} eats the biggest slice in the box. ")
        else:
            print(f"\n{userName} takes a second to look at the box. .")
            print(f"He decides he should just get ready for work. ")
            print(f" He's going to have lunch at that new joint anyways! ")
        print(f"His phone starts ringing. It's his alarm for work! Oh no he is going to be late for his job at {manJob}! ")
        print(f"{userName} heads towards the {jobTransport} to head to work. ")
        input(f"\nPress the enter key to continue...")
        if maneatYogurt == "yes" and maneatPizza == "yes":
            print(f"\nAfter {userName} gets to work he starts to not feel well. ")
            print(f"He rushes to the bathroom where he becomes increasingly sick. ")
            print(f"He definitely shouldn't have eaten that {yogurtType} yougurt or the {pizzaType} pizza! ")
            print(f"{userName} goes to his boss and asks if he can go home. ")
            print(f" His boss at {manJob} sees how sick {userName} is and sends him home from work to rest. ")
        elif maneatYogurt == "no" and maneatPizza == "no":
            print(f"\n{userName} Makes it to work and has a very productive day. ")
            print(f"He even got to eat at that new lunch spot with his work crush! ")
            print(f"At the end of the day {userName} heads home to enjoy his night. ")
        else:
            print(f"\n{userName} makes it to work and notices his stomach hurts a little. ")
            print(f"throughout the day {userName} has to use the restroom more than normal. ")
            print(f"Since his stomach hurts he decides to not go to lunch at that new place down the street. ")
            print(f"At the end of the workday the man goes home and goes to bed hoping he will feel better tomorrow. ")
        print("\nTHE END")
        keepPlaying = input(f"\nDo you want to play again? Type yes or no: ")
        while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
         keepPlaying = input(f"Please type yes or no: ")