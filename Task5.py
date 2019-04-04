"""
@author: s.suvorova
2. Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
Ваша задача — вывести дату в текстовом виде,
например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)
"""
days={'01':'первое','02':'второе','03':'третье','04':'четвертое','05':'пятое','06':'шестое',
      '07':'седьмое','08':'восьмое','09':'девятое','10':'десятое','11':'одинадцатое','12':'двенадцатое',
      '13':'тринадцатое','14':'четырнадцатое','15':'пятнадцатое','16':'шестнадцатое','17':'семнадцатое',
      '18':'восемнадцатое','19':'девятнадцатое','20':'двадцатое','21':'двадцать первое',
      '22':'двадцать второе','23':'двадцать третье', '24':'двадцать четвертое',
      '25':'двадцать пятое','26':'двадцать шестое','27':'двадцать седьмое','28':'двадцать восьмое',
      '29':'двадцать девятое','30':'тридцатое','31':'тридцать первое'}
months={'01':'января','02':'февраля','03':'марта','04':'апреля','05':'мая',
        '06':'июня','07':'июля','08':'августа','09':'сентября','10':'октября','11':'ноября','12':'декабря'}
short_months=('04','06','09','11')
data=input('Введите дату в формате dd.mm.yyyy ')
data_list=data.split('.')#преобразуем строку в список с разделителем точка
if len(data_list)==3 :#если есть все три элемента даты
    if data_list[1] in short_months:#для коротких месяцев удаляем 31-е число
        del days['31']
    elif   data_list[1]=='02' :#отдельно работаем с февралем
        if int(data_list[2])%4!=0 or int(data_list[2])%100==0:#для простого года
            del days['31']
            del days['30']
            del days['29']
        else:#для високосного
            del days['31']
            del days['30']

    #теперь выводим ответ
    if data_list[0] in days.keys() and data_list[1] in months.keys():
        print(days[data_list[0]], months[data_list[1]],data_list[2],'года')
     #но если такого дня не бывает
    else:  print('вы ввели странную дату')
else:
    print('вы ввели неверный формат')




