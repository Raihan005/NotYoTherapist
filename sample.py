import random
def cat():
    meows = ['meow','Meow..',"Meowww","MEOW","MEWOOOWWWW...",'meOWW',"MeOw..","MEEowW","Meoooww..."]
    purs = 'purrrrrr......'
    cmd = random.randint(0,1)
    if cmd == 0:
        len = random.randint(10,20)
        position = -1
        while position!= 0:
            position = random.randint(0,8)
            print(meows[position],end=' ')
            len-=1
    else:
        print(purs) 
cat()