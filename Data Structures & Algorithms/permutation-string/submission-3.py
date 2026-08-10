class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): 
            return False 


        freq1 = {}
        for i in range(len(s1)):
            if s1[i] in freq1:
                freq1[s1[i]] += 1
            else:
                freq1[s1[i]] = 1 

        l = 0
        r = len(s1)
        while r <= len(s2):
            curr = s2[l:r]
            freq2 = {}
            for i in range(len(curr)):
                if curr[i] in freq2:
                    freq2[curr[i]] += 1
                else:
                    freq2[curr[i]] = 1 
            
            print(freq1)
            print(freq2)
            if freq2 == freq1:
                return True
            l += 1 
            r += 1
        return False 