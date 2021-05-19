import csv
import os
import pandas as pd


class Student:
    def __init__(self, name, family):
        """
        :param name: name of student
        :param family: family of student

        """
        self.name = name
        self.family = family

    def see_course(self):
        reader = pd.read_csv('info_course.csv')
        print(reader)

    def see_course_selected(self):

        with open('info_select_course.csv', 'r') as out:
            reader = csv.DictReader(out)
            # for line in reader:
            for row in reader:
               if row['Name'] == self.name and row['Family'] == self.family:
                   print(row['Name'], row['Family'], row['Course'], row['confirmation'])


    def select_course(self, course):
        file_exists = os.path.isfile('info_select_course.csv')
        with open('info_select_course.csv', 'a') as writable:
            headers = ['Name', 'Family', 'Course', 'confirmation']
            writer = csv.DictWriter(writable, delimiter=',', lineterminator='\n', fieldnames=headers)
            if not file_exists:
                writer.writeheader()

            writer.writerow({'Name': self.name, 'Family': self.family, 'Course': course, 'confirmation': False})


    def delete_course(self, course):

        # with open('info_select_course.csv', 'r') as out:
        #   reader = csv.DictReader(out)
        #   df_s = reader[:4]
        #   for row in reader:
        #
        #       if row['Name'] == self.name and row['Family'] == self.family and row['Course'] == course:
        #           df_s = df_s.drop(
        #               df_s[(df_s.Name == self.name) and (df_s.Family == self.family) and (df_s.Course == course)].index)
        #           df_s.to_csv('info_select_course.csv', 'w', index=False)

          with open('info_select_course.csv', 'r+') as out:
              reader = csv.DictReader(out)
              for row in reader:
                  if row['Name'] == self.name and row['Family'] == self.family and row['Course'] == course:
                      list_data = [self.name,self.family,course]
                      del list_data[0:3]
                      print (self.name)
                  else:
                   break

