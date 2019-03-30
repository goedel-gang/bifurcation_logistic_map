import decimal

from time import sleep

def logi_map(x_n, r):
    return r * x_n * (1 - x_n)

def stable_points(prec, f):
    decimal.getcontext().prec = prec
    x = decimal.Decimal(0.5)
    seen = set()
    while x not in seen:
        seen.add(x)
        x = f(x)
    endpoint = x
    x = f(x)
    osc = [x]
    while x != endpoint:
        x = f(x)
        osc.append(x)
    return osc

if __name__ == "__main__":
    for r in range(24, 35):
        print(0.1 * r, stable_points(6, lambda x: logi_map(x, decimal.Decimal(0.1 * r))))
