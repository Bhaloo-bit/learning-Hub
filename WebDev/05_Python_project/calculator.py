print("mini calculator")


def add(num1, num2):
        return(num1 + num2)

def sub(num1, num2):
        return(num1 - num2)

def multiply(num1, num2):
        return(num1 * num2)

def divide(num1, num2):
        return(num1 % num2)

def avg(num1 , num2):
        return (num1 + num2) /2
print("** Please select and Options ** \n",\
        "1. Addtion", "2. Subtration", "3. Multiply" ," 4. Divide" , "5. Average"  
    )

select = int(input("Select Operations 1, 2, 3, 4, 5 :"))

num1 = int(input("Enter any numbers : "))
num2 = int(input("Enter any numbers : "))

if (select == 1):
        print('result :',add(num1 , num2))
elif(select == 2):
    print('result :',sub(num1 , num2))        
elif(select == 3):
    print('result :', multiply(num1 , num2))        
elif(select == 4):
    print('result :', divide(num1 , num2))        
else:
    (select == 5)
    print('result :',avg(num1 , num2))        
