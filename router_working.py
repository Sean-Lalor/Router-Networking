import socket#server
import select
import sys
#from datetime import datetime
import calendar
import time
import random

udp_host = '127.0.0.1'; #Host IP
bufferSize  = 1024;
Router_Limit = 7;
periodic_Timer = 1.5;
time_Out = periodic_Timer*6;

def routingTableCheck(CurrentT, RecievedT, Cost, Origin):
    '''After recieving a packet and having it verified the router need to 
    adjust the current rounting table and if changes are made send a response 
    packet to the orginal sender'''
    
    tmpT = [];
    for ID in range(len(RecievedT)):
        "Both will always match in length"
        if CurrentT[ID][2] > RecievedT[ID][2] + Cost:
            #If impossibe on router will be overridden and if smaller will adjusted
            tmpT.append([ID+1, Origin, RecievedT[ID][2]+Cost]);
        elif CurrentT[ID][1] == Origin and RecievedT[ID][2] == 16:
            #Failed route through router discontinue
            tmpT.append([ID+1, 0, 16]);
        else:
            tmpT.append(CurrentT[ID]);
    if tmpT == CurrentT:
        tmpT = 0;
    return tmpT;

def displayTable(table):
    print("RIP router 2.42")
    for router in table:
        #MaKE mEEE prETtY
        if router[1] != 0:
            print("ID: ", router[0], " ParentID: ", router[1], " Cost: ", router[2]);
        else:
            print("ID: ", router[0], " Router unreachable");
    print("");
    pass;
    
def number_of_socks(udp_host, input_list, sock_draw):
    """ """
    for sock_num in range(0, len(sock_draw)):
        #takes input file and creates a socket for each port available
        sock_draw[sock_num] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
        sock_draw[sock_num].bind((udp_host, int(input_list[sock_num])));
    return sock_draw;
        
def port_List(out_list):
    '''Keeps the main tidy converts all ports into ints for ease of access'''
    port_list = [];
    parentList = [];
    cost = [];
    for index in range(len(out_list)):
        port_list.append(int(out_list[index][0]));
        cost.append(int(out_list[index][1]));
        parentList.append(int(out_list[index][2]));
    return port_list, parentList, cost;
        
def hexConversion(inputString):
    '''Takes the string and returns a string of hex values'''
    final = "";
    for item in inputString:
        current = str(hex(ord(item))[2:]);
        final += current + " ";
    #Cut the excess off final
    final = final.rstrip(final[-1])
    return final;
    
def headerfunction(cost, nextRouter, Origin, metric = 0):
    '''Sets up the function for transport creating the header less the checksum'''
    frontEnd = '';
    command = "00"
    version = " 02"
    source = " 00 0" + str(Origin)
    address_family = " 00 00 00 0" + str(Origin);
    dest = " 00 00 00 0" + str(nextRouter)
    the_Void = " 00 00 00 00 00 00 00 00"
    metric = metric + cost;
    the_Metric = " 00 00 00 "
    if (len(str(metric))) < 2:
        the_Metric += "0" + str(metric);
    else:
        the_Metric += str(metric);
    frontEnd += command + version + source + address_family + dest + the_Void + the_Metric    
    return frontEnd;
    
################################parser##########################################

def parser(fileText):
    """Recieves the input text of a config file reads through and if it passes all
    requied checks returns a list of tuples including all relavent data else
    returns appropriate error
    file should be in the form
    ('routerId ')Number/n('input-ports ') Number(', ')*('output-ports ') Number1('-')Number2('-')Number3(', ')*
    If successful returns in the form
    [routerId, [ID_num]*, [(o_num, cost, out_ID)*]]
    """
    #defined values
    line_1 = 'router_ID ';
    line_2 = 'input-ports ';
    line_3 = 'output-port ';
    input_list = [];
    temp_num = '';    
    temp_out = '';    
    output_list = [];
    test_num = 10;
    ID_num = '';    
    failed = False;
    
    if line_1 != fileText[0:10]:
        ID_num = "First line not correct format\n";
        failed = True;

    if failed == False and test_num != len(fileText)-1:
        while fileText[test_num].isnumeric() == True:
            ID_num += fileText[test_num];
            test_num += 1;
            if len(ID_num) == 0:
                ID_num = "No ID given\n";
    
    if int(ID_num) < 1 or int(ID_num) > 64000 and failed == False:
        failed = True;
        ID_num = "Id_num not within apropriate range\n";
            
    if line_2 != fileText[test_num: test_num+12] and failed == False:
        ID_num = "Second line not correct format\n";   
        failed = True;
        
    test_num += 12;
    
    if failed == False and test_num != len(fileText)-1:
        while fileText[test_num-1].isalpha() != True:
            if fileText[test_num].isnumeric() == True:
                temp_num += fileText[test_num];
            else:
                if temp_num != '':
                    input_list.append(temp_num);
                    temp_num = '';
            test_num += 1;
    if temp_num != '':
        input_list.append(temp_num);
    test_num -= 1;
    
    
    if len(input_list) == 0 and failed == False:
        failed = True;
        ID_num = "No Input Ports given";
    
    for port in input_list:
        if int(port) > 1024 and int(port) < 64000:
            Id_num = "Input ports not in range";
    
    if line_3 != fileText[test_num: test_num+12] and failed == False:
        ID_num = "Third line not correct format";     
        failed = True;
        
    test_num += 12;
    
    if failed == False and test_num != len(fileText)-1:
        while test_num != len(fileText):
            if fileText[test_num] != ' ':
                temp_out += fileText[test_num];
            else:
                output_list.append(temp_out);
                temp_out = '';
            test_num += 1;
        
    if temp_out != '':
        output_list.append(temp_out);
    out_list = [];
    for item in output_list:
        out_list.append(tuple(item.split('-')));
    
    if len(out_list) == 0 and failed == False:
        failed = True;
        ID_num = "No Output Ports given\n";    
    
    for port in out_list:
        if int(port[0]) < 1024 or int(port[0]) > 64000:
            ID_num = "Output ports not within range";
    
    if failed == True:
        return ID_num, None, None;
    else:
        return [ID_num, input_list, out_list];
    
def reconstruct(data):
    '''takes the data recieved and converts it back to an appliable format'''
    data = data.split(" ")
    #print(data)
    failed = False;
    frontEnd = '';
    command = data[0]
    version = data[1]
    source = data[2:4]
    address_family = data[4:8];
    dest = data[8:12];
    the_Void = data[12:20]
    metric = data[20:24]
    if command != "00":
        print("Error reading command discarding packet")
        failed = True;
    if version != "02" and failed == False:
        print("Error reading version type: expected type 2")
        failed = True;
    if source[0] != "00" and failed == False and int(source[1]) > Router_Limit:
        failed = True;
        print("Error reading Source from Packet")
    cost = int(metric[-1])
    OrgID = int(address_family[-1])
    tableData = data[24:]
    bracketCount = 0;
    final = []
    for item in tableData:
        current = chr(int(item, 16));
        if current == "[":
            bracketCount += 1;
            #Start new internal list
            newList = [];
            currentNum = '';
        if current == "]" and bracketCount != 1:
            bracketCount -= 1;
            #End of internal list add to the main list
            final.append(newList)
        if current != "[" and current != "]":
            #Internal of list
            if current == ",":
                newList.append(int(currentNum))
                currentNum = ''
            else:
                currentNum += current
        elif len(final) == 7 and len(final[-1]) != 3:
            newList.append(int(currentNum))
    return final, cost, OrgID;

############################## parser ##########################################
        
def open_config(filename):
    """read of each line add it to a single string and then return the string"""
    file = open(filename, 'r');
    lines = file.readlines();
    data = "";
    for line in lines:
        data += line;
    dat_list = data.split('\n');
    final = '';
    for dat in dat_list:
        final += dat;
    return final;

def main():
    router_file = sys.argv[1];
    data = open_config(router_file);
    #ID_num has 2 functions if succesful contains this routers ID else is error
    ID_num, input_list, out_list = parser(data);
    #Has the parser returned a properly processed file
    if type(input_list) == type(None):
        #No End fuction Before Initialisation
        print("Error config file failure");
        print(ID_num);
    else:
        #Yes create sock_draw and establish sockets
        sock_draw = len(input_list)*[0];
        #Add the current router to the table
        #Frame [[ID_Router, Parent, Cost]]
        CurrentT = [];
        for row in range(1, Router_Limit+1):
            if row == int(ID_num):
                CurrentT.append([int(ID_num), int(ID_num), 0]);
            else:
                CurrentT.append([row, 0, 16])
        sock_draw = number_of_socks(udp_host, input_list, sock_draw);
        #Outgoing socket is sock_draw[0] in all cases
        portList, parentList, cost = port_List(out_list);
        timerDict = {}
        trigger_delay = 0;
        delay = 4;
        
        while(True):
            '''Send and recieve my homies'''
            #Generate a random value
            rng_Value = random.random();
            addage = 0.4 * rng_Value;
            #Randomised packet sending
            time.sleep(0.8 + addage);
            
            for index in range(len(portList)):
                address = (udp_host, portList[index]);
                #Standard message Origin is current ID number
                #print(address, portList[index])
                PacktTable = []
                for router in CurrentT:
                    #If router parent is nexthop set to "infinite"
                    if router[1] == parentList[index]:
                        PacktTable.append([router[0],0,16])
                    else:
                        PacktTable.append(router)
                        
                msg_String = str(PacktTable);
                msg_String = hexConversion(msg_String);
                #Standard update
                frontEnd = headerfunction(cost[index], parentList[index], ID_num);
                msg_String = frontEnd + " " + msg_String;
                msg = bytearray(msg_String.encode("utf-8"));
                sock_draw[0].sendto(msg, address);
                
                if trigger_delay <= calendar.timegm(time.gmtime()):
                    #Standard update
                    read, _, _ = select.select(sock_draw, [], [], 2);
                else:
                    #Ignore updates til trigger clears
                    read = [];
                
                for incoming in read:                
                    #Save message from port
                    data, addr = incoming.recvfrom(bufferSize);
                    msg_Recieved = data.decode("utf-8");
                    RecvTable, Cost, OrgID = reconstruct(msg_Recieved);
                    Temp = routingTableCheck(CurrentT, RecvTable, Cost, OrgID);
                    if Temp != 0:
                        #New Table make change
                        CurrentT = Temp;
                        displayTable(CurrentT)
                        trigger_delay = calendar.timegm(time.gmtime()) + delay;
                    timerDict[OrgID] = calendar.timegm(time.gmtime())+time_Out; 
                    
            failedID = [];        
            for ID in timerDict:
                if timerDict[ID] < calendar.timegm(time.gmtime()):
                    failedID.append(ID)
                    exchange = [];
                    for router in CurrentT:
                        if router[1] == ID:
                            exchange.append([router[0], 0, 16])
                        else:
                            exchange.append([router[0], router[1], router[2]])
                    CurrentT = exchange;
                    displayTable(CurrentT);
                    
            if len(failedID) != 0:
                trigger_delay = calendar.timegm(time.gmtime()) + delay;
                for ID in failedID:
                    del timerDict[ID];                
main()
