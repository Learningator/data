'''
demo script to process data from backend request
'''

# python imports
import pandas as pd
import json


def demo_get_data_from_backend():
    ''' function only for development and test purpose.'''
    f = open('data_test.txt', 'r')
    data = f.read()
    f.close()
    return json.loads(data)


def load_dataset():
    df_courses_dataset = pd.read_csv('dataset_courses.csv', sep=';')
    return df_courses_dataset


def is_course_in_dataset(df_student, df_dataset):
    Boolean = []
    for row in df_student.index:
        Boolean.append(df_student.loc[row]['title']
                       in list(df_dataset["Course"]))
    data = df_student['title'][Boolean]
    data = pd.DataFrame(data)
    return data


def get_levels(data):
    basic_key_word = ['Básic', 'Fundamentos', 'Introducción', 'Práctico']
    difficulty_level = []
    for i in data.index:
        is_basic = False
        for key_word in basic_key_word:
            if key_word in data.loc[i]['title']:
                difficulty_level.append('Basico')
                is_basic = True
                break
        if not is_basic:
            difficulty_level.append('Intermedio')
    return difficulty_level


if __name__ == "__main__":
    data_init = demo_get_data_from_backend()

    df_student_courses = pd.DataFrame(data_init['courses'])
    df_courses = load_dataset()
    df_data = is_course_in_dataset(df_student_courses, df_courses)

    df_data['field'] = data_init['field']
    df_data['subfield'] = data_init['subfield']
    df_data['level'] = ''

    difficulty_levels = get_levels(df_data)

    df_data['level'] = difficulty_levels
    df_data.to_csv(r'result.csv', index=False, sep=';')
