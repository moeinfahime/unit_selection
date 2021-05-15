import fileinput
import os

import user
import csv
import pandas as pd


class Staff:
    def __init__(self, name, family):
        """
        :param name: name of staff
        :param family: family of staff

        """

    @staticmethod
    def course_define(title, professor, id, unit, capacity):

        file_exists = os.path.isfile('info_course.csv')
        with open('info_course.csv', 'a') as csvfile:
            csv_columns = ['Title', 'professor', 'ID', 'Unit', 'Capacity']
            writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=csv_columns)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Title': title, 'professor': professor, 'ID': id, 'Unit': unit, 'Capacity': capacity})


    @staticmethod
    def see_course(name_student, family_student):
        with open('info_select_course.csv', 'r') as read:
            reader = csv.DictReader(read)

            for line in reader:
                for row in reader:
                    if row['Name'] == name_student and row['Family'] == family_student:
                        print(row['Name'], row['Family'], row['Course'], row['confirmation'])

                    else:
                        from colorama import Fore, Back, Style
                        print(Fore.LIGHTBLUE_EX + '"' + "The name of this student does not exist." + '"')
                        print(Style.RESET_ALL)

    @staticmethod
    def course_enroll(name_student, family_student, course, confirmation):

        change = pd.read_csv('info_select_course.csv')
        location = 0

        with open('info_select_course.csv', 'r', newline="") as my_file:
            csv_reader = csv.DictReader(my_file)
            for row in csv_reader:
                if row['Name'] == name_student and row['Family'] == family_student and row['Course'] == course:
                    row['confirmation'] = confirmation

                    change.loc[location, 'confirmation'] = confirmation
                    change.to_csv('info_select_course.csv', index=False)
                location += 1


    def staff_computer(self):
        pass

    def financial(self):
        pass


# math,amini,21,3,20
# english,as,23,3,30
# magnetic,d,32,6,25

# Staff_Education.course_define()
