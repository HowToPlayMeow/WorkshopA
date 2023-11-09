def ID ():
    IS = int(input("กรอกรหัสนักเรียน : "))
    US = input("กรอกชื่อนักเรียน : ")
    PS = float(input("กรอกเกรดเฉลี่ยของนักเรียน : "))
    return IS , US , PS
def cal ( PS ):
    if PS < 2:
        NOPE = "ไม่ผ่าน"
    else :
        NOPE = "ผ่าน"
    return NOPE
def show ( IS , US , PS , NOPE ):
    print (f"| รหัสนักเรียน : {IS} | ชื่อนักเรียน : {US} |")
    print (f"| เกรดเฉลี่ยของนักเรียน : {PS} | ผลการเรียน : {NOPE} |")

print ("***----------------***")
IS , US , PS = ID ()
print ("***----------------***")
NOPE = cal ( PS )
show ( IS , US , PS , NOPE )
print ("***----------------***")