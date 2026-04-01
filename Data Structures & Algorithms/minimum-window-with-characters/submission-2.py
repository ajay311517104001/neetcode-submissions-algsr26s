class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""


        t_map , window = {} ,{}
        for i in t:
            t_map[i] = t_map.get(i,0) + 1
        have , need = 0 , len(t_map)
        

        l =0
        res , reslen = [-1,-1] , float('+inf')
        for r in range(0,len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in t_map and window[c] == t_map[c]:
                have+=1
            
            while have == need:
                # update res
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                # decrement
                window[s[l]]-=1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have-=1
                l+=1
        return s[res[0]: res[1]+1] if reslen!= float('+inf') else ""




        