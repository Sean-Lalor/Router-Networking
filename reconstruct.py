def reconstruct(data):
    '''takes the data recieved and converts it back to an appliable format'''
    data = data.split(" ")
    #print(data)
    age = int(data[1])
    #print(age)
    msgType = int(data[3])
    #print(msgType)
    LinkStateID = int(data[7])
    AdvertisingID = int(data[11])
    tableData = data[21:]
    #print(tableData)
    #From here muct convert back to readable format
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
    return final;
    

def main():
    piece1 = "00 01 00 01 00 00 00 05 00 00 00 06 00 00 00 00  00 e4 00 24 5b 5b 31 2c 20 2d 31 2c 20 "
    piece2 = "35 5d 2c 20 5b 32 2c 20 2d 31 2c 20 2d 31 5d 2c 20 5b 33 2c 20 2d 31 2c 20 2d 31 5d 2c 20 5b 34 2c 20 2d 31 2c 20 2d 31 5d 2c 20 5b 35 2c 20 2d "
    data = piece1 + piece2 + "31 2c 20 2d 31 5d 2c 20 5b 36 2c 20 36 2c 20 30 5d 2c 20 5b 37 2c 20 2d 31 2c 20 2d 32 5d 5d 00"
    reconstruct(data);
main()