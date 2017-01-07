from itertools import permutations

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ['0:00']
        if num > 10:
            return ['0:00']
        
        
        minute_num = 0
        
        if num > 4:
            minute_num = num - 4
            num = 4
        
        answer = []
        
        while (num >= 0) and (minute_num<7):

            hours = list(set([int(''.join(map(str,z)), 2) for z in permutations(num*[1] + (4-num)*[0])]))
            minutes = list(set([int(''.join(map(str,z)), 2) for z in permutations(minute_num*[1] + (6-minute_num)*[0])]))

            for hour in hours:
                for minute in minutes:
                    if (hour < 13) and (minute < 60):
                        
                        out_str = ''
                        out_str+=str(hour)
                        out_str+=':'
                        
                        if len(str(minute))<2:
                            out_str+='0'
                        out_str+=str(minute)
                        
                        answer.append(out_str)
            
            num-=1
            minute_num+=1
        
        answer.sort()
        return answer


if __name__ == "__main__":
    sol = Solution()
    print sol.readBinaryWatch(2)