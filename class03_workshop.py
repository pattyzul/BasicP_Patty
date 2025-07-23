monster = 300
sword1 = 150
sword2 = 90
sword3 = 60

play= True
while play:
    print("------welcome to kiritu game-------")
    print("Do you want to [1] kick monster")
    print("Do you want to [2] ride jakkayan nee :(")
    x = int(input("--pls choose your way--: "))
    if x == 1:
        print("keng mak pai tor")
        tell = int(input("how many rounds do u want to attack!!!: "))
        for i in range(tell):
            print("choose weapon[1] :", sword1)
            print("choose weapon[2] :", sword2)
            print("choose weapon[3] :", sword3)
            weapon = int(input("you weapon isss: "))
            if (weapon == 1):
                print(150)
                monster = monster-150
            elif (weapon == 2):
                print(90)
                monster = monster-90
            else:
                print(60)
                monster = monster-60
            print("monster health",monster )
            if monster == 0:
                print("we win keng jung auan")
            elif monster > 0 and i == tell:
                print("lose :(")
                break    
    elif x == 2:
        print("kak mak ")




