
def getValues(numbers):
    num=int(input('How many numbers do you wish to enter in the list : '))
    for i in range(num):
        accept=int(input('Enter a number '))
        numbers.append(accept)
    return numbers

def putValues(myList):
    print('The list is ',myList)

def sortList(myList):
    myList.sort()
    return myList

def displaySmallLarge(myList):
    print('Second Smalest ',myList[1])
    small=len(myList)
    print('Second Largest ',myList[small-2])

def search(s,myList):
    i=0
    while i<len(myList):
        if s == myList[i]:
            print(myList[i],' Found at index ',i)
        else:
            print(myList[i],'Not Found')
        i=i+1

def findSmallLarge(myList):
    print('Smalled element in the list ',min(myList)) 
    print('Largest element in the list ',max(myList)) 

def main():
    print('Call a function to read elements in the list')
    numbers=[]
    myList=getValues(numbers)
    print('Call a function to write the elements of the list')
    putValues(myList)
    print('Call a function to find the Smallest and largest element in the list')
    findSmallLarge(myList)
    print('Call a function to search for a value in the list and find the location')
    s=int(input('Enter a number to search for '))
    search(s,myList)
    
main()
