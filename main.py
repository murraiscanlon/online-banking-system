from functions import *

username = 'Brandon'
password = 'brandon123ABC'

# Step 1
# import_and_create_dictionary('bank.txt')

user_accounts = {
    'Brandon': 'brandon123ABC',
    'Jack': 'jack123POU',
    'James': '100jamesABD',
    'Sarah': 'sd896ssfJJH',
}

log_in = {
    'Brandon': True,
    'Jack': False,
    'James': False,
    'Sarah': False,
}

# Step 2
# signup(user_accounts, log_in, username, password)

# Step 3
#import_and_create_accounts('user.txt')

# Step 4
login(user_accounts, log_in, username, password)

