#
# Scrapes reddit for stock information and compiles into a data frame
#

import praw
import cred
import pandas as pd
import time
test_df = None


def build_reddit_data_frame():
    reddit = praw.Reddit(client_id=cred.c[0],
                         client_secret=cred.c[1],
                         user_agent=cred.c[2])

    # subreddits to scrape
    subreddits = ["CryptoTechnology",
                  "CryptoCurrency",
                  "CryptoMarkets",
                  "algotrading",
                  "altcoin",
                  "NFT"]

    #, "Pennystocks", "StockMarket", "Stocks",
    #"Crypto", "Wallstreetbets", "GME", "EconMonitor",
    #"SecurityAnalysis", "Accounting", "Finance", "Options", "algotrading"]

    # attributes from post, author, comments

    column_names = ["subreddit",
                    "post_name",
                    "author_name",
                    "time_created",
                    "num_comments",
                    "karma",
                    "karma_ratio",
                    "comment",
                    "comment_time",
                    "comment_karma"]

    df = pd.DataFrame(columns=column_names)

    for s in subreddits:
        posts = reddit.subreddit(s).hot(limit=25) # grab top n posts
        for p in posts:
            # Skip over stickied posts
            if p.stickied == False:
                submission = reddit.submission(id=p.id)  # get comments
                submission.comments.replace_more(limit=0)  # removes all more comments/Continue buttons
                for c in submission.comments.list():  # for every comment in post 
                    try: # Exception for deleted comments
                        entry = {"subreddit": s,  # data frame row
                                 "post_name": submission.title,
                                 "author_name": submission.author.name,
                                 "time_created": submission.created_utc,
                                 "num_comments": submission.num_comments,
                                 "karma": submission.score,
                                 "karma_ratio": submission.upvote_ratio,
                                 "comment": c.body,
                                 "comment_time": c.created_utc,
                                 "comment_karma": c.score}
                        # df = df.concat(entry, ignore_index=True)   
                        df.loc[len(df)]  = entry
                    except AttributeError:  
                        continue


    # Output
    print("df shape: ", df.shape)
    today_date = time.strftime("%m-%d-%Y")
    base_path = r'/mnt/c/Users/nilsm/Dropbox/Projects/Raven/data_dumps/'
    extension = ".csv"
    full_path = base_path + "data_" + today_date + extension
    df.to_csv(full_path)
    global test_df
    test_df = df
    return df


def main():
    print("df shape: ", test_df.shape)
    subreddits = test_df["subreddit"]
    print(set(subreddits))


if __name__ == "__main__":
    main()