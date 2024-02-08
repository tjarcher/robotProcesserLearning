set = "12345678"
hands = "LR"
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
    action = hands[0] + set[0]
    actionIndex = actionSet.index(action) + 1
    actionReward = 0
    for i in range(len(rewards)):
        if rewards[i][0] == set:
            actionReward = int(rewards[i][actionIndex])
            for j in range(len(set)):
                for k in range(len(hands)):
                    potentialAction = hands[k] + set[j]
                    potentialActionIndex = actionSet.index(potentialAction) + 1
                    potentialActionReward = int(rewards[i][potentialActionIndex])
                    if potentialActionReward > actionReward:
                        actionReward = potentialActionReward
                        actionIndex = potentialActionIndex
                        action = potentialAction
    piece = action[1]
    pieceIndex = set.find(piece)
    print("In state " + set + ", the best action is " + action + ", with a reward of " + str(actionReward))
    set = set[:pieceIndex] + set[pieceIndex+1:]


            
