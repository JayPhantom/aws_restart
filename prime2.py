
#declare array to place prime numbers
store_prime = []

#iterate between prime numbers
for i in range(2,250):
    prime = True
    for j in range(2,i):
        if (i%j==0):
            break
    else:
       #store prime numbers in an array
       store_prime.append(i)

#convert saved prime numbers from int to string
x = str(store_prime)

#declare two variables
string_prime=''
content =" "

#command to save converted prime numbers to results2.txt
textfile = open('/Users/Jacob/Documents/AWS Resstart/results2.txt', 'w')

#write saved prime numbers
textfile.writelines(string_prime.join(x))



