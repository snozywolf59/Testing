# Loại khách: V
# Giá tiền: P
import unittest


def thanhToan(v, p):
    if p <= 0:                              #1
        return 'Hoa don khong hop le!'      #2
    if p > 5000:                            #3
        return 'Hoa don khong hop le!'      #4
    if not v:                               #5
        if p < 100:                         #6
            return 'Khong uu dai'           #7
        if p < 1000:                        #8
            return 'Giam 5%'                #9
        return 'Giam 5%, tang voucher'      #10
    if p < 100:                             #11
        return 'Tang voucher'               #12
    if p < 1000:                            #13
        return 'Giam 5%, tang voucher'      #14
    return 'Giam 10%, tang voucher'         #15


class TestThanhToan(unittest.TestCase):
    def less_than_zero(self):      #1T - 2
        self.assertEqual(
            thanhToan(False, -10),
            "Hoa don khong hop le!"
        )

    def more_than_five_thousand(self): #1F - 3T - 4
        self.assertEqual(
            thanhToan(True, 5010),
            'Hoa don khong hop le!'
        )

    def not_vip_less_than_hundred(self): #1F - 3F - 5T - 6T - 7
        self.assertEqual(
            thanhToan(False, 80),
            'Khong uu dai'
        )

    def not_vip_less_than_thousand(self): #1F - 3F - 5T - 6F - 8T - 9
        self.assertEqual(
            thanhToan(False, 720),
            'Giam 5%'
        )

    def not_vip_more_than_thousand(self): #1F - 3F - 5T - 6F - 8F - 10
        self.assertEqual(
            thanhToan(False, 1500),
            'Giam 5%, tang voucher'
        )

    def vip_less_than_hundred(self):    #1F - 3F - 5F - 11T - 12
        self.assertEqual(
            thanhToan(True, 30),
            "Tang voucher"
        )

    def vip_less_than_thousand(self):   #1F - 3F - 5F - 11F - 13T - 14
        self.assertEqual(
            thanhToan(True, 273),
            "Giam 5%, tang voucher"
        )

    def vip_more_than_thousand(self):   #1F - 3F - 5F - 11F - 13F - 15
        self.assertEqual(
            thanhToan(True, 3700),
            'Giam 10%, tang voucher')


if __name__ == '__main__':
    unittest.main()
