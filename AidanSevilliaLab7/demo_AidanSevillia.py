from AidanSevilliaLab7 import Message # Importing!!!


user = Message("Aidan Sevillia", "Geri Lamble") #Hello Professor!
lines = ["-Python", "-An 'A'"]

for x in range(0, len(lines)): #run string checker program in a for loop
    if user.str_ok(lines[x]):
        user.append_body(lines[x])

print(user.to_string()) #return EVERYTHING by calling the 'to_string' function and applying the 'user' data

#C:\Users\Xeno\PycharmProjects\AidanSevilliaLab7\venv\Scripts\python.exe C:\Users\Xeno\PycharmProjects\AidanSevilliaLab7\better_demo_AidanSevillia.py

#To: Geri Lamble
#From: Aidan Sevillia

#For Christmas I want:
#-Python
#-An 'A'

#Process finished with exit code 0