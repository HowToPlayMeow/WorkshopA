def ID():
    IU = int(input("กรอกรหัสพนักงาน : "))
    NU = input("กรอกชื่อพนักงาน : ")
    PP = int(input("กรอกยอดที่ขายของได้ : "))
    return IU , NU , PP
def cal( PP ):
    if PP < 1000 :
        com = 0.0
        text_com = 0.0
    elif PP <= 2000 :
        com = 0.01
        text_com = 1
    elif PP <= 3000 :
        com = 0.03
        text_com = 3
    else :
        com = 0.05
        text_com = 5
    H_P = PP * com
    H_P_all = ( PP * com ) + PP
    return com , H_P , H_P_all , text_com
def show( IU , NU , PP , text_com , H_P , H_P_all):
    print (f"| รหัสพนักงาน : {IU} | ชื่อพนักงาน : {NU} | ยอดที่ขายของได้ : {PP} บาท |")
    print (f"| เปอร์เซ็นต์ที่ได้จากคอมมิชชั่น : {text_com} % | ได้ค่าคอมมิชชั่นเป็นจำนวนเงิน : {H_P:.2f} บาท |")
    print (f"| ได้รับเงินเป็นจำนวน : {H_P_all:.2f} บาท |")
print ("***---------------------------***")
IU , NU , PP = ID()
print ("***---------------------------***")
cal( PP )
com , H_P , H_P_all , text_com = cal( PP )
show( IU , NU , PP , text_com , H_P , H_P_all)
print ("***---------------------------***")