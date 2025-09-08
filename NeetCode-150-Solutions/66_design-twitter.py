"""
Implement a simplified version of Twitter which allows users to post tweets,
follow/unfollow each other, and view the 10 most recent tweets within their own
news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:
- Twitter() Initializes the twitter object.
- void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by
the user userId. You may assume that each tweetId is unique.
- List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet
IDs in the user's news feed. Each item must be posted by users who the user is
following or by the user themself. Tweets IDs should be ordered from most recent
to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId
follows the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId
unfollows the user with ID followeeId.
"""


class Twitter:
    """
    The main challenge for this problem is the getNewsFeed implementation
    which involves returning the 10 most recent tweets posted either by the
    user itself or its followees.
    We can achieve that by building a heap data structure on-demand whenever
    requesting the feed. For each tweet posted by the user, and by its followees
    we add them to a max heap based on their posted timestamp and pop items
    when capacity exceeds 10 such that to always keep the 10 most recent in 
    the data structure.
    """

    def __init__(self):
        self.tweetCount = 0
        self.follows = {}  # key is the user, value is the set of his followees
        # key is the user, vlaue is a list of tweets i.e., (count, tweet)
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetCount += 1
        elem = (self.tweetCount, tweetId)

        if userId not in self.tweets:
            self.tweets[userId] = [elem]
        else:
            self.tweets[userId].append(elem)

    def getNewsFeed(self, userId: int) -> List[int]:
        recentTweets = []  # implemented as a min heap
        followees = list(self.follows.get(userId, set()))
        # treating the user itself as a followee when building the min heap
        followees.append(userId)

        for f in followees:
            if f in self.tweets:
                for c, t in self.tweets[f]:
                    # least recent tweet at the top (lowest c)
                    heapq.heappush(recentTweets, (c, t))

                    if len(recentTweets) > 10:
                        heapq.heappop(recentTweets)

        return [tweetId for _, tweetId in sorted(recentTweets, key=lambda data: -data[0])]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.follows:
                self.follows[followerId] = set([followeeId])
            else:
                self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and \
                followerId in self.follows and \
                followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
