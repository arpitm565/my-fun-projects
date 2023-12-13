#A Dice simulator which allows recurrence of 6, 3 times
import random as r
a = (input("Greetings user! Would you like to roll the dice ? , Yes or No " ).lower())
def inputchecker(a) :
    if a == "yes":
        print("You have entered yes, lets continue!")
        return True
    elif a == "no":
        print('Thank you, and have a ncie day!')
        return False
    else :
        raise ValueError(" Invalid input. Kindly enter yes or no only. ")
        return False
if inputchecker(a)  :
   v1 =   r.randint(1,6)
   print("The value appeared is : ", v1 )
   if v1 == 6 :
       v2 =  r.randint(1,6)
       print("The second value appeared is : ", v2 )
       if v2 == 6 :
         print("YAY! you got a second roll")
         v3 =   r.randint(1,6)
         print("The third value appeared is : ", v3 )
         if v3 == 6 :
             print("YAY! third roll! ")
             print('Oh! only 3 6s are allowed') 
     
