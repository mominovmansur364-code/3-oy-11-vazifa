import csv

def add_book():
    try:
        f = open("11_vazifa/books.csv", "r", encoding="UTF-8")
        f.close() 
    except  FileNotFoundError:
        with open("11_vazifa/books.csv","w",encoding="UTF-8",newline="") as f:
            pen=csv.writer(f)
            pen.writerow(["title","author"])
    nomi=input("Kitob nomi: ")
    muallif=input("Muallifi: ")

    with open("11_vazifa/books.csv","a",encoding="UTF-8",newline="") as f:
        pen=csv.writer(f)
        pen.writerow([nomi.capitalize(),muallif.capitalize()])
        print("Muvaffaqiyatli saqlandi!")

def show_books():
    try:
        with open("11_vazifa/books.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))
            if not data:
                print("Kitoblar mavjud emas!")
                return
            print("="*20)
            for i in data:
                print(f"Kitob nomi: {i['title']}")
                print(f"Muallifi: {i['author']}")
                print("="*20)
    except FileNotFoundError:
        pass
        print("Kitoblar mavjud emas!")   

def search_book():
    try:
        with open("11_vazifa/books.csv","r",encoding="UTF-8") as f:
            data=list(csv.DictReader(f))

            qidiruv=input("Qidirayotgan kibobingizni muallifini kiriting:")
            topildi=0
            for i in data:
                if i['author'].lower()==qidiruv.lower():
                    topildi=1
                    print(f"Kitob nomi: {i['title']} muallifi: {i['author']}")
            if topildi==0:
                print("Bu muallifning kitoblari topilmadi!")
    except FileNotFoundError:
        pass
        print("Fayl topilmadi!")

while True:
    print("======MENYU======")
    print("1-Kitob qoshish")
    print("2-Kitoblarni ekranga chiqarish")
    print("3-Kitobni qidirish")
    print("4-Chiqish")
    print("="*20)
    tanlov=input("Tanlang: ")

    if tanlov=="1":
        add_book()
    elif tanlov=="2":
        show_books()
    elif tanlov=="3":
        search_book()
    elif tanlov=="4":
        print("Etiboringiz uchun rahmat!")
        break
    else:
        print("Notogri buyruq kiritildi! Qaytadan kiriting!")

                

