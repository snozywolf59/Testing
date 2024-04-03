def fee(price: int, lv: int) -> int:
    if price < 100 or price > 400:
        return 0
    if lv > 3 or lv < 1:
        return 0
    while lv > 0:
        price = 2 * price
        lv = lv - 1
    return price


if __name__ == '__main__':
    p = 120
    lv = 3
    print(fee(p, lv))
