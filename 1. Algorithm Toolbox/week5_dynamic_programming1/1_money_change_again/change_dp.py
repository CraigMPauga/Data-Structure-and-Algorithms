# Uses python3
import sys

def get_change(m):
    #write your code here
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        pass

def DPChange(money,coins):

    minNumCoins = [None]*(money+1)
    minNumCoins[0] = 0

    for m in range(1,money+1):
        minNumCoins[m] = 10**3 + 1
        for i in range(1,len(coins)):
            if m>=coins[i]:
                NumCoins = minNumCoins[m-coins[i]] + 1
                if NumCoins < minNumCoins[m]:
                    minNumCoins[m] = NumCoins
    return minNumCoins[money]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    coins = [0,1,3,4]
    print(DPChange(m,coins))
