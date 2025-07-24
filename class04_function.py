def hello():
    print("hello")
    
hello()

def hello(word):
    print(word)
    
hello("hello word")

def hello(name):
    print(name)

name = input()
hello(name)



def sum(a,b):
    result = a + b
    return result


num1 = int(input("กรอกเลข1: ")) #3
num2 = int(input("กรอกเลข2: ")) #4

print(sum(num1,num2))




def add(num1,num2):
    result = num1 + num2
    return result
 
def minus(num1,num2):
    result = num1 - num2
    return result
 
def mutiple(num1,num2):
    result = num1*num2
    return result
 
def divide(num1,num2):
    result = num1 / num2
    return result
 
def is_even(num):
    result = num%2
    if (result == 0):
        x = "even"
    else:
        x = "odd"    
    return x
 
def main():
    num1 = int(input("กรอกเลขตัวที่ 1: "))
    num2 = int(input("กรอกเลขตัวที่ 2: "))
    print(" + - * / เอาอันไหนน้อง")
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] /")
    operation = input("เลือกสักอัน: ")
    # ตรงนี้ให้น้องๆเขียน condition (if-else) ว่าถ้ามันตรงกับเลขนั้นในเมนูจะให้ใช้ฟังก์ชั่นอะไร
    if (operation == "1"):
        result = add(num1,num2)
        print("ผลบวกคือ:",result)
    elif (operation == "2"):
        result = minus(num1,num2)
        print("ผลลบคือ:",result)
    elif (operation == "3"):
        result = mutiple(num1,num2)
        print("ผลคูณคือ:",result)
    elif (operation == "4"):
        result = divide(num1,num2)
        print("ผลหารคือ:",result)   
 
    # เรียก is_even เพื่อเช็กว่าผลลัพที่ได้มันเป็นเลขคู่มั้ย
    print(is_even(result))
    print(int(result))

main()