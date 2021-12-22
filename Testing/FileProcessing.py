def addStudent():
    myFile=open(r'studentdb.txt','a')
    id=int(input('Enter student ID: '))
    while id!=0:
        name=input('Enter Student Name: ')
        grade=float(input('Enter student Grade: '))
        myFile.write(str(id)+'\t')
        myFile.write(name+'\t')
        myFile.write(str(grade)+'\t')
        myFile.write('\n')
        id=int(input('Enter student ID: '))
    myFile.close()

def displayStudent():
    myFile=open(r'studentdb.txt','r')
    line=myFile.readline()
    while line!='':
        print(line)
        line=myFile.readline()
    myFile.close()


def main():
    print('Open and Write to an existing file ')
    print()
    addStudent()
    print()
    displayStudent()

main()
