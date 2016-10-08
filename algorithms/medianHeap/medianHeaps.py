from heapq import *

def medianHeap(n, numbers):
    #n = int(raw_input().strip())
    medians = []
    maxHeap = []
    minHeap = []
    a = numbers[0]
    b = numbers[1]
    heappush(maxHeap, -1*min(a,b) )
    #print a
    medians.append(a)
    medians.append((a+b)/2)
    #print (a+b)/2.
    heappush(minHeap, max(a,b) )
    

    for x in range(2,n):
        num = numbers[x]
        
        if num < -1*maxHeap[0]:
            heappush(maxHeap, -1*num)
            
        else:
            heappush(minHeap, num)
        
        if len(maxHeap) - len(minHeap) > 1:
            element = -1*heappop(maxHeap)
            heappush(minHeap, element)
            res = (-1*maxHeap[0] + minHeap[0])/2.
            medians.append(res)
            
        elif len(maxHeap) - len(minHeap) < -1:
            element = heappop(minHeap)
            heappush(maxHeap, -1*element)
            res = (-1*maxHeap[0] + minHeap[0])/2.
            medians.append(res)

        else:
            if len(minHeap) > len(maxHeap):
                #print minHeap[0]
                medians.append(minHeap[0])
            elif len(minHeap) < len(maxHeap):
                medians.append(-1*maxHeap[0])

            else:
                #print -1*maxHeap[0]
                res = (-1*maxHeap[0] + minHeap[0])/2.
                medians.append(res)

                

        print "current number: {0}".format(num)

        print "Max Heap: {0}".format(maxHeap)

        print "Min Heap: {0}".format(minHeap)
        

    return medians  

    
def main():
    f = open('input1.txt','r')
    f2 = open('output1.txt','r')
    input = [float(x) for x in f.read().splitlines()][1:10+1]
    ourOutput = medianHeap(len(input), input)
    output = [float(x) for x in f2.read().splitlines()][0:9+1]
    print ourOutput
    print output
    if ourOutput == output:
        print "correct"
    else:
        print "wrong"


main()
    
        
    
