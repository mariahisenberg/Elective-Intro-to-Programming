num1=10 
num2= 5
def do_math():
    quiz=float(input(f"what is {num1}+ {num2}: "))
    # print(quiz)

    answer= num1 + num2
    # print(answer)
    
    while quiz != answer:
    print("i'm sorry. that is not the correct answer. please try again.")
    do_math()

    print(f"congrats. the correct answer is {answer}")

 do_math()
