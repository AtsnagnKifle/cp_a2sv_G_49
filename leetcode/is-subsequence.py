class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ind = 0
        t_ind = 0
        while s_ind<len(s) and t_ind<len(t):
            if s[s_ind]==t[t_ind]:
                s_ind+=1
                t_ind+=1
            else:
                t_ind+=1
        if s_ind==len(s):
            return True
        else:
            return False