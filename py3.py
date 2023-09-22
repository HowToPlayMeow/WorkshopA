def IDS():
    name = input("ชื่อรายการสินค้า : ")
    price = int(input("ราคาสินค้า : "))
    return name , price
def cal( price ):
    vat = price * 0.07
    out = price + vat
    return vat , out
def show( name , price , vat , out):
    print (f"ชื่อรายการสินค้า : {name}")
    print (f"ราคาสินค้า : {price:.2f}")
    print (f"Vat 7% : {vat:.2f}")
    print (f"ราคาที่ต้องชำระ {out:.2f}")
print ("------------------------")
name , price = IDS()
print ("------------------------")
vat , out = cal( price )
show( name , price , vat , out)
print ("----------END-----------")