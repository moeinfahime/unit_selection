import csv

import pandas as pd


class Student:
    def __init__(self, name, family):
        """
        :param name: name of student
        :param family: family of student

        """
        self.name = name
        self.family = family

    def read_course(self):
        reader = pd.read_csv('info_course.csv')
        print(reader)

    def select_course(self,course):
        info_select_course = pd.read_csv('info_select_course.csv')
        with open('info_select_course.csv', 'a+') as writable:
            fieldnames = ['Name', 'Family', 'Course', 'confirmation']
            csv_writer = csv.DictWriter(writable, fieldnames=fieldnames)
            for value, line in enumerate(info_select_course):
                if line == 0:
                    csv_writer.writerow(
                        {'Name':'Name', 'Family':'Family', 'Course':'Course', 'confirmation': False})

            csv_writer.writerow({'Name':self.name, 'Family':self.family, 'Course':course, 'confirmation': False})

        selected_course = pd.read_csv('info_select_course.csv')
        # print(selected_course)

    def delete_course(self,course):
        with open('info_selsect_course.csv','a+') as out:
            writer = csv.writer(out)
            for row in csv.reader(out):
                if row['Name'] == self.name and row['Family'] == self.family and row ['Course'] == course:
                    writer.writerow(row)

# student = Student('F','D','C')
# student.read_course()
