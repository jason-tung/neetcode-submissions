class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(lambda: deque(maxlen=10))
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)
        candidates = [k for followed_id in self.following[userId] for k in self.posts[followed_id]]
        candidates.sort(key=lambda k: -k[0])
        return [k[1] for k in candidates[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
