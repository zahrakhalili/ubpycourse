Edame="y"
Motezadha=dict()
Motezadha['black']='white'
Motezadha['dark']='light'
Motezadha['fat']='thin'
Motezadha['tall']='small'
while Edame=="y":
    Kalame = input("Lotfan kalame morede nazar ra vared konid:")
    if Kalame in Motezadha.keys():
        print("Motezad in kalame :" + Motezadha[Kalame])
    else:
        print("Motezad in kalame mojood nist!!!")
        Danestan=input("Aya motezad in kalame ra midanid?")
        if Danestan=="y":
            Motezad=input("Lotfan motezad kalame "+Kalame+" ra vared konid:")
            Motezadha[Kalame] = Motezad
    Edame= input("Aya edame midahid?")




