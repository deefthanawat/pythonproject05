def ca1lculate_selling_price(cost_price):
    selling_price =cost_price * 1.10
    return selling_price

cost_price = float(input('ราาคาสินค้า(ต้นทุน)'))

result = ca1lculate_selling_price(cost_price)
print('ราคาขายสินค้า:{:2}'.format(result))