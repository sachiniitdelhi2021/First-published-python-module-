# defining first function for getting the sum of any number of input numbers 

def add_numbers(*args):
    
    ''''' This is the function which is used for getting the sum of any number of input
    numbers and for giving any number of input arguments we are using (*args)
    
    ex : 
    
    add_numbers(1,2,3,4)
    
    ---> result will be : 10'''''
    
    a=0
    for i in args:
        a=a+i
    return a
        
# defining second function for getting the product of any number of input numbers 

def mul_numbers(*args):
    
    ''''' This is the function which is used for getting the product of any number of input
    numbers and for giving any number of input arguments we are using (*args)
    
    ex : 
    
    mul_numbers(1,2,3,4)
    
    ---> result will be : 24'''''
    
    a=1
    for i in args:
        a=a*i
    return a


# defining Third function for getting the division two numbers  

def div_numbers(a,b):
    
    ''''' This is the function which is used for getting the division of any two input
    numbers.
    
    ex : 
    
    div_numbers(4,2)
    
    ---> result will be : 2.0'''''
    return a/b


# defining fourth function for getting the subtraction of two numbers  

def sub_numbers(a,b):
    
    ''''' This is the function which is used for getting the subtraction of any two input
    numbers.
    
    ex : 
    
    sub_numbers(4,2)
    
    ---> result will be : 2'''''
    return a-b


# defining fifth function for getting the simple interest
def simple_int(P,R,T):
    
    ''''' This function is used for getting the simple interest for given principle amount,
    Rate and the Time(yrs).
    
    keywords :
    
    p : is the principle amount 
    R : is the rate 
    T : is the time duration in years
    
    ex :
    
    simple_int(10000,5,5)
    
    ---> result will be : 2500'''''
    
    s=(P*R*T)/100
    return s

# defining sixth functon for getting the compound interest 

def compound_int(P,R,T):
    
    ''''' This function is used for getting the compound interest for given principle amount,
    Rate and the time duration (years).
    
    keywords : 
    
    p : is the principle amount (Rs).
    R : is the rate 
    T : is the time duration in years.
    
    ex :
    
    compound_int(10000,10.25,5)
    ---> result will be : 6288.946267774416'''''
    
    
    Amount = P * (pow((1 + R / 100), T))
    CI = Amount - P
    return "Compound interest is : "+' '+ str(CI)


# defining seventh function for getting the 'log' of any given +ve number 

def get_log(n,b):
    
    ''''' This function is used for getting the log of any given positive number to any base 
    
    keywords : 
    
    n : is the number of which 'log' is to be find 
    b : is the base for getting the log of any number 
    
    ex : get_log(256,4)
    
    log4(256) = log2(256)/log2(4)  in this we are finding log of 256 for base 4 
    
    ----> result will be : 4'''''
    from math import log2
    
    return 'log_n_to_base_b is :'+' '+str(log2(n)//log2(b))


# defining eight function for getting e^x for any 'x'

def exp_power(n):
    
    ''''' This function is used for getting the value of exponent for any power
    
    keywords : 
    
    n : is the number for calculating (e)^n
    
    ex : 
    
    exp_power(1)
    
    ----> result will be : 2.718281828459045'''''
    
    from math import exp
    
    return 'exponet(e) to the power {} is :'.format(n) +' '+ str(exp(n))   


# defining ninth function for getting the roots of quadratic equation 

def Roots_quad(a,b,c):
    
    ''''' This function is used for getting the real roots of quadratic equation.
    (a*x^2+b*x+c) where a, b and c are the constants.
    
    ex : 
    x^2+4*x+4=0
    real roots are: -2,-2'''''
    
    z=(b**2)-4*a*c

    if z>=0:
        root_1=(-b+z**0.5)/(2*a)
        root_2=(-b-z**0.5)/(2*a)
        print('Roots are real:')
        print('root 1 is : {}'.format(root_1),'&', 'root 2 is : {}'.format(root_2))


    else:
        print('The given quadratic equation does not have real roots')
    

# defining tenth function for getting the value of any number to any number 

def num_power(n1,n2):
    
    ''''' This function is used for getting the value of any power of any number.
    keywords :
    n1 : is the number
    n2 : is the power 
    
    ex :
    
    num_power(2,2)
    ---> result will be : 4'''''
    
    return n1**n2
