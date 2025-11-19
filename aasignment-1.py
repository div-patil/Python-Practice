# Q1.
name = input("Enter a name: ")
age = int(input("Enter your age: "))
print(f'Hello myself {name}!, i am {age} year old')

# Q2.
num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : "))
print("product of two number = ", num1*num2)
print("sum of two number = ", num1+num2)
print("differnce of two number = ", num1-num2)
print("Quotient of two number = ", num1//num2)

# Q3. 
num3 = float(input("Enter a float number : "))
float_num1 = float(num1)
float_num2 = float(num2)
print("Average :",(float_num1+float_num2+num3) / 3)

# Q4.
str_num = input("Enter a number")
i_num = int(str_num)
f_num = float(str_num)
s_num = str(str_num)
print(f'int number {i_num}, float number {f_num}, string {s_num}')

# Q5.
print(f'Evalute this expression 10+3*2**2',10+3*(2**2))

# Q6.
n1= int(input("Enter a first number"))
n2= int(input("Enter a second number"))
n3 = n1 + n2
n1 = n3-n1
n2 = n3-n1
print("swap two number",n1,n2)

temparature = input("Enter a temparature")
temparature = float(temparature)
FahrenheitTemp =((temparature * (9/5)) + 32)
print(f'FahrenheitTemp = {FahrenheitTemp}')

# 
radius = int(input("Inter a radius ="))
print(f'Area of circle = ',(3.14 * (radius **2)))

# 
Principal = int(input("Enter a principle"))
Rate = int(input("Enter a rate"))
Time = int(input("Enter a time"))
simple_interest = (Principal * Rate * Time)//100
print(f'simple interest =',simple_interest)

#
n1 = float(input("Enter a number in decimal points eg.45.89"))
integer_part = int(n1)
print("integer part = ",integer_part)

print("fractional part = ", round(n1 - integer_part, 2) )

