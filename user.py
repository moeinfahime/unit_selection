import hashlib
import os.path
import pandas as pd
import csv
import random
import logging

mylogger = logging.getLogger("loger1")
mylogger.setLevel(logging.INFO)       #change default
# create handlers
file_handeler_event = logging.FileHandler('file_event.log')
std_handeler = logging.StreamHandler()

# set level for handlers
file_handeler_event.setLevel(logging.INFO)
std_handeler.setLevel(logging.ERROR)

log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handeler_event.setFormatter(log_format)

# add handlers to logger
mylogger.addHandler(file_handeler_event)
mylogger.addHandler(std_handeler)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):

        pass_hash = hashlib.md5(str(self.password).encode("utf-8")).hexdigest()
        file_exists = os.path.isfile('register.csv')
        with open('register.csv', 'a') as csvfile:
            headers = ['Username', 'Password', 'Personal_code']
            writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            if len(self.password) == 4:
                #Create a student number
                Personal_code = '1400' + self.password
                writer.writerow({'Username': self.username, 'Password': pass_hash, 'Personal_code': Personal_code})

                from colorama import Fore, Back, Style
                print(Fore.LIGHTBLUE_EX + '"' + "Your name has been registered." + '"')
                print(Fore.RED + f'Please keep this code...\nStudent number: {Personal_code}')
                print(Style.RESET_ALL)


            else:
                # Create a personal number
                Personal_code = '00' + self.password
                writer.writerow({'Username': self.username, 'Password': pass_hash, 'Personal_code': Personal_code})

                from colorama import Fore, Back, Style
                print(Fore.LIGHTBLUE_EX + '"' + "Your name has been registered." + '"')
                print(Fore.RED + f'Please keep this code...\nPersonal code: {Personal_code}')
                print(Style.RESET_ALL)

    def login(self):
        pass_hash = hashlib.md5(str(self.password).encode("utf-8")).hexdigest()
        try:
            with open('register.csv', 'r') as read:
                reader = csv.DictReader(read)

                for line in reader:

                    if line['Username'] == self.username and line['Password'] == pass_hash:
                        return True

                else:

                    from colorama import Fore, Back, Style
                    print(Fore.RED + '"' + "invalid username or password!" + '"')
                    print(Style.RESET_ALL)

                    return False
        except:
            print("File Has Error")
            mylogger.error("File Has Error")

    def change_password(self, new_password):
        pass_hash_new = hashlib.md5(str(new_password).encode("utf-8")).hexdigest()
        pass_hash = hashlib.md5(str(self.password).encode("utf-8")).hexdigest()
        change = pd.read_csv('register.csv')
        location = 0

        with open('register.csv', 'r') as my_file:
            csv_reader = csv.DictReader(my_file)
            for row in csv_reader:
                if row['Username'] == self.username and row['Password'] == pass_hash:
                    self.password = pass_hash_new
                    print("Your password is changed.")
                    change.loc[location, 'Password'] = pass_hash_new
                    change.to_csv('register.csv', index=False)
                location += 1

    def check_Personal_code(self, Personal_cod):
        pass_hash = hashlib.md5(str(self.password).encode("utf-8")).hexdigest()
        with open('register.csv', 'r') as read:
            reader = csv.DictReader(read)

            for line in reader:
                if line['Username'] == self.username and line['Password'] == pass_hash \
                        and line['Personal_code'] == Personal_cod:
                    from colorama import Fore, Back, Style
                    print(Fore.LIGHTBLUE_EX + '"' + "Personal code/Student number is correct!" + '"')
                    print(Style.RESET_ALL)

                    return True
            else:

                from colorama import Fore, Back, Style
                print(Fore.RED + '"' + "invalid Personal code!" + '"')
                print(Style.RESET_ALL)
                mylogger.error("Personal code or length of your password is incorrect . ")
                return False
