class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        ans = []
        for ind,ch in enumerate(s):
            if ch in d:
                d[ch][1] = ind
            else:
                d[ch] = [ind,ind]
        st = -1
        end = -1
        print(d)
        for ch1
            if st==-1:
                st = d[ch][0]
                end  = d[ch][1]
            else:
                if end < d[ch][0]:
                    ans.append(end+1-st)
                    st = d[ch][0] 
                    end = d[ch][1]
                elif st <= d[ch][0] and end < d[ch][1]:
                    end =  d[ch][1]
        ans.append(end-st+1)
        return ans
        