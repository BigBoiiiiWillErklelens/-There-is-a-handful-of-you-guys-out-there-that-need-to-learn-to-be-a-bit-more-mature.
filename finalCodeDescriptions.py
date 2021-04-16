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
        
"""
This function is the function that adds to a list. When it is called, It asks you to type
an interger and then it adds that interger to the list.
"""
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))

"""
This function allows you to make the program add a bunch of numbers at once. You get to pick
how many numbers will be added and how high the numbers will go. It add random numbers.
"""
def addABunch():
    print("We're gonna add a bunch of intergers here!")
    numToAdd = input("How many intergers would you like to add   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(), int(numToAdd):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")

"""
THIS FUNCTION LETS YOU SEE WHAT NUMBER IS AT A SPECIFIC INDEX POSITION
"""
def indexValues():
    print("Ohhhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are your curoius about?")
    print(myList[int(indexPos)])

"""
This function can sort a the list into smallest to largest number. This
could be useful to find the median.
"""
def sortList(myList):
    print("An elephant told me you needed some sorted data!")    
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list?  Y/N")
    if showMe.lower() == "y":
        print(unique_list)

'''
This searches for a random number
'''
def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])

"""
This function lets you search for a number in the list. You can type in a number and then it will
tell you at which index position it is in.
"""
def linearSearch():
    print("we're gonna check out each item one at a time in your list! NO GOOD.")
    searchItem = input("What you lookin for, partner?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

"""
nah
"""
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] ==

'''
scary
'''
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

"""
THIS, lets you see your list. 
"""
def printLists():
    if len(unique_list) == :
        print(myList)
    else:
        whichOne = input("Which list? sorted or unsorted?   ")
        if whichOne.ower() == "sorted":
            print(unique_list)
        else:
            print(myList)

"""
This is supposed to let you download your code but it is all osrts of dysfunctional and doesn't work.
"""

def downloadCode():
        f.write("Now the file has more content!")
    f.close()

    
    f = open("demofile2.txt", "r")
    print(f.read())
    

#DunDeRmaIn
if __name__ == "__main__":
    mainProgram()
    #POO
