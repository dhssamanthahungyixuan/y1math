# What are the odd numbers from 1 to num?

num = 123
for i in range(1, num+1):
  if i % 2 == 1: # or != 0
    print(i, end=' ')
for i in range(2, num+1):
  if i % 2 == 1: # or != 0
    print(i, end=' ')
