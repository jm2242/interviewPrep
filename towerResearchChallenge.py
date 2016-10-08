__author__ = 'jonathanmares'


def  findingDigits(foo):

    for num in foo:
        totaldigits = 0
        for digit in [int(x) for x in str(num)]:
            try:
                if num % digit == 0:
                    totaldigits += 1
            except:
                pass
        print(totaldigits)



#findingDigits([12,1012])

def findmissing(nums):
    for x in range(0,len(nums)):
        if x==0:
            if nums[1] - nums[0] < nums[2] - nums[1]:
                return int((nums[2] - nums[1])/2 + nums[1])

            elif nums[1] - nums[0] == nums[2] - nums[1]:
                difference = nums[1] - nums[0]
            else:
                return int((nums[1] - nums[0])/2 + nums[0])
        else:
            if nums[x] - nums[x-1] != difference:
                return int((nums[x] - nums[x-1])/2 + nums[x-1])
#print(findmissing([1,5,7,9,11]))

def similarities(string):
    totalsum = 0
    for x in range(0,len(string)):
        suffix = string[x:]
        current_sum = 0
        for y in range(0,len(suffix)):
            if string[y] == suffix[y]:
                current_sum += 1
            else:
                break
        totalsum +=current_sum
    return totalsum

#print(similarities("aa"))


def collatz(bound, k):

    for n in range(1,bound+1):
        steps = 0
        originalnumber = n
        while n>1:
            steps +=1
            if n % 2 == 1:
                n = 3*n + 1
            else:
                n = n / 2
        if steps <= k:
            print(originalnumber)

#collatz(10,3)

def trading(stocks):
    max_profit = 0
    for y in range(0,len(stocks)-1):
        buy = y
        sellmax = y + 1
        current_profit = 0
        for minute in range(y,len(stocks)):
            if stocks[minute] - stocks[buy] > current_profit:
                sellmax = minute
                current_profit = stocks[minute] - stocks[y]

        if current_profit < 0:
            pass
        else:
            print("buy at ", buy, " sell at ", sellmax)
            print("current profit is: ", current_profit)
            max_profit += current_profit
            print("max profit so far is :", max_profit)
    return max_profit

def main():
    print(trading([5,3,2]))


