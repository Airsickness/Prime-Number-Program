import json
import numpy as np
import time
import random as rand
import matplotlib.pyplot as plt
ln = lambda n : np.log(n)
filename = 'primeNumbers.json'
print("Initialising. . .")
pi = '\u03C0'
class bcolours:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#FUNCTIONS AND METHODS------------------------------------------
def writeFileJSON(new_data):
    try:
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data["primes"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
            
    except FileNotFoundError:
        print("File not found")
    
    except:
        print("Something else went wrong. . .")
        
def entryCounter():
    try: 
        
        with open(filename, "r") as file:
            data = json.load(file)
            num_of_entries = len(data["primes"])
            return num_of_entries
        
    except FileNotFoundError:
        print("File not found")
    
    except:
        print("Something went wrong. . .")
        
def primeOccurrence():
    with open(filename, 'r') as file:
        data = json.load(file)
        last_element = data['primes'][-1]
        PRIME_OCCURRENCE_INT = last_element / ln(last_element)
        ROUNDED_PRIME_OCCURRENCE = float(f'{PRIME_OCCURRENCE_INT:.0f}')
        
        return ROUNDED_PRIME_OCCURRENCE
    
def primeOccurrenceComparison():
    try:
        print("The number of primes in the list is: ", entryCounter())
    
        with open(filename, 'r') as file:
            data = json.load(file)
            last_element = data["primes"][-1]
        
        print("The estimate for the number of primes between ", 1, " and ", last_element, "\n using the Prime Number Theorem ", pi, "(x)",  " is: ", primeOccurrence())
    except IndexError:
        print("Numbers must be positive integers and not zero. Please run the program again.")
    except ValueError:
        print("Non integer entries are not accepted.")
        
def primeChecker(maxNum, printToFile):
    for num in range(1, maxNum):    
        if num == 1:
            continue
        elif num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                if printToFile == True:
                    writeFileJSON(num)
                else:
                    print(num)
        else:
            print(num,"is not a prime number")
            
def clearFileJSON():
    f = open(filename, "w")
    text = '''{"primes": []}'''
    f.write(text)

    
def lvlOfAccuracy():
    try:
         with open(filename, 'r') as file:
                data = json.load(file)
                last_element = data["primes"][-1]
                num_of_entries = len(data["primes"])
                prime_number_theorem_estimate = last_element / ln(last_element)
                percentage_accuracy = prime_number_theorem_estimate / num_of_entries * 100
                rounded_percentage_accuracy = float(f'{percentage_accuracy:.3f}')
                print("The level of accuracy of the Prime Number Theorem is ", rounded_percentage_accuracy, "%")
    except IndexError:
        print("")
    except:
        print("Something went wrong (not IndexError)")

    


#MAIN CODE------------------------------------------------------

Flag = True 
print("Welcome to the Prime Number Program (PNP).")
while Flag == True:
    try:
        answer_to_intro = input("Do you want primes between 1 and N OR to check a number for factors?       [M/S/T] ")
        if answer_to_intro == "M".lower():
            upperBoundIn = int(input("Enter the number you want primes between (1 to N): "))
            clearFileJSON()
            start_time = time.time()
            print("Looking for primes. . .")
            primeChecker(upperBoundIn, True)
            primeOccurrenceComparison()
            lvlOfAccuracy()
            time_to_run = float((" %s " % (time.time() - start_time)))
            rounded_time_to_run = float(f'{time_to_run:.3f}')
            if rounded_time_to_run <= 5:
                print(bcolours.GREEN + "The program took", rounded_time_to_run, "seconds to execute" + bcolours.ENDC)
            elif rounded_time_to_run > 5 and rounded_time_to_run <= 15:
                print(bcolours.WARNING + "The program took", rounded_time_to_run, "seconds to execute" + bcolours.ENDC)
            else:
                print(bcolours.FAIL + "The program took", rounded_time_to_run, "seconds to execute" + bcolours.ENDC)

        elif answer_to_intro == "S".lower():
            num = int(input("Enter the number N you want to check: "))
            if num == 1:
                print(num, "is not a prime number")
            elif num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        print(num,"is not a prime number")
                        print(i,"times",num//i,"is",num)
                        break
                else:
                    print(num,"is a prime number")


            else:
                print(num,"is not a prime number")

        elif answer_to_intro == "T".lower():
            print("Terminating. . .")
            rand_sleep = rand.randint(1, 3)
            time.sleep(rand_sleep)
            Flag = False
            print("Program Terminated")

        else:
            print("Enter either M for Multiple, S for Single, or T for Terminate")
    except ValueError:
        print("Please enter positive integers only")