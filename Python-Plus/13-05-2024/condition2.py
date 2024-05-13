def ticket(age):
    if age <=5:
        return 0
    else:
        return 100

print(ticket(4))


def ticket2(age):
    return 0 if age <=5 or age >= 60 else 100 # ternaty


def ticket2a(age):
    if age <=5 or age >= 60:
        return 0
    else:
        return 100

print(ticket2(70))
print(ticket2(35))
print(ticket2(3))

def ticket3(age, is_local):
    if (age <=5 or age >= 60) and is_local:
        return 0
    else:
        return 100

print(ticket3(3, False))


def demo(a):
    if a >=10 and a <= 20:
        print("ok")
    else:
        print("not ok")

def demo2(a):
    if 10 <= a <= 20:
        print("ok")
    else:
        print("not ok")

demo2(18)
