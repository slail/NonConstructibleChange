'''
Non-Constructible Change
Given an array of positive integers representing the values of coins in your
possession, write a function that returns the minimum amount of change
the minimum sum of money) that you cannot create. The given coins can
have any positive integer value and aren't necessarily unique
(i.e., you can have multiple coins of the same value).
For example, if you're given coins = [1, 2, 5] ,
the minimum amount of change that you can't create is 4 .
If you're given no coins, the minimum amount of change that
you can't create is 1.
'''

# O(nlogn) Time | O(1) Space
def nonConstructibleChange(coins):
    coins.sort()
    current_balance = 0
    for coin in coins:
        if coin > current_balance + 1:
            return current_balance + 1
        current_balance += coin
    return current_balance + 1

print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))