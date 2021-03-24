import webbrowser as wb
import time
import requests
import bs4
import selenium


def main():
    wb.open("https://www.reddit.com/r/stocks")
    # time.sleep()
    res = requests.get("https://www.reddit.com/r/stocks")
    # print(requests.status_codes)
    # res.raise_for_status()
    print(len(res.text))
    print(res.text[:2500])


if __name__ == "__main__":
    main()
