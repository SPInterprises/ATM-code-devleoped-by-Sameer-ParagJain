print("Welcome to the State Bank of India\n",end="This code is developed by:- Sameer\Parag\n")
restart="y"
chances=3
balance=18000
left_tries=0

while chances>=0:
    print("Warning: If you entered wrong pin in 3 time then your Atm card will be blocked: So be carefully\n Remaining Attempt:" ,chances-left_tries)

    pin=int(input("Please enter your 4-digit pin:\n"))
    if pin==8860:
        print("Your Atm Pin is  Succeesfully Verify: You can access it\n")
        if left_tries==chances:
            print("You have exhausted limit please contact our SBI Bank")
        while restart not in ("n","no","N","No"):
            print("Please press 1 for Your Balance\n")
            print("Please press 2 for Your Withdraw\n")
            print("Please press 3 for Pay in\n")
            print("Please press 4 for Return card\n")
            option= int(input("what would u like to choose  above option ?\n"))
            if option==1 :
                print("Your Balance is $",balance,"\n")
                restart=input("Would u like to go back ? y/n \n")
                if restart in ("N","No",'n','no'):
                    print("thankyu for using our banking with SBI")
                    quit()
            elif option==2:
                option2=('y')
                withdraw=float(input("How much would yu like to withdraw\n$10/$20/$40/$50/$60/$100 and for other press 1\n"))
                if withdraw in [10,20,40,50,60,100]:
                    balance=balance-withdraw
                    print("\nYour balance is Now $",balance)
                    restart=input("what would yu like to do y/n \n")
                    if restart in ('n','no',"N","No"):
                        print("Thankyu for banking with SBI")
                        exit()
                elif withdraw==[10,20,40,50,60,100]:
                    print("Invalid Amount,please re-try\n")
                    restart=("y")
                elif withdraw==1:
                    withdraw=float(input("Please enter the desired amount:"))
                    balance=balance-withdraw
                    print("your balance is $",balance)
                    restart=input("would you like to go back y/n\n")
                    if restart in ('n','no',"N","No"):
                        print("Thankyu for banking with SBI")
                        exit()

            elif option==3:
                pay_in=float(input("How much would you like to pay in?\n"))
                balance=balance+pay_in
                print("\nyou balance is now $ ",balance)
                restart=input("would you like to go back y/n\n")
                if restart in ("n",'no','N','No'):
                    print("thankyu for using with SBI")
                    exit()
            elif option==4:
                print("please wait while your card is return....\n")
                print("Thankyu for banking with SBI")
            else:
                print("Please enter a correct number\n")
                restart='y'
    elif pin!=8860:
        print("Incoreect Password")
        chances=chances-1
        if chances==0:
            print("\n No more try ,Contact-Support@SBI.co.in")
            exit()


