print(1, 2, 3, 4 *2, sep = '+', end=' = ')
print (1+2+3+(4*2))

ans = '5 + 19 = '
expr = 5 + 19
print (str(ans) + str(expr))

s1 = 10

print("Таблица умножения: \n")
for i in range(1, s1 + 1):
    print(*range(i, i * s1 + 1, i), sep='\t')
