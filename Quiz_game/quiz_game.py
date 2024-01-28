print ("\n\t\tWelcome To Quiz Game")
print("\n For each correct answer you Score +1 and for each wrong answer -0.5 is reduced")

start = input('\nDo you want to play ? ')
if start.lower() =='yes' or start.lower() =='y' or start.lower()== 's':
    print ("\nlet's play")
elif start.lower() =='no' or start.lower =='n' :
    print("ok! The end")
    quit()   
else :
    print("Type Yes Or No")
    
if start.lower() =='yes' or start.lower() =='y' or start.lower()== 's':
    score = 0
#question 1 --------------------------------------------------------------------------------------------------------------------------------------
    ans_1 =input('''\nWhat does the 'len()' function do in Python? \na) Returns the total number of elements in a list \nb) Returns the length of a string\nc) Returns the number of characters in a file\nd) Returns the sum of all elements in a list\nEnter the correct option : ''').lower()
    if ans_1 == 'b' :
        print("\ncorrect. (+1) one point is added")
        score +=1
    elif ans_1=='a' or ans_1 =='c' or ans_1 =='d':
        print("\nIncorrect. (-0.5) .5 point is reduced")
        score =score-0.5
    else :
        print("not a Valid Option (a/b/c/d)")
#question 2 ---------------------------------------------------------------------------------------------------------------------------------------
    ans_1 =input('''What is the correct way to define a function in Python?\na) def function_name:\nb) function function_name():\nc) define function_name():\nd) def function_name():\nEnter the correct option :''').lower()
    if ans_1 == 'd' :
        print("\ncorrect. (+1) one point is added")
        score +=1
    elif ans_1=='a' or ans_1 =='c' or ans_1 =='b':
        print("\nIncorrect. (-0.5) .5 point is reduced")
        score =score-0.5
    else :
        print("not a Valid Option (a/b/c/d)")
#question 3 ---------------------------------------------------------------------------------------------------------------------------------------
    ans_1 =input('''\nWhat is the result of the expression 3 + 2 * 4?\na) 20\nb) 15\nc) 11\nd) 17 \nEnter the correct option :''').lower()
    if ans_1 == 'c' :
        print("\ncorrect. (+1) one point is added")
        score +=1
    elif ans_1=='a' or ans_1 =='b' or ans_1 =='d':
        print("\nIncorrect. (-0.5) .5 point is reduced")
        score =score-0.5
    else :
        print("not a  Valid Option (a/b/c/d)")
#question 4 ---------------------------------------------------------------------------------------------------------------------------------------
    ans_1 =input('''\nHow do you check the type of a variable in Python?\na) typeof(x)\nb) typeOf(x)\nc) type(x)\nd) typeof x : \nEnter the correct option :''').lower()
    if ans_1 == 'c' :
        print("\ncorrect. (+1) one point is added")
        score +=1
    elif ans_1=='a' or ans_1 =='b' or ans_1 =='d':
        print("\nIncorrect. (-0.5) .5 point is reduced")
        score =score-0.5
    else :
        print("not a  Valid Option (a/b/c/d)")
#question 5---------------------------------------------------------------------------------------------------------------------------------------
    ans_1 =input('''\nWhich of the following is a valid Python list?\na) [1, 2, 3, "four"]\nb) {1, 2, 3, 4}\nc) (1, 2, 3, 4)\nd) {"one": 1, "two": 2, "three": 3}\nEnter the correct option : ''').lower()
    if ans_1 == 'a' :
        print("\ncorrect. (+1) one point is added")
        score +=1
    elif ans_1=='b' or ans_1 =='c' or ans_1 =='d':
        print("\nIncorrect. (-0.5) .5 point is reduced")
        score =score-0.5
    else :
        print("\nNot a Valid Option (a/b/c/d)")
#score and result----------------------------------------------------------------------------------------------------------------------------------
    total_score = score
    if total_score == 5 :
        print("Great !")
        print("You Scored " ,total_score)
    elif total_score <5 and total_score >=3 :
        print('Good!')
        print("You Scored " ,total_score)
    elif total_score <3 and total_score >0 :
        print("Not Bad !")
        print("You Scored " ,total_score)
    else :
        print("prepare well and try again")
        print("You Scored " ,total_score)
    if total_score > 2 :
        print ("Well Played ! Thank You ")

        
        

