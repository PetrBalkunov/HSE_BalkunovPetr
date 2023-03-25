s1 = 10

print("Таблица умножения: \n")
for i in range(1, s1 + 1):
    print(*range(i, i * s1 + 1, i), sep='\t')
