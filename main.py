
import reddit_tractor_beam as rtb
import comment_blender as cb


def main():
    data = rtb.build_reddit_data_frame() # Scrape reddit
    comment_data = cb.analyse(data)


    # reddit = praw.Reddit(client_id=cred.c[0],
    #                      client_secret=cred.c[1],
    #                      user_agent=cred.c[2])
    #
    # subreddits = ["Investing","Pennystocks", "StockMarket", "Stocks",
    #               "Crypto", "Wallstreetbets", "GME", "EconMonitor",
    #               "SecurityAnalysis", "Accounting", "Finance", "Options",
    #               "algotrading"]
    # column_names = ["subreddit",
    #                 "post_name", "author_name",
    #                 "time_created", "num_comments",
    #                 "karma", "karma_ratio"
    #                          "comment", "comment_time", "comment_karma"]
    # df = pd.DataFrame(columns=column_names)
    # for s in subreddits:
    #     posts = reddit.subreddit(s).hot(limit=10)
    #     for p in posts:
    #         submission = reddit.submission(id=p.id)  # get comments
    #         submission.comments.replace_more(limit=0)  # removes all more comments/Continue buttons
    #         for c in submission.comments.list():  # for every comment in post
    #             entry = {"subreddit": s,
    #                      "post_name": submission.title,
    #                      "author_name": submission.author.name,
    #                      "time_created": submission.created_utc,
    #                      "num_comments": submission.num_comments,
    #                      "karma": submission.score,
    #                      "karma_ratio": submission.upvote_ratio,
    #                      "comment": c.body,
    #                      "comment_time": c.created_utc,
    #                      "comment_karma": c.score}
    #             df = df.append(entry, ignore_index=True)
    # print("df shape: ", df.shape)
    # df.to_csv("data.csv")
    # a = df["subreddit"]
    # print(set(a))
    #
    # # hot_posts = reddit.subreddit("Stocks").hot(limit=1)
    # # for p in hot_posts:
    # #     ids.append(p.id)
    # # print(ids)
    #
    # # Printout ids for top 10 current posts
    # # ids = []
    # # hot_posts = reddit.subreddit("Stocks").hot(limit=10)
    # # for p in hot_posts:
    # #     ids.append(p.id) # get IDs
    # # #print(ids)
    #
    # # submission = reddit.submission(id = ids[0])  # get comments for post ID
    # # #print(submission.comments[0].body)
    # # # print( submission.title)
    # # # for t  in submission.comments:
    # # #     print(t.body)
    # #
    # # # posts = []
    # # # ml_subreddit = reddit.subreddit('MachineLearning')
    # # # for post in ml_subreddit.hot(limit=10):
    # # #     posts.append(
    # # #         [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    # # # posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    # # # print(posts)
    # #
    # # submission.comments.replace_more(limit=0) # removes all more comments/Continue buttons
    # # for comment in submission.comments.list():
    # #     print(comment.author.comment_karma)
    # #     print(comment.created_utc)

    print("okay")


if __name__ == "__main__":
    main()
