import random
set = "12345678"
rewards = []
rewardFileRead = open("rewards.txt", "r")
numLines = sum(1 for _ in rewardFileRead)
rewardFileRead.seek(0)
numStates = numLines / 17

for b in range(int(numStates)):
    rewards.append(["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"])
for c in range(len(rewards)):
    for d in range(len(rewards[c])):
        temp = rewardFileRead.readline()
        rewards[c][d] = temp[:len(temp)-1]
rewardFileRead.close()

actionSet = ["L1", "R1", "L2", "R2", "L3", "R3", "L4", "R4", "L5", "R5", "L6", "R6", "L7", "R7", "L8", "R8"]
while set != "":
    actionInd = random.randint(0,len(set)-1)
    hands = ["L", "R"]
    action = set[actionInd]
    hand = hands[random.randint(0,1)]
    action = hand + action
    column = actionSet.index(action) + 1
    newSet = set[:actionInd] + set[actionInd+1:]
    oldSet = set
    set = newSet
    
    
    score = input('Action ' + action + ' was taken, please input reward:')

    tableCheck = 0
    for i in range(len(rewards)):
        if rewards[i][0] == oldSet:
            tableCheck = 1
            row = i

    if tableCheck == 1:
        rewards[row][column] = score
    else:
        newRow = [oldSet, "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        newRow[column] = score
        rewards.append(newRow)

rewardsFile = open("rewards.txt","w")
for j in range(len(rewards)):
    for k in range(len(rewards[j])):
        rewardsFile.write(rewards[j][k])
        rewardsFile.write('\n')
      
rewardsFile.close()

#for i in range(len(rewards)):
    #print(rewards[i])
    

    