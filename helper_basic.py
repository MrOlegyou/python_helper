age = 10 # int - ціле число
text = "Hello World" # str - строка
temperature = 1.5 # float - дріб
is_big = True # bool - логічний вираз

products = ["milk", "bread", "apple"] # list - список
cartoons = {"Cars": "McQueen", "Panda Kung Fu": "Po"} # dict - словник (ключ-значення)
scandinavia = ("Norway", "Sweden", "Finland") # tuple - кортеж (незмінюваний список)
years = {2016, 2020, 2024, 2028, 2032} # set - набір (без повторень)

#-------------------------------

your_age = input("Введіть ваш вік") # функція для введення тексту (завжди повертає str)

#-------------------------------

pens = 80 # ручки
pensils = 80 # олівці

# знаки для порівняння: > , < , == , >= , <=
if pens < pensils:
    print("Олівців більше")
elif pens == pensils:
    print("Предметів порівну")
else:
    print("Ручок більше")

#-------------------------------

# цикл у діпазоні від 0 до 24
for i in range(25):
    ...

# цикл у діпазоні від 10 до 24
for i in range(10, 25):
    ...

# цикл у діпазоні тексту: t, e, x, t, a, b, c
for i in "textabc":
    ...

# цикл у діпазоні списку: Milk, Bread, Coca-Cola
for i in ["Milk", "Bread", "Coca-Cola"]:
    ...

# цикл з умовою (працює поки ручок менше ніж 120)
while pens < 120:
    ...

# цикл з умовою (працює завжди)
while True:
    break # розриває цикл, коли необхідно

#-------------------------------

# робота зі списком
group = ["Василь", "Тимур"]
group.append("Петро") # додаємо до кінця списку
lengt = len(group) # знаходимо довжину списку

#-------------------------------

# робота з класами
class Human():
    def __init__(self, size, height, material="Шкіра"): # конструктор класу
        # властивості
        self.size = size
        self.height = height
        self.material = material
    
    # методи
    def go(self):
        print("Ходити")

    def jump(self):
        print("Стрибати")

    def talk(self):
        print("Говорити")

# створення об'єктів
Hodun = Human("XXXL", 200)
Hodun.go()

Poprygun = Human("L", 175)
Poprygun.jump()
Poprygun.talk()

Govorun = Human("S", 102)
Govorun.go()
Govorun.talk()

#-------------------------------

# імпортування модулів (pip install ...)
import time
import random
import json
import requests
import customtkinter

# робота з часом
seconds = time.time() # кількість секунд з початку Епохи (01.01.1970)
time.sleep(5) # програма засинає на 5 сек

# робота з випадковими числами (рандом)
number1 = random.random() # рандомне число від 0 (включно) до 1 (не включно)
number2 = random.randint(1, 5) # рандомне число від 1 (включно) до 5 (включно)

# робота з json (ключ-значення)
with open("database.json", "w") as file: # запис даних
    json.dump({"key": "value"}, file)

with open("database.json", "r") as file: # зчитування даних
    data = json.load(file)

# робота з requests (API - запити; клієнт-сервер; HTTP)
# 200 - успіх
# 400 - помилка з боку клієнта
# 500 - помилка з боку сервера
result = requests.get("https://api.nationalize.io/?name=Petro") # зробити GET запит
print(result.json()) # дістати результат запиту

# робота з GUI (графічний інтерфейс)
app = customtkinter.CTk() # створення застосунку-вікна
app.geometry("500x500") # налаштування розміру вікна
app.title("Login Window") # назва вікна
app.grid_columnconfigure(0, weight=1) # один стовпчик посередині вікна

login_label = customtkinter.CTkLabel(app, text = "Text") #надпис на екрані
login_label.grid(row=0, column=0, padx=0, pady=0)

app.mainloop() #цикл роботи застосунку