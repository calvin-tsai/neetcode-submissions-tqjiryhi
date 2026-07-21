class Twitter:

    def __init__(self):
        # map between userID (follower) and followee list
        #    -> what users is this user following? useful for feed

        # map between userID and tweetID and time

        # time (wall clock) that increments globally

        self.followers = defaultdict(set)

        # {userID : [(time, tweetid), (time, tweetid)]}
        self.tweets = defaultdict(list)

        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # get all tweets by user and user's followers and put them in a list
        # sort by time 
        # output just tweetId
        allTweets = self.tweets[userId][:]
        for followee in self.followers[userId]:
            allTweets.extend(self.tweets[followee])

        allTweets.sort(key=lambda x: -x[0]) # sorts by first item, which is time

        return [j for _, j in allTweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        # add follower to the users follow list
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove follower from the user's follower list
        self.followers[followerId].discard(followeeId)