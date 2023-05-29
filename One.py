import sqlite3 as sq
import random

def file_open():
    note = []
    with open('ttb.txt',encoding='utf-8') as f:
        for x in f:
            note.append(x)
    return note

def save_file(name):
    with open('ttb.txt','w',encoding='utf-8') as f:
        for x in name:
            print(x)
            f.write(x)

start = True
notebook = file_open()


def imput_word(words,translation):    #1
    with sq.connect('EnglishDict.db') as con:
        cur = con.cursor()			
        cur.execute("INSERT INTO dicts VALUES (?,?)",(words,translation))
        print('Success')

def read_dicts(x): #2
    with sq.connect('EnglishDict.db') as con:
        cur = con.cursor()
        cur.execute("SELECT Translation FROM dicts WHERE Word = (?)",(x,))
        result = cur.fetchone()
        print(*result)

def input_sentence(sentence, translation): #3
    with sq.connect('EnglishDict.db') as con:
        cur = con.cursor()			
        cur.execute("INSERT INTO trans VALUES (?,?,1)",(sentence,translation))        
        print('Success')
        


def create_organaizer(): #4
    txt = input('Пишите свою заметку тут \nНо помните нажатие Enter сразу сохранит заметку \n') + '\n'
    #txt.rjust('\n')
    notebook.append(txt)
    save_file(notebook)
    print('Success')

def change_organaizer(x):
    text = input('Пишите новую заметку, она будет на месте старой \n') + '\n'
    notebook.insert(x,text)
    notebook.pop(x+1)
    save_file(notebook)

def get_organaizer(): #5
    num = len(notebook)
    print(notebook[0])
    print('Введите номер записи для выбора и нажмите Enter')
    if len(notebook) > 1:
        go = True
    else:
        print('Пока нет записей')
        return False
    while go:
        for x in range(1,num):
            n = notebook[x]
            print(str(x) + ')' + ' ' + n[:15]) 
        try:
            answer = int(input('Введите 0 для выхода \n'))
            if answer > len(notebook):
                raise Exception()
            elif answer == 0:
                raise ZeroDivisionError()
            verb = input('r = Прочитать заметку. w = изменить заметку. d = удалить заметку 0 = выход: ')
            if verb.lower() == 'r':
                print(notebook[answer])
            elif verb.lower() == 'w':
                change_organaizer(int(answer))
            elif verb.lower() == 'd' or verb.lower() == 'в':
                notebook.pop(answer)
                save_file(notebook)
                print('Удаленно')
            elif verb == '0':
                print('Bye')
                go = False
        except ZeroDivisionError:
            return False
        except Exception as cop:
            print(cop)
            print('Вы ввели неверное действие')

    
        

    

def test_study(): #6
    start = True
    while start:
        with sq.connect('EnglishDict.db') as con:
            cur = con.cursor()
            cur.execute("SELECT sum(ID) FROM trans")
            res = cur.fetchone()[0]
            if res is None:
                raise ZeroDivisionError()
            x = random.randint(1,res)            
            cur.execute("SELECT Word FROM trans WHERE rowid = (?)",(x,))
            get_sentence = cur.fetchone()[0]
            print(get_sentence)
            cur.execute("SELECT Translation FROM trans WHERE rowid = (?)",(x,))
            get_answer = cur.fetchone()[0]
            answer = input()
            if answer.lower() == get_answer.lower():
                print('Правильно!')
            else:
                print('Ой, где то ошибочка вышла')
            
            
        ans = input('Нажмите Enter что бы продолжить. Нажмите 0 + Enter что бы выйти \n')
        if ans == '0':
            start = False
    return False
   

print("""Вас приветствует личный блокнот для перевода версии 0.1
Добавляйте слова, ищите среди уже добавленых слов перевод.
Также вы можете добавить устойчивое предложение или узнать его перевод""")

print()
print('Выберите действие:')
menu = """1) - Добавить слово.
2) - Перевести слово.
3) - Добавить предложение
4) - Создать заметку
5) - Посмотреть заметки
6) - Проверить знания
0) - Выход"""


while start:
    print(menu)
    answ = input()
    try:
        answ = int(answ)
        if answ == 1:
            a = input('Напишите слово на Английском: \n')
            b = input('Напишите перевод: \n')
            imput_word(a,b)
            
        elif answ == 2:
            a = input('Напишите слово на Английском: \n')
            read_dicts(a)
            
        elif answ == 3:
            a = input('Напишите предложение на Английском: \n')
            b = input('Напишите перевод: \n')
            input_sentence(a,b)
            
        elif answ == 4:
            create_organaizer()
            
        elif answ == 5:
            get_organaizer()
            
        elif answ == 6:
            test_study()
            
        elif answ == 0:
            start = False
            
        else:
            print("Unknow comand. Try again ")

    except ZeroDivisionError:
        print('Пока нет предложений для проверки знаний')
            
    except Exception as cop:
        print(cop)
        print('Вы ввели неверное действие')

    ans = input('Нажмите Enter что бы продолжить. Нажмите 0 + Enter что бы выйти \n')
    if ans == '0':
        start = False 

			
	
