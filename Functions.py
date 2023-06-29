import numpy as np
import json
filename = 'primeNumbers.json'
ln = lambda n : np.log(n)
pi = '\u03C0'

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

    