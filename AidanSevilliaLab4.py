

def main():
#defining main

    hamlet = True #preparing the circumstances
    horatio = True #preparing the circumstances
    ophelia = True #preparing the circumstances

    while hamlet == True: #setting up while loop

        input1 = input("Input File: ")

        try:
            open(input1)

        except IOError:
            print("Please enter a valid file name. ")
            continue
        inFile = open(input1, "r")
        break

    while horatio == True:

        input2 = input("Output File: ")

        try:
            open(input2)

        except IOError:
            outFile = open(input2, "a+")
            break

        print("That file already exists. ")
        continue



    shopping1 = inFile.read()

    format1 = shopping1.split('\n')

    print(format1)



main()