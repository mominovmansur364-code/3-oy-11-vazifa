import csv

def add_student():
    try:
        f = open("11_vazifa/students.csv", "r", encoding="UTF-8")
        f.close()
    except FileNotFoundError:
        with open("11_vazifa/students.csv", "w", encoding="UTF-8", newline="") as f:
            pen = csv.writer(f)
            pen.writerow(["name", "age"])

    ism = input("Ism kiriting: ")
    yosh = input("Yoshi: ")
    
    with open("11_vazifa/students.csv", "a", encoding="UTF-8", newline="") as f:
        pen = csv.writer(f)
        pen.writerow([ism.capitalize(), yosh])
        print("Malumotlar saqlandi!")

def show_student():
    try:
        with open("11_vazifa/students.csv", "r", encoding="UTF-8") as f:
            data = list(csv.DictReader(f))
            if not data:
                print("Talabalar mavjud emas!")
                return
            
            print("=" * 20)
            for i in data:
                print(f"Ism: {i['name']}")
                print(f"Yosh: {i['age']}")
                print("=" * 20)
    except FileNotFoundError:
        pass
        print("Talabalar mavjud emas!")

def ortacha_yosh():
    try:
        with open("11_vazifa/students.csv", "r", encoding="UTF-8") as f:
            data = list(csv.DictReader(f))
            jami_yosh = 0
            soni = 0
            for i in data:
                soni += 1
                jami_yosh += int(i['age'])
            
            if soni == 0:
                print("Talabalar mavjud emas!")
                return
                
            ortacha = jami_yosh / soni
            print(f"O'rtacha yosh: {ortacha}")
    except FileNotFoundError:
        pass
        print("Talabalar mavjud emas!")

while True:
    print("======MENYU======")
    print("1-Talaba qoshish")
    print("2-Talabalarni ko'rish")
    print("3-O'rta yoshni hisoblash")
    print("4-Chiqish")
    print("=" * 20)
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        add_student()
    elif tanlov == "2":
        show_student()
    elif tanlov == "3":
        ortacha_yosh()
    elif tanlov == "4":
        print("Etiboringiz uchun rahmat!")
        break
    else:
        print("Notogri buyruq kiritildi!")