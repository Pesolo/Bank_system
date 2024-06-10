import csv
import pandas as pd
import os

class Bank:

    @staticmethod
    def create(id, name, dob):
        file = "data.csv"
        id = id
        name = name
        age = dob
        new_data = [id, name, age, "0.00"]
        with open(file, "a", newline="") as dfile:
            writer = csv.writer(dfile)
            writer.writerow(new_data)

    @staticmethod
    def deposit(id_, amount):
        lst = []
        #extract the csv file
        with open("data.csv", "r") as file :
            myfile = csv.DictReader(file)
            fieldname = myfile.fieldnames
            for row in myfile:
                if row["id"] == str(id_):
                    curr_value = float(row["balance"])
                    new_bal = curr_value + float(amount)
                    row["balance"] = "{:.2f}".format(new_bal)
                    print(f"#{amount}, successfully added")
                # else:
                #     print("You dont have an account with this bank")
                #     return
                lst.append(row)

        #update data
        with open("data.csv", "w", newline="") as file:
            newfile = csv.DictWriter(file, fieldnames=fieldname)
            newfile.writeheader()
            for row in lst:
                newfile.writerow(row)

    @staticmethod
    def withdraw(id_, amount):
        lst = []
        # extract the csv file
        with open("data.csv", "r", newline="") as file:
            myfile = csv.DictReader(file)
            fieldname = myfile.fieldnames
            for row in myfile:
                if row["id"] == str(id_):
                    curr_value = float(row["balance"])
                    if curr_value > float(amount):
                        new_bal = curr_value - float(amount)
                        row["balance"] = "{:.2f}".format(new_bal)
                        with open(f"{id_}.txt", mode="a") as file:
                            file.write(f"\n #{amount}, withdraw")
                        print(f"#{amount}, successfully withdrawn")
                    else:
                        print("Insufficient balance")
                        return
                # else:
                #     print("You dont have an account with this bank")
                #     return
                lst.append(row)

        # update data
        with open("data.csv", "w", newline="") as file:
            newfile = csv.DictWriter(file, fieldnames=fieldname)
            newfile.writeheader()
            for row in lst:
                newfile.writerow(row)

    @staticmethod
    def transfer(id_, amount, user):
        lst = []
        # extract the csv file
        with open("data.csv", "r", newline="") as file:
            myfile = csv.DictReader(file)
            fieldname = myfile.fieldnames
            for row in myfile:
                if row["id"] == str(id_):
                    curr_value = float(row["balance"])
                    if curr_value > float(amount):
                        new_bal = curr_value - float(amount)
                        row["balance"] = "{:.2f}".format(new_bal)
                        with open(f"{id_}.txt", mode="a") as file:
                            file.write(f"\n #{amount}, transferred to Banking id{user} ")
                    else:
                        print("Insufficient balance")
                        return
                if row["id"] == str(user):
                    curr_value = float(row["balance"])
                    new_bal = curr_value + float(amount)
                    row["balance"] = "{:.2f}".format(new_bal)
                    with open(f"{user}.txt", mode="a") as file:
                        file.write(f"\n #{amount}, recieved from Banking id{id_} ")
                lst.append(row)

        # update data
        with open("data.csv", "w", newline="") as file:
            newfile = csv.DictWriter(file, fieldnames=fieldname)
            newfile.writeheader()
            for row in lst:
                newfile.writerow(row)

        print(f"#{amount}, succefully transferred to Bankid{user}")

    @staticmethod
    def del_acct(id_):
        file_path = f"{id_}.txt"

        # Check if the file exists before attempting to delete it
        if os.path.exists(file_path):
            df = pd.read_csv("data.csv")
            id_to_delete = str(id_)

            df = df[df['id'].astype(str).str.strip() != id_to_delete.strip()]

            df.to_csv("data.csv", index=False)

            os.remove(file_path)
            print(f"Banking Id {id_} records has been deleted.")
        else:
            print(f"Banking Id {id_} does not exist.")

