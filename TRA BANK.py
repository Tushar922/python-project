import random
import time
import re
import os

class Customers:

    """This is the initial method of the customer class"""
    def __init__(self):
        self.customer_list = {"name": [], "surname": [], "password": [], "accountnum": [], "balance": []}

    """When this method is called, accountnum and balance occurs, name, surname and password are taken as parameter
    After password parameter sends to the choosing_password method to be controlled for validation """

    def create_customers(self, name, surname, password):
        while True:
            flag = 0
            self.accountnum = str(random.randint(10000000, 99999999))
            self.balance = 0
            self.name = name
            self.surname = surname
            self.password = self.choosing_password(password)
            if not bool(self.password):
                flag = -1
                return flag
            elif flag == 0:
                return flag

    """This method adds the customer information to the customer list"""

    def add_customer(self):
        self.customer_list["name"].append(self.name)
        self.customer_list["surname"].append(self.surname)
        self.customer_list["password"].append(self.password)
        self.customer_list["accountnum"].append(self.accountnum)
        self.customer_list["balance"].append(self.balance)

    """This method removes the chosen customer from the customer list
     after controlling whether chosen customer is exist or not """

    def remove_customer(self, remove_name, remove_surname):
        for i in self.customer_list["name"]:
            if remove_name == i:
                for k in self.customer_list["surname"]:
                    index = self.customer_list["surname"].index(k)
                    if remove_surname == k:
                        self.customer_list["name"].pop(index)
                        self.customer_list["surname"].pop(index)
                        self.customer_list["password"].pop(index)
                        self.customer_list["accountnum"].pop(index)
                        self.customer_list["balance"].pop(index)
                        wait(3)
                        print("Your operation completed")

    """This method controls whether chosen customer is exist or not and send remove_name and remove_surname to 
    remove_customer method as parameters"""

    def is_there_customer(self, remove_name, remove_surname):
        flag = 0
        for i in self.customer_list["name"]:
            if remove_name == i:
                for k in self.customer_list["surname"]:
                    if remove_surname == k:
                        self.remove_customer(remove_name, remove_surname)
                        return flag

    """This method controls name, surname and password in customer list for sign in"""

    def entrance_control(self, entrance_name, entrance_surname, entrance_password):
        for i in self.customer_list["name"]:
            if entrance_name == i:

                for k in self.customer_list["surname"]:
                    if entrance_surname == k:

                        for j in self.customer_list["password"]:
                            if entrance_password == j:

                                return True

    """This method defines some conditions to customers' password definition"""

    def choosing_password(self, entrance_password):
        flag = 0
        while True:
            if len(entrance_password) < 8:
                flag = -1
                break
            elif not re.search("[a-z]", entrance_password):
                flag = -1
                break
            elif not re.search("[A-Z]", entrance_password):
                flag = -1
                break
            elif not re.search("[0-9]", entrance_password):
                flag = -1
                break
            elif not re.search("[-_!@]\n", entrance_password):
                flag = -1
                break
            elif re.search("\s", entrance_password):
                flag = -1
                break
            else:
                flag = 0
                print("Valid password")
                return entrance_password
        if flag == -1:
            print("Invalid password")

    """"This method controls the name and surname of customer who the money will transfer to in money transfer part """

    def money_transfer_validation(self, name, surname):

        for i in self.customer_list["name"]:
            if name == i:

                for k in self.customer_list["surname"]:
                    if surname == k:
                        return True


""""This method keeps wait after some operations """

def wait(n):
    str = "Your transaction is running"
    point = "."
    print(str, end="")
    for i in range(n):
        os.system('cls')
        print(point)
        time.sleep(0.5)
        point += "."


def main():

    customer = Customers()

    while True:

        print("-----------------------------\n"
              "WELCOME TO THE TRA BANK\n"
              "-----------------------------\n"
              "Please choose your operation \n"
              "=============================\n"
              "[1] Sign in\n"
              "[2] Sign up\n"
              "[3] Management")

        selection = input("")

        if selection == "1":
            entrance_name = input("Name:")
            entrance_surname = input("Surname:")
            entrance_password = input("Password:")
            if customer.entrance_control(entrance_name, entrance_surname, entrance_password):

                while True:

                    index = int(customer.customer_list["password"].index(entrance_password))
                    print("Welcome..{}\t{}        \n"
                          "Chose your operation   \n"
                          "-----------------------\n"
                          "[1] Account information\n"
                          "[2] Withdraw money     \n"
                          "[3] Deposit money      \n"
                          "[4] Money transfer     \n"
                          "[Q or q] Quit          \n".format(entrance_name.title(), entrance_surname.upper()))
                    selection = input()
                    if selection == "q" or selection == "Q":

                        break

                    elif selection == "1":
                        while True:

                            print("Name: {}       \n"
                                  "Surname:{}     \n"
                                  "Password:{}    \n"
                                  "account no:{} \n"
                                  "Balance:{}".format(customer.customer_list["name"][index], customer.customer_list["surname"][index],
                                                                    customer.customer_list["password"][index], customer.customer_list["accountnum"][index],
                                                                    customer.customer_list["balance"][index]))
                            input("to menu press enter")
                            break
                    elif selection == "2":
                        while True:

                            wd_money = int(input("Write the the amount of money that you want to withdraw"))
                            if customer.customer_list["balance"][index] < wd_money:
                                wait(3)
                                print("You don not have enough money to apply this operation")
                                input("to menu press enter")
                                break
                            elif customer.customer_list["balance"][index] > wd_money:
                                customer.customer_list["balance"][index] -= wd_money
                                wait(3)
                                print("Operation completed")
                                input("to menu press enter")
                                break
                            elif customer.customer_list["balance"][index] == wd_money:
                                selection = input("You are about to withdraw all your money are you sure? [yes/y][no/n]")
                                if selection == "n" or selection == "N":
                                    print("Operation is cancelling...")
                                    input("to menu press enter")
                                    break
                                elif selection == "y" or selection == "Y":
                                    customer.customer_list["balance"][index] -= wd_money
                                    wait(3)
                                    print("Operation completed")
                                    input("to menu press enter")
                                    break
                                elif selection != "y" or selection != "Y" or selection != "n" or selection != "N":
                                    while True:
                                        print("Please press valid button")
                                        break

                    elif selection == "3":
                        while True:

                            deposit = int(input("Enter the amount that you want to deposit:"))
                            customer.customer_list["balance"][index] += deposit
                            wait(3)
                            print("Operation completed")
                            input("to menu press enter")
                            break
                    elif selection == "4":
                        while True:
                            print("To whom do you want to send money?")
                            name = input("Name:")
                            surname = input("Surname:")
                            if customer.money_transfer_validation(name, surname):
                                index_transfer = int(customer.customer_list["surname"].index(surname))
                                if index_transfer != index:
                                    try:
                                        transfer_money = int(input("How much money do you want to send to {}\t{}".format(customer.customer_list["name"][index_transfer],
                                                                                                    customer.customer_list["surname"][index_transfer])))
                                        if transfer_money > customer.customer_list["balance"][index]:
                                            input("You do not have enough money to transfer \n"
                                                  "enter to return menu")
                                            break
                                        elif transfer_money == customer.customer_list["balance"][index]:
                                            selection = input("You are about to send all your money are you sure [y/n] ")

                                            if selection == "Y" or selection == "y":

                                                   customer.customer_list["balance"][index_transfer] += transfer_money
                                                   customer.customer_list["balance"][index] -= transfer_money
                                                   wait(3)
                                                   print("Operation completed")
                                                   break
                                            elif selection == "N" or selection == "n":

                                                print("Operation cancelling...")
                                                break
                                            else:
                                               while True:
                                                   print("Press valid button")
                                                   break

                                        elif transfer_money < customer.customer_list["balance"][index]:
                                            customer.customer_list["balance"][index_transfer] += transfer_money
                                            customer.customer_list["balance"][index] -= transfer_money
                                            wait(3)
                                            print("Operation completed")
                                            break
                                    except ValueError:
                                        print("Please write integer value")
                                        break
                                else:
                                    print("You can not send money on your own")

                            else:
                                print("Could not find user")
                                break

                    else:
                        while True:
                            print("Invalid choice")
                            break
            else:
                while True:
                    if input("Wrong password or username \n"
                             "to main menu press enter") == "":
                        break
        elif selection == "2":
            while True:

                flag = customer.create_customers(input("Name:"), input("Surname:"), input("Primary conditions for password validation:          \n"
                                                                                   "1.Minimum 8 characters.                              \n"
                                                                                   "2.The alphabets must be between [a-z]                \n"
                                                                                   "3.At least one alphabet should be of Upper Case [A-Z]\n"
                                                                                   "4.At least 1 number or digit between [0-9].          \n"
                                                                                   "5.At least 1 character from [ _ or - or ! or @ ]."))

                if flag == 0:
                    print("Your account is creating")
                    wait(3)
                    print("Your account has been created")
                    customer.add_customer()
                    input("-----------------------------\n"
                          "To continue press enter")
                    break
                while True:
                    if flag == -1:
                        break

        elif selection == "3":
            while True:

                print("Welcome to management part")
                selection = input("--------------------------\n"
                                  "Make a selection \n"
                                  "[1] Show the customer information\n"
                                  "[2] Remove customers\n"
                                  "[Q] to return main menu")
                                  
                if selection == "1":
                    print("Name:{}\n"
                          "Surname:{}\n"
                          "Password:{}\n"
                          "accountnum:{}\n"
                          "Balance:{}".format(customer.customer_list["name"],
                                                  customer.customer_list["surname"],
                                                  customer.customer_list["password"],
                                                  customer.customer_list["accountnum"],
                                                  customer.customer_list["balance"]))
                elif selection == "2":
                    if len(customer.customer_list["name"]) == 0:
                        print("There are no customers")
                        enter = input("Press enter to return main menu\n")
                        if enter == "":
                            break
                    else:
                        flag = customer.is_there_customer(input("Name"), input("Surname"))
                        if flag == 0:
                            while True:

                                enter = input("Press enter to return main menu\n"
                                              "--------------------------------")
                                if enter == "":
                                    break
                                elif enter != "":
                                    while True:
                                        print("Please press valid button\n"
                                              "Press enter to return main menu\n")
                                        break
                        else:
                            print("The user can not found")

                elif selection == "q" or selection == "Q":
                    break
                else:
                    while True:

                        print("Press valid button")
                        break
        else:
            while True:

                print("Please make a valid selection")
                print("-----------------------------\n"
                      "To continue press enter")
                input()
                break

main()