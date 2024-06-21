import time

print("please insert CARD")
time.sleep(5)
pasword = 1234
pin = int(input("enter your atm pin"))

balance = 5000

if pin == pasword:
    while True:
        print("""
        1 == balance
        2 == withdrawal balance
        3 == deposit balance
        4 == exit""")

        try:
            option = int(input("please enter your choice"))


        except:
            print("please enter a valid option")
            print("=====================================================")
            print("=====================================================")
            print("=====================================================")

        if option == 1:
            print("your current balance is:", balance)
            print("=====================================================")
            print("=====================================================")
            print("=====================================================")

        if option == 2:
            withdraw_amount = int(input("please enter the withdrawl amount"))
            balance = balance - withdraw_amount
            print(withdraw_amount, "is debited from your account")
            print("your current balance is:", balance)

            print("=====================================================")
            print("=====================================================")
            print("=====================================================")

        if option == 3:
            deposit_amount = int(input("please enter the deposit amount"))
            balance = balance + deposit_amount
            print(deposit_amount, "is credit from your account")
            print("your current balance is:", balance)

            print("=====================================================")
            print("=====================================================")
            print("=====================================================")

        if option == 4:
            breakpoint()




else:
    print("wrong pin try again")
