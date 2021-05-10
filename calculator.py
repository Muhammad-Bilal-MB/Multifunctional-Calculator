import math

expression = ""

def Sum(first_value , second_value):                #Sum Function
    print(first_value + second_value)

def Subtract(first_value , second_value):           #Subtraction Function
    print(first_value - second_value)               

def Multiply(first_value , second_value):           #Multiplication Function
    print(first_value * second_value)

def Divide(first_value , second_value):             #Division Function
    if second_value == 0:
        print("Infinite Error")
    elif (first_value == 0 and second_value == 0):
        print("0/0 Form Encountered")
    else:             
        print(first_value / second_value)

def Square_Root(value):                             #Square Root Function  
    if value < 0:
        print("Imaginary value Error")
    else:                                   
        print(math.sqrt(value))

def Power(first_value , second_value):              #Power Function
    print(first_value ** second_value)

def Square(value):                                  #Square Function
    print(value ** 2)

def Cube(value):                                    #Cube Function
    print(value ** 3)

def Modulus(first_value , second_value):            #Modulus (Remainder) Function
    print(first_value % second_value)

def Sine(value):                                     #Sine Fucntion , Generalized over (-900 to 900 Degress)
    if (value == -180 or value == -360 or value == -540 or value == -720 or value == -900 or value == 0 or
       value == 180 or value == 360 or value == 540 or value == 720 or value == 900):
        print(0) 
    elif (value == -270 or value == -630 or value == 90 or value == 450 or value == 810):
        print(1)
    elif (value == -810 or value == -450 or  value == -90 or value == 270 or value == -630):
        print(-1)
    else:                                  
        print(math.sin(value))

def Cosine(value):                                  #Cosine Function , Generalized over (-900 to 900 Degress)
    if (value == -810 or value == -630 or value == -450 or value == -270 or value == -90 or value == 90 or
       value == 270 or value == 450 or value == 630 or value == 810):
        print(0) 
    elif (value == -720 or value == -360 or value == 0 or value == 360 or value == 720):
        print(1)
    elif (value == -900 or value == -540 or value == -180 or value == 180 or value == 540 or value == 900):
        print(-1)
    else:
        print(math.cos(value))

def Tangent(value):                                 #Tangent Function , Generalized over (-900 to 900 Degress)
    if (value == -900 or value == -720 or value == -540 or value == -360 or value == -180 or value == 0 or
        value == 180 or value == 360 or value == 540 or value == 720 or value == 900):
        print(0)
    elif (value == -855 or value == -675 or value == -495 or value == -315 or value == -135 or value == 45 or
        value == 225 or value == 405 or value == 585 or value == 765):
        print(1)
    elif (value == -765 or value == -585 or value == -405 or value == -225 or value == -45 or value == 135 or
        value == 315 or value == 495 or value == 675 or value == 855):
        print(-1)
    else:      
        print(math.tan(value))

def Logarithm(value):                               #Logarithm Function
    print(math.log(value))

def Exponential(value):                             #Exponential Function
    print(math.exp(value))



value_1 = float(input())
value_2 = float(input())
operator = str(input())

if operator == "+":
    Sum(value_1 , value_2)
elif operator == "-":
    Subtract(value_1 , value_2)
elif operator == "*":
    Multiply(value_1 , value_2)
elif operator == "/":
    Divide(value_1 , value_2)
elif operator == "sqrt":
    Square_Root(value_1)
elif operator == "^":       
    Power(value_1 , value_2)
