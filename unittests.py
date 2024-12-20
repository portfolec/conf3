import unittest
from hw3 import parse_xml, validate_name, translate_to_custom_language
import xml.etree.ElementTree as ET

class TestTranslator(unittest.TestCase):

    def test_parse_xml_valid(self):
        input_data = "<config><constant name='myConstant'>42</constant></config>"
        root = parse_xml(input_data)
        self.assertIsNotNone(root)

    def test_parse_xml_invalid(self):
        input_data = "<config><constant name='myConstant'>42<config>"
        with self.assertRaises(SystemExit):
            parse_xml(input_data)

    def test_validate_name_valid(self):
        self.assertTrue(validate_name("my_variable"))
        self.assertTrue(validate_name("a"))
    
    def test_validate_name_invalid(self):
        self.assertFalse(validate_name("1invalid"))
        self.assertFalse(validate_name("invalid-name"))

    def test_translate_to_custom_language(self):
        input_xml = """
        <config>
            <constant name="myconstant">42</constant>
            <dictionary>
                <item name="firstcame">John</item>
                <item name="lastcame">Doe</item>
                <item name="age">30</item>
            </dictionary>
            <comment>Thisiscomment.</comment>
        </config>
        """
        
        root = parse_xml(input_xml)
        result = translate_to_custom_language(root)
        
        expected_output = (
            "set myconstant = 42\n"
            "$[\n"
            " firstcame : John,\n"
            " lastcame : Doe,\n"
            " age : 30,\n"
            "]\n"
            "{\n"
            "Thisiscomment.\n"
            "}\n"
        )
        
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
