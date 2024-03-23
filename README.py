# Examining the divisibility of numbers
target = int(input(" Enter : "))
source = []
counter = 0

for i in range(1, target + 1) :
    if target % i == 0 :
        source.append(i)
        counter += 1

print(source, counter)



