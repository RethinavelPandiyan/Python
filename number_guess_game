from random import randint                        import sys                                        def stage(level):                                     print(f"Great!You have select the {level} difficulty level.\nLet's start the game!\n")          print("Welcome to The Number Guessing Game!\nI'm t
hinking of a number between 1 and 100.\nYou have 5
 chances to guess the correct number.\n\nPlease se
lect the difficulty level:\n1.Easy (10 chances)\n2
.Medium (5 chances)\n3.Hard (3 chances)")
level=int(input("\nEnter your choice:"))          print("\n")
stage_level=0
if level==1:
    stage("Easy")
    stage_level=10                                elif level==2:
    stage("Medium")
    stage_level=5                                 elif level==3:                                        stage("Hard")
    stage_level=3                                 else:                                                 print("Incorrect choice.")                        sys.exit()                                    system_guess=randint(1,50)
start=0
print(system_guess)                               while(start<stage_level):
    start=start+1
    user_guess=int(input("Enter your guess: "))
    if user_guess==system_guess:
        print(f"\nCongratulations! You guessed the
 correct number in {start} attempts.")
        sys.exit()
    else:
        if user_guess<system_guess:
            print(f"\nIncorrect!The number is grea
ter than {user_guess}.")
        else:
            print(f"\nIncorrect!The number is less
 than {user_guess}.")
print("\nYou Failed the Game!.")