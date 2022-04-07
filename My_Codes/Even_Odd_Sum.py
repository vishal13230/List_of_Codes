l1 = [12,24,23,34,35,56,24]

def even_odd_sum(l1):
    even_sum = 0
    odd_sum = 0
    for i in l1:
        if i % 2 == 0:
            even_sum = even_sum + i 
        else:
            odd_sum = odd_sum + i
    return even_sum, odd_sum

print(even_odd_sum(l1))