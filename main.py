import pandas
from profile import Bank
import random
import os



def unique_id():
    data = pandas.read_csv("data.csv")
    ids = [x for x in data["id"]]
    id = 1 if len(ids) < 1 else max(ids) + 1
    return id
    # while True:
    #     id = random.randint(1, 10)
    #     if str(id).strip() not in ids:
    #         return id

    # for index in data.index:
    #     if data["id"][index] != str(id):
    #         return id
    #     else:
    #         id = random.randint(1, 10)

def profile_create():
    name = input("Enter your name: ")
    age = input("Enter your date of birth(dd-mm-yyyy): ")
    try:
        id = unique_id()
        print(f"Your banking Id is {id}")
        Bank.create(id, name, age)
        with open(f"{str(id)}.txt", "w", newline="") as file:
            file.write("Transaction history")

    except FileNotFoundError:
        bank_details = {
            'id': ["1"],
            'names': [name],
            'DOB': [age],
            'balance': ["0.00"]
        }

        customers_data = pandas.DataFrame(bank_details)
        customers_data.to_csv("data.csv", index=False)
        print("Your Banking ID is 1")
        with open("1.txt", "w", newline="") as file:
            file.write("Transaction history")



def mak_deposit():
    user = input("Enter your banking id: ")
    mon_dep = input("Enter the amount you wish to deposit: ")

    file_path = f"{user}.txt"
    # Check if the file exists
    if os.path.exists(file_path):
        Bank.deposit(id_=user, amount=mon_dep)
        with open(f"{user}.txt", mode="a") as file:
            file.write(f"\n #{mon_dep}, Deposited")

    else:
        print(f"The banking id {user} does not exist.")



def mak_withdraw():
    user = input("Enter your banking id: ")
    mon_wit = input("Enter the amount you wish to withdraw: ")
    file_path = f"{user}.txt"
    # Check if the file exists
    if os.path.exists(file_path):
        Bank.withdraw(id_=user, amount=mon_wit)

    else:
        print(f"The banking id {user} does not exist.")


def balance():
    id_ =str(input("Enter your banking id: "))
    myfile = pandas.read_csv("data.csv")

    for (index, row) in myfile.iterrows():
        if str(row["id"]) == id_:
            print(f"Your Balance is #{row['balance']}")

def transfer_funds():
    user = input("Enter your banking id: ")
    benef = input("Enter the banking id you want to make transfer  to : ")
    money = input("Enter the amount you want to transfer: ")

    send_path = f"{user}.txt"
    rec_path = f"{benef}.txt"

    if not os.path.exists(send_path):
        print("Your banking id is invalid")
        return

    if not os.path.exists(rec_path):
        print("Reciever banking id is invalid")
        return

    Bank.transfer(user, money, benef)


def open_page():
    entry = input("If you are a new user press 1\n" "If you are an existing user press 2\n" "Please Select: ")
    if entry == "1":
        return "1"
    elif entry == "2":
        return "2"
    else:
        print("Wrong Selection")
        open_page()


def banking_oper():
    choice = input("To deposit press 1\n" "To withdraw press 2\n" "To check balance press 3\n"
                   "To transfer money press 4\n" "To check transaction history press 5\n" 
                   "To delete your account press 6\n" "To Exit press 7\n" "Please select: ")
    if choice == "1":
        return "1"
    elif choice == "2":
        return "2"
    elif choice == "3":
        return "3"
    elif choice == "4":
        return "4"
    elif choice == "5":
        return "5"
    elif choice == "6":
        return "6"
    elif choice == "7":
        return "7"
    else:
        print("Wrong Selection")
        return banking_oper()

def transact_hist():
    user = input("Input your Banking Id: ")
    file_path = f"{user}.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()

        print(content)
    else:
        print(f"banking id{user}, does not exist")


def acct_del():
    choice = input("Are you sure you want to delete your account, Enter Y/N: ").lower()
    if choice == "y":
        user = input("Enter Your Banking id: ")
        Bank.del_acct(user)



banking = True
print("Welcome to A325 Bank")
if open_page() == "1":
    profile_create()

while banking:
    choice = banking_oper()
    if choice == "1":
        mak_deposit()
    elif choice == "2":
        mak_withdraw()
    elif choice == "3":
        balance()
    elif choice == "4":
        transfer_funds()
    elif choice == "5":
        transact_hist()
    elif choice == "6":
        acct_del()
    elif choice == "7":
        print("Thank You for banking with us")
        banking = False


