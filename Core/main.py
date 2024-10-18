from Commands import command_list
from os import path
import configparser

def _accCreate():
    print("Create an account before using NanoCore!")
    username = input("Create a username: ")
    password = input("Create a password: ")
    users_data = configparser.ConfigParser()
    users_data[username] = {'password': password}
    with open('users.ini', 'w') as configfile:
        users_data.write(configfile)
        main()

def _accEnter():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users_data = configparser.ConfigParser()
    users_data.read('users.ini')
    if username in users_data and users_data[username]['password'] == password:
        print("Authentication successful. Access granted.")
        main()
    else:
        print("Authentication failed. Check your username and password.")
        _accEnter()

def main():
    print("Welcome to NanoCore")
    while True:
        command_list()

if path.exists("users.ini"):
    _accEnter()
else:
    _accCreate()
