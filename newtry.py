import numpy as np



def passw(N):
    success = 0

    for j in range (N):
        realPass = np.random.randint(0, 456977) #create a random assigned password
        dodol=np.random.randint(0,456977,330000) #create a list of m random passwords
        if realPass in dodol: #check if the list has the assigned password
            success=success+1
    print ('success probabilit is :',(success/N))

