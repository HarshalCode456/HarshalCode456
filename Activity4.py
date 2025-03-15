actualpay=float(input("How much will you buy an apple for? ="))
saleamount=float(input("How much will you sell it for?="))
amount=saleamount-actualpay
if actualpay > saleamount:
    print("There is a loss")
else:
    print(amount,"That is your profit")
