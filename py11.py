def ID ():
    PN = int(input("กรอกเบอร์โทรศัพท์ : "))
    UN = input("กรอกชื่อผู้ใช้เบอร์โทรศัพท์ : ")
    TC = float(input("กรอกจำนวนที่ต้องการใช้โทรศัพท์ : "))
    return PN , UN , TC
def CMC ( TC ):
    if TC <= 15 :
        min = 5 
    elif TC <= 30 :
        min = 3
    else :
        min = 1.50
    MT = TC * min
    return min , MT
def show ( PN , UN , TC , MT ):
    print (f"| ชื่อผู้ใช้เบอร์โทรศัพท์ : {UN} | เบอร์โทรศัพท์ : {PN} |")
    print (f"| จำนวนที่ใช้โทร : {TC} นาที | ตกนาทีละ : {min} บาท |")
    print (f"| เป็นจำนวนเงิน : {MT} บาท |")
print ("***-----------------------***")
PN , UN , TC = ID ()
print ("***-----------------------***")
min , MT = CMC ( TC )
show ( PN , UN , TC , MT )
print ("***-----------------------***")