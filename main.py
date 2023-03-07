'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
(Попробуйте использовать множества и их пересечение)
'''

# def up_sort(some_set):
#     for _ in range(len(some_set)):
#         print(min(some_set), end=' ')
#         some_set.remove(min(some_set))
#
# import random
# set_a = {random.randint(-10, 11) for _ in range(int(input('n = ')))}
# print(set_a)
# set_b = {random.randint(-10, 11) for _ in range(int(input('m = ')))}
# print(set_b)
# set_c = set_a & set_b
# print(set_c)
# up_sort(set_c)

'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
'''
import random
berr = list(random.randint(1, 501) for _ in range(int(input('Сколько кустов на грядке: '))))
print(berr)
if len(berr) == 1:
    print(berr[0])
elif len(berr) == 2:
    print(berr[0] + berr[1])
else:
    amount = list()
    for i in range(len(berr) - 1):
        amount.append(berr[i - 1] + berr[i] + berr[i + 1])
    amount.append(berr[i - 2] + berr[i - 1] + berr[0])
    print(max(amount))



