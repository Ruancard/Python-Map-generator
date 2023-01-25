import random

horizontal = int(input('sign horizontal size:'))
vertical = int(input('sign vertical size:'))
lemb = 1
yn = 0

for i in range(1,vertical):
    end_branco = random.randrange(1,horizontal)
    ini_branco = lemb

    space = []
    if yn == 1:
        if ini_branco < end_branco:
            for s in range (ini_branco,end_branco):
                space.append(s)
    
        elif ini_branco > end_branco:
            for s in range (end_branco,ini_branco):
                space.append(s)
        else:
            space.append(lemb)
    else:
        space.append(lemb)

    for h in range(0,horizontal):
        if h in space:
            print(' ', end="")
        else:
            print('x', end="")
    yn = random.randrange(0,2)
    
    if yn == 1:
        lemb = space[-1]
    if yn == 0:
        lemb = space[0]
    print('')