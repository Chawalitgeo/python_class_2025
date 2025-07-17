#scop Variable - Global ND LOCAL variable
x = "awesome" #string

def my_function(): #สร้างคำสั่งเฉพาะ
    x = "stupid"
    print("python is " + x)
    
my_function()
print("python is " + x)