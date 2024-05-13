x = "Peter Parker" #global scope / module scope

def fn():
  x = "Spiderman" #local
  print("Inside fn()", x)

#ฟังก์ชันจะไม่รู้ว่า x คืออะไร
def fn2():
  x = "Mr. " + x
  print("inside fn()", x)

#ระบุ x ว่าใช้ global x ทำให้ x มีค่าเท่ากันกับ Peter Parker ** ไม่ใช่สิ่งที่ดีในการระบุเมื่อเขียนโปรแกรม ใช้เมื่อจำเป็นเท่านั้น
def fn3():
  global x
  x = "Mr. " + x
  print("inside fn()",x)

print(x)
fn3()
print(x)

