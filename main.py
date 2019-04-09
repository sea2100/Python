# 3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
# # Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
# # Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# # так и отдельные функции из модуля.
import rand_from_list as rd
import work_dir as dr

num_list=[1,2,5,8,9,5,3]
char_list=['s','d','f','g','h','dd','eee']
emp_list=[]
print(rd.rand_el(num_list))
print(rd.rand_el(char_list))
print(rd.rand_el(emp_list))

dr.create_dir()
dr.del_dir()
