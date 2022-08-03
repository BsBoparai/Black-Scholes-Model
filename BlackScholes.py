import math
import scipy.stats as st
from matplotlib import pyplot as plt

def blackScholes(SP, EP, T, Vol, RFR):
    x = st.norm.cdf(D1(SP, EP, T, Vol, RFR))
    y = st.norm.cdf(D2(st.norm.ppf(x), Vol, T))
    z = (SP)*(x)-(EP)/(pow(math.e, RFR*(T/360)))*y
    return z


def D1(SP, EP, T, Vol, RFR):
    x = (math.log(SP/EP)+(RFR+0.5*(Vol**2))*(T/365))/(Vol*math.sqrt(T/365))
    return x 

def D2(D_1, Vol, T):
    x = D_1 - Vol*math.sqrt(T/365)
    return x

def get_PL(SP, EP, T, Vol, RFR, rnge, PP):
    PL = [[], []]
    TP = round(SP*(1+rnge))
    BP = round(SP*(1-rnge))
    if BP <= 0:
        BP = 1
    for i in range(BP, TP):
        PL[0].append(i)
        p = round(blackScholes(i, EP, T, Vol, RFR) - PP, 2)
        PL[1].append(p)
    return PL

def create_chart(a):
    plt.plot(a[0], a[1])
    plt.xlabel('Underlying Stock Price($)')
    plt.ylabel('Profit or Loss($)')
    plt.show()

def main():
    q = float(input("What is the current underlying stock price? "))
    w = float(input("What is the option strike price? "))
    e = float(input("How many days until experation? "))
    r = float(input("input the IV(as a decimal) "))
    t = float(input("input the current Risk Free Rate(as a decimal) "))
    y = float(input("input the potential price movement range(as a decimal) "))
    u = float(input("input the option purchase price "))
    PL = get_PL(q, w, e, r, t, y, u)
    create_chart(PL)

main()