class Twitter:

    def __init__(self):
        self.count = 0
        self.followermap = defaultdict(set)
        self.tweet = defaultdict(list)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.count , tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        heap = []
        res = []

        self.followermap[userId].add(userId)
        for followee in self.followermap[userId]:
            index = len(self.tweet[followee])-1
            if index>=0:
                count , tweetId = self.tweet[followee][index]
                heap.append([count , tweetId , followee , index -1])
        heapq.heapify(heap)
        while heap and len(res) < 10:
            count , tweetId , followee , index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                count , tweetId = self.tweet[followee][index]
                heapq.heappush(heap , [count , tweetId , followee , index -1])
        return res

                


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followermap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followermap[followerId] and followerId != followeeId:
            self.followermap[followerId].remove(followeeId)
        
