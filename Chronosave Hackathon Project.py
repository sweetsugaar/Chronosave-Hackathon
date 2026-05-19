import time
global total_spending
global balance_input_num
global money_input_num
money_input_num = 0
global rent_input_num
rent_input_num = 0
global groceries_input_num
groceries_input_num = 0
global saving_balance
saving_balance = 0

def menu():
    menu_input = input("\nWhich would you like to do next? [Case Sensitive] (Salary, Rent, Groceries, Savings, Done): ")
    if menu_input == "Salary":
        money()
    elif menu_input == "Rent":
        rent_and_utilities()
    elif menu_input == "Groceries":
        groceries()
    elif menu_input == "Savings":
        savings()
    elif menu_input == "Done":
        done()
    else:
        print("Please re-enter the next option you would like to go to, as you most likely typed the option incorrectly.")
        time.sleep(2)
        menu()

def not_num():
    print("Please only use numbers, we can not process letters.")
    time.sleep(2)
def budget_program():
    print("Welcome to ChronoSaves, where we help you budget your finances.")
    time.sleep(2)
    balance_input = input("How much money do you currently have: ")
    if not balance_input.isnumeric():
        not_num()
        budget_program()
    else:
        global balance_input_num
        balance_input_num = int(balance_input)
        print(f"You currently have {balance_input_num} Dollars in your account")
        time.sleep(1)
        menu()
    #salary
def money():
    money_input = input("What is your monthly salary (Round Down to the Nearest Dollar): ")
    if not money_input.isnumeric():
        not_num()
        money()
    else:
        global money_input_num
        money_input_num = int(money_input)
        print(f"Your monthly salary is: {money_input}")
        time.sleep(1)
        menu()

def rent_and_utilities():
    rent_input = input("Please enter the amount you pay for and house utilities (Round up to the Nearest Dollar): ")
    if not rent_input.isnumeric():
        not_num()
        rent_and_utilities()
    else:
        global rent_input_num
        rent_input_num = int(rent_input)
        print(f"You pay {rent_input} dollars for rent and utilities. ")
        time.sleep(1)
        menu()
def groceries():
    groceries_input = input("Please enter your weekly spending on groceries: ")
    if not groceries_input.isnumeric():
        not_num()
        groceries()
    else:
        global groceries_input_num
        groceries_input_num = int(groceries_input)
        print(f"Your weekly grocery spending is {groceries_input} dollars ")
        time.sleep(1)
        menu()
def savings():
    global saving_balance
    check_savings=input("Do you want to check your savings account? Y/N: ")
    if check_savings == "Y":
        print(f"You currently have {saving_balance} dollars in your savings account. ")
        time.sleep(1)
        transfer()
    if check_savings == "N":
        input("Sending you back to the Menu...")
        time.sleep(2)
        menu()
    else:
        print("Choose Y or N.")
        savings()
def transfer():
    amount=input("\nHow much money do you want to transfer? ")
    amount_num = int(amount)
    global balance_input_num
    if amount_num > balance_input_num:
        print("You dont have enough money in your current balance.")
        transfer()
    else:
        global saving_balance
        saving_balance += amount_num
        balance_input_num -= amount_num
        print(f"\nYour balance is now ${balance_input_num}, and you have ${saving_balance} in your savings")
        retransfer_input = input("Would you like to transfer more into your savings account? Y/N ")
        if retransfer_input == "Y":
            transfer()
        elif retransfer_input == "N":
            menu()
def done():
    if money_input_num == 0:
        print("You have not filled out your monthly income ")
        time.sleep(1)
        menu()
    elif rent_input_num == 0:
        print("You have not filled out your rent and utility bills")
        time.sleep(1)
        menu()
    elif groceries_input_num == 0:
        print("You have not filled out your grocery expenses")
        time.sleep(1)
        menu()
    else:
        done_input = input(f"Your current balance is {balance_input_num} \n You make {money_input_num} dollars monthly \n You spend {rent_input_num} dollars monthly on rent and utilities \n You spend {groceries_input_num} dollars weekly on groceries \n You have {saving_balance} dollars in your savings account \n Is all this correct?: Y/N?: ")
        if done_input == "Y":
            global total_spending
            total_spending = rent_input_num+(groceries_input_num*4)
            print(f"\nYou have {balance_input_num}, you make {money_input_num} dollars a month and spend {total_spending} dollars a month. ")
            changes()
            if total_spending > money_input_num:
                difference = money_input_num-total_spending
                print(f"Your monthly balance will be {difference}. I recommend you cut down on your spending. ")
                changes()
        if done_input == "N":
            print("Sending you back to the Menu...")
            menu()

def changes():
    change=input("Do you want to change anything? Y/N:  ")
    if change == "Y":
        menu()
    elif change== "N":
        print("Your Budgeting has been completed, have a nice day!")
    else:
        print("Please pick one")
        changes()

budget_program()