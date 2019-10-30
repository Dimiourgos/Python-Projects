def main():

    hamlet = True

    dictionary = ["placeholder"] #create dictionary and create 1 placeholder for 0
    item1Pos = [] #initialize the apple position
    item2Pos = [] #initialize the art position

    while hamlet == True:

        selectedFile = input("Enter the name of the input file: ")

        try:
            open(selectedFile)

        except IOError:
            print("Please enter a valid file name. ")
            print("   ")
            continue

        break

    with open(selectedFile, encoding='utf-8') as f:
        for line in f:
            dictionary.append(str(line))
    for x in range(len(dictionary)):
        if dictionary[x].__contains__("apple"): #find "apple"
            item1Pos.append(x)
        if dictionary[x].__contains__("art"): #find "art"
            item2Pos.append(x)

    print("apple: ", item1Pos)
    print("art: ", item2Pos)

main()

#C:\Users\Xeno\PycharmProjects\AidanSevilliaLab5\venv\Scripts\python.exe
#C: / Users / Xeno / PycharmProjects / AidanSevilliaLab5 / AidanSevilliaLab5.py
#Enter the name of the input file: worldender
#Please enter a valid file name.

#Enter the name of the input file: hello.dat
#Please enter a valid file name.

#Enter the name of the input file: t5.dat
#apple: [1, 11]
#art: [5]

#Process finished with exit code 0
