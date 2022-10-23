def routerCost(crtRouter, recvRouter, cost, origin):
    #print(crtRouter)
    #print(recvRouter)
    #print('\n')
    
    #Unsure but worth checking
    return crtRouter;

def routingTableCheck(CurrentT, RecievedT, OrgID, Cost):
    '''After recieving a packet and having it verified the router need to 
    adjust the current rounting table and if changes are made send a response 
    packet to the orginal sender'''
    tmpT = [];
    if CurrentT[OrgID-1][2] == -1:
        CurrentT[OrgID-1][2] = Cost;
    
    for index in range(len(CurrentT)):
        if crtRouter[1] == -1 and recvRouter[1] != -1:
            #Current router has an infinite route to the recvrouter value
            crtRouter[1] = recvRouter[1];
            crtRouter[2] = recvRouter[2] + cost;
        elif crtRouter[1] != -1 and recvRouter[1] != -1:
            #Current Router and RecvRouter both have active paths
            #Check for each and aquire easiest path.
        if crtRouter[2] > recvRouter[2] + cost:
            #recvied route is cheaper in total change path
            crtRouter[2] = recvRouter[2] + cost;
            crtRouter[1] = origin;
            #Else pass no changes to cost path
        elif crtRouter[1] == origin and recvRouter[1] == -1:
            #Path through location has become redundent
            crtRouter[1] = -1;
            crtRouter[2] = -1;
    if tmpT == CurrentT:
        #No changes have been made
        tmpT = 0;
    #Usage will check the type of tmpT of number no send else will broadcast pkt
    return tmpT;

#Testing the New format
router1 = [[1,1,0], [2,2,1], [3,2,4], [4,2,8], [5,6,6], [6,6,6], [7,7,8]]
router2 = [[1,1,1], [2,2,0], [3,-1,-1], [4,-1,-1], [5,1,7], [6,1,6], [7,1,9]]
#router3 = Failed
router4 = [[1,1,1], [2,2,0], [3,-1,-1], [4,-1,-1], [5,5,2], [6,5,3], [7,7,6]]
router5 = [[1,6,6], [2,6,7], [3,4,6], [4,4,2], [5,5,0], [6,6,1], [7,4,8]]
router6 = [[1,1,5], [2,1,6], [3,5,7], [4,5,7], [5,5,1], [6,6,0], [7,5,9]]
router7 = [[1,1,8], [2,1,9], [3,4,10], [4,4,6], [5,4,8], [6,4,9], [7,7,0]]

#def main():
    #routingTableCheck(CurrentT, RecievedT, OrgID, Cost)
    #print(routingTableCheck(router5, router4, 4, 2))
    #Change Propergate
    #print(routingTableCheck(router7, router4, 4, 6))
    #Change Propergate
    #print(routingTableCheck(router6, router5, 5, 1))
    #Change Propergate
    #print(routingTableCheck(router1, router2, 2, 1))
    #Change Propergate
    #print(routingTableCheck(router7, router1, 1, 8))
    #No Change Stop
    #print(routingTableCheck(router6, router1, 1, 5))
    #No Change Stop
    #print(routingTableCheck(router1, router6, 6, 5))
    #Change Propergate
    #print(routingTableCheck(router7, router1, 1, 8))
    #no Change Stop
    #print(routingTableCheck(router2, router1, 1, 1))
    #Nowhere To Send Stop
#main()

#1
print([[1,6,6], [2,6,7], [3,-1,-1], [4,4,2], [5,5,0], [6,6,1], [7,4,8]])
#2
print([[1,1,8], [2,1,9], [3,-1,-1], [4,4,6], [5,4,8], [6,4,9], [7,7,0]])
#3
print([[1,1,5], [2,1,6], [3,-1,-1], [4,5,7], [5,5,1], [6,6,0], [7,5,9]])
#4
print([[1,1,0], [2,2,1], [3,-1,-1], [4,-1,-1], [5,6,6], [6,6,6], [7,7,8]])
#5
print(0)
#6
print(0)
#7
print([[1,1,0], [2,2,1], [3,-1,-1], [4,6,12], [5,6,6], [6,6,6], [7,7,8]])
#8
print(0)
#9
print([[1,1,1], [2,2,0], [3,-1,-1], [4,1,13], [5,1,7], [6,1,6], [7,1,9]])
