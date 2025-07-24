x = ["sun", "tik"]

print(x)

x[0] = "vava"
print(x)
x.append("ton") #เพิ่มคนเข้าไป
print(x)


x = ["sun", "tik" , "ton", "vava", "gap"]
print(len(x)) #check จำนวน
for i in range(len(x)):
    print(x[i])
for speaker in x :
    print(speaker)




score = [99, 10 ,20 ,50]
sum = 0
for i in range(len(score)):
    print(sum)
    sum +=score[i]
    
print("total: ", sum)
    
num = [1,2,3,4,5,6,7,8,9,10]
for number in num:
    if(number % 2 == 0):
        print("even: ", number)
    else:
        print("odd: ", number)
 


students = [
    {"name":"sun", "sid":671305, "score":100},
    {"name":"tik", "sid":671305, "score":80},
    {"name":"vava", "sid":671305, "score":-10000}
]
for stu in students:
    if(stu["score"] >= 90):
        stu["score"] = "A"
    elif(stu["score"]>= 70):
        stu["score"] = "B"
    else:
        stu["score"] = "super F!!!!"
    print(stu["name"],stu["score"])