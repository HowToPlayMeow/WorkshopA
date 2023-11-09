def IB ():
    NB = int(input("กรอกหมายเลข 0 - 25 : "))
    return NB
def RB ():
    import random
    RN = random.randint( 0 , 25 )
    return RN
def SB ( NB , RN ):
    if NB == RN:
        print (f"Your is number : {NB} | Number Bingo is : {RN} | Correct, You are the win")
    else :
        print (f"Your is number : {NB} | Number Bingo is : {RN} | Not, Correct!!!")
print ("***---------------------------***")
NB = IB()
print ("***---------------------------***")
RN = RB ()
SB ( NB , RN )
print ("***---------------------------***")