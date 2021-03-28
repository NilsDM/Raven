
def stock_name_parser():
    stock_symbols = []
    stock_names = []

    # Extract all stock names and symbols from NASDAQ
    nasdaq = open("nasdaqlisted.txt", mode = "r")
    n_line = nasdaq.readlines()
    for line in n_line:
        curr = line.split('|')
        stock_symbols.append(curr[0])
        stock_name = (curr[1].split(","))
        stock_names.append(stock_name[0])
    nasdaq.close()

    # Extract all stock names and symbols from Other listed
    other = open("otherlisted.txt", mode = "r")
    o_line = other.readlines()
    for line in o_line:
        curr = line.split('|')
        stock_symbols.append(curr[0])
        stock_name = (curr[1].split(","))
        stock_names.append(stock_name[0])
    other.close()

    # make stock dictionary key[stock_symbol] = val[stock_name]
    i = 0
    stocks_dict = {}
    while i < len(stock_names):
        stocks_dict[stock_symbols[i]] = stock_names[i]
        i += 1

    return stocks_dict




def main():
    stock_name_parser()
    print("ok")


if __name__ == "__main__":
    main()
