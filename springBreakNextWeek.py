"""
Program goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INTs from STRs
3. We need to provide choices to the user
    a. Add more valurs to a list
    b. Return a value at a specific index

"""
import random
myList = []
unique_list = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print ("Choose from the following options. Type a number below!")
            choice = input ("""1. Add to a list or
2. Add a bunchof numbers
3. Return the value at an index
4. Random search
5. Linear search
6. Print contents of list
7. Quit program""")
            #Add a way to catch bad user responses
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "4":
                linearSearch()
            elif choice == "5":
                print(myList)
            elif choice == "6":
                sortList(myList)
            else:
                break
        except:
            print("You made a whoopsie!")
        
        
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of intergers here!")
    numToAdd = input("How many intergers would you like to add   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(), int(numToAdd):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")

def indexValues():
    print("Ohhhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are your curoius about?")
    print(myList[int(indexPos)])

def sortList(myList):
    print("An elephant told me you needed some sorted data!")    
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list?  Y/N")
    if showMe.lower() == "y":
        print(unique_list)

def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("we're gonna check out each item one at a time in your list! NO GOOD.")
    searchItem = input("What you lookin for, partner?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def printLists():
    if len(unique_list) == :
        print(myList)
    else:
        whichOne = input("Which list? sorted or unsorted?   ")
        if whichOne.ower() == "sorted":
            print(unique_list)
        else:
            print(myList)

#DunDeRmaIn
if __name__ == "__main__":
    mainProgram()
    #POO
