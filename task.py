
import timeit

def find_coins_greed (sum):
    coins = [50, 10, 2, 1]
    res = {}

    for coin in coins:
        if sum >= coin:
            count = sum // coin
            sum -= coin * int(count)
            res[coin] = count
    return res


def find_min_coins (sum):
    coins = [50, 10, 2, 1]
    n = len(coins)
    result = {}

    min_coins = [float('inf')] * (sum + 1)    
    min_coins[0] = 0

    for coin in coins:        
        for x in range(coin, sum + 1):           
            if min_coins[x - coin] + 1 < min_coins[x]:          
                min_coins[x] = min_coins[x - coin] + 1
    
    if min_coins[sum] == float('inf'):
        return -1    

    for coin in sorted(coins, reverse=True):
        if sum == 0:
            break
        count = 0
        while sum >= coin and min_coins[sum - coin] == min_coins[sum] - 1:
            sum -= coin
            count += 1
        if count > 0:
            result[coin] = count

    return result
    

moneys = [35, 95, 115, 556, 1231, 55302]

for money in moneys:

    greed = find_coins_greed(money)
    dynamic = find_min_coins(money)

    find_coins_greed_time = timeit.timeit('find_coins_greed(money)', globals=globals(), number=100)
    find_coins_dynamic_time = timeit.timeit('find_min_coins(money)', globals=globals(), number=100)
    
    print(f'Час виконання функції жадібного підходу для суми монет {money} скадає {find_coins_greed_time}, а необхідна кількість монет {greed}')
    print(f'Час виконання функції динамічного підходу для суми монет {money} скадає {find_coins_dynamic_time}, а необхідна кількість монет {dynamic}')













