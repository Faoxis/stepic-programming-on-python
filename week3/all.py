
# coding: utf-8

# # 3. Модуль 3

# ## 3.1. Функции

# In[ ]:

# Функция с произвольным числом аргументов
def min(*a): # *а означает, что мы накапливаем все значения в список а
    m = a[0]
    for x in a:
        if m > x:
            m = x;
    return m


# In[10]:

# Функция со значениями параметров по умолчанию
def my_range(start, stop, step = 1): # если параметр step не указан, то он автоматически по умолчанию станет равен 1
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res

print(my_range(1, 10, 1))
print(my_range(1, 10, 1))


# In[11]:

# Передача параметра по имени
print(my_range(step = 1, stop = 10, start = 1))


# In[12]:

# Если в качестве аргумента функции передать переменную, но в функцию будет передана ее локальная копия
def changeArg(a):
    a = 100
b = 0
changeArg(b)
print(b) # b = 0


# In[17]:

# Однако, если передать объект, а не переменную, то он изменится
def changeArg(a):
    a.append(123)
b = []
changeArg(b)
print(b) # список b содержит новый элемент 


# In[ ]:

# Задача 1
def f(x):
    # put your python code here
    ans = 0
    if x <= -2:
        ans = 1 - (x + 2) * (x + 2)
    elif -2 < x <= 2:
        ans = -x / 2
    elif 2 < x:
        ans = (x - 2) * (x - 2) + 1
    return ans


# In[43]:

# Задача 2
def modify_list(l):
    i = 0
    while len(l) > i:
        if l[i] % 2 == 1:
            del l[i]
            i = i - 1
            
        i = i + 1
    for j in range(len(l)):
        l[j] = l[j] // 2
        
        
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]


# ## 3.2. Словари

# ### 3.2.1. Множества

# In[44]:

s = set() # Создание пустого множества
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} # Создание непустого множества, повторные элементы удаляются
'orange' in basket # Проверка на наличие элемента в множеств


# In[ ]:

# Операции с множествами
s.add('element')
s.remove('element') # если элемента нет, то ошибка
s.discard('element') # удаление элемента без вызова ошибки при его отсутствии
s.clear() # удаление всех элементов множества
len(s) # число элементов в очереде


# ### 3.2.1. Словари

# In[45]:

# Словарь позволяет хранить значения в парах ключ-значение
# Структура данных словаря - dict
d = {} # создание пустого словаря, способ 1
d = dict() # создание пустого словаря, способ 2
d = {'a': 239, 10: 100}
print(d['a'])
print(d[10])


# In[47]:

# Операции со словарями
'key' in d # Проверка словаря на наличие ключа
'key' not in d

d['key'] = 'door' #добавление в словарь d по ключу key значение door
d['key'] # получение значения по ключу, если такого ключа нет, то ошибка
d.get('key') # получение значение по ключу, если такого ключа нет, то функция вернет None
del d['key'] # удаление из словаря ключ-значения


# In[ ]:

# Характеристики словарей:
#     Изменяемы
#     Элементы не имеют порядка
#     Все ключи различны
#     Ключи неизменяемы


# In[65]:

# Перебор элементов словаря
d = {'C': 14, 'A': 12, 'T':9, 'G':18}
for key in d:
    print(key, end=' ') # G C A T
print()
for key in d.keys():
    print(key, end = ' ') #G C A T
print()
for value in d.values():
    print(value, end=' ') #18 14 12 9
print()
for key, value in d.items():
    print(key,'-', value, end = ';') #A - 12;G - 18;T - 9;C - 14;


# In[72]:

# Задача 1
def update_dictionary(d, key, value):
    if d.get(key) is not None:
        d[key] += [value]
    elif d.get(2 * key) is not None:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
            
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}


# In[82]:

# Задача 2

def countKeyValue(d, key):
    key = key.lower()
    if d.get(key) is not None:
        d[key] = d[key] + 1
    else:
        d[key] = 1


strings = [s for s in input().split(" ")]
myDict = dict()
for s in strings:
    countKeyValue(myDict, s)

for key,value in myDict.items():
    print(key, value)


# In[89]:

# Задача 3
n = int(input())
d = dict()
x = 0
for i in range(n):
    x = int(input())
    if d.get(x) is not None:
        print(d[x])
    else:
        d[x] = f(x)
        print(d[x])


# ## 3.3. Файловый ввод/вывод

# ### 3.3.1. Чтение из файла

# In[94]:

inf = open('D:/1.txt', 'r') # открытие файла D:\1.txt на чтение (r (read) как второй аргумент)
s1 = inf.readline() # чтение первой строки
s2 = inf.readline() # чтение второй строки
inf.close() # закрытие файла

# можно использовать специальную конструкцию для чтения из файла (данный способ рекомендуется)
with open('D:\\1.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()
# здесь файл уже закрыт


# In[ ]:

# полезные функции
s = inf.readline().strip() # функция strip() позволяет избавится от символов типа \t, \n и т.д.
os.path.join('.', 'dirname', 'filename.txt') # склеивание из нескольких частей полный путь к файлу 


# In[102]:

# Построчное чтение файла
with open('D:\\1.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)


# ### 3.3.1. Запись в файл

# In[97]:

ouf = open('D:\\1.txt', 'w')
ouf.write('Some text\n')
ouf.write(str(25))
ouf.close()

# рекомендуемая альтернатива
with open('D:\\1.txt', 'w') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))
# здесь файл уже закрыт


# In[129]:

# Задача 2
def countStrings(d, key):
    key = key.lower()
    if d.get(key) is not None:
        d[key] = d[key] + 1
    else:
        d[key] = 1

def maxCountString(d):
    maxValue = 0
    maxKey = 'a'
    for key in d:
        if d[key] > maxValue:
            maxValue = d[key]
            maxKey = key
    
    for key in d:
        if d[maxKey] == d[key] and maxKey != key:
            if key < maxKey:
                maxKey = key
                
    
    return [maxKey, d[maxKey]]
    
        
        
d = dict()
with open('D:\\dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip()
        strings = [s for s in line.split(" ")]
        for s in strings:
            countStrings(d, s)
            
resList = maxCountString(d)

with open('D:\\1.txt', 'w') as output:
    myString = str(resList[0]) + ' ' + str(resList[1]) + '\n';
    output.write(myString)


# In[22]:


myList = []
myDict = dict()

meanMath = 0
meanPhys = 0
meanRuss = 0
n = 0

with open('D:\\dataset_3363_4.txt') as inputFile:
    for line in inputFile:
        n = n + 1
        line = line.strip()
        contain = [s for s in line.split(';')]
        myList += [((int(contain[1]) + int(contain[2]) + int(contain[3])) / 3)]
        meanMath += int(contain[1])
        meanPhys += int(contain[2])
        meanRuss += int(contain[3])
        
meanMath = meanMath / n
meanPhys = meanPhys / n
meanRuss = meanRuss / n
        
with open('D:\\1.txt', 'w') as outputFile:
    for s in myList:
        myString = str(s) + '\n'
        outputFile.write(myString)
    myString = str(meanMath) + " " + str(meanPhys) + " " + str(meanRuss)
    outputFile.write(myString)

