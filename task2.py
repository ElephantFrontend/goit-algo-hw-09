# Створюємо функцію.
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    # Таблиця для мінімільної кількості монет для кожної суми від 0 до amount.
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 # 0 монет для суми 0

    # Заповнення таблиці dp.
    for coin in coins:
        for x in range(coin, amount +1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] +1

    # Відновлення набору монет з таблиці dp.
    result = {}
    current = amount
    while current > 0:
        for coin in coins:
            if current >= coin and dp[current - coin] == dp[current] - 1:
                result[coin] = result.get(coin, 0) +1
                current -= coin
                break
    return result

# Виводимо результат.
print(find_min_coins(113))