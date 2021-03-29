import re


def analyse(df, stocks):
    # column 9 contains comment body
    i = 0
    symbols = list(stocks.keys())
    print(symbols)
    while i < len(df): # for every row in data frame
        comment = df.iloc[i][9]
        for s in symbols: # for every stock name
            pattern = re.compile(r'{}'.format(s))
            matches = pattern.finditer(comment)
            for match in matches: # For every match found (do processing here)
                print(match)

        # print(comment)
        i += 1

    #print(stocks[0])
    print("okay")


def main():

    pass


if __name__ == "__main__":
    main()