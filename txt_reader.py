import re
import typing


# Step 1 bank dict
def import_and_create_dictionary(filename: str) -> dict:
    d = {}

    for line in open(filename, 'r+'):
        pairlist = line.split('\n')
        pairwords = pairlist[0].split(':')
        key = pairwords[0].strip()
        if key != '':
            # print(f"key: {key}, value: {pairwords[1].strip()}")
            value = pairwords[1].strip()
            if bool(re.search(r'\d', value)):
                # print(f"key2: {key}, value: {value}")
                value = float(value)
                if key in d:
                    value += d[key]
                    d.update({key: value})
                else:
                    d[key] = value
    # testing
    # print(f'bank dictionary: {d}')
    return d


# Step 3
def import_and_create_accounts(filename: str) -> tuple:
    user_accounts = {}
    log_in = {}

    for line in open(filename, 'r+'):
        user_list = line.strip().split(' - ')

        # Validating credentials here because I can't figure out how to consistently get functions in other
        # Jupyter Notebook cells to work right.  This should really just call the sign-up or validate password
        # functions in the previous cell
        try:
            status4 = True
            if user_list[0] in user_accounts:
                status4 = False
                print(f'username already exists: {user_list[0]} - {user_list[1]}')
            if len(user_list[1]) < 8:
                status4 = False
                print(f'Password is not long enough: {user_list[0]} - {user_list[1]}')
            if user_list[0] == user_list[1]:
                status4 = False
                print(f'username and password can not be the same: {user_list[0]} - {user_list[1]}')

            status1 = status2 = status3 = False  # password charcter validation
            for c in user_list[1]:
                if 64 < ord(c) < 91:  # Uppercase
                    status1 = True
                if 96 < ord(c) < 123:  # Lowercase
                    status2 = True
                if 47 < ord(c) < 58:  # numbers 0-9
                    status3 = True

            if status1 and status2 and status3 and status4:
                user_accounts[user_list[0]] = user_list[1]
                log_in[user_list[0]] = False
            #     print(
            #         f'credentials successfully added to user_accounts dictionary and inital log_in dictionary: {user_list[0]} - {user_list[1]}')
            # else:
            #     print(
            #         f'password must include at least 1: lowercase, uppercase, and number: {user_list[0]} - {user_list[1]}')
        except IndexError as e:
            print(f'IndexError exception handled: {user_list[0]}')

    # debugging
    # print(f'user_accounts dictionary: {user_accounts}')
    # print(f'log_in dictionary: {log_in}')
    return user_accounts, log_in
