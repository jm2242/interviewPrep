__author__ = 'jonathanmares'
import random









#My version of inplace quicksort using left/right method, unfinished. Doesn't work.
def quickSortAlternate(lst):
    if len(lst)==1:
        return lst
    elif len(lst)==0:
        return lst
    else:
             #p = random.randrange(0,len(lst),1)
        left = 0
        right = len(lst)-1
        p = right
        print("unsorted list:", lst)
        print("length of list: ", len(lst))
        print("index of partition is:", p)
        print("partition is: ",lst[p])
        print("setting right bound to: " + str(right))
        while left <= right:
            while lst[left] < lst[p]:
                left += 1
            while lst[right] > lst[p]:
                right -= 1
            if left <= right:
                print("swapping the " + str(left) + "th " + "index with the " + str(right) + "th " + "index")
                temp = lst[left]
                lst[left] = lst[right]
                lst[right] = temp
                print("swap step: ", lst)
                left +=1
                right -=1
            print("left is:", left)
            print("right is:", right)



#print(quickSort([0,3,2,1,10,5,8]))

#quicksort from rosettaCode. Not sure how the quicksort recursive part works, specifically how
#array is returned, since the function doesn't seem to return anything.
def quicksort(array):
    return _quicksort(array, 0, len(array) - 1)
def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        _quicksort(array, start, right)
        _quicksort(array, left, stop)




def insertionSort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 0:
        return None
    else:
        sortedList = [lst.pop()]
        #print("The sorted list is:", sortedList)
        #While the unsorted list is not empty
        #print("the length of the original unsorted list is:", len(lst))
        #print("the original unsorted list is:",lst)
        while len(lst) > 0:
            #Pop off the last element from the unsorted list
            curElem = lst.pop()
            #print("the current element is:", curElem)
            #print("the unsorted list is:", lst)
            #Loop through sorted list, find where to place it
            for x in range(0,len(sortedList)):
                if curElem < sortedList[x]:
                    sortedList.insert(x,curElem)
                    print("The sorted list is now:", sortedList)
                    break
                #place current element at the end of the list if it is the largest
                if x==len(sortedList)-1:
                    sortedList.append(curElem)
                    print("The sorted list is now:", sortedList)
        return sortedList

#print(insertionSort([4,3,2,16,5,4,5,100,57,90]))


# looks like this works
# I think you can actually do this without using a merged [], cause you can overwrite the input lst
def mergeSort(lst):
    print("Calling Merge sort with" + str(lst))
    if len(lst) <= 1:
        return lst
    mid = int(len(lst) / 2)
    # recursive calls
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    l=0
    r=0
    merged = []
    while (l<=len(left)-1 and r<=len(right)-1):
        if left[l] <= right[r]:
            merged.append(left[l])
            l+=1
        else:
            merged.append(right[r])
            r+=1

    #glue the rest of either the left or right to merged
    if l <= len(left)-1:
        merged = merged + left[l:]

    if r <= len(right) - 1:
        merged = merged + right[r:]

    return merged

def main():
    print(mergeSort([54,26,93,17,77,31,44,55,20]))

main()




# testList = [1,2,3,4]
# curElem = testList.pop()
# print(testList)
#
#















