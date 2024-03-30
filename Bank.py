#  MÔ TẢ BÀI TOÁN
#  Một hệ thống bán hàng có đưa ra ưu đãi tùy theo mức giá đơn hàng mà người mua mua và loại khách. 
#  Quy định giá trị tối đa của hóa đơn là 5 triệu:
#  Khách thường     Dưới 100k	    Không ưu đãi
#	                100k – 1000k	Giảm 5%
#	                Hơn 1000k	    Giảm 5% + voucher
#  Khách vip	    Dưới 100k	    Tặng voucher
#	                100k – 1000k	Giảm 5% + tặng voucher
#            	    Hơn 1000k	    Giảm 10% + tặng voucher
#    Hãy thiết kế chương trình thỏa mãn:
#    -	Input:
#        o	Loại khách hàng (Vip hay không)
#        o	Số tiền của hóa đơn (đơn vị nghìn đồng, ví dụ: 5 = 5000VND)
#    -	Output: Ưu đãi của khách hàng được hưởng dưới dạng text.




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
    def test_p1(self):      #1T - 2
        self.assertEqual(
            thanhToan(False, -10),
            "Hoa don khong hop le!"
        )

    def test_p2(self): #1F - 3T - 4
        self.assertEqual(
            thanhToan(True, 5010),
            'Hoa don khong hop le!'
        )

    def test_p3(self): #1F - 3F - 5T - 6T - 7
        self.assertEqual(
            thanhToan(False, 80),
            'Khong uu dai'
        )

    def test_p4(self): #1F - 3F - 5T - 6F - 8T - 9
        self.assertEqual(
            thanhToan(False, 720),
            'Giam 5%'
        )

    def test_p5(self): #1F - 3F - 5T - 6F - 8F - 10
        self.assertEqual(
            thanhToan(False, 1500),
            'Giam 5%, tang voucher'
        )

    def test_p6(self):    #1F - 3F - 5F - 11T - 12
        self.assertEqual(
            thanhToan(True, 30),
            "Tang voucher"
        )

    def test_p7(self):   #1F - 3F - 5F - 11F - 13T - 14
        self.assertEqual(
            thanhToan(True, 273),
            "Giam 5%, tang voucher"
        )

    def test_p8(self):   #1F - 3F - 5F - 11F - 13F - 15
        self.assertEqual(
            thanhToan(True, 3700),
            'Giam 10%, tang voucher')


if __name__ == '__main__':
    unittest.main()
