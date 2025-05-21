# 1. Параметры функции

# function sumNumbers(a, b, c, d = 0, e = 0) {
#     return a + b + c + d + e;
# }

# // Пример использования:
# console.log(sumNumbers(1, 2, 3)); // 6 (1+2+3+0+0)
# console.log(sumNumbers(1, 2, 3, 4)); // 10 (1+2+3+4+0)
# console.log(sumNumbers(1, 2, 3, 4, 5)); // 15 (1+2+3+4+5)
# 2. Оператор return и возвращение результата

# function isEven(number) {
#     return number % 2 === 0
# }

# // Пример использования:
# console.log(isEven(4))
# console.log(isEven(7))
# 3. Функция как тип, параметр и результат другой функции

# function applyFunctionToArray(func, numbers) {
#     return numbers.map(func)
# }

# // Пример использования:
# const square = x => x * x
# const numbers = [1, 2, 3, 4]
# console.log(applyFunctionToArray(square, numbers))
# 4. Область видимости переменных

# let count = 0 

# if (true) {
#     let temp = 10
#     count += temp
#     console.log(temp) // выведет 10
# }

# console.log(count) // Работает выведет 10
# // console.log(temp) // Ошибка temp is not defined
# 5. Простой счётчик (замыкание)

# function createCounter() {
#     let count = 0
#     return function() {
#         return ++count
#     }
# }

# // Пример использования
# const counter = createCounter()
# console.log(counter())
# console.log(counter())
# console.log(counter())
