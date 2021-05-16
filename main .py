import sys
import logging
from Staff import Staff
from Student import Student
from user import User
from Course import Course
from colorama import Fore, Back, Style

mylogger = logging.getLogger("loger1")
# create handlers
file_handeler_event = logging.FileHandler('file_event.log')
std_handeler = logging.StreamHandler()

# set level for handlers
file_handeler_event.setLevel(logging.INFO)
std_handeler.setLevel(logging.ERROR)

log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
file_handeler_event.setFormatter(log_format)

# add handlers to logger
mylogger.addHandler(file_handeler_event)
mylogger.addHandler(std_handeler)

# Select the login type
print(Fore.MAGENTA + 'select one of these two:\n 1-signin\n 2-signup')
print(Style.RESET_ALL)
user_selection = int(input('your selection: '))
username = input('enter your username: ')
password = input('enter your password: ')

# Build a sample of the class user
username_sample = User(username, password)

# login
if user_selection == 1:
    #calling the class login from module of user
    result = username_sample.login()

    # Enter the password for three times if it is incorrect
    if result == False:
        mylogger.error("invalid username or password!")
        a = 0
        while a < 2:
            if result == False:

                username = input('enter your username: ')
                password = input('enter your password: ')
                username_sample = User(username, password)

                if result == True:

                    print(Fore.LIGHTBLUE_EX + '"' + "successfully logged in!" + '"')
                    print(Style.RESET_ALL)
                    a = 4

                elif result == False and a == 1:
                    mylogger.error("invalid username or password and you can not log in!")
                    print(Fore.RED + '"' + "Sorry, you can not log in." + '"')
                    print(Style.RESET_ALL)

            a += 1

    else:
        #logging of login
        mylogger.info("Login done.")
        print('\n')

elif user_selection == 2:
    #
    username_sample.register()
    sys.exit()
else:
    print(Fore.RED + '\ninvalid input')
    print(Style.RESET_ALL)


if result == True:

    personal_code = input("Please enter your personal code: ")

    """
    The number of characters indicates that the user is a student or staff:
    student: 4
    staff (Education): 6
    staff (Computer site): 7
    staff (Financial): 8

    """
    """ student   """
    if len(password) == 4 and username_sample.check_Personal_code(personal_code) == True:
        mylogger.info("Personal code and length of your password is correct.")
        name, family = input('name,family: ').split(',')
        student = Student(name, family)
        print(Fore.RED + "1- See course list and selection course \n2- See course and Delete course ")
        print(Style.RESET_ALL)
        selection = int(input('selection : '))

        if selection == 1:
            student.read_course()
            print(Fore.RED + "Be careful: The number of requested units must be between 10 and 20. ")
            print(Style.RESET_ALL)
            number_course = int(input('Number of course requested: '))
            sum_units_selected = 0
            selected_course = []
            for i in range(number_course):
                course_request = input('Enter course : ')
                student.select_course(course_request)
                mylogger.info("The course selected.")
                fill_capacity = 1
                title, professor, id, unit = input("Enter: Title,Professor,ID,Unit : ").split(',')
                capacity = int(input('Capacity: '))
                sum_units_selected = sum_units_selected + int(unit)
                course = Course(title, professor, id, unit, capacity)
                course.capacity_update(fill_capacity)
                selected_course.append(course_request)
                print(
                    Fore.LIGHTGREEN_EX + f'Total requested units:{sum_units_selected} and Elective course is {selected_course}')
                print(Style.RESET_ALL)
                # print(f'Total requested units:{sum_units_selected} and Elective courses is {course}')
                if 10 <= sum_units_selected <= 20:
                    print(Fore.RED + "The number of requested units is selected successfully. ")
                    print(Style.RESET_ALL)

            else:
                print(Fore.RED + "The number of requested units is not between 10 and 20. ")
                print(Style.RESET_ALL)


        elif selection == 2:
            number_course = int(input('Number of course requested to delete: '))
            deleted_course = []
            for i in range(number_course):
                student.read_course()
                course_request = input('Enter course to delete : ')
                student.delete_course(course_request)
                mylogger.info("The course deleted.")
                fill_capacity = -1
                title, professor, id, unit = input("Enter: Title,Professor,ID,Unit : ").split(',')
                capacity = int(input('Capacity: '))
                course = Course(title, professor, id, unit, capacity)
                course.capacity_update(fill_capacity)
                deleted_course.append(course_request)
                print(
                    Fore.LIGHTGREEN_EX + f'Elective course to delete is {course_request}')
                print(Style.RESET_ALL)

    # else:
    #     print(Fore.RED + "Personal code or length of your password is incorrect . ")
    #     print(Style.RESET_ALL)
    """   Staff(Education)  """
    if len(password) == 6 and username_sample.check_Personal_code(personal_code) == True:
        name, family = input('name,family: ').split(',')
        staff = Staff(name, family)

        print(Fore.LIGHTCYAN_EX + "Enter one of the following numbers:"
                                  " \n1- Definition of Course \n2- View and Enroll elective courses ")
        print(Style.RESET_ALL)
        selection = int(input('selection: '))
        if selection == 1:
            number_course_define = int(input('How many lessons do you want to define?'))
            for i in range(number_course_define):
                title, professor, id, unit, capacity = input("Enter: Title,Professor,ID,Unit,Capacity : ").split(',')
                course = Course(title, professor, id, unit, capacity)
                staff.course_define(title, professor, id, unit, capacity)

        elif selection == 2:

            name, family = input('Name of student,Family of student: ').split(',')
            staff.see_course(name, family)
            number_course = int(input('How many lessons do you want to enroll?: '))

            for n in range(number_course):
                course = input('Course: ')
                print('If you approve the choice of course, Enter 1(means True):')
                selection = int(input('selection: '))
                if selection == 1:
                    staff.course_enroll(name, family, course, True)
                    print("Done.")
                elif selection == 0:
                    print(f'The course of {course} was not approved for {name} {family}. ')

"""
Change password by user.
"""

if result == True:
    change_pass = int(input("Are you change your password:(Yes:1 , No:2) "))
    if change_pass == 1:
        password_new = input('Enter new password: ')
        if len(password_new) == len(password):
            username_sample.change_password(password_new)
            # username_sample.login()
        elif len(password_new) != len(password):
            print(f'Password length must be {len(password)}.')
            password_new = input('Enter new password: ')
            if len(password_new) == len(password):
                username_sample.change_password(password_new)
                # username_sample.login()
            else:
                print('Sorry, you can not log in.')

# Password of Student: 4 character
# Password of Staff(Education) : 6 character
# Password of Staff(Computer Site) : 8 character
# Password of Staff(Financial) : 10 character
