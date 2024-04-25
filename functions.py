#นิยาม
def greet_pook():
    print('Hello Pook')

#เรียกใช้ (call)
greet_pook()

    
def greet(name):
     print('Hello '+name)
     
greet('Jackie')  
greet('Por')
greet('Ple')
greet('Bumebim')
greet('Nan')
greet('Kaofang')
greet('Tonmint')


def yok2(x):
    return x**2

a = yok2(5)
print(a)


def x_haan_duay_y(x,y):
    if y ==0:
        print('หารด้วยศูนย์ไม่ได้')
        return 'ลองใหม่อีกครั้ง'
    return x/y
print(x_haan_duay_y(2,3))
print(x_haan_duay_y(2,0))
