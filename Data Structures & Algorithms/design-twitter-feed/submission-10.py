import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.follow_graph: dict[int, set[int]] = {}
        self.tweets: dict[int, list] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [self.time, tweetId]
        self.time-=1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        if userId not in self.follow_graph:
            self.follow_graph[userId] = set()
        self.follow_graph[userId].add(userId)
        for followee in self.follow_graph[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(min_heap, [count, tweetId, followee, index - 1])
        
        while min_heap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(min_heap, [count, tweetId, followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_graph:
            self.follow_graph[followerId] = set()
        self.follow_graph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_graph:
            if followeeId in self.follow_graph[followerId]:
                self.follow_graph[followerId].remove(followeeId)
