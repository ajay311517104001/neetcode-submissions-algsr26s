class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = {}
        for k in tasks:
            hmap[k]= hmap.get(k , 0) +1
        maxHeap = [ -v for v in hmap.values()]
        heapq.heapify(maxHeap)

        que = deque()

        time = 0

        while maxHeap or que:
            time+=1

            if maxHeap:
                bal = 1 + heapq.heappop(maxHeap)
                if bal:
                    que.append([bal , time+n])
                
            if que and  time == que[0][1]:
                heapq.heappush(maxHeap , que.popleft()[0])
        return time