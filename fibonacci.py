nterm = 8

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterm <= 0:
   print("Please enter a positive integer")
elif nterm == 1:
   print("Fibonacci sequence upto",nterm,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterm,":")
   while count < nterm:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
