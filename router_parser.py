def parser(fileText):
    """Recieves the input text of a config file reads through and if it passes all
    requied checks returns a list of tuples including all relavent data else
    returns appropriate error
    file should be in the form
    ('routerId ')Number/n('input-ports ') Number(', ')*('output-ports ') Number1('-')Number2('-')Number3(', ')*
    If successful returns in the form
    [routerId, [ID_num]*, [(o_num, cost, out_ID)*]]
    """
    
    #Defined values
    line_1 = 'router_ID ';
    line_2 = 'input-ports ';
    line_3 = 'output-port ';
    input_list = [];
    temp_num = '';    
    temp_out = '';    
    output_list = [];
    out_list = [];
    test_num = 10;
    #has 2 uses If successful returns ID_num of router else explains failures
    ID_num = ''; 
    #Prevents changes to ID_num after failure to explain issue with input
    failed = False;
    
    #Check if first line is correct
    if line_1 != fileText[0:test_num]:
        ID_num = "First line not correct format";
        failed = True;
        
    #Check for ID_number and adjust ID_num value if exists
    if failed == False and test_num != len(fileText)-1:
        while fileText[test_num].isnumeric() == True:
            ID_num += fileText[test_num];
            test_num += 1;
    
    #Checks if ID_num was present in supplied string
    if len(ID_num) == 0:
        #For case where number is avalible but is end of line hence missed
        if fileText[test_num].isnumeric() == True:
            ID_num += fileText[test_num];
        else:
            ID_num = "No ID given";
            failed = True;
    
    #Check if second line is correct
    if line_2 != fileText[test_num: test_num+12] and failed == False:
        ID_num = "Second line not correct format";   
        failed = True;
    
    #Adjustment to test_num after line_2 check
    test_num += 12;
    
    #Checks for and appends to Input list if input ports are supplied
    if failed == False:
        while fileText[test_num-1].isalpha() != True and test_num < len(fileText)-1:
            #Appends any numbers to temp_num to get the full port number
            if fileText[test_num].isnumeric() == True:
                temp_num += fileText[test_num];
            else:
                #Resets for next possible number
                if temp_num != '':
                    input_list.append(temp_num);
                    temp_num = '';
            #Continue through while loop
            test_num += 1;
    
    #For case where temp_num is at end of line for failure explaination
    if temp_num != '':
        input_list.append(temp_num);
    
    #Check for any Input ports and return failed if there are none
    if len(input_list) == 0 and failed == False:
        failed = True;
        ID_num = "No Input Ports given";
        
    #Adjustment after while loop for third line check
    test_num -= 1;    
    
    #Check if line 3 is correct
    if line_3 != fileText[test_num: test_num+12] and failed == False:
        ID_num = "Third line not correct format";     
        failed = True;
    
    #Adjustment after line three check
    test_num += 12;
    
    #Checks for and appends to Input list if Output ports are supplied
    if failed == False and test_num < len(fileText)-1:
        while test_num != len(fileText):
            if fileText[test_num] != ' ':
                temp_out += fileText[test_num];
            else:
                output_list.append(temp_out);
                temp_out = ''
            test_num += 1;
        
    if temp_out != '':
        output_list.append(temp_out)
    
    for item in output_list:
        out_list.append(tuple(item.split('-')));
    
    
    
    if len(out_list) == 0 and failed == False:
        failed = True;
        ID_num = "No Output Ports given";    
    else:
        #Check output ports, costs and destination addresses are present
        for port in out_list:
            if len(port) == 3:
                for element in port:
                    if element.isnumeric() == False:
                        #Explain fault and break loop
                        ID_num = "Element of port is wrong";
                        failed = True;
                        break;
            else:
                #Length of Output data incorrect 
                ID_num = "Output data is not correct length";
                failed = True;
    
    if failed == True:
        return ID_num;
    else:
        return [ID_num, input_list, out_list];
    
testfile1 = "router_ID 7input-ports 10001, 10004output-port 4007-8-1 7007-6-4";
#testfile2 = "YEEEEET";
#testfile3 = '';
#testfile4 = "router_ID 4input-ports 10001, 10004output-port 4007-8-e 7007-6-4";
#testfile5 = "router_ID input-ports 10001, 10004output-port 4007-8-1 7007-6-4";
#testfile6 = "router_ID 7";
#testfile7 = "router_ID 4input-ports 10001, 10004";
#testfile8 = "router_ID 5input-ports 10001, 10004output-port ";
#testfile9 = "router_ID 7input-ports ";
#testfile10 = "router_ID 4input-ports 10001, 10004output-port 4007-8";

result = parser(testfile10);
if type(result) == type(''):
    print(result)
else:
    for i in result:
        print(i);