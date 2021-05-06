import unittest

from pknyx.core.dptXlator.dptXlator2ByteSigned import DPTXlator2ByteSigned
from pknyx.core.dptXlator.dptXlatorBase import DPTXlatorValueError


class DPT2ByteSignedTestCase(unittest.TestCase):

    def setUp(self):
        self.testTable = (
            (-32768, 0x8000, b"\x80\x00"),
            (-4, 0xfffc, b"\xff\xfc"),
            (-1, 0xffff, b"\xff\xff"),
            (0, 0x0000, b"\x00\x00"),
            (1, 0x0001, b"\x00\x01"),
            (32767, 0x7fff, b"\x7f\xff"),
        )
        self.dptXlator = DPTXlator2ByteSigned("8.xxx")

    def tearDown(self):
        pass

    # def test_constructor(self):
    # print self.dptXlator.handledDPT

    def test_typeSize(self):
        self.assertEqual(self.dptXlator.typeSize, 2)

    def test_checkValue(self):
        with self.assertRaises(DPTXlatorValueError):
            self.dptXlator.checkValue(self.dptXlator._dpt.limits[1] + 1)

    def test_dataToValue(self):
        for value, data, frame in self.testTable:
            value_ = self.dptXlator.dataToValue(data)
            self.assertEqual(value_, value, "Conversion failed (converted value for %s is %d, should be %d)" %
                             (hex(data), value_, value))

    def test_valueToData(self):
        for value, data, frame in self.testTable:
            data_ = self.dptXlator.valueToData(value)
            self.assertEqual(data_, data, "Conversion failed (converted data for %d is %s, should be %s)" %
                             (value, hex(data_), hex(data)))

    def test_dataToFrame(self):
        for value, data, frame in self.testTable:
            frame_ = self.dptXlator.dataToFrame(data)
            self.assertEqual(frame_, frame, "Conversion failed (converted frame for %s is %r, should be %r)" %
                             (hex(data), frame_, frame))

    def test_frameToData(self):
        for value, data, frame in self.testTable:
            data_ = self.dptXlator.frameToData(frame)
            self.assertEqual(data_, data, "Conversion failed (converted data for %r is %s, should be %s)" %
                             (frame, hex(data_), hex(data)))


if __name__ == '__main__':
    unittest.main()