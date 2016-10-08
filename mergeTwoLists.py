__author__ = 'jonathanmares'


def mergeLists(list1,list2):
        if list1 == []:
            return list2
        if list2 == []:
            return list1
        list1 = list(reversed(list1))
        list2 = list(reversed(list2))
        newlist = []
        while list1 and list2:
            if list1[-1] < list2[-1]:
                newlist.append(list1[-1])
                list1.pop()
            else:
                newlist.append(list2[-1])
                list2.pop()
        while list2:
            newlist.append(list2[-1])
            list2.pop()
        while list1:
            newlist.append(list1[-1])
            list1.pop()
        return newlist

def main():
    list1  = [3,4,6,10,11,15]
    list2 = [1,5,8,12,14,19]
    print(mergeLists(list1,list2))

main()