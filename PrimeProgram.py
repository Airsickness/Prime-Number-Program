import json
import numpy as np
import time
import random as rand
from Functions import *
print("Initialising. . .")
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