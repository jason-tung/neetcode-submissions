class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(lambda: deque(maxlen=10))
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        
    # better than editorial solution. instead of building k size heap
    # we should heapify and pop k
    # heapifying is so cheap don't need to do kn inserts at log k
    # total: kn logk
    # kn to build entire heap + k log kn but slightly more space at kn
    # total: kn + k log kn, k log kn < kn log k 
    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)
        candidates = [k for followed_id in self.following[userId] for k in self.posts[followed_id]]
        heapq.heapify_max(candidates)
        res = []
        for _ in range(10):
            if candidates:
                res.append(heapq.heappop_max(candidates)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
