def rotateLetter(c, amount):
    
    cAsNum = ord(c)
    
    
    # deal with wrap around
    if (ord(c.lower()) - amount) < 97:
        # if capital
        if cAsNum <= 90:
            return chr( ord('Z') - (amount - (cAsNum - ord('A')) - 1) )
            
        
        
        # if lowercase
        else:
            return chr( ord('z') - (amount - (cAsNum - ord('a')) -1)  )
            
        
    
    return chr(ord(c) - amount)



if __name__ == "__main__":
    print rotateLetter('A', 3)
