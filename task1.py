# Створюємо функцію.
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount %= coin
    return result
# Виводимо результат.
print(find_coins_greedy(113))