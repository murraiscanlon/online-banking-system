from termcolor import colored
from txt_writer import  update_user, update_bank


# User can sign up for an account.
def signup(user_accounts: dict, log_in: dict, username: str, password: str, bnk: dict) -> bool:
    if username in user_accounts:
        print('username already exists')
        return False

    if username == password:
        print('username and password can not be the same')
        return False

    isValidPassword = validate_password(password)

    if isValidPassword:
        user_accounts[username] = password
        log_in[username] = False
        update_user(user_accounts)
        bnk[username] = "0"
        update_bank(bnk)
        print(f'Account successfully created for "{username}"')
        # TODO Do I set log-ins to False here or in the next function? Why is log-in a parameter??
    else:
        print('password must include at least 1: lowercase, uppercase, and number')
    # debugging
    # print(f"user_accounts dict: {user_accounts}")
    return True


# Once user has signed-up, they can log in to their account
def login(user_accounts: dict, log_in: dict, username: str, password: str) -> bool:
    if username not in user_accounts:
        print(colored(f'\nError: username is not found: "{username}"', 'red'))
        return False
    elif user_accounts[username] != password:
        print(colored(f'\nError: username and password do not match: "{username}" "{password}"', 'red'))
        return False
    else:
        if log_in[username]:
            print(colored(f'\nError: already logged-in: "{username}" "{password}"', 'red'))
            return False

    if username == password:
        print(colored(f'\nusername and password can not be the same: "{username} - {password}"'), 'red')
        return False

    isValidPassword = validate_password(password)

    if isValidPassword:
        log_in.update({username: True})
        print(colored(f'\nLog-in successful.', 'green'))
        # For testing
        # print(f'\nlog_in dictionary: {log_in}')
        # print(f'\nuser_accounts dictionary: {user_accounts}')
        return True
    else:
        print(
            colored(f'\npassword must include at least 1: lowercase, uppercase, and number: "{username} - {password}"',
                    'red'))
        return False


# update account balance
def update(bank, log_in, username, amount):
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
        update_bank(bank)
        print(
            f'account deposit successful: {username}: previous balance = {current_amount}, new balance = {bank[username]} ')
        return True
    elif amount < 0:
        if current_amount + amount < 0:
            print(f'Unable to complete the transaction: {username} {amount}')
            return False
        else:
            current_amount = bank[username]
            bank.update({username: (current_amount + amount)})
            update_bank(bank)
            print(f'account withdraw successful: previous balance = {current_amount}, new balance = {bank[username]} ')
            return True
    else:
        print(f'An error has occurred in the update amount function')
        return False


# transfer from one account to another
def transfer(bank, log_in, userA, userB, amount):
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

    # Make transfer
    # TODO This is only updating the bank parameter dictionary, NOT the bank.txt
    current_amount_userA = bank[userA]
    current_amount_userB = bank[userB]
    bank.update({userA: (current_amount_userA - amount)})
    bank.update({userB: (current_amount_userB + amount)})
    update_bank(bank)
    print(f'transfer successful, {userA} new balance = {bank[userA]}, {userB} new balance = {bank[userB]}')
    return True


# change password
def change_password(user_accounts: dict, log_in: dict, username: str, old_password: str, new_password: str) -> bool:
    if username not in user_accounts:
        print(f'{username} not found')
        return False

    if not log_in[username]:
        print(f'{username} must be logged-in to continue')
        return False

    if user_accounts[username] != old_password:
        print(f'{old_password} does not match the original password')
        return False

    if new_password == old_password:
        print(f'{new_password} should not match {old_password}')
        return False

    isValidPassword = validate_password(new_password)

    if isValidPassword:
        user_accounts.update({username: new_password})
        update_user(user_accounts)
        print(colored(f'password updated for {username}', 'green'))
        return True

    print(f'an error has occurred. Password has not been updated for: {username}')
    return False


# delete account
def delete_account(user_accounts: dict, log_in: dict, bank: dict, username: str, password: str) -> bool:
    if username not in user_accounts:
        print(f'{username} was not found')
        return False
    if user_accounts[username] != password:
        print(f'{username} incorrect password')
        return False
    if not log_in[username]:
        print(f'{username} is not currently logged in')
        return False

    deleted_account = user_accounts.pop(username)
    deleted_account = log_in.pop(username)
    deleted_account = bank.pop(username)

    update_user(user_accounts)
    update_bank(bank)

    print(f'{username} has been successfully deleted')
    return True


# Helper function for signup and login
def validate_password(password: str) -> bool:
    if len(password) < 8:
        print(colored(f'\nError: Password is not long enough: "{password}"', 'red'))
        return False

    status1 = status2 = status3 = False  # password charcter validation

    for c in password:
        if 64 < ord(c) < 91:  # Uppercase
            status1 = True
        if 96 < ord(c) < 123:  # Lowercase
            status2 = True
        if 47 < ord(c) < 58:  # numbers 0-9
            status3 = True

    return status1 and status2 and status3
