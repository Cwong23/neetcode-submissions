class User:
    def __init__(self):
        self.tweets = [] # list
        self.following = set()


class Twitter:
    def __init__(self):
        self.users = {}
        self.timestamp = 0

    def createUser(self, userId: int) -> None:
        self.users[userId] = User()
        self.follow(userId, userId)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # O(1)
        if userId not in self.users:
            self.createUser(userId)
        self.users[userId].tweets.append([-self.timestamp, tweetId])
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # only gets up to 10 tweets
        # O(nlogn)
        tweets = []
        for followee in self.users[userId].following:
            tweets.extend(self.users[followee].tweets)
        heapq.heapify(tweets)

        res = []
        for i in range(min(10, len(tweets))):
            res.append(heapq.heappop(tweets)[1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        # O(1)
        if followerId not in self.users:
            self.createUser(followerId)
        if followeeId not in self.users:
            self.createUser(followeeId)
        self.users[followerId].following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # O(1)
        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)
        
