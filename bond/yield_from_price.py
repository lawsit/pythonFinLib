import argparse
import math
 
 # Calculate Bond Yield through trial-and-error.
'''
Solving the equation by hand requires an understanding of the relationship between a bond’s price and its yield, 
as well as of the different types of bond pricings. Bonds can be priced at a discount, at par and at a premium. 
When the bond is priced at par, the bond’s interest rate is equal to its coupon rate. A bond priced above par 
(called a premium bond) has a coupon rate higher than the interest rate, and a bond priced below par 
(called a discount bond) has a coupon rate lower than the interest rate. So if an investor were calculating 
YTM on a bond priced below par, he or she would solve the equation by plugging in various annual interest rates 
that were higher than the coupon rate until finding a bond price close to the price of the bond in question 
(quote from: Investopedia).
'''


 
def total_present_value(face_value, coupon, periods, rate):
    total_pv = 0
    for n in range(1, periods+1):
        total_pv += coupon / math.pow((1 + rate), n)
 
    total_pv += face_value / math.pow((1 + rate), periods)
 
    return total_pv
    
 
def yield_from_price():   
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=float, help='specifies the current price')
    parser.add_argument('-f', type=float, default=1000, help='specifies the face Value')
    parser.add_argument('-r', type=float, default=5, help='specifies the annual coupon rate in %')
    parser.add_argument('-y', type=int, default=15, help='specifies the number of years remaining to maturity')
    parser.add_argument('-s', action='store_true', default=False, help='coupon is a semi-annual coupon. Default is annual')
    args = parser.parse_args()
    print (args)
 
    coupon_rate = args.r / 100.0
    coupon = args.f * coupon_rate
    factor = 2 if args.s else 1
 
    print("------------------------------------------------")
    print("Price: %s" % args.p)
    print("Face Value: %s" % args.f)
    print("Annual coupon rate: %.2f%%" % args.r)
    print("Coupon: %s" % coupon)
    print("Semi-annual coupon: %s" % args.s)
    print("Years remaining: %s" % args.y)
    print("\n")
 
 
    ytm = coupon_rate
    condition = True
    while condition:
        if (args.p < args.f):
            ytm += 0.00001
        else:
            ytm -= 0.00001
 
        total_pv = total_present_value(args.f, coupon/factor, args.y*factor, ytm/factor)
 
        if (args.p < args.f):
            condition = total_pv > args.p
        else:
            condition = total_pv < args.p
 
    print("Yield to Maturity:  %.2f%%" % (ytm*100.0))
 
 
if __name__ == '__main__':
     yield_from_price()
     #python yield_from_price.py -p 139.87 -f 99.94 -r 6.250 -y 12 -s