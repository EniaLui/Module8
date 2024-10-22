def add_everything_up(a: (str, float, int), b: (str, float, int)):
    try:
        return a + b
    except TypeError:
       return f'{a}{b}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.457, 7))

