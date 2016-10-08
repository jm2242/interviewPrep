__author__ = 'jonathanmares'


def robot(m,r,c):
    print(r,c)
    # if we've reached the end, return the path
    if r==len(m)-1 and c==len(m[0])-1:
        return True

    # going down
    try:
        if m[r+1][c]:
            #p.add((r+1,c))
            #print(p)
            robot(m,r+1,c)
    except:
        pass
    # going right
    try:
        if m[r][c+1]:
            #p.add((r,c+1))
            #print(p)
            robot(m,r,c+1)
    except:
        pass

    return False


def main():
    m = [[True,True,True,True],[True,True,True,True],[True,True,True,True]]
    p = set()
    print(robot(m,0,0))



main()

