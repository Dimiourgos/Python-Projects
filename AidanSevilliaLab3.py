

def main():
#defining main

    hamlet = True #preparing the circumstances

    while hamlet == True: #setting up while loop
        try:

            goods = str(input("Please enter what you bought today: "))
            moolah = float(input("Please enter how much you paid for groceries today: "))

            if (10 < moolah) & (moolah < 60):
                coupon = moolah * 0.08
                coupon = float(round(coupon, 2))
                print("   ")
                print("You spent", moolah, "on", goods, "today")
                print("   ")
                print("You have received a", coupon, "dollar coupon for your next visit! (8% of your purchase)")
                print("   ")
                print("   ")

        #setting up the 10 to 60 range

            elif (60 < moolah) & (moolah < 150):
                coupon = moolah * 0.10
                coupon = float(round(coupon, 2))
                print("   ")
                print("You spent", moolah, "on", goods, "today")
                print("   ")
                print("You have received a", coupon, "dollar coupon for your next visit! (10% of your purchase)")
                print("   ")
                print("   ")

        #setting up the 60 to 150 range

            elif (150 < moolah) & (moolah < 210):
                coupon = moolah * 0.12
                coupon = float(round(coupon, 2))
                print("   ")
                print("You spent", moolah, "on", goods, "today")
                print("   ")
                print("You have received a", coupon, "dollar coupon for your next visit!(12% of your purchase)")
                print("   ")
                print("   ")

        #setting up the 150 to 210 range

            elif 210 < moolah:
                coupon = moolah * 0.14
                coupon = float(round(coupon, 2))
                print("   ")
                print("You spent", moolah, "on", goods, "today")
                print("   ")
                print("You have received a", coupon, "dollar coupon for your next visit! (14% of your purchase)")
                print("   ")
                print("   ")

        #setting up the over 210 range

            elif (0 < moolah) & (moolah < 10):
                print("   ")
                print("You spent", moolah, "on", goods, "today")
                print("   ")
                print("You did not spend enough to qualify for a coupon")
                print("   ")
                print("   ")

            # setting up the over 0 to 10 range

            elif moolah == -42:
                hamlet = False

        #including kill switch for debugging

        except ValueError:
            print("   ")
            print ("Please input a valid value cost.")
            print("   ")
            print("   ")

        #rejecting route

main()
#proper run

#C:\Users\Xeno\PycharmProjects\Assign3\venv\Scripts\python.exe
#C: / Users / Xeno / PycharmProjects / Assign3 / Assign3.py

#Please enter what you bought today: apples

#Please enter how much you paid for groceries today: 5

#You spent 5.0 on apples today

#You did not spend enough to qualify for a coupon

#Please enter what you bought today: bananas

#Please enter how much you paid for groceries today: 15

#You spent 15.0 on bananas today

#You have received a 1.2 dollar coupon for your next visit! (8 % of your purchase)

#Please enter what you bought today: lemons

#Please enter how much you paid for groceries today: 65

#You spent 65.0 on lemons today

#You have received a 6.5 dollar coupon for your next visit! (10 % of your purchase)

#Please enter what you bought today: oranges

#Please enter how much you paid for groceries today: 155

#You spent 155.0 on oranges today

#You have received a 18.6 dollar coupon for your next visit!(12 % of your purchase)

#Please enter what you bought today: durians

#Please enter how much you paid for groceries today: 215

#You spent 215.0 on durians today

#You have received a 30.1 dollar coupon for your next visit! (14 % of your purchase)

#Please enter what you bought today: shrooms

#Please enter how much you paid for groceries today: id like 4 officer

#Please input a valid value cost.

#Please enter what you bought today: -42

#Please enter how much you paid for groceries today: -42

#Process finished with exit code 0
