
import reddit_tractor_beam as rtb
import stock_name_tractor_beam as stb
import comment_blender as cb


def main():
    reddit_data = rtb.build_reddit_data_frame() # Scrape reddit
    stock_data = stb.stock_name_parser()
    comment_data = cb.analyse(reddit_data, stock_data)

    print("okay")


if __name__ == "__main__":
    main()
