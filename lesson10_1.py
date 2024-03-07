def pow(x):
     return x ** 2

def some_gen(begin, end, func):
    for i in range(end):
         yield begin
         begin = func(begin)


print('OK')
