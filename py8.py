def IW ():
    WP = int(input("กรอกค่า PH ของน้ำ : "))
    return WP
def CP (WP):
    if WP<= 8 :
        com = 0
    else :
        com = 1
    return com
def SP( com ):
    if com == 0:
        print ("Result is Normal")
    else :
        print ("Result is Alkali")

print ("***---------------------------***")
WP = IW()
print ("***---------------------------***")
CP ( WP )
SP( CP (WP) )
print ("***---------------------------***")