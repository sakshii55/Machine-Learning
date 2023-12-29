# take principal period and rate of intrest

p=float(input("Please enter principal in INR:"))
n=float(input("Please enter number of years:"))
r=float(input("Please enter rate of intrest %p.a.:"))

# calculate simple intrest
I = p*n*r/100

# calculate total amount
A=p+I

# PRINT ABOVE RESULTS
print(f'Simple Intrest :{I:.2f}INR')
print(f'Total amount is :{A:.2f}INR')
