import re


# Step 1 bank dict
def import_and_create_dictionary(filename):
    '''
    This function is used to create a bank dictionary.  The given argument is the filename to load.
    Every line in the file will look like
    key: value
    Key is a user's name and value is an amount to update the user's bank account with.  The value should be a
    number, however, it is possible that there is no value or that the value is an invalid number.

    What you will do:
    - Try to make a dictionary from the contents of the file.
    - If the key doesn't exist, create a new key:value pair.
    - If the key does exist, increment its value with the amount.
    - You should also handle cases when the value is invalid.  If so, ignore that line and don't update the dictionary.
    - Finally, return the dictionary.

    Note: All of the users in the bank file are in the user account file.
    '''

    d = {}

    # your code here
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
    print(f'bank dictionary: {d}')
    return d





# Step 3
def import_and_create_accounts(filename):
    '''
    This function is used to create an user accounts dictionary and another login dictionary.  The given argument is the filename to load.
    Every line in the file will look like
      username - password

    If the username and password fulfills the requirement, add the username and password into the user accounts dictionary.
    To make sure that the password fulfills these requirements, be sure to use the signup function that you wrote above.

    For the login dictionary, the key is the username, and its value indicates whether the user is logged in, or not.
    Initially, all users are not logged in.

    Finally, return the dictionaries.

    Note: All of the users in the bank file are in the user account file.
    '''

    user_accounts = {}
    log_in = {}

    # your code here
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
                print(
                    f'credentials successfully added to user_accounts dictionary and inital log_in dictionary: {user_list[0]} - {user_list[1]}')
            else:
                print(
                    f'password must include at least 1: lowercase, uppercase, and number: {user_list[0]} - {user_list[1]}')
        except IndexError as e:
            print(f'IndexError exception handled: {user_list[0]}')

    print(f'user_accounts dictionary: {user_accounts}')
    print(f'log_in dictionary: {log_in}')
    return user_accounts, log_in