def Intro(): 

  print ("Hello! We are here to tell you the last closing price of the 15 stocks Yahoo Finance said are the best stocks to buy!")
  main()
def main():
  SandPTop15 = {'GE': 136.54, 'UNH': 510.23, 'ISRG': 383.77, 'BABA' : 71.85, 'V':277.18, 'CRM':125.97, 'MA':460.58, 'TMO':551.82, 'UBER':68.07, 'DHR': 246.33, 'NVDA':661.6, 'META':474.99, 'AMZN':171.81, 'MSFT':411.22, 'GOOGL':142.38 }
  stock = input("What stock price would you like to know? Please enter the ticker symbol. ")
  if stock in SandPTop15:
    print(SandPTop15[stock])
    print ("Enter another ticker or literally anything else to end")
  else:
    print("That is not one of the 15 they said are best stocks to buy! Try again")
    print()
    main()

Intro()

#code taken from my Intro To Programming course last year