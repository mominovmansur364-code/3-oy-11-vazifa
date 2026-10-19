import csv

def yangi_buyurtma():
    try:
        f = open("11_vazifa/orders.csv", "r", encoding="UTF-8")
        f.close() 
    except FileNotFoundError:
        with open("11_vazifa/orders.csv","w",encoding="UTF-8",newline="") as f:
            pen=csv.writer(f)
            pen.writerow(["order_id","product_name","category","quantity","price","customer","date"])
    buyurtma_raqami=input("Buyurtma Id sini kiriting: ")
    name=input("Mahsulot nomi: ")  
    kategoriya=input("Kategoriyasi: ")
    soni=input("Soni: ")
    narxi=input("Narxi: ")
    xaridor=input("Xaridorning ismi: ")
    date=input("Ishlab chiqarilgan sanasi (yil.oy.kun) korinishida kiriting: ")   

    with open("11_vazifa/orders.csv","a",encoding="UTF-8",newline="") as f:
        pen=csv.writer(f)
        pen.writerow([buyurtma_raqami,name.capitalize(),kategoriya.capitalize(),soni,narxi,xaridor.capitalize(),date])
        print("Muvaffaqiyatli saqlandi!")

def show_products():
    try:
        with open("11_vazifa/orders.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Hech narsa topilmadi!")
                return
                print("=======MAHSULOTLAR HISOBOTI=======")
            for i in data:
                print(f"Mahsulot ID si: {i['order_id']}")
                print(f"Mahsulot nomi: {i['product_name']}")
                print(f"Mahsulot kategoriyasi: {i['category']}")
                print(f"Mahsulot soni: {i['quantity']}")
                print(f"Mahsulot narxi: {i['price']}")
                print(f"Mahsulotning xaridorining ismi: {i['customer']}")
                print(f"Mahsulot ishlab chiqarilgan sana: {i['date']}")
                print("="*20)
    except FileNotFoundError:
        print("Xatolik!")

def search_name():
    try:
        with open("11_vazifa/orders.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            qidiruv=input("Xaridorning ismini kiriting: ")
            print("Siz qidirgan xaridor sotib olgan mahsulotlar")
            topildi=0
            print("="*20)
            for i in data:
                if i['customer'].lower()==qidiruv.lower():
                    topildi=1
                    print(f"Mahsulot ID si: {i['order_id']}")
                    print(f"Mahsulot nomi: {i['product_name']}")
                    print(f"Mahsulot kategoriyasi: {i['category']}")
                    print(f"Mahsulot soni: {i['quantity']}")
                    print(f"Mahsulot narxi: {i['price']}")
                    print(f"Mahsulotning xaridorining ismi: {i['customer']}")
                    print(f"Mahsulot ishlab chiqarilgan sana: {i['date']}")
                    print("="*20)
            if topildi==0:
                print("Kechirasiz bunday ismli xaridor mavjud emas!")
    except FileNotFoundError:
        print("Xatolik!")
def umumiy_savdo():
    try:
        with open("11_vazifa/orders.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            umumiy=0
            jami=0
            soni=0
            print("="*20)
            for i in data:
                soni+=1
                jami+=int(i['quantity'])*int(i['price']) 
                umumiy+=jami
                print(f"Mahsulot nomi: {i['product_name']}")
                print(f"Umumiy summasi: {jami}")
                print("="*20)
            ortacha=umumiy/soni
            print(f"Mahsulotlarning umumiy summasi: {umumiy}")
            print(f"Sotilgan mahsulotlar soni: {soni}")
            print(f"O'rtacha sotuv summasi: {round(ortacha):.2f}")
    except FileNotFoundError:
        print("Xatolik!")

def max_product():
    try:
        with open("11_vazifa/orders.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Hech narsa topilmadi!")
                return
            
            eng_qimmat_buyurtma = data[0]
            max_summa = int(data[0]['quantity']) * int(data[0]['price'])

            for i in data:
                joriy_summa = int(i['quantity']) * int(i['price'])
                if joriy_summa > max_summa:
                    max_summa = joriy_summa
                    eng_qimmat_buyurtma = i
                    
            print("="*20)
            print(f"Eng qimmat buyurtma tafsilotlari:")
            print(f"Mahsulot nomi: {eng_qimmat_buyurtma['product_name']}")
            print(f"Kategoriyasi: {eng_qimmat_buyurtma['category']}")
            print(f"Xaridor: {eng_qimmat_buyurtma['customer']}")
            print(f"Soni: {eng_qimmat_buyurtma['quantity']} ta")
            print(f"Umumiy xarid summasi: {max_summa} so'm")
            print("="*20)
    except FileNotFoundError:
        print("Xatolik! Fayl topilmadi.")

while True:
    print("========MENYU========")
    print("1-Buyurtma qoshish")
    print("2-Buyurtmalarni ekranga chiqarish")
    print("3-Xaridor ismi bilan qidirish")
    print("4-Savdo boyicha ma'lumotlar")
    print("5-Eng qimmat xaridni topish")
    print("6 -Chiqish")
    print("="*20)
    tanlov=input("Tanlang: ")

    if tanlov=="1":
        yangi_buyurtma()
    elif tanlov=="2":
        show_products()
    elif tanlov=="3":
        search_name()
    elif tanlov=="4":
        umumiy_savdo()
    elif tanlov=="5":
        max_product()
    elif tanlov=="6":
        print("E'tiboringiz uchun tashakkur!")
        break
    else:
        print("Noto'g'ri buyruq kiritildi!")
        print("Qaytadan urinib ko'ring!")
