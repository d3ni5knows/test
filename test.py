print('Hello World')

import re

with open('/Users/denis_macbook/Desktop/Courses/Нетология/Data Scientist/Подготовка (урок 1)/urls.txt', 'r') as file:
    for i in file:
        pattern = re.compile('^.[a-z]')
        i = i.strip()
        if pattern.match(i):
            print(i)
