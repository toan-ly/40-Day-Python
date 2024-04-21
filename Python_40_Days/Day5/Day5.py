# 1
ls = list(range(1, 11))
print(ls)

# 2
print(ls[:5])

# 3
print([i for i in ls if i % 2])
        
# 4
sum = 0
for i in ls:
    sum += i
print(sum)