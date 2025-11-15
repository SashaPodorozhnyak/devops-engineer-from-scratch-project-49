def make_counter():
    count = 0  # переменная во внешней области видимости
    
    def counter():
        nonlocal count  # говорим, что используем переменную из внешней области
        count += 1
        return count
    
    return counter

print(make_counter())
print(make_counter())