        
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
    line_2 = '\ninput-ports ';
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
                
    if line_2 != fileText[test_num: test_num+13] and failed == False:
        ID_num = "Second line not correct format\n";   
        failed = True;
    
    test_num += 13;
    
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
                temp_out = ''
            test_num += 1;
        
    if temp_out != '':
        output_list.append(temp_out)
    out_list = []
    for item in output_list:
        out_list.append(tuple(item.split('-')))
    
    if len(out_list) == 0 and failed == False:
        failed = True;
        ID_num = "No Output Ports given\n";    
    
    if failed == True:
        return ID_num;
    else:
        return [ID_num, input_list, out_list]
    
router1 = "router_ID 5\ninput-ports 8004, 8006\noutput-port 7005-2-4 9005-1-6"
print(router1)
final = parser(router1)
print(final)