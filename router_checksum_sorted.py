check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
# compliment value is 15 
compliment = {}
numeral = {}
#convert hex letters to number for easier calculation
for i in range(16):
    compliment.__setitem__(check[i], check[(15-i)])
    numeral.__setitem__(check[i], i)
    
def filters(original):
    """ """   
    practice = original.split()
    #digisum kps track of the summed values so far
    digisum = 0
    #takes the lenght of the checksum calue to let the forloop know how many bits need to be processed
    practice_len = len(practice)
    sum_single = 0
    sum_second = 0
    #print(practice_len)
    for i in range(practice_len):
        #resetting the carries
        carry1 = 0
        carry2 = 0       
        digit = practice[i]
        #print("why you bully????", digit)
        single = -1
        second = -1
        for n in digit:
            if (single == -1) and (second == -1):
                single = n
                if type(single) != type(int):
                    single = numeral[(single)]
                    #print("convert_single", single)
                else:
                    second = int(n)  
            else:
                second = n
                if type(second) != type(int):
                    second = numeral[(second)]
                    #print("convert_second", second)
                else:
                    second = int(n)
            #print('single', single, 'second', second)
        sum_single += single
        if (sum_single >= 16):
            carry1 = 1           
        sum_second += second
        
        if (sum_second >= 16):
            carry2 = 1
            
        sum_single = (sum_single + carry2)%16
        #print('sum of the single', sum_single)
        if (sum_single > 9):
            to_hex = check[sum_single]
            #print('to hex', to_hex, 'the number', n)
        else:
            to_hex = check[sum_single]
            #print('to hex', to_hex, 'the number', n)        
        sum_second = (sum_second + carry1)%16
        #print(sum_second)
        #print('sum of the second', sum_second)
        if (sum_second > 9):
            to_hex2 = check[sum_second]
            #print('to hex2', to_hex2, 'the number', n)
        else:
            to_hex2 = check[sum_second]
            #print('to hex2', to_hex2, 'the number', n)
    #print(sum_single)
    #print(sum_second)
    sum_single = check[sum_single]
    sum_second = check[sum_second]
    digisum = str(sum_single) + str(sum_second)
    #print("here we are", digisum)
    new_list = original + " " + digisum
    #print("here we are", new_list)
    return digisum, new_list
    
def checksum1(digisum):
    """apply 1st compliment by grabing the inverse of the single and second values """
    digi_single = 0
    digi_second = 0
    for i in digisum:
        if (digi_single == 0) and (digi_second == 0):
            digi_single = i
            if type(digi_single) != type(int):
                digi_single = numeral[digi_single]
                #print("convert_single", single)
                # this converts the letters into numerical form so there compliment can be searched for in the compliment list based using the numerical value as a index
            else:
                digi_second = int(i)           
        else:
            digi_second = i
            if type(digi_second) != type(int):
                digi_second = numeral[digi_second]
                #print("convert_second", second)
                # this converts the letters into numerical form so there compliment can be searched for in the compliment list based using the numerical value as a index
            else:
                digi_second = int(i)
            
    #grab incerse values
    print("check single", digi_single)
    print("check second", digi_second)
    #print(type(digi_single))
    str_digi_single = compliment[str(digi_single)]# converted to strings to look up stings by index number in the compliment list-
    str_digi_second = compliment[str(digi_second)]# - Ask sean still a bit confused
    print(str_digi_single, str_digi_second)
    #produce the 1's compliment of the checksum by concatenating the two compliment strings
    ones_compliment = str_digi_single + str_digi_second 
    print(ones_compliment)
    return ones_compliment, digi_single, digi_second, str_digi_single, str_digi_second  
    
def checksum2(digisum, digi_single, digi_second, str_digi_single, str_digi_second):
    """apply 2's compliment to the checksum and the 1's compliment checksum"""
    #step 1 add 1 to ones_compliment 
    precarry1 = 0
    precarry2 = 0
    digi_second = digi_second - 1 # the -1 may cause problems in the future
    if (digi_second < 0): 
        precarry1 = 1
        digi_single = (digi_single - precarry1)%16
        
    if (digi_single < 0):
        precarry2 = 1
        digi_second = (digi_second - precarry)%16     
    #check if digi second is greater than 15 and if you need a carry
    print("this is what i want", digi_second)
    str_digi_second = compliment[str(digi_second)]
    print('step1 complete')
    ones_compliment = str_digi_single + str_digi_second
    #print('step1 complete')
    #step 2 create a list of the checksum and the 1's compliment
    check_list = [digisum, ones_compliment]
    print(check_list)
    chcarry1 = 0
    chcarry2 = 0
    #two_sum keeps track of the summed values so far
    two_sum = 0
    #takes the lenght of the checksum calue to let the forloop know how many bits need to be processed
    check_len = len(check_list)
    chsum_single = 0
    chsum_second = 0
    #print(practice_len)
    for i in range(check_len):
        #resetting the carries
        chcarry1 = 0
        chcarry2 = 0        
        chdigit = check_list[i]
        #print(digit)
        chsingle = 0
        chsecond = 0
        for q in chdigit:
            if (chsingle == 0) and (chsecond == 0):
                chsingle = q
                if type(chsingle) != type(int):
                    chsingle = numeral[chsingle]
                    #print("convert_single", single)
                else:
                    chsecond = int(q)
                    #pass
                    
            else:
                chsecond = q
                if type(chsecond) != type(int):
                    chsecond = numeral[chsecond]
                    #print("convert_second", second)
                else:
                    chsecond = int(q)
                    #pass
            #print('single', single, 'second', second)
        chsum_single += chsingle
        if (chsum_single >= 16):
            chcarry1 = 1        
        #sum_single = (sum_single + carry2)%16

            
        chsum_second += chsecond
        if (chsum_second >= 16):
            chcarry2 = 1
            
        chsum_single = (chsum_single + chcarry2)%16
        #print('sum of the single', sum_single)
        if (chsum_single > 9):
            to_hex = check[chsum_single]
            #print('to hex', to_hex, 'the number', n)
        else:
            to_hex = check[chsum_single]
            #print('to hex', to_hex, 'the number', n)        
        chsum_second = (chsum_second+ chcarry1)%16
        #print('sum of the second', sum_second)
        if (chsum_second > 9):
            to_hex2 = check[chsum_second]
            #print('to hex2', to_hex2, 'the number', n)
        else:
            to_hex2 = check[chsum_second]
            #print('to hex2', to_hex2, 'the number', n)
    print(chsum_single)
    print(chsum_second)
    two_sum = str(chsum_single) + str(chsum_second)
    print(two_sum)
    
    if two_sum == "00":
        print("Yes it works")
    return two_sum
 
def main():
    """ """
    original = "00 01 00 01 00 00 00 06 00 00 00 05 00 00 00 00 00 7e 24 5b 5b 31 2c 20 2d 31 2c 20 2d 31 5d 2c 20 5b 32 2c 20 2d 31 2c 20 2d 31 5d 2c 20 5b 33 2c 20 2d 31 2c 20 2d "
    original2 = "31 5d 2c 20 5b 34 2c 20 2d 31 2c 20 2d 31 5d 2c 20 5b 27 35 27 2c 20 27 35 27 2c 20 30 5d 2c 20 5b 36 2c 20 2d 31 2c 20 2d 31 5d 2c 20 5b 37 2c 20 2d 31 2c 20 2d 31 "
    original3 = "5d 5d 00"
    original4 = original + original2 + original3
    #data = " 00 00 00 01 00 00 00 00 00"
    #original2 = original + data;
    digisum, new_list = filters(original3)
    #print("come on baby", new_list)
    #print("go you good thing", digisum)
    #ones_compliment, digi_single, digi_second, str_digi_single, str_digi_second = checksum1(digisum)
    #print("ones_compliment is passing through", ones_compliment)
    #print('hello', digi_single, digi_second)
    #twos_compliment = checksum2(digisum, digi_single, digi_second, str_digi_single, str_digi_second)
    #print('its me', twos_compliment)
    print(new_list)
    
main()
