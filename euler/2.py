last = 1
current = 1
even_sum = 0

while last < 4_000_000:
    nth = last + current
    last = current
    current = nth
    if last % 2 == 0:
        even_sum += last

print(even_sum)
