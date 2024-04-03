import unittest


def fee(price: int, lv: int) -> int:    #1
    if price < 100 or price > 400:      #2
        return 0                        #3
    if lv > 3 or lv < 0:                #4
        return 0                        #5
    while lv > 0:                       #6
        price = 2 * price               #7
        lv = lv - 1                     #8
    return price/2                      #9


class TestFee(unittest.TestCase):
    def test_T00(self):
        self.assertEqual(fee(10, 0), 0)

    def test_T01(self):
        self.assertEqual(fee(150, 5), 0)

    def test_T02(self):
        self.assertEqual(fee(200, 0), 100)

    def test_T03(self):
        self.assertEqual(fee(320, 1), 320)

    def test_T04(self):
        self.assertEqual(fee(250, 2), 500)


if __name__ == '__main__':
    unittest.main()
