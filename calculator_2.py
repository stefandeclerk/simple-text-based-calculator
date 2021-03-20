import pyinputplus as pyip
import sys

print ("\nWelcome to the Weird Ass Calculator\n\n")

while True:
    task = input("What would you like to do? add, subtract, multiply, divide? ")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    sign = ["plus", "minus", "times", "divided by"]

    action = [(int(num1) + int(num2)),
              (int(num1) - int(num2)),
            (int(num1) * int(num2)),
              (int(num1) / int(num2))]

    def choose():
        if task == "add":
            print (action[0])
        elif task == "subtract":
            print (action[1])
        elif task == "multiply":
            print (action[2])
        elif task == "divide":
            print (action[3])

    def calc():
        if task == "add":
            return sign[0]
        elif task == "subtract":
            return sign[1]
        elif task == "multiply":
            return sign[2]
        elif task == "divide":
            return sign[3]
  
    print (f"\nAnswer: {num1}", (calc()), f"{num2} is ", end='')
    choose()
    
    prompt = (f"\nWould you like to do another calculation? ")
    another = pyip.inputYesNo(prompt)

    if another == "no":
        sys.exit()

        
             

  


     


