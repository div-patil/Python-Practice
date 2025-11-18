# Q1 
salary = int(input("Enter a Salary : "))
if (salary < 30000):
    print("5% GST")
elif (salary >= 30000 and salary <=70000):
    print("15% GST")
elif (salary > 70000):
    print("25% GST")


# Q2.
first_number = int(input("Enter First Number."))
second_number = int(input("Enter Second Number."))
for i in range(first_number,second_number,2):
    print(i,end=" ")

# Q3.
num = int(input("Enter a Number : "))
while num > 0:
    rem = num % 10
    print(rem,end="")
    num//=10

# Q4.
def count_num(num):
    count = 0
    while num > 0:
       rem = num % 10
       count+=1
       num//=10
    return count
count_num(200)

# Q5.
def sum_num(num):
    sum=0
    while num > 0:
       sum += num % 10
       num//=10
    return sum
sum_num(200)

# Q6.

def print_num():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(i,end=" ")
print_num

#  Q7.
def play():
    while(True):
        user_res= input("Enter a number or Write quit to terminate: ")
        if user_res == 'quit':
            break
        else:
            num = int(user_res)
            if num > 0:
                print("Number is positive!!")
            else:
                print("Number is negative!!")
    
    
# Q8.
def calculator(a,b,operator):
    match(operator):
        case '+':
            print("Sum =",a+b)
        case '-':
            print("sub =",a-b)
        case '*':
            print("mul =",a*b)
        case '/':
            print("div =",a//b)
        case _:
            print("oprator are invalid")

# Q9.
def is_prime(n):
    for i in range(2,n):
        if n%2 == 0:
            return False
    return True

# Q10.
def guess_num():
    num_guess = 90
    while(True):
        num = int(input("Enter a number"))
        if num == num_guess:
            print("number is guess")
            break
        elif num > num_guess:
            print("number is high")
        elif num < num_guess:
            print("number is low")

