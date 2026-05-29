#program to find HCF/GCD

# enter 2 numbers
numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))

#using Eucliden algorithms
while(numberSmallest) :
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberLargest
    numberLargest = numberStore

print("HCF is : ", numberLargest)