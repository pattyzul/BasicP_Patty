distance = int(input("sen tang"))
4
if (distance <5 ):
    print("ราคาเท่ากับ 0")
elif (distance >=5 and distance <= 50):
    print("ราคาเท่ากับ 10")
elif (distance >=51 and distance <= 100):
    print("ราคาเท่ากับ 15")
elif (distance >=101 and distance <= 300):
    print("ราคาเท่ากับ 25")    
elif (distance >=301 and distance <= 500):
    print("ราคาเท่ากับ 35")
else:
    print("ราคาเท่ากับ 45")   