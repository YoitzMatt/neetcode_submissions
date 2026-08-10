class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        m_v = {}
        ret_val = [[] for i in range(len(nums) + 1)]
        # keep track of how many occurences of an element there are 
        for i in nums:
            m_v[i] = 1 + m_v.get(i,0)  
        for n_items, c_count in m_v.items(): # gives every key value pair 
            ret_val[c_count].append(n_items)
        
        ret = []
        for i in range(len(ret_val) -1, 0, -1):
            for n in ret_val[i]:
                ret.append(n)
                if(len(ret) == k):
                    return ret 