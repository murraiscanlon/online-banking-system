from txt_reader import import_and_create_dictionary, import_and_create_accounts
from user_actions import signup, login, change_password, update, transfer, delete_account


def main():
    bank = import_and_create_dictionary("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")  # returns dictionaries

    while True:
        # for debugging
        # print('bank:', bank)
        # print('user_accounts:', user_accounts)
        # print('log_in:', log_in)
        # print('')

        option = input(
            "------------\n"
            "Options Menu\n"
            "------------\n"
            "\t1. login\n"
            "\t2. signup\n"
            "\t3. change password\n"
            "\t4. delete account\n"
            "\t5. update amount\n"
            "\t6. make a transfer\n"
            "\t0. exit\n"
            "What do you want to do?  Please enter a numerical option here: ")
        if option == "1":
            username = input("Please input the username: ")
            password = input("Please input the password: ")
            login(user_accounts, log_in, username, password)  # refactored with typehints

        elif option == "2":
            username = input("Please enter a username: ")
            password = input("\tPassword requirements:\n"
                             "\t1. 8 characters or longer\n"
                             "\t2. contains uppercase and lowercase letters\n"
                             "\t3. Contains at least 1 number\n"
                             "Please enter a valid password: ")
            signup(user_accounts, log_in, username, password, bank)

        elif option == "3":
            username = input("Please input the username: ")
            old_password = input("Please input the old password: ")
            new_password = input("Please input the new password: ")
            change_password(user_accounts, log_in, username, old_password, new_password)

        elif option == "4":
            username = input("Please input the username: ")
            password = input("Please input the password: ")
            delete_account(user_accounts, log_in, bank, username, password)

        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "0":
            break
        else:
            print("The option is not valid. Please re-enter the option.\n")


# automatically run main()
if __name__ == '__main__':
    main()
