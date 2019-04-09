# 1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
# В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке,
# из которой запущен данный код. Затем создайте вторую функцию, удаляющую эти папки.
# Проверьте работу функций в этом же модуле.
import os

def create_dir() :
    for i in range(9):
        path_name=os.path.join(os.getcwd(),'dir_{}'.format(i+1))
        os.mkdir(path_name)
        #print('dir_{}'.format(i+1))
def del_dir():
    for i in range(9):
        path_name=os.path.join(os.getcwd(),'dir_{}'.format(i+1))
        os.rmdir(path_name)

#create_dir()
#del_dir()

