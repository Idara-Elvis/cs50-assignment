
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(x):
    x = x.replace("$", "  ")
    return float(x)


def percent_to_float(p):
    p = p.replace("%", " ")
    return float(p) / 100
   



main()


life = (input("What is the great question of Life, the Universe and Everything? "))

if life == "42" or life == "forty two" or life == "forty-two":
   print("Yes")
else:
   print("no")


greet = input("Greeting: ")

if greet == "hello" or greet.startswith("hello"):
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")




file = input("File name: ").strip()

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")





def main():
    x, y, z= input("Expression: ").split(' ')
    x, z = int(x), int(z)
    if y == '+':
        print(f"{x + z:.1f}")
    elif y =="-":
        print(f"{x - z:.1f}")
    elif y == "*":
        print(f"{x * z:.1f}")
    elif y == "/":
        print(f"{x / z:.1f}")

main()





def main():
    meal = input("What time is it? ")
    time = convert(meal)
    print(time)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hour,minute = time.split(":")
    cal = float(minute) / 60
    return float(hour) + cal
    

    
if __name__ == "__main__":
    main()





camel = input("camelcase: ")
print("snake_case: ", end="")
for c in camel:
    if c.isupper():
        print("_", c.lower(), end="")
    else:
        print(c, end="")



amount_due = 50

while amount_due > 0:
    print("amount_due: ", amount_due)
    coin = int(input("insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due -= coin
change_owed = abs(amount_due)
print(amount_due)



prompt = input("input: ")
print("output: ", end="")

vowels = ["a","e","i","O","u"]
for v in prompt:
    if not v in vowels:
        print(v, end="")

print() 



def main():
    plate = input("input: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    for i in s:
        if i in ["."," ","!","?"]:
            return False

    return True

main()




fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "lemon": 15,
    "honeydew melon": 50,
    "plum":70,
    "kiwifruit":90,
    "peach":60,
    "lime":20,
    "nectarine":60,
    "pineapple": 50,
    "strawberries": 50,
    "orange": 80,
    "grapes": 90,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

fruit_answer = input("item: ")
for i in fruits:
    if i == fruit_answer:
        print("calories:",fruits[i])





while True:

    fuel = input("fraction: ")
    try:
        up_num, down_num = fuel.split("/")
        new_up = int(up_num)
        new_down = int(down_num)

        cal = new_up / new_down
        if cal <= 1:
            break

    except(ValueError, ZeroDivisionError):
        pass

calculate = cal * 100

if calculate <= 1:
    print("E")
elif calculate >= 99:
    print("F")
else:
    print(f"{calculate}%")

  

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total_amount = 0

while True:
    try:
        answer = input("item: ").title()
        if answer in menu:
            total_amount += menu[answer]
            print("total: $", end="")
            print("{:.2f}".format(total_amount))


    except EOFError:
        print()
        break


grocery = {}

while True:
    try:
        item = input().lower()
        if item in grocery:
            grocery[item] += 1

        else:
            grocery[item] = 1

    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        break

from ast import Interactive


month = [
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    get_date = input("date: ")
    try:
        m,d,y= get_date.split("/")
        if int(m) >= 1 and int(m) <=12 and int(d) >=1 and int(d) <= 31:
            break

    except:
        try:
            old_m,old_d,y = get_date.split(" ")
            for i in range(len(month)):
                if old_m == month[i]:
                    month = i + 1
                day = old_d.replace(",","")
            if int(m) >= 1 and int(m) <=12 and int(d) >=1 and int(d) <= 31:
                break

        except:
            print()
            pass

print(f"{y}-{int(m):02}-{int(d):02}")    















































































































































