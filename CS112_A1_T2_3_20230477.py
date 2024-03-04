#file: CS112_A1_T2_3_20230477.py
#Purpose: Number scramble --> to obtain 3 numbers from 1 to 9 that sum up to 15
#Youssef Ahmed Adel Sabry Elkashef
#20230477

lst = [1,2,3,4,5,6,7,8,9] #main list
lst1 = [] #list for player 1
lst2 = [] #list for player 2
print("Welcome to Number scrabble game\n ")
print("Each player takes turn to pick a number from 1 --> 9\n")
print("the first player to collect numbers that sum up to 15 WINS\n")


def has_sum_of_15(numbers):#Function to check if the sum of any three numbers in a list is equal to 15
    if len(numbers) < 3:
        return False
    for i in range(len(numbers)):
        remaining_numbers = numbers[:i] + numbers[i + 1:]
        if has_sum_of_15(remaining_numbers):
            return True
        if sum(remaining_numbers) == 15 - numbers[i]:
            return True
    return False
while lst != []: # Main loop runs until the list is empty
    while True:# takes input from player 1 and checks that the number is in the list
        print(lst)
        move1 = int(input("player 1: "))
        if move1 in lst:
            lst1.append(move1)
            lst.remove(move1)
            break
        else:
            if move1 > 9 or move1 == 0:
                print("Pick a number from 1 - 9")
            else:
                print("number has alredy been chosen")
    if has_sum_of_15(lst1):#Checks if player 1 won
        print("player 1 wins")
        break
    else:
        pass
    if lst == []:#Checks if it is a draw
        print("DRAW")
        break
    while True:# takes input from player 2 and checks that the number is in the list
        print(lst)
        move2 = int(input("player 2: "))
        if move2 in lst:
            lst2.append(move2)
            lst.remove(move2)
            break
        else:
            if move1 > 9 or move1 == 0:
                print("Pick a number from 1 - 9")
            else:
                print("number has alredy been chosen")
    if has_sum_of_15(lst2):#check if player 2 won
        print('player2 wins')
        break
    else:
        pass
    