def ID () :
    GL = input("กรอกชื่อหัวหน้ากรุ๊ปทัวร์ : ")
    NL = int(input("กรอกเบอร์ติดต่อกลับภายหลัง : "))
    P = int(input("กรอกจำนวนคนที่จะไปเที่ยวกับกรุ๊ปทัวร์ : "))
    return GL , NL , P
def CP ( P ) :
    if P <= 2 :
        pay = 300
    elif P <= 5 :
        pay = 250
    elif P <= 10 :
        pay = 210
    else :
        pay = 150
    return pay
def show ( GL , NL , P , pay ) :
    print (f"| ชื่อหัวหน้ากรุ๊ปทัวร์ : {GL} | เบอร์ติดต่อกลับภายหลัง : {NL} |")
    print (f"| จำนวนคนที่จะไปเที่ยวกับกรุ๊ปทัวร์ : {P} | ตกคนละ {pay} บาท |")
    print (f"| ยอดรวมทั้งหมดที่ต้องชำระ {P * pay}")

print ("***------------------------***")
GL , NL , P = ID ()
print ("***------------------------***")
pay = CP ( P )
show ( GL , NL , P , pay )
print ("***------------------------***")