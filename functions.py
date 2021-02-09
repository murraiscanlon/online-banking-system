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


# For Testing
# result = import_and_create_dictionary('bank.txt')
# print(f"import_and_create_dictionary, result: {result}")


# Step 2
def signup(user_accounts, log_in, username, password):
    '''
    This function allows users to sign up.
    If both username and password meet the requirements, updates the username and the corresponding password in the user_accounts,
    and returns True.

    If the username and password fail to meet any one of the following requirements, returns False.
    - The username already exists in the user_accounts.
    - The password must be at least 8 characters.
    - The password must contain at least one lowercase character.
    - The password must contain at least one uppercase character.
    - The password must contain at least one number.
    - The username & password cannot be the same.

    For example:
    - Calling signup(user_accounts, log_in, "Brandon", "123abcABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK", "123ABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK","abcdABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK", "123aABCD") will return True. Then calling
    signup(user_accounts, log_in, "BrandonK", "123aABCD") again will return False.

    Hint: Think about defining and using a separate valid(password) function that checks the validity of a given password.
    This will also come in handy when writing the change_password() function.
    '''
    # your code here
    if username in user_accounts:
        print('username already exists')
        return False
    if len(password) < 8:
        print('Password is not long enough')
        return False
    if username == password:
        print('username and password can not be the same')
        return False

    status1 = status2 = status3 = False
    for c in password:
        if 64 < ord(c) < 91:
            status1 = True
        if 96 < ord(c) < 123:
            status2 = True
        if 47 < ord(c) < 58:
            status3 = True

    if status1 and status2 and status3:
        user_accounts[username] = password
        print('log-in successful')
        # TODO Do I set log-ins to False here or in the next function? Why is log-in a parameter??
    else:
        print('password must include at least 1: lowercase, uppercase, and number')

    print(f"user_accounts dict: {user_accounts}")  # for testing
    return status1 and status2 and status3


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


# Step 4
def login(user_accounts, log_in, username, password):
    '''
    This function allows users to log in with their username and password.
    The users_accounts stores the usernames and passwords.

    If the username does not exist or the password is incorrect, return False.
    Otherwise, return True.

    For example:
    - Calling login(user_accounts, "Brandon", "123abcAB") will return False
    - Calling login(user_accounts, "Brandon", "brandon123ABC") will return True

    Note: If a user is already logged in, this should return False - a user cannot log
    in a second time once logged in
    '''

    # your code here
    # if log_in[username]: # Check to see if user is already logged-in
    #     print(f'user already logged in: {username}')
    #     return False

    if username not in user_accounts:
        print(f'username is not found: {username}')
        return False
    elif user_accounts[username] != password:
        print(f'username and password do not match: {username} {password}')
        return False
    else:
        if log_in[username]:
            print(f'already logged-in: {username} {password}')
            return False

    # Validate password. . .the long way. . .AGAIN
    if len(password) < 8:
        print(f'Password is not long enough: {username} - {password}')
        return False
    if username == password:
        print(f'username and password can not be the same: {username} - {password}')
        return False

    status1 = status2 = status3 = False  # password charcter validation
    for c in password:
        if 64 < ord(c) < 91:  # Uppercase
            status1 = True
        if 96 < ord(c) < 123:  # Lowercase
            status2 = True
        if 47 < ord(c) < 58:  # numbers 0-9
            status3 = True

    if status1 and status2 and status3:
        log_in.update({username: True})
        print(f'log-in successful: {username} - {password}')
        print(f'log_in dictionary: {log_in}')
        print(f'user_accounts dictionary: {user_accounts}')
        return True
    else:
        print(f'password must include at least 1: lowercase, uppercase, and number: {username} - {password}')
        return False


# Step 5
def update(bank, log_in, username, amount):
    '''
    In this function, you will try to update the given user's bank account with the given amount.
    The amount is an integer, and can either be positive or negative.

    To update the user's account with the amount, the following requirements must be met:
    - The user exists in log_in and his/her status is True, meaning, the user is logged in.

    If the user doesn't exist in the bank, create the user.
    - The given amount can not result in a negative balance in the bank account.

    return True if the user's account was updated.

    For example:
    - Calling update(bank, log_in, "Brandon", 100) will return False, unless "Brandon" is first logged in.  Then it
    will return True.
    - Calling update(bank, log_in, "Brandon", -200) will return False
    '''

    # your code here
    update_status = False  # May not need this. Not sure of convention. No return statement at the very end
    current_amount = 0.0

    if username in log_in:  # program throws KeyError without this line first
        if not log_in[username]:  # log-in value must be True to proceed
            print(f'user is not logged-in: {username}')
            return False
    else:
        print(f'user is not found in log_in: {username}')
        return False

    if username not in bank:
        bank[username] = current_amount
        print(f'user has been added: {username}, with initial amount -  {bank[username]}')

    # Update the account balance
    current_amount = bank[username]
    if amount > 0:
        bank.update({username: (current_amount + amount)})
        print(f'account deposit successful: {username}: previous balance = {current_amount}, new balance = {bank[username]} ')
        return True
    elif amount < 0:
        if current_amount + amount < 0:
            print(f'Unable to complete the transaction: {username} {amount}')
            return False
        else:
            current_amount = bank[username]
            bank.update({username: (current_amount + amount)})
            print(f'account withdraw successful: previous balance = {current_amount}, new balance = {bank[username]} ')
            return True
    else:
        print(f'An error has occurred in the update amount function')
        return False


# Step 6
def transfer(bank, log_in, userA, userB, amount):
    '''
    In this function, you will try to make a transfer between two user accounts.
    The bank is a dictionary, where the key is the username and the value is the amount to transfer.
    Amount is always positive.

    What you will do:
    - Deduct the amount from userA and add it to userB, which makes a transfer.
    - You should consider some following cases:
      - userA must be in accounts and his/her log-in status must be True.
      - userB must be in log_in, regardless of log-in status.  userB can be absent in accounts.
      - No user can have a negative amount. He/she must have a positive or zero amount.

    Return True if a transfer is made. If a user is invalid or the amount is invalid, return False.
    userA must be in bank and userB can be absent from bank. No user can have a negative balance.
    Each must have a positive or zero balance

    For example:
    - Calling transfer(bank, log_in, "BrandonK", "Jack", 100) will return False
    - Calling transfer(bank, log_in, "Brandon", "JackC", 100) will return False
    - After logging "Brandon" in, calling transfer(bank, log_in, "Brandon", "Jack", 10) will return True
    - Calling transfer(bank, log_in, "Brandon", "Jack", 200) will return False

    Note that the arguments correspond as follows:
        o bank: The bank accounts dictionary
        o log_in: The user accounts dictionary
        o userA: The account from which the funds will be transferred
        o userB: The account to which the funds will be transferred
        o amount: The amount to transfer
    '''

    # your code here
    if userA not in bank:
        print(f'{userA} is not in the bank dictionary')
        return False
    if userA not in log_in or userB not in log_in:
        print(f'{userA} or {userB} was not found in log_in dictionary')
        return False
    if not log_in[userA]:
        print(f'{userA} is not logged-in')
        return False
    if amount > bank[userA]:
        print(f'not enough funds to make the transfer from {userA}, current amount = {bank[userA]}')
        return False
    if userB not in bank:
        bank[userB] = 0.0
    if bank[userA] < 0 or bank[userB] < 0:
        print(f'{userA} or {userB} has a current negative balance')
        return False

    #Make transfer
    #TODO This is only updating the bank parameter dictionary, NOT the bank.txt
    current_amount_userA = bank[userA]
    current_amount_userB = bank[userB]
    bank.update({ userA: (current_amount_userA - amount)})
    bank.update({ userB: (current_amount_userB + amount)})
    print(f'transfer successful, {userA} new balance = {bank[userA]}, {userB} new balance = {bank[userB]}')
    return True

# Step 7
def change_password(user_accounts, log_in, username, old_password, new_password):
    '''
    This function allows users to change their password.

    If all of the following requirements are met, change the password and return True. Otherwise, return False.
    - The username exists in the user_accounts.
    - The old_password is the user's current password.
    - The new_password should be different from the old one.
    - The new_password fulfills the requirement in signup.

    For example:
    - Calling change_password(user_accounts, log_in, "BrandonK", "123abcABC" ,"123abcABCD") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "123abcABCD", "123abcABCDE") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "brandon123ABC", "brandon123ABC") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "brandon123ABC", c"123abcABCD") will return True

    Hint: Think about defining and using a separate valid(password) function that checks the validity of a given password.
    This will also come in handy when writing the signup() function.
    '''

    # your code here
    if username not in user_accounts:
        print(f'{username} not in user_accounts dict')
        return False
    if user_accounts[username] != old_password:
        print(f'{old_password} does not match the original password')
        return False

    if new_password == old_password:
        print(f'{new_password} should not match {old_password}')
        return False

    if len(new_password) < 8:
        print('new_password is not long enough')
        return False

    status1 = status2 = status3 = False
    for c in new_password:
        if 64 < ord(c) < 91:
            status1 = True
        if 96 < ord(c) < 123:
            status2 = True
        if 47 < ord(c) < 58:
            status3 = True

    if status1 and status2 and status3:
        user_accounts.update({username: new_password})
        print(f'password updated for {username}')
        return True

    print(f'an error has occurred. Password has not been updated: {username}')
    return False









