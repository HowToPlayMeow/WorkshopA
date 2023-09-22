def IDS():
    id = int(input("รหัสนักศึกษา : "))
    name = input("ชื่อนักศึกษา : ")
    So1 = float(input("คะแนนนักศึกษารอบที่ 1 : "))
    So2 = float(input("คะแนนนักศึกษารอบที่ 2 : "))
    So3 = float(input("คะแนนนักศึกษารอบที่ 3 : "))
    return id , name , So1 , So2 , So3
def cal (So1 , So2 , So3):
    score_all = (So1 + So2 + So3) / 3 
    return score_all
def show(id , name , So1 , So2 , So3 , score_all):
    print (f"รหัสนักศึกษา : {id}")
    print (f"ชื่อนักศึกษา : {name}")
    print (f"คะแนนนักศึกษารอบที่ 1 : {So1}")
    print (f"คะแนนนักศึกษารอบที่ 2 : {So2}")
    print (f"คะแนนนักศึกษารอบที่ 3 : {So3}")
    print (f"เฉลี่ยคะแนนทั้ง 3 คะแนนได้ : {score_all:.2f}")
print ("------------------------")
id , name , So1 , So2 , So3 = IDS()
print ("------------------------")
show(id , name , So1 , So2 , So3 , cal (So1 , So2 , So3))
print ("----------END-----------")