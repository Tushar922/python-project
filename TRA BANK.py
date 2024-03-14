import random
import time
import re
import os

class Customers:
    def __init__(self):
        self.customer_list = {"name": [], "surname": [], "password": [], "accountnum": [], "balance": [], "loan": []}

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

    def add_customer(self):
        self.customer_list["name"].append(self.name)
        self.customer_list["surname"].append(self.surname)
        self.customer_list["password"].append(self.password)
        self.customer_list["accountnum"].append(self.accountnum)
        self.customer_list["balance"].append(self.balance)
        self.customer_list["loan"].append(0)  # Initialize loan amount to 0 for new customers

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
                        self.customer_list["loan"].pop(index)
                        wait(3)
                        print("Your operation completed")

    def is_there_customer(self, remove_name, remove_surname):
        flag = 0
        for i in self.customer_list["name"]:
            if remove_name == i:
                for k in self.customer_list["surname"]:
                    if remove_surname == k:
                        self.remove_customer(remove_name, remove_surname)
                        return flag

    def entrance_control(self, entrance_name, entrance_surname, entrance_password):
        for i in self.customer_list["name"]:
            if entrance_name == i:
                for k in self.customer_list["surname"]:
                    if entrance_surname == k:
                        for j in self.customer_list["password"]:
                            if entrance_password == j:
                                return True

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

    def money_transfer_validation(self, name, surname):
        for i in self.customer_list["name"]:
            if name == i:
                for k in self.customer_list["surname"]:
                    if surname == k:
                        return True

    def apply_loan(self, name, surname, loan_amount):
        for i in range(len(self.customer_list["name"])):
            if self.customer_list["name"][i] == name and self.customer_list["surname"][i] == surname:
                current_balance = self.customer_list["balance"][i]
                if loan_amount <= current_balance * 2:  # Example: Loan amount cannot exceed double the current balance
                    self.customer_list["balance"][i] += loan_amount
                    self.customer_list["loan"][i] += loan_amount
                    wait(3)
                    print("Loan successfully applied!")
                    return True
                else:
                    wait(3)
                    print("Loan amount exceeds eligibility (maximum loan amount is double the current balance)")
                    return False
        wait(3)
        print("Customer not found!")
        return False


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
              "[3] Apply for Loan\n"
              "[4] Management")

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
                          "[5] Apply for Loan     \n"
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
                                  "Balance:{}\n"
                                  "Loan:{}".format(customer.customer_list["name"][index], customer.customer_list["surname"][index],
                                                  customer.customer_list["password"][index], customer.customer_list["accountnum"][index],
                                                  customer.customer_list["balance"][index], customer.customer_list["loan"][index]))
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
                                    except ValueError:
                                        print("erorr",191)
                    elif selection == "5":
                        while True:
                            loan_amount = float(input("Enter the loan amount: "))
                            customer.apply_loan(entrance_name, entrance_surname, loan_amount)
                            

if __name__ == "__main__":
    main()