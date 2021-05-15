import csv
import fileinput

import pandas as pd


class Course:
    def __init__(self, title, professor, id, unit, capacity):
        self.title = title
        self.Professor_name = professor
        self.id = id
        self.unit = unit
        self.capacity = capacity
        self.__filled_capacity=0

    def capacity_update(self,update_capacity):

        change = pd.read_csv('info_course.csv')
        location = 0

        with open('info_course.csv', 'r') as my_file:
            csv_reader = csv.DictReader(my_file)
            self.__filled_capacity += update_capacity
            print(self.__filled_capacity)
            for row in csv_reader:
                if row['Title'] == self.title and row['ID'] == self.id:
                    row['Capacity'] = self.capacity - self.__filled_capacity
                    change.loc[location, 'Capacity'] = self.capacity - self.__filled_capacity
                    change.to_csv('info_course.csv', index=False)
                location += 1
