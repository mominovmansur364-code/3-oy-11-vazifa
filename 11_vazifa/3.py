import csv

def add_product():
    try:
        f = open("11_vazifa/expenses.csv", "r", encoding="UTF-8",newline="")
        f.close() 
    except FileNotFoundError:
        with open("11_vazifa/expenses.csv","w",encoding="UTF-8",newline="") as f:
            pen=csv.writer(f)
            pen.writerow(["category","amount","date"])
    kategoriya=input("Kategoriyasi: ")
    narx=input("Narxi: ")
    kuni=input("Ishlab chiqarilgan sanasi (yil.oy.kun) korinishida kiriting: ")

    with open("11_vazifa/expenses.csv","a",encoding="UTF-8") as f:
        pen=csv.writer(f)
        pen.writerow([kategoriya.capitalize(),narx,kuni])
        print("Muvaffaqiyatli saqlandi!")
def show_prodeuct():
    try:
        with open("11_vazifa/expenses.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Mahsulotlar mavjud emas!")
                return
            print("======Hisobot======")
            for i in data:
                print(f"Kategoriyasi: {i['category']}")
                print(f"Narxi: {i['amount']}")
                print(f"Ishlab chiqarilgan sana: {i['date']}")
                print("="*20)
    except FileNotFoundError:
        pass
        print("Mahsulotlar mavjud emas!")
def umumiy_summa():
    try:
        with open("11_vazifa/expenses.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Mahsulotlar mavjud emas!")
                return
            print("-"*20)
            print("Mahsulotlar hisob-kitobi")
            print("-"*20)   
            jami=0       
            for i in data:
                jami+=int(i['amount'])
                print(f"{i['category']} umumiy narxi: {i['amount']}")
                print("-"*20)
            print(f"Ombordagi mahsulotlarning umumiy summasi: {jami}")
    except FileNotFoundError:
        pass
        print("Mahsulotlar mavjud emas!")

while True:
    print("========MENYU========")
    print("1-Mahsulot qoshish")
    print("2-Mahsulotlarni ekranga chiqarish")
    print("3-Mahsulotlarni umumiy narxi")
    print("4 -Chiqish")
    print("="*20)
    tanlov=input("Tanlang: ")

    if tanlov=="1":
        add_product()
    elif tanlov=="2":
        show_prodeuct()
    elif tanlov=="3":
        umumiy_summa()
    elif tanlov=="4":
        print("E'tiboringiz uchun rahmat!")
        break
    else:
        print("Bunday buyruq mavjud emas! Qaytadan urining!")


