
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0: return 0
        elif n == 1: return 1
        elif n in cache: return cache[n] #Повертаємо значення з кешу, якщо воно вже є

        #Pекурсивне обчислення
        result = fibonacci(n-1) + fibonacci(n-2) 
        cache[n] = result  # Зберігаємо результат у кеш
        return result
    return fibonacci

fib = caching_fibonacci()
print(fib(1))
print(fib(10))
print(fib(15))