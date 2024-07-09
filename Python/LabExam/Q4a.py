# Write a python program to initialize a dictionary of usernames and passwords associated with it.  
# passwd={‘rahul’: ‘genius’, ‘kumar’: ‘smart’, ‘ankita’: ‘intelligent’} 
# Define the following functions: 
# a) To print all the items in the dictionary. 
# b) To print all the keys in the dictionary. 
# c) To print all the values in the dictionary. 
# d) To get the passwords of users. For example, passwd[‘rahul’]= genius 
# e) Change the password of a particular user. For example, passwd[‘ankita’]=‘brilliant’

def items(passwd):
    print(passwd.items())

def keys(passwd):
    print(passwd.keys())

def values(passwd):
    print(passwd.values())

def get_passwd(passwd, name):
    print(f"Password of {name} is {passwd[name]}")

def change_passwd(passwd, name, new_passwd):
    passwd[name] = new_passwd
    print(f"New password of {name} is {passwd[name]}")

passwd = {
    'rahul': 'genius',
    'kumar': 'smart',
    'ankita': 'intelligent'
}
items(passwd)
keys(passwd)
values(passwd)
get_passwd(passwd, 'rahul')
change_passwd(passwd, 'ankita', 'brilliant')
items(passwd)