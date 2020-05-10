import unittest

from excel_data_receiver.excel_data_getter import ExcelDataGetter


class TestExcelReceiver(unittest.TestCase):
    test_file = ExcelDataGetter(
        "/home/nmramorov/repos/diplom/diplom_data/Chronometer/test_protocol_new_format.xlsx")

    def test_sheetnames_existance(self):
        self.assertNotEqual(self.test_file.get_sheetnames(), None)
        self.assertNotEqual(self.test_file.get_sheetnames(), [])

    def test_find_start_values_row(self):
        self.assertIsInstance(self.test_file.find_start_values_row(), int)

    def test_get_required_data(self):
        self.assertNotEqual(self.test_file.get_required_data(), None)
        self.assertNotEqual(self.test_file.get_required_data(), [])

    def test_get_excel_data(self):
        self.assertNotEqual(self.test_file.get_excel_data(), None)
        self.assertNotEqual(self.test_file.get_excel_data(), [])


if __name__ == "__main__":
    unittest.main()
