#Name: Seeley Seward
#Class: 6th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.
numblist =[1,2,3,4,5,6,7,8,9,10]
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers=0
oddNumbers =0
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for i in numblist:
    if i % 2 == 0:
        evenNumbers +=1
    else:
         oddNumbers +=1

# Print the total count of even and odd numbers.
print(evenNumbers)
print(oddNumbers)