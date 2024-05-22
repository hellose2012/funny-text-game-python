import time
import random
g = [1, 2, 3, 4, 5, 6, 7]
def vobor_ocTpoBa(a, re):
        b = random.randint(1, 5)
        if b == 1:
            print("ты нашёл цветок")
            bv2 = random.randint(1,10)
            if bv2 == 1:
                print("он исчез у вас в руках")
        else:
            print("ты не нашёл цветок")
        if b == 1 and bv2 != 1:
            re = True
        else:
            re = False
        return re
def otshot_time():
    for i in range(7):
        print(g[-(i+1)])
        time.sleep(1)
print("привет\nкто ты?")
d = input("")
if d == 'никто':
    print('да, ты никто')
else:
    print('нет, ты никто')
time.sleep(2)
print('!!! это надо исправлять !!!')
time.sleep(2)
print('но я тебе не помогу')
time.sleep(2)
print("LOL\nзачем мне помогать тебе если ты никто\n:)\n\n")
time.sleep(2)
print('попросить помочь - 1\nпопытаться самому перестать быть никем - 2')
vopros1 = int(input())
if vopros1 == 1:
    print("OK, но ты должен принести волшебный цветок")
    time.sleep(2)
    print('где он я не знаю')
    time.sleep(2)
    print("он есть на одном из пяти островов")
    time.sleep(2)
    print('цветок то появляется то исчезает')
    time.sleep(2)
    print('пока ты плывёшь на остров цветок может исчезнуть')
    time.sleep(3)
    print('поэтому тебе может понадобится много попытов')
    time.sleep(4)
    print('PS  м-м-м...  ну бувает очепятка в слове попыток =))')
    time.sleep(4)
    print("на какой остров ты пойдёшь\n(выбери число от 1 до 5)")
    vopros2 = int(input())
    octrov = bool(False)
    print("до каждого острова плыть 7 сек")
    otshot_time()
    octrov = vobor_ocTpoBa(vopros2, octrov)
    while octrov == False:
        print("на какой остров ты пойдёшь\n(выбери число от 1 до 5)")
        vopros2 = int(input())
        octrov = bool(False)
        print("до каждого острова плыть 7 сек")
        otshot_time()
        octrov = vobor_ocTpoBa(vopros2, octrov)
    print("\nспасибо что принёс цветок")
    time.sleep(2)
    print("ну ладно цветок мне не нужен")
    time.sleep(2)
    print("я его выкину")
    time.sleep(3)
    print("ты н втором ранге всего их 5 попав на пятый ты перестаниш быть никем")
    print(' + \n + + \n + + + \n + + + я \n + + + + + ')
    print("да ладно мне лень я нарекаю тебя кемто великим")
else:
    print("ты умер никем так и не став кем - то")
