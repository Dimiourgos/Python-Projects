

def main():
    sum = 0
    dictionary = []
    horatio = True

    while horatio == True:

        try:
            print("   ")
            selectedFile = input("Please enter file name: ")

            with open(selectedFile, encoding='utf-8') as f:
                for line in f:
                    dictionary.append(line)

            try:
                dictionary[11]
                print("Please choose a valid file. ")
                print("   ")
            except IndexError:
                try:
                    dictionary[10]
                    for x in range(len(dictionary)):
                        sum += x
                    x -= 10
                    print("Sum: ", sum)
                except IndexError:
                    print("Please choose a valid file1. ")
                    print("   ")

        except IOError:
            print("Please enter a valid file name. ")
            print("   ")


main()


#C:\Users\Xeno\PycharmProjects\AidanSevilliaLab6\venv\Scripts\python.exe C:/Users/Xeno/PycharmProjects/AidanSevilliaLab6/AidanSevilliaLab6.py
#
#Please enter file name: good.dat
#Sum:  55
#
#Please enter file name: bad1.dat
#Please choose a valid file.
#
#Please enter file name: bad2.dat
#Please choose a valid file.
#
#Please enter file name: bad3.dat
#Please choose a valid file.
#
#Please enter file name: bad4.dat
#Please choose a valid file.
#
#Please enter file name: err.dat
#Please enter a valid file name.
