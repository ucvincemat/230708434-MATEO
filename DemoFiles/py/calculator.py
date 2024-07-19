# MATEO, Vince N.

#'''''''.......#
programIsAlive = True
calcStates = ('1','2','3','4','5')
evalStates = ('Q','W','E','R','X','q','w','e','r','x')

lineDivider = "--------------------------------------"
goodbyeMsg = """--.--|              |                        
  |  |---.,---.,---.|__/     ,   .,---..   . 
  |  |   |,---||   ||  \     |   ||   ||   | 
  `  `   '`---^`   '`   `    `---|`---'`---' 
                             `---'           
                                             
         for using CLS Calculator™!          
          ~ Have a wonderful day! ~          
"""

#'''''''.......#
class Calculator:
    def plus(self, xop, yop):
        return xop + yop        # baisc addition           
    def minus(self, xop, yop):
        return xop - yop        # basic subtraction
    def times(self, xop, yop):
        return xop * yop        # basic multiplication
    def over(self, xop, yop):
        return xop / yop        # basic division
    def power(self, xop, yop):
        return xop ** yop       # basic exponentiation

class Evaluator:
    def __init__(self, num):
        self.integer = num
    def isOdd(self):
        return self.integer % 2 != 0     # check if it its not divisible by 2
    def isEven(self):
        return self.integer % 2 == 0     # check if it is divisible by 2
    def isPositive(self):
        return self.integer > 0          # check if more than zero (positive)
    def isNegative(self):
        return self.integer < 0          # check if less than zero (negative)

def floatCastCheck(x):
    try:
        float(x)
        return True
    except:
        return False

def intCastCheck(x):
    try:
        int(x)
        return True
    except:
        return False

def displayOptions():
    print(
        "Program functions:\n",
        "[1] Add Two Numbers",
        "[2] Subtract Two Numbers",
        "[3] Multiply Two Numbers",
        "[4] Divide Two Numbers",
        "[5] Exponentiate\n",
        "[Q] Check if a Number is Odd",
        "[W] Check if a Number is Even",
        "[E] Check if a Number is Positive",
        "[R] Check if an Integer is Negative\n",
        "[X] Exit the program",
    sep = "\n")

#'''''''.......#
print("Welcome to CLS Calculator™!\n", lineDivider)
calculator = Calculator()

#'''''''.......#
while programIsAlive:
    displayOptions()
    print(lineDivider)
    modeOfOperation = input("Enter your choice: ")
    if modeOfOperation not in calcStates + evalStates:
        print("Invalid Command! Please input a valid option.")
        continue

    elif modeOfOperation.upper() == 'X':
        print(goodbyeMsg)
        programIsAlive = False
        break
    
    elif modeOfOperation.isnumeric(): # Calculate
        while True:
            print(lineDivider)
            firstOperand = input("First Operand: ")
            secondOperand = input("Second Operand: ")
            print(lineDivider)

            if floatCastCheck(firstOperand):
                firstOperand = float(firstOperand)
            else:
                print("<!> Value invalid! Please try again!")
                continue
            
            if floatCastCheck(secondOperand):
                secondOperand = float(secondOperand)
            else:
                print("<!> Value invalid! Please try again!")
                continue


            if modeOfOperation == '1':
                result = calculator.plus(firstOperand, secondOperand)
            elif modeOfOperation == '2':
                result = calculator.minus(firstOperand, secondOperand)
            elif modeOfOperation == '3':
                result = calculator.times(firstOperand, secondOperand)
            elif modeOfOperation == '4':
                if secondOperand != 0: result = calculator.over(firstOperand, secondOperand)
                else: result = "Math ERROR: Cannot divide by zero"
            elif modeOfOperation == '5':
                result = calculator.power(firstOperand, secondOperand)
            break

    elif modeOfOperation.isalpha(): # Evaluate
        while True:
            print(lineDivider)
            number = input("Input number: ")
            print(lineDivider)

            if floatCastCheck(number):
                number = float(number)
            else:
                print("<!> Value invalid! Please try again!")
                continue

            numberCheck = Evaluator(number)
            if modeOfOperation.upper() == 'Q':
                result = numberCheck.isOdd()
            elif modeOfOperation.upper() == 'W':
                result = numberCheck.isEven()
            elif modeOfOperation.upper() == 'E':
                result = numberCheck.isPositive()
            elif modeOfOperation.upper() == 'R':
                result = numberCheck.isNegative()
            break
    
    if modeOfOperation in calcStates and intCastCheck(result): result = int(result)
    
    print("RESULT:", result, '\n', lineDivider)
    
    while True:
        runAgain = input("Would you like to do more calculations? (Y/N) ")

        if runAgain.upper() not in ('Y','N'):
            print("Please type Y or N!")
        elif runAgain.upper() == 'N':
            print(lineDivider, goodbyeMsg, sep="\n")
            programIsAlive = False
            break
        elif runAgain.upper() == 'Y':
            print(lineDivider)
            break