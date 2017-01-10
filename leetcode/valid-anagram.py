from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
            
        d = defaultdict(lambda: 0)
        
        # count characters
        for c in s:
            d[c] += 1
        
        # reverse count
        for c in t:
            d[c] -= 1
        items = d.items()
    
        # if any of the keys map to a nonzero value, then one of the words
        # either contains fewer characters or has a different number of
        # each character
        for key, value in items:
            if value != 0:
                return False
        else:
            return True
        
            
        
        # return set(s) == set(t) and len(s) == len(t)
        