#Importing the math library
import math

#Defining the menu function
def menu ():
    print ("Start the program? [0/1]")
    print ("[0] No")
    print ("[1] Yes")

#Defining the prime_number function
def prime_number():
    mltpl = int(input("Enter a number : "))
    square = math.ceil(math.sqrt(mltpl))
    fctr = []
    is_prime = True
    
    #Determining the condition of the multiple based on mltpl integer
    if mltpl<2:
        is_prime=False
    else:
        for fac in range(2,square+1):
            if mltpl==fac:
                is_prime=True
            elif mltpl%fac==0:
                is_prime=False
                break
    
    #Determining the factors of mltpl then appending to the fctr list
    if mltpl>1 :
        for dvsr in range (1,mltpl+1):
            if mltpl%dvsr==0:
                fctr.append(dvsr)
    
    #Determining the output based on the value of is_prime boolean
    if is_prime==False:
        if mltpl<2:
            print (mltpl," is a binary number")
        elif math.sqrt(mltpl)%1==0:
            print (mltpl," is a composite number")
            print (mltpl," is a square number of ",int(math.sqrt(mltpl)))
            print ("Factors of ",mltpl," are : ",fctr)
        else:
            print (mltpl," is a composite number")
            print ("Factors of ",mltpl," are : ",fctr)
    else:
        print (mltpl," is a prime number")
        print ("Factors of ",mltpl," are : ",fctr)
    
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
