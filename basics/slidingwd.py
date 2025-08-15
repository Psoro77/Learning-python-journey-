



def profitcalc(prices : list[int]) -> int :
    if len(prices)<2 :
                return 0
    profit = 0
    L= 0
    R = 1
    while(not R >= len(prices)):
                diff = prices[R]- prices[L]
                if diff < 0 :
                    L+=1
                else :
                    profit = max(diff, profit) 
                    R+=1
    return profit


prices = [5, 4, 6, 1, 3, 2]

print(profitcalc(prices))