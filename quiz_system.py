print("QUIZ GAME WITH PASSWORD AND MARKING SYSTEM")
print("WELCOME")
print()# to add space
score=0 # defining score variable
# password
a="123"
passw=input("enter your password: ")
if passw==a:
    # quiz
    #Q1
    ans1=input(f"ques1: who is th founder of Pakistan? \n enter your answer: ")
    if ans1.lower()== "quaid-e-azam":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"wrong,you got {score} score")
        
    #Q2
    ans2=input(f"ques2: What is the only planet in our solar system known to support life? \n enter your answer: " )
    if ans2.lower()== "earth":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")
        
    #Q3   
    ans3=input(f"ques3: Which continent is also a country? \n enter your answer: ")
    if ans3.lower()== "australia":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")
        
    #Q4
    ans4=input(f"ques4: In which city is the Eiffel Tower located? \n enter your answer: ")
    if ans4.lower()== "paris":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")
        
    #Q5
    ans5=input(f"ques5: Which force pulls objects toward the center of the Earth? \n enter your answer: ")
    if ans5.lower()== "gravity":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")
        
    #Q6
    ans6=input(f"ques6: Which organ is responsible for pumping blood throughout the human body? \n enter your answer: ")
    if ans6.lower()== "heart":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")
        
    #Q7    
    ans7=input(f"ques7: What is the frozen form of water called? \n enter your answer: ")
    if ans7.lower()== "ice":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")
        
    #Q8
    ans8=input(f"ques8:What is the opposite of 'slow'? \n enter your answer: ")
    if ans8.lower()== "fast":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")
        
    #Q9
    ans9=input(f"ques9: How many fingers does a typical human have on one hand? \n enter your answer: ")   
    if ans9.lower()== "five" or "5":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")
        
    #Q10
    ans10=input(f"ques10: What do you call the day after today? \n enter your answer: ")
    if ans10.lower()== "tomorrow":
        score+=1 # add points to the score variable
        print(f"correct,you got 1 point")
        print(f"your total score is {score} ")
    else:
        print(f"wrong,you got 0 point")
        print(f"your total score is {score} ")

    print() # to add space in output

    print(f"your total score is {score}/10")  # gives total score

    print() # to add space in output

    percentage=(score/10)*100 # calculate the percentage
    
    print(f"your percentage if {percentage}%") # prints percentage

    print() # to add space in output

    # grading system
    if percentage>=90 and percentage<=100:
        print("Your grade is A+ ")
    elif percentage>=80 and percentage<=89: 
        print("Your grade is A") 
    elif percentage>=70 and percentage<=79:
        print("Your grade is B+")   
    elif percentage>=60 and percentage<=69:
        print("Your grade is B")
    elif percentage>=50 and percentage<=59:
        print("Your grade is C")
    else:
        print("fail")
    # retry
k=input("press t if you want to try again or e for exit: ")
if k == "t":
    print("press ctrl+F5 to start again")
else:
    print("Good bye!")
