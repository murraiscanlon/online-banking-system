from functions import *

username = 'BrandonK'
password = ''
amount = 10

userA = 'Brandon'
userB = 'BrandonK'


# Step 1
# import_and_create_dictionary('bank.txt')

bank = {
    'Brandon': 115.5,
    'Patrick': 18.9,
    'Sarah': 827.43,
    'Jack': 45.0,
    'James': 128.87
}

user_accounts = {
    'Brandon': 'brandon123ABC',
    'Jack': 'jack123POU',
    'James': '100jamesABD',
    'Sarah': 'sd896ssfJJH',
    'BrandonK': '123aABCD'
}

log_in = {
    'Brandon': True,
    'Jack': False,
    'James': False,
    'Sarah': False,
    'BrandonK': True
}

# Step 2
# signup(user_accounts, log_in, username, password)

# Step 3
#import_and_create_accounts('user.txt')

# Step 4
# login(user_accounts, log_in, username, password)

# Step 5
# update(bank, log_in, username, amount)

# Step 6
transfer(bank, log_in, userA, userB, amount)

