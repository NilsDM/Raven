import re

def symbol_cleaner(s):
    for i in s:
        if i == "$" or i == ".":
            return False
        else:
            return True

def count_match(s, symbol_count):
    if s in symbol_count:
        symbol_count[s] += 1
    else:
        symbol_count[s] = 1
    return symbol_count


def analyse(df, stocks):
    # column 9 contains comment body
    i = 0
    symbols = list(stocks.keys())
    symbol_count = {}
    while i < len(df): # for every row in data frame
        comment = df.iloc[i][9]
        for s in symbols: # for every stock name
            if symbol_cleaner(s):
                pattern = re.compile(r'{}'.format(s))
                matches = pattern.finditer(comment)
                for match in matches: # For every match found (do processing here)
                    symbol_count = count_match(s, symbol_count)
        #print(comment)
        i += 1
    #print(stocks[0])
    #print(symbol_count)
    for key in symbol_count:
        if key not in symbols:
            print("False")
            del symbol_count[key]
        else:
            print("good to go")
    print(symbol_count)
    print("okay")


def main():

    pass


if __name__ == "__main__":
    main()