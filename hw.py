
def HW():
    # Implement a Python program that it will take the following inputs:
    print("HW Python STOCK PROFIT CALCULATOR - Individual Homework")
    # A stock symbol
    print("Enter Stock Symbol:")
    stockSymbol = input()
    # Allotment (number of shares)
    print("Enter Allotment (number of shares):")
    noOfShares= int(input())
    # Final share price (in dollars)
    print("Enter Final share price(in dollars):")
    sharePrice= float(input())
    # Sell commission (in dollars)
    print("Enter Sell commission (in dollars):")
    sellComm = float(input())
    # Inital share price (in dollars)
    print("Enter Inital share price (in dollars):")
    initSharePrice = float(input())
    # Buy commission (in dollars)
    print("Enter buy commission (in dollars):")
    buyComm= float(input())
    # Captial gain tax rate (in %)
    print("Enter gain tax rate (in %)")
    taxRate= float(input())

    # Output the following items after computation:
    print("After computation:")

    # Proceeds (Allotment x Final share price)
    proceeds = noOfShares*sharePrice
    print("Proceeds: $", proceeds)

    # Cost (Allotment x Initial Share Price + commissions + Tax on Capital Gain)
    init_cost= noOfShares*initSharePrice + sellComm + buyComm
    cost_ex = (proceeds-init_cost)*(taxRate/100)
    cost = init_cost + cost_ex
    print("Costs: $", cost)

    # Net Profit (in dollars)
    profit = proceeds - cost
    print("Net profit: $", profit)

    # Return on investment (in %)
    roi= (profit/cost) * 100 
    print("Return on investment: %", roi)

    # Break even price (in dollars)
    breakEven = init_cost/noOfShares
    print("Break even: $", breakEven)

HW()


