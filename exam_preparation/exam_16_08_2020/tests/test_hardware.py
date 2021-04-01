from exam_preparation.exam_16_08_2020.project.hardware.hardware import Hardware
from exam_preparation.exam_16_08_2020.project.software.light_software import LightSoftware
from exam_preparation.exam_16_08_2020.project.software.express_software import ExpressSoftware
import unittest


class TestHardware(unittest.TestCase):
    def test_attributes(self):
        params = ['Linux', "Power", 200, 300]
        hardware = Hardware(*params)
        result = [hardware.name, hardware.type, hardware.capacity, hardware.memory, hardware.software_components]
        expected_result = ['Linux', "Power", 200, 300, []]
        self.assertListEqual(result, expected_result)

    def test_install_method(self):
        params = ['Linux', "Power", 200, 300]
        hardware = Hardware(*params)
        light_software = LightSoftware('SSD', 50, 60)
        express_software = ExpressSoftware('HHD', 60, 70)
        hardware.install(light_software)
        hardware.install(express_software)
        result = hardware.software_components
        expected_result = [light_software, express_software]
        self.assertEqual(result, expected_result)

    def test_install_method_raise(self):
        params = ['Linux', "Power", 200, 300]
        hardware = Hardware(*params)
        light_software = LightSoftware('SSD', 100, 150)
        light_software2 = LightSoftware('SSD', 100, 150)
        express_software = ExpressSoftware('HHD', 50, 100)
        hardware.install(light_software)
        hardware.install(express_software)
        with self.assertRaises(Exception) as exp:
            hardware.install(light_software2)
        self.assertEqual(exp.exception.args[0], "Software cannot be installed")

    def test_uninstall_method(self):
        params = ['Linux', "Power", 50, 70]
        hardware = Hardware(*params)
        light_software = LightSoftware('SSD', 10, 20)
        light_software2 = LightSoftware('SSD', 10, 20)
        express_software = ExpressSoftware('HHD', 20, 25)
        hardware.install(light_software)
        hardware.install(light_software2)
        hardware.install(express_software)
        hardware.uninstall(express_software)
        result = hardware.software_components
        expected_result = [light_software, light_software2]
        self.assertEqual(result, expected_result)

    def test_uninstall_method_if_not_in_components(self):
        params = ['Linux', "Power", 50, 70]
        hardware = Hardware(*params)
        light_software = LightSoftware('SSD', 10, 20)
        light_software2 = LightSoftware('SSD', 10, 20)
        express_software = ExpressSoftware('HHD', 20, 25)
        hardware.install(light_software)
        hardware.install(light_software2)
        hardware.install(express_software)
        hardware.uninstall(express_software)
        try:
            hardware.uninstall(express_software)
        except:
            ValueError
        result = hardware.software_components
        expected_result = [light_software, light_software2]
        self.assertEqual(result, expected_result)

    # def test_get_light_software_components_count(self):
    #     params = ['Linux', "Power", 200, 300]
    #     hardware = Hardware(*params)
    #     light_software = LightSoftware('SSD', 50, 60)
    #     express_software = ExpressSoftware('HHD', 60, 70)
    #     hardware.install(light_software)
    #     hardware.install(express_software)
    #     result = hardware.get_light_software_components_count()
    #     expected_result = 1
    #     self.assertEqual(result, expected_result)

    # def test_get_express_software_components_count(self):
    #     params = ['Linux', "Power", 200, 300]
    #     hardware = Hardware(*params)
    #     light_software = LightSoftware('SSD', 50, 60)
    #     express_software = ExpressSoftware('HHD', 60, 70)
    #     hardware.install(light_software)
    #     hardware.install(express_software)
    #     result = hardware.get_express_software_components_count()
    #     expected_result = 1
    #     self.assertEqual(result, expected_result)

    # def test__repr__method(self):
    #     params = ['Linux', "Power", 200, 300]
    #     hardware = Hardware(*params)
    #     result = hardware.__repr__()
    #     expected_result = "Hardware Component - Linux\nExpress Software Components: 0\nLight Software Components: 0\nMemory Usage: 0 / 300\nCapacity Usage: 0 / 200\nType: Power\nSoftware Components: None"
    #     self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
