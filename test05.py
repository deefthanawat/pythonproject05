"""คำนวณหาภาษีที่ต้องจ่าย และเงินเดือนสุทธิของพนักงานแล้วแสดงผลทางหน้าจอ
โดยรับค่ารหัสพนักงาน ฃื่อพนักงาน และเงินเดือนปกติของพนักงานทางแป้นพิมพ์
ทั้งนี้เงินเดือนสุทธิของพนักงานนั้นจะต้องหักค่าภาษีและเบี้ยประกันสังคมออกจากเงินเดือนปกติเสียก่อน
โดยที่พนักงานต้องเสียภาษี 7% ของเงินเดือนปกติและจ่ายค่าเบี้ยประจำสังคม 500บาท"""

#ขอ 5 ฟังก์ชั่น ดังนั้นต้องหาให้ได้ 5 feature

#คำนวณเงินเดือนพนักงาน
#ป้อนรหัสผ่านพนักงาน : <input>
#ป้อนฃื่อพนักงาน : <input>
#ภาษีเป็นเงิน : <output> บาท (ชอทศนิยม 2 ตำแหน่ง)
#เงินเดือนสุทธิเป็นเงิน : <output> บาท (ขอทศนิยม 2 ตำแหน่ง)

def calculate_tax(salary):
    tax = salary * 0.07
    return tax

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    net_salary = salary - tax - 500
    #หักเบี้ยประกันสังคม 500 บาท
    return net_salary

def get_employee_info():
    employee_id = input('ป้อนรหัสผ่านพนักงาน:')
    employee_name =  input('ป้นชื่อพนักงาน:')
    regular_saraly = float(input('เงินเดือนพนักงาน:'))
    return employee_id, employee_name, regular_saraly

def display_results(tax, net_salary):
    print('ภาษีเป็นเงินซ {:.2f}บาท'.format(tax))
    print('เงินเดือนสุทธิเป็นเงิน: {:.2f}บาท'.format(net_salary))

employee_id, employee_name,regular_salary = get_employee_info()
tax = calculate_tax(regular_salary)
net_salary = calculate_net_salary(regular_salary)
display_results(tax, net_salary)