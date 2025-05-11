#Importing the math library
import math

#Defining the menu function
def menu ():
    print ("Start the program? [0/1]")
    print ("[0] No")
    print ("[1] Yes")

#Defining the prime_number function
def prime_number():
    numbr = int(input("Enter a number : "))
    square = math.ceil(math.sqrt(numbr))
    fktr = []
    is_prime = True
    if numbr==0 or numbr==1:
        is_prime=False
    else:
        for fac in range(2,square+1):
            if numbr==fac:
                is_prime=True
            elif numbr%fac==0:
                is_prime=False
                break
    
    #Determining the factors of numbr then append to the fktr list
    for i in range (1,numbr+1):
        if numbr%i==0:
            fktr.append(i)
    
    #Determining the output based on the value of is_prime boolean
    if is_prime==False:
        if numbr==0:
            print (numbr," has many factors")
        elif numbr==1:
            print (numbr," has only one factor")
        elif math.sqrt(numbr)%1==0:
            print (numbr," is a square number of ",int(math.sqrt(numbr)))
            print ("Factors of ",numbr," are : ",fktr)
        else:
            print (numbr," is not a prime number")
            print ("Factors of ",numbr," are : ",fktr)
    else:
        print (numbr," is a prime number")
        print ("Factors of ",numbr," are : ",fktr)

    #Determining the output if the value numbr integer is binary
    
#Displaying the menu function
print()
menu ()
option = int(input("[0/1] => "))
while option != 0:
    if option ==1 :
        prime_number()
    else:
        print ("Input is invalid.")
    print ()
    menu()
    option = int(input("[0/1] => "))

print ("That's a wrap. Thanks.")