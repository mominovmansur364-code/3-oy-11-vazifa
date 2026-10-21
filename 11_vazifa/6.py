import csv

def add_product():
    try:
        f=open("11_vazifa/werehouse.csv","r",encoding="UTF-8")
        f.close()
    except FileNotFoundError:
        with open("11_vazifa/werehouse.csv","w",encoding="UTF-8",newline="") as f:
            pen=csv.writer(f)
            pen.writerow(["product_id","name","category","quantity","price"])
    buyurma_id=input("Buyurtma ID sini kiriting: ")
    nomi=input("Buyurtma nomi: ")
    kategoriyasi=input("Buyurtma kategoriyasi: ")
    soni=input("Soni: ")
    narxi=input("Narxi: ")

    with open("11_vazifa/werehouse.csv","a",encoding="UTF-8",newline="") as f:
        pen=csv.writer(f)
        pen.writerow([buyurma_id,nomi.capitalize(),kategoriyasi.capitalize(),soni,narxi])
        print("Muvaffaqiyatli saqlandi!")

def show_product():
    try:
        with open("11_vazifa/werehouse.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Hech narsa topilmadi!")
                return
            print("========Mahsulotlar hisoboti========")
            for i in data:
                print(f"Mahsulot ID si: {i['product_id']}")
                print(f"Mahsulot nomi: {i['name']}")
                print(f"Mahsulot kategoriyasi: {i['category']}")
                print(f"Mahsulot soni: {i['quantity']}")
                print(f"Mahsulot narxi: {i['price']}")
                print("="*20)
    except FileNotFoundError:
        print("Xatolik!")

def update_product():
    try:
        fayl_nomi="11_vazifa/werehouse.csv"

        with open(fayl_nomi,"r",encoding="UTF-8") as f:
            oqish=csv.DictReader(f)
            qator_nomlari=oqish.fieldnames
            data=list(oqish)
            if not data:
                print("Hech narsa topilmadi!")
                return
            product_id=input("Yangilamoqchi bolgan mahsulotingizni ID sini kiriting: ")
            topildi=0
            for i in data:
                if product_id==i['product_id']:
                    topildi=1
                    print("1-Narxni yangilash")
                    print("2-Sonini yangilash")
                    tanlov=input("Tanlang: ")
                    if tanlov=="1":
                        yangi_narx=input("Yangi narxni kiriting: ")
                        i['price']=yangi_narx
                    elif tanlov=="2":
                        yangi_son=input("Yangi sonni kiriting: ")
                        i['quantity']=yangi_son
                    break
            if topildi:
                with open(fayl_nomi,"w",encoding="UTF-8",newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=qator_nomlari)
                    writer.writeheader()
                    writer.writerows(data)
                    print("Muvaffaqiyatli saqlandi!")
            else:
                print("Bunday mahsulot mavjud emas!")

    except FileNotFoundError:
        print("Xatolik!")


def delete_product():
    fayl_nomi="11_vazifa/werehouse.csv"
    try:
        with open(fayl_nomi,"r",encoding="UTF-8") as f:
            oqish=csv.DictReader(f)
            qator_nomlari=oqish.fieldnames
            data=list(oqish)
            if not data:
                print("Hech narsa topilmadi!")
                return
            product_id=input("O'chirmoqchi bolgan mahsulotingizni ID sini kiriting: ")
            topildi=0
            for i in data:
                if product_id==i['product_id']:
                    topildi=1
                    data.remove(i)
                    break
            if topildi:
                with open(fayl_nomi,"w",encoding="UTF-8",newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=qator_nomlari)
                    writer.writeheader()
                    writer.writerows(data)
                    print("Muvaffaqiyatli o'chirildi!")
            else:
                print("Bunday mahsulot mavjud emas!")

    except FileNotFoundError:
        print("Xatolik!")

def summa_products():
    try:
        with open("11_vazifa/werehouse.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Fayl bo'sh!")
                return
            umumiy=0
            print("======MAHSULOTLAR HISOB-KITOBI=====")
            for i in data:
                jami=float(i['quantity'])*float(i['price'])
                umumiy+=jami
                print(f"{i['name']} ning jami summasi: {jami:.2f}")
                print("="*20)
            print(f"Ombordagi umumiy mahsulotlar summasi: {umumiy:.2f}")
    except FileNotFoundError:
        print("Xatolik!")

while True:
    print("========MENYU========")
    print("1-Mahsulot qoshish")
    print("2-Barcha mahsulotlarni ko'rish")
    print("3-Mahsulotlarni yangilash")
    print("4-Mahsulotlarno o'chirish")
    print("5-Mahsulotlar hisob kitobi")
    print("6 -Chiqish")
    print("="*20)
    tanlov=input("Tanlang: ")

    if tanlov=="1":
        add_product()
    elif tanlov=="2":
        show_product()
    elif tanlov=="3":
        update_product()
    elif tanlov=="4":
        delete_product()
    elif tanlov=="5":
        summa_products()
    elif tanlov=="6":
        print("E'tiboringiz uchun tashakkur!")
        break
    else:
        print("Noto'g'ri buyruq kiritildi!")
        print("Qaytadan urinib ko'ring!")
