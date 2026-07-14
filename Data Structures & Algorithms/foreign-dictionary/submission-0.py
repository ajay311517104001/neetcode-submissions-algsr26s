class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:set() for word in words for c in word}

        # return if there is prefix
        # if not update the directed graph

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        # tri color dfs
        res= []
        state = {c:0 for c in graph}

        def solve(c):
            if state[c] == 2:
                return True
            if state[c] == 1:
                return False
            
            state[c] = 1
            for n in graph[c]:
                if not solve(n):
                    return False
            state[c] = 2
            res.append(c)
            return True

        for c in graph:
            if not solve(c):
                return ""
        return "".join(reversed(res))

                

        