#1. Initialize with git init
#2. input a number
#3. if number is larger than 0, it becomes max-int
#4. if number is greater than 0, user can input another number
#5. repeat step 3 and 4 until negative number is given
#6. if negative number is given, print largest number



num_int = int(input("Input a number: "))# Do not change this line
max_int = 0
if num_int > 0:
    max_int = num_int
    while num_int > 0:
        num_int = int(input("Input a number: "))
        if num_int > max_int:
            max_int = num_int
    

print("The maximum is", max_int)    # Do not change this line
