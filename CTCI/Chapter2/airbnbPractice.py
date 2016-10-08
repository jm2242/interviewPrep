__author__ = 'jonathanmares'



def printSpiral(M, y, x):
    numberOfElements = x * y

    r= 0
    c = 0
    left= False
    up = False
    down = False
    right = True
    visited = []
    for col in range(0,y):
        visited.append(x * [False])

    for i in range(0,numberOfElements+25):
        print('itteration: ' + str(i))
        print('row: ' + str(r) + ", col: " + str(c))
        if r>=0 and r<y and c>=0 and c<x:
            if not visited[r][c]:
                visited[r][c] = True
                print(M[r][c])

            # we've hit a visited element, so time to change direction
            else:
                print('We have visited row: ' + str(r) + ", col: " + str(c))
                if right:
                    c = c - 1
                    down = True
                    right = False
                elif down:
                    r = r - 1
                    down = False
                    left = True
                elif up:
                    r = r + 1
                    up = False
                    right = True
                elif left:
                    c = c + 1
                    left = False
                    up = True
            if right:
                c = c + 1
            elif left:
                c = c -1
            elif down:
                r = r+ 1
            else:
                r = r - 1
        else:
            if right:
                c = c - 1
                r = r + 1
                down = True
                right = False
            elif down:
                r = r - 1
                c = c - 1
                down = False
                left = True
            elif up:
                r = r + 1
                c = c + 1
                up = False
                right = True
            elif left:
                c = c + 1
                r = r - 1
                left = False
                up = True



def main():
    M = []
    M.append([1,2,3,4])
    M.append([5,6,7,8])
    M.append([9,10,11,12])
    #printSpiral(M,3, 4) # inputs: Matrix, rows, cols
    #matrix = [[0 for i in range(5)] for j in range(6)]
    print(matrix)
main()