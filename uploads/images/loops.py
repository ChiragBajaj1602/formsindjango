# iteration in the list by the loops that iterates over it
list1=[109,108,78]
for x in list1:
    print(x)
i=1
while i<6:
    print(i)
    i+=1
print("i is no longer than 6")
# iterating through the string using for loops
string1="banana"
for x in string1:
    print(x)
    if x=='a':
        break
primes=[2,3,5,7]
for prime in primes:
    print(prime)
for x in range(5):
    print(x)
for x in range(3,6):
    print(x)
for x in range(3,8,2):
    print(x)
count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break
for x in range(10):
    if x%2==0:
        continue
    print(x)