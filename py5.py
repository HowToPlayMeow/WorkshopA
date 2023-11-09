def inputdata ():
    UP = int(input("ป้อนรหัสพนักงาน : "))
    UN = input("ป้อนชื่อพนักงาน : ")
    UM = int(input("ป้อนเงินเดือนพนักงาน : "))
    return UM , UN , UP
def add (UM):
    Additional_taxes = UM * 0.07
    return Additional_taxes
def sso (UM):
    have_user = UM - 500 
    return have_user
def user (have_user , Additional_taxes):
    use_money = have_user - Additional_taxes
    return use_money
def vat (Additional_taxes ,user):
    print (f"ภาษีเป็นเงิน : {Additional_taxes:.2f} บาท")
    print (f"เงินเดือนสุทธิเป็นเงิน : {user:.2f} บาท")

print ("--------------------------------------------")
print ("--------------คำนวณเงินเดือนพนักงาน------------")
print ("--------------------------------------------")
UM , UN , UP = inputdata ()
print ("--------------------------------------------")
vat (add (UM) ,user (sso (UM), add (UM)))
print ("--------------------------------------------")