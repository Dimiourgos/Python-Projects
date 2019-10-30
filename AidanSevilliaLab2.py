
#request input for num_let
num_let = input("Enter your family name: ")
num_let_sum = len(num_let)
#request input for my_id
my_id = input("Enter your G#: ")
my_id_sum = sum(int(c)for c in my_id.strip())
if 2 <= num_let_sum <= 15:
    # begin user feedback
    print("n_let is: ", num_let_sum)
    print("my_id is: ", my_id_sum)
    # printing manipulated feedback
    ex1 = my_id_sum / 2
    print("expression 1: ", str(round(ex1, 2)))
    ex2 = my_id_sum % 2
    print("expression 2: ", str(round(ex2, 2)))
    ex3 = sum(range(num_let_sum + 2))
    print("expression 3: ", str(round(ex3, 2)))
    print("expression 4: ", my_id_sum + num_let_sum)
    print("expression 5: ", abs(num_let_sum - my_id_sum))
    ex6 = (my_id_sum) / (num_let_sum + 1100)
    print("expression 6: ", str(round(ex6, 2)))
    print("expression 7: ", (num_let_sum % num_let_sum) and (my_id_sum * my_id_sum))
    print("expression 8: ", 1 or (my_id_sum / 0))
    print("expression 9: ", round(3.15, 1))
else:
    print("Please enter")

import datetime

dateNow = datetime.datetime.now()
print("Date: ", dateNow)









#C:\Users\Xeno\AppData\Local\Programs\Python\Python37\python.exe C:/Users/Xeno/PycharmProjects/Assign2/Assign2.py
#Enter your family name: Sevillia
#Enter your G#: 12345
#n_let is:  8
#my_id is:  12
#expression 1:  6.0
#expression 2:  0
#expression 3:  45
#expression 4:  20
#expression 5:  4
#expression 6:  0.01
#expression 7:  0
#expression 8:  1
#expression 9:  3.1
#Date:  2019-09-04 23:48:30.020929

#Process finished with exit code 0
