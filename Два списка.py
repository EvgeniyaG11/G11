import random

a = random.sample(range(1, 11), 5)

print("List A: " + str(a))

b = random.sample(range(1, 21), 5)

print("List B: " + str(b))

result = list(set(a) & set(b))

print("Common elements for two lists: " + str(result))
