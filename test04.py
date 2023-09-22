'''รับข้อมูลจำนวนแต็ม 5 จำนวนจากผุู้ใฃ้แสดงและคำนวณหาผลรวม
และค่าเฉลี่ยของข้อมูลที่รับเข้ามาเป็นเท่าใดแล้วแสดงผลทางหน้าจอ'''

#ขอ 4 ฟังก์ฃั่น ดั้งนั้นหาให้ได้ 4 feature

# ========================
# Program Average 5 Number 
# ========================
# Enter number 1 :  <input>
# Enter number 2 :  <input>
# Enter number 3 :  <input>
# Enter number 4 :  <input>
# Enter number 5 :  <input>
# ========================
# Sum of 5 number is : <input>
# Average of 5 number is  :  <output>
# ========================

def get_number():
    number = []
    for i in range(5):
        num = int(input("ป้อนหมายเลข {}: ".format(i+1)))
        number.append(num)
    return number

def calculate_sum(number):
    return sum(number)

def calculate_average(number): 
    return sum(number) / len(number)

def display_resual(total, average):
    print('ผลรวมของตัวเลข 5 ตัว คือ : ',total)
    print('ค่าเฉลี่ยของ 5 หมายเลขล คือ:{:.4f}'.format(average))

number = get_number()
total = calculate_sum(number)
average = calculate_average(number)
display_resual(total, average)

