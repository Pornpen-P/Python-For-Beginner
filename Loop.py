a = [0,1,2,3,'Pook']
for i in a:
 print(i)

for i in range(4):
    print(i)

    
for name in ['Jalerr','Apo','Bible','Jeff']:
    print('I like ' + name)

x = 4
while x > 0:
    print(x)
    x = x - 1


while True:
    name = input("ชื่ออะไรจ๊ะ? : ")
    if name == 'exit' :
        print("ออกจากโปรแกรม")
        break
    print("สวัสดี " + name)
