class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        substrings = []
        maxLength = 0
        maxPalindrome = ""
        for idx, c in enumerate(s):
            current = [c]
            substrings.append(current)
            for c2 in s[idx+1:]:
                current = current + [c2]
                substrings.append(current)
        
        for s in substrings:
            if self.isPalindrome(s):
                if maxLength < len(s):
                    maxLength = len(s)
                    maxPalindrome = ''.join(s)
                
        
        
        return maxPalindrome
        
    def isPalindrome(s):
        if len(s) == 1:
            return True

        for x in range(0, len(s)/2):
            if s[x] != s[-x-1]:
                return False
        else:
            return True


if __name__ == "__main__":
    solution = Solution()
    test = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print solution.longestPalindrome(test)
