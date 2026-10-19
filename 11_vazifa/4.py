import csv

def add_expense():
    try:
        f = open("11_vazifa/my_byudget.csv", "r", encoding="UTF-8")
        f.close() 
    except FileNotFoundError:
        with open("11_vazifa/my_byudget.csv","w",encoding="UTF-8",newline="") as f:
            pen=csv.writer(f)
            pen.writerow(["category","amount","date"])
    kategoriya=input("Kategoriyasi: ")
    narx=input("Narxi: ")
    kuni=input("Ishlab chiqarilgan sanasi (yil.oy.kun) korinishida kiriting: ")

    with open("11_vazifa/my_byudget.csv","a",encoding="UTF-8") as f:
        pen=csv.writer(f)
        pen.writerow([kategoriya.capitalize(),narx,kuni])
        print("Muvaffaqiyatli saqlandi!")
def show_expenses():
    try:
        with open("11_vazifa/my_byudget.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Hech narsa topilmadi!")
                return
            print("=======HISOBOT=======")
            for i in data:
                print(f"Kategoriyasi: {i['category']}")
                print(f"Narxi: {i['amount']}")
                print(f"Ishlab chiqarilgan sanasi: {i['date']}")
                print("-"*20)
    except FileNotFoundError:
        pass
        print("Hech narsa topilmadi!")

def search_category():
    try:
        with open("11_vazifa/my_byudget.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Hech narsa topilmadi!")
                return
            qidir=input("Qidirayotgan mahsulotingizni kategoriyasini kiriting: ")
            topildi=0
            for i in data:
                if i['category'].lower()==qidir.lower():
                    topildi=1
                    print("Siz qidirayotgan kategoriya boyicha mahsulotlar")
                    print(f"Kategoriyasi: {i['category']}")
                    print(f"Narxi: {i['amount']}")
                    print(f"Ishlab chiqarilgan sanasi: {i['date']}")
                    print("-"*20)
            if topildi==0:
                print("Bu kategoriyada mahsulotlar mavjud emas!")
    except FileNotFoundError:
        pass
        print("Hech narsa topilmadi!")


def calculate_states():
    try:
        with open("11_vazifa/my_byudget.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Hech narsa topilmadi!")
                return
            jami=0
            soni=0
            print("========HISOBOT========")
            for i in data:
                soni+=1
                jami+=int(i['amount'])
                print(f"Kategoriyasi: {i['category']}")
                print(f"Narxi: {i['amount']}")
                print("-"*20)
            ortacha=jami/soni
            print(f"Mahslotlarning umumiy summasi: {jami}")
            print(f"Kategoriyalar soni: {soni}")
            print(f"Mahsulotlarning ortacha summasi: {ortacha}")
    except FileNotFoundError:
        pass
        print("Hech narsa topilmadi!")

def max_expense():
    try:
        with open("11_vazifa/my_byudget.csv","r",encoding="UTF-8") as f:
                data=list(csv.DictReader(f))
                if not data:
                    print("Hech narsa topilmadi!")
                    return
                eng_qimmat=0
                eng_qimmat_nomi=""
                for i in data:
                    if int(i['amount'])>int(eng_qimmat):
                        eng_qimmat=i['amount']
                        eng_qimmat_nomi=i
                print(f"Eng qimmat mahsulot kategoriyasi: {eng_qimmat_nomi['category']}")
                print(f"Narxi: {eng_qimmat}")
    except FileNotFoundError:
        pass
        print("Hech narsa topilmadi!")

while True:
    print("========MENYU========")
    print("1-Mahsulot qoshish")
    print("2-Mahsulotlarni ekranga chiqarish")
    print("3-Mahsulotlarni kategoriya boyicha qidirish")
    print("4-Mahsulotlarni jami va ortacha qiymatini hisoblash")
    print("5-Eng qimmat mahsulotni topish")
    print("6 -Chiqish")
    print("="*20)
    tanlov=input("Tanlang: ")

    if tanlov=="1":
        add_expense()
    elif tanlov=="2":
        show_expenses()
    elif tanlov=="3":
        search_category()
    elif tanlov=="4":
        calculate_states()
    elif tanlov=="5":
        max_expense()
    elif tanlov=="6":
        print("Etiboringiz uchun tashakkur!")
        break
    else:
        print("Notogri buyruq kiritildi! Qaytadan urinib koring!")