
##create a lis of 4 charecter, all lower case words (80,000words)
##create a random 4 charecter, All lower case word set as password (possibilities are 26**4)
##check to see if password is in the list. Run this experiment N=1000
##calculat the probabilty of password being in the list

import string
import random

KEY_LEN = 4

def key_gen():
    keylist = [random.choice(string.ascii_lowercase) for i in range(KEY_LEN)]
    return ("".join(keylist))

def passWordhacking(N):
    success = 0
    for j in range(N):
        randomPassword=key_gen()
        thePassList=[]
        for i in range(80000):
            thePassList.append(key_gen())
        if randomPassword in thePassList:
            success = success+1
    print("the probability of pass being in passList is: ", (success/N))
