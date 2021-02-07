import re


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
                if d.keys().__contains__(key):
                    value += d[key]
                    d.update({key: value})
                else:
                    d[key] = value

    return d

result = import_and_create_dictionary('bank.txt')
print(f"import_and_create_dictionary, result: {result}")