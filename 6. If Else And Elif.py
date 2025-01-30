rquired_age_at_school = 5
your_age = input("How old are you ?")

# Counting The Possibilities & Returning The Answer

if  your_age == rquired_age_at_school: 
    print("Congratulations! You can join school") 
                                 
elif your_age < 20: 
    print("You should join higher secondary school")

elif your_age >= 20:
    print("You should go to College")    

elif your_age <= 2:
    print("You are too young ?")

else:
    print("Sorry! You can not join school")




