__author__ = 'antonkon and alexlazar'
import os
import re

def parse_words(file):
    return
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))]

def get_num(str):
    regex = re.compile('[-+]?(?:(?: \d* \. \d+ ) | (?: \d+ \.? ))(?: [Ee] [+-]? \d+ ) ?', re.VERBOSE)
    return regex.findall(str)[0].replace('.', ',') + '\n'



def parse_files():
    print("Input N")
    N = input()
    new_file = '/Users/antonkon/Desktop/baklanov' //DIRECTORY TO SAVE TO
    multiply_time = []
    matrix_trace = []
    for P in range(2, 25):
        file_path = '/Users/antonkon/Desktop/Data_4/Data_Home_Work/multiplay_matrix.tests/N=' +str(N) +'_P=' + str(P) + '/' //DIRECTORY WITH DATA 
        file_path += get_immediate_subdirectories(file_path)[0] + '/' + 'output'
        print(file_path)
        f = open(file_path, 'r')
        print(P)
        for x in f.readlines():
            if ('Mult' in x):
                multiply_time.append(x)
            elif ('Res' in x):
                matrix_trace.append(x)
        f.close()

    new_file += str(N) + '.txt'
    f = open(new_file, 'w+')

    f.write('Multiply time \n')
    for x in multiply_time:
        f.write(get_num(x))

    f.write('\n')

    f.write('Matrix trace \n')
    for x in matrix_trace:
        f.write(get_num(x))

    f.close()

parse_files()
