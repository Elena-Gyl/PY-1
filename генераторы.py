"""Функция - генератор"""

def gen(n):
    i = 0
    while i < n:
        i+=1
        yield i # не return (завершает)
        # передает значение и ждет обращения в след раз

res = gen(5)
print(res) # <generator object gen at 0x000002188FB15A80>
# возвращает только одно значение
# ориентир на экономию памяти
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
#print(next(res))

""" Выражение - генератор"""
result = (i for i in range(5))
print(result) # <generator object <genexpr> at 0x000001E5DB2359C0>

