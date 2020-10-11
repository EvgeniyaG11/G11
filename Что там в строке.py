words = str("Autumn leaves upon the ground, Yellow, brown and red, Winter’s getting closer, The trees are going to bed")

print(words)

find = input('Enter letter to find ')

count = int(0)

for i in words:

    if i == find:

     count = count + 1

print("Number of times it occurs is: " + str(count))
