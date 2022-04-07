def even_odd(x):
    if x % 2 == 0 :
        return "The number {} is even".format(x)
    else:
        return "The number {} is odd".format(x)
    
even_odd(24)

list1 = [12,32,34,53,24]

list(map(even_odd, list1))