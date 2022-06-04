# checking whether number is prime or not 

num = int(input('Enter number to check whether it is prime or not :  '))
prime = True
for i in range(2, num):
    if(num%i==0):
       divisible_by = i
       prime = False
    break
    
# print(prime)
if prime:
    print(f'{num} is prime ')
else:
    print(f'{num} is composite , because it  is divisible by {divisible_by}')