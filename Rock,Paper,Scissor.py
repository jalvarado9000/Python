import random
test_seed = int(input("insert a random seed number "))
random.seed(test_seed)

while True:
    user_input = int(input("select 0 for rock, 1 for paper, 2 scissors "))
    random_integer = random.randint(0,2)
    print("\n\n")
    # Rock Paper Scissors ASCII Art


    Rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    Paper = '''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    '''

    Scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    game_op = [Rock,Paper,Scissors]






    if user_input == 0:
        print("You selected \n Rock")
        print(game_op[user_input])
        if random_integer  == 0:
            print("Computer selected \n Rock")
            print(game_op[random_integer])
            print("Its a Draw")
        elif random_integer == 1:
            print("Computer selected \n Paper")
            print(game_op[random_integer])
            print("You Loose")
        else:
            print("Computer selected \n Scissors")
            print(game_op[random_integer])
            print("You Win")
            
    elif user_input == 1:
        print("You selected \n Paper")
        print(game_op[user_input])
        if random_integer  == 0:
            print("Computer selected \n Rock")
            print(game_op[random_integer])
            print("You Win")
        elif random_integer == 1:
            print("Computer selected \n Paper")
            print(game_op[random_integer])
            print("Its a Draw")
        else:
            print("Computer selected \n Scissors")
            print(game_op[random_integer])
            print("You Loose")
            
    else:
        print("You selected \n Scissors")
        print(game_op[user_input])
        if random_integer  == 0:
            print("Computer selected \n Rock")
            print(game_op[random_integer])
            print("You Loose")
        elif random_integer == 1:
            print("Computer selected \n Paper")
            print(game_op[random_integer])
            print("You Win")
        else:
            print("Computer selected \n Scissors")
            print(game_op[random_integer])
            print("Its a Draw")
               
        

        






