A = int(input('Type A: '))

B = int(input('Type B: '))

C = int(input('Type C: '))

while A <= B:

    print('A = ' + str(A) + "; B = " + str(B) + "; A still less than B")

    A = A + C

print('Finally! A is greater than B!')