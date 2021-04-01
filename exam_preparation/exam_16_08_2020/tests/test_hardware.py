from exam_preparation.exam_16_08_2020.project.hardware.hardware import Hardware
from exam_preparation.exam_16_08_2020.project.software.software import Software
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

    # def setUp(self):
    #     self.h = Hardware("Lenovo", "Power", 800, 32)
    #     self.s = Software("Win", "Light", 10, 20)
    #     self.e = Software("Win", "Express", 1000, 2000)
    #
    # def test_init(self):
    #     self.assertEqual(self.h.name, "Lenovo")
    #     self.assertEqual(self.h.type, "Power")
    #     self.assertEqual(self.h.capacity, 800)
    #     self.assertEqual(self.h.memory, 32)
    #
    # def test_empty_software_components(self):
    #     self.assertEqual(self.h.software_components, [])
    #
    # def test_add_to_software_components(self):
    #     self.h.install(self.s)
    #     self.assertEqual(self.h.software_components, [self.s])
    #
    # def test(self):
    #     self.h.install(self.s)
    #     self.assertEqual(self.h.software_components, [self.s])
    #     self.h.uninstall(self.s)
    #     self.assertEqual(self.h.software_components, [])
    #
    # def test_cannot_add_due_to_high_requirements(self):
    #     with self.assertRaises(Exception) as ex:
    #         self.h.install(self.e)
    #     self.assertEqual("Software cannot be installed", str(ex.exception))
    #     self.assertEqual(self.h.software_components, [])


if __name__ == '__main__':
    unittest.main()
