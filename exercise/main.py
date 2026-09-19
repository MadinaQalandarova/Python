#Topshiriq 1

ism = input()
print(f"Salom, {ism}!")

#Topshiriq 2

age = int(input("Tug'ilgan yilingizni kiriting: "))
print(f"Siz {2026-age} yoshdasz!")

#Topshiriq 3

p = float(input("Kvadratning tomonini kiriting: "))
print(f"Kvadratning perimetri: {4 * p}")

#Topshiriq 4

fruits = input("Mevalarni kiriting: ").split(" ")
print(f"Mevalar: {', '.join(fruits)}")


#Topshiriq 5

number = int(input("Sevimli soningni yoz: "))
print(f"Sevimli soningni kvadrati: {number ** 2}")
print(f"Sevimli soningni kubi: {number ** 3}")

#Topshiriq 6

sonlar = [10, 20, 30, 40, 50]
print(sonlar[0])
print(sonlar[-1])

#Topshiriq 7

mevalar = ["olma", "banan", "apelsin", "nok"]
mevalar.insert(1, "uzum")
print(mevalar)

#Topshiriq 8


cars = []
mashina = input("Mashinalar nomini kiritng: ")
cars.append(mashina)
print(cars)

#Topshiriq 9

regions = ["Toshkent", "Samarqand", "Buxoro", "Farg'ona"]
print(regions.remove("Buxoro"))

#Topshiriq 10

raqamlar = [41, 27, 3, 44, 50]
raqamlar.sort()
print(raqamlar)

#Topshiriq 11

a = [15, 25, 35, 45]
b =  sum(a) / len(a)     #o'rta arifmetik qiymatni hisoblash
print(b)

#Topshiriq 12   

big = input("Sonlarni kiriting: ").split(" ")
c = max(big)
d = min(big)
print(f"Eng katta son: {c}, Eng kichik son: {d}")   

#Topshiriq 13 teskari tartibda ro'yxat chiqarish

numberList = input("Bir nechta son kiriting: ").split(" ")
numberList.reverse()
print(f"Teskari tartibda: {numberList}")

#Topshiriq 14 element mavjudligini tekshirish

bozorlik = ["olma", "yog", "non", "sut"]
mijoz = input("Nima olasz? ")
if mijoz in bozorlik:
    print(f"Ha, bizda {mijoz} bor")
else:
    print(f"Uzr, bizda {mijoz} yo'q")

#Topshiriq 15 ro'yxat birlashtirish 

number1 = [1, 2, 3]
number2 = [4, 5, 6]
jami = number1 + number2
print(jami)

#Topshiriq 16 element indeksini aniqlash

ranglar = ["qizil", "yashil", "ko'k", "sariq"]
rangi = input("Rangni kiriting: ")
if rangi in ranglar:       
    print(f"Bu rang indeks raqami: {ranglar.index(rangi)}")   
else:
    print("Bunday rang mavjud emas!")