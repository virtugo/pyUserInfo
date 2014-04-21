# coding=Windows-1251

# --------------------------------------------------
# Показываем инфу по юзеру
# Вбиваем имя или юзаем последнее использованное
# --------------------------------------------------

import subprocess
import os

if os.path.exists('name.txt'):
    if os.path.isfile('name.txt'):
        fn = open('name.txt')
        lastName = fn.read() # читаем имя юзера
        fn.close()
        inputName = input('Имя пользователя (Enter для ' + lastName + '): ')
        # ------------------------------------------------------------------
        if inputName == '': # Если не ввели имя юзера
            inputName = lastName # используем последнее введенное
    else:
        inputName = input('Имя пользователя: ')
else:
    inputName = input('Имя пользователя: ')
print() # пустая строка

# Записываем в файл последнее имя юзера
fn = open('name.txt', 'w' )
fn.write(inputName)
fn.close()

rInput = 'net user ' + inputName + ' /DOMAIN | find "Последний пароль задан"'
pInput = 'net user ' + inputName + ' /DOMAIN | find "Действие пароля завершается"'

p = subprocess.Popen(pInput, shell=True, stdout = subprocess.PIPE)
out1 = p.stdout.read()
r = subprocess.Popen(rInput, shell=True, stdout = subprocess.PIPE)
out2 = r.stdout.read()

print (out2.decode('CP866'))
print (out1.decode('CP866'))

print('-------------------------------------') # пустая строка
input('Enter для выхода...') # не закрываем консоль
