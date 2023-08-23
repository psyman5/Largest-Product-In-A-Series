
numberString = input("Input your number: ")
digitsRequired = int(input("Input how many adjacent digits in a row: ")) #the number of adjacent digits to check, example digitsRequired = 2 for 2392 would check for 23 and not 239

numList = []


def productListFunc(numberString): #determines greatest products of adjacent digits
    numberList = []
    spacedList = []
    #sumList = []
    multList = []
    multipliedNumber = 1 #number that changes through multiplication with digits.

    for element in numberString: #creates a list that contains all digits of the string in integer form as individual list entries
        numberList.append(int(element))
    for i in range(0,(len(numberList)-1)): #separates the number into equally sized chunks to check until the number is no 
                                            #longer divisible by digitsRequired where it takes a partial amount , e.g. 13/5 = 5 5 3
        spacedList.append(numberList[i:i+digitsRequired])
    
    for element in spacedList: #checks for zeroes in sequences and automatically removes those sequences.
        trashCan = element
        for i in trashCan:
            if i == 0:
                while trashCan in spacedList: spacedList.remove(trashCan)

    for element in spacedList: #multiplies remaining numbers after pruning zeroes
        for c in element:
            multipliedNumber = multipliedNumber * c
        multList.append(multipliedNumber)
        multipliedNumber = 1

    return [max(multList), spacedList[multList.index(max(multList))]] #returns the product



#functions used to theorize the main function's cohesiveness. Not useful.

def listPopper():
    randList = [2,3,51,6,7,0,223,56,5,0]
    listOfLists = [[0,2,3],[12,4,1],[12,5,8],[0,0,8],[0,0,8],[0,0,0,0,0,0,0]]
    for element in listOfLists:
        trashCan = element
        for c in element:
            if c == 0:
                while trashCan in listOfLists: listOfLists.remove(trashCan)
    print(listOfLists)

def multiplierFunc():
    numList = [1,2,5,4,8]
    numListList = [[1,2,5,4,8],[1,2,5,4,8],[1,2,5,4,8],[1,2,5,4,8]]
    multList = []
    multipliedNumber = 1
    #for element in numList:
        #multipliedNumber = multipliedNumber * element

    for element in numListList:
        print(element)
        for c in element:
            print(c)
            multipliedNumber = multipliedNumber * c
        print(multipliedNumber)
        multList.append(multipliedNumber)
        multipliedNumber = 1

    print(multList)


print(productListFunc(numberString))