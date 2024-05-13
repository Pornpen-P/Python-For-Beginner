# come 3, pay 2
# come 4, pay 3

# input -> process -> output

# input
# come_x = 4
# pay_y = 3
# per_head = 399
# pax = 10

# #print((pax // come_x) * (pay_y * per_head))
# #print(pax % come_x * per_head)

# total= (pax // come_x) * (pay_y * per_head) + (pax % come_x * per_head)
# print(total)

#เริ่มจากการคิดคำนวณ และพัฒนามาเขียนเป็นฟังก์ชันไว้เลือกใช้ ตามลำดับ 

def come_x_pay_y(pax, per_head , come_x, pay_y):
  total= (pax // come_x) * (pay_y * per_head) + (pax % come_x * per_head)
  return total

print(come_x_pay_y(3,399,3,2))
