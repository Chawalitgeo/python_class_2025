a = 1 #int #ตัวเลข
b = 1.1 #float #ทศนิยม
c = '1' #string ข้อความที่มีตัวฟันหนู
print(a+a) #ผลลัพธ์ = 2
print(a+b) #ผลลัพธ์ = 2.2
print(b+b) #ผลลัพธ์ =  1 1
#print(a+c) #ผลลัพธ์ = error





print(type(a)) #บอกหน้าที่ว่าเป็น int/float/str
print(type(b)) #บอกหน้าที่ว่าเป็น int/float/str
print(type(c)) #บอกหน้าที่ว่าเป็น int/float/str

#convert types
a = float(a) #float
b = int(b)
c = int(c)
print(a) #เปลี่ยนจากเลขเดี่ยวเป็นทศนิยม
print(b) #เปลี่ยนจากทศนิยมเป็นเลขเดี่ยว
print(c) #เปลี่ยนจากข้อความเป็นตัวเลข