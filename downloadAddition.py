"""
Program goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INTs from STRs
3. We need to provide choices to the user
    a. Add more valurs to a list
    b. Return a value at a specific index

"""
import matplotlib
import random
myList = []
unique_list = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print ("Choose from the following options. Type a number below!")
            choice = input ("""1. Add to a list or
2. Add a bunch of numbers
3. Get an item at an index
4. Sort list
5. Random Search
6. Linear search
7. Recursive binary search
8. Iterative binary search
9. Print list
10. Download Code
11. Quit   """)
            #Add a way to catch bad user responses
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch
            elif choice == "7":
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
            elif choice == "8":
                sortList(myList)
            elif choice == "9":
                printList
            elif choice == "10":
                downloadCode

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

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] ==

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
        return -1

def printLists():
    if len(unique_list) == :
        print(myList)
    else:
        whichOne = input("Which list? sorted or unsorted?   ")
        if whichOne.ower() == "sorted":
            print(unique_list)
        else:
            print(myList)

def downloadCode():
        f.write("Now the file has more content!")
    f.close()

    
    f = open("demofile2.txt", "r")
    print(f.read())
    

#DunDeRmaIn
if __name__ == "__main__":
    mainProgram()
    #POO
