import sys
import os
import random
import shutil

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Tests for PA1 in each TEST_PA1 test file!")
    else:
        print("Wrong Number of Arguments.")
        exit()

    masterLs = ["implies", "npIMPnq", "nqIMPnp", "iff", "nand", "npANDnq", "nor", "npORnq"]

    perFiles = [50, 60, 70, 80, 90] # percentages
    numFiles = []
    for i in range(len(perFiles)):
        decimal = perFiles[i]*0.01 # 50 -> 0.5
        numFiles.append(round(len(masterLs)*decimal))
        random.shuffle(masterLs)
        testFiles = masterLs[:numFiles[i]]
        print(testFiles)
    
