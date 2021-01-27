def loe_failist(f):
    file=open(f,"r", encoding="utf-8-sig")
    aeg=[]
    for line in file:
        aeg.append(line.strip())
        file.close
    return aeg
def salvesta_failisse(f,text):
    file=open(f,"a",encoding="utf-8-sig")
    file.write(text+"\n")
    file.close()
    aeg=[]
    aeg=loe_failist(f)
    return aeg

def new_sen():
    ru_word=input("Введи слово на русском")
    en_word=input("Enter sentence on english")
    salvesta_failisse("ru.txt",ru_word)
    salvesta_failisse("en.txt",en_word)
    print(ru_list)
    print(en_list)

def tõlkimine(ru_list,en_list):
    slovo=input("Введи слово")
    if slovo in ru_list:
        ind=ru_list.index(slovo)
        print(f"{slovo}-{en_list[ind]}")
    elif slovo in en_list:
        ind2=en_list.index(slovo)
        print(f"{slovo}-{en_list[ind]}")

def parandus():
    viga=input("Какое слово хотите исправить?")
    if viga in ru_list:
        ind=ru_list.index(viga)
        print(f"Будет исправлена пара слов{viga}-{en_list[ind]}")
        ru_list.pop(ind)
        en_list.pop(ind)
        new_sen()
    elif viga in en_list:
        ind=en_list
        print(f"Будет исправлена пара слов{viga}-{rus_list[ind]}")
        ru_list.pop(ind)
        en_list.pop(ind)
        new_sen()
    else:
        print(f"{viga.upper()} отсутствует в словаре")
        return ru_list,en_list

ru_list=loe_failist("ru.txt")
en_list=loe_failist("en.txt")
print(ru_list)
print(en_list)

while True:
    v=input("Перевод-1, Новое слово-2, Исправить ошибку-3, Проверка знаний-4")
    if v=="1":
        tõlkimine(ru_list,en_list)1
    elif v=="2":
        ru_list,en_list=new_sen()
    elif v=="3":
        print(ru_list,en_list)
        ru_list,en_list=parandus
        (ru_list,en_list)
        print(ru_list,en_list)