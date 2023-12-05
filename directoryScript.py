import sys
import os
import random
import shutil

if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        print("Wrong Number of Arguments.")
        exit()

    masterLs = []
    otherFiles = []
    for filei in os.listdir("./" + directory):
        if "_test" in filei:
            masterLs.append(filei)
        else:
            otherFiles.append(filei)

    print(otherFiles)
    perFiles = [50, 60, 70, 80, 90] # percentages
    numFiles = []
    for i in range(len(perFiles)):
        decimal = perFiles[i]*0.01 # 50 -> 0.5
        numFiles.append(round(len(masterLs)*decimal))
        random.shuffle(masterLs)
        testFiles = masterLs[:numFiles[i]]
        print(testFiles)
        newTestDir = directory + "_" + str(perFiles[i])
        os.mkdir(newTestDir)
        for fname in testFiles:
            shutil.copy2(directory + "/" + fname, newTestDir)
        for fname in otherFiles:
            if os.path.isdir(directory + "/" + fname):
                shutil.copytree(directory + "/" + fname, newTestDir + "/" + fname)
            else:
                shutil.copy2(directory + "/" + fname, newTestDir)
    
