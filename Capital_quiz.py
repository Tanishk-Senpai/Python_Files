import random

state_capital = {'Haryana':'Chandigarh','Rajasthan':'Jaipur'}
state = list(dict.fromkeys(state_capital))
capital = list(dict.values(state_capital))

correct_answers = 0
wrong_answers = 0
while True:
    random_num = random.randrange(0, 2)

    print("Guess the capital of this state:", state[random_num], end='\n')
    capital_input = input()
    if capital_input.lower() == capital[random_num].lower():
        print("Correct!")
        correct_answers += 1
    elif capital_input.lower() != capital[random_num].lower():
        print("Wrong")
        wrong_answers += 1
    loop = input("do you want to play again? (y/n): ")
    try:
        if loop.lower() == 'y':
            continue
        elif loop.lower() == 'n':
            break
        else:
            raise Exception
    except:
        print("Invalid input")
        loop = input("do you want to play again? (y/n):")
        if loop.lower() == 'y':
            continue
        elif loop.lower() == 'n':
            break

print(f"Total Correct Answers: {correct_answers}")
print(f"Total Wrong Answers: {wrong_answers}")