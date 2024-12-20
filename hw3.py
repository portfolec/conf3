import sys
import xml.etree.ElementTree as ET
import re

def parse_xml(input_data):
    """Парсинг XML данных и возврат корневого элемента."""
    try:
        root = ET.fromstring(input_data)
        return root
    except ET.ParseError as e:
        print(f"Ошибка парсинга XML: {e}")
        sys.exit(1)

def validate_name(name):
    """Проверка корректности имени по заданному шаблону."""
    pattern = r'^[a-z][a-z0-9_]*$'
    if not re.match(pattern, name):
        print(f"Ошибка: некорректное имя '{name}'")
        return False
    return True

def translate_to_custom_language(xml_root):
    """Преобразование XML в учебный конфигурационный язык."""
    output = ""
    
    for elem in xml_root:
        # Пример обработки элементов
        if elem.tag == "constant":
            name = elem.get("name")
            value = elem.text.strip()
            if validate_name(name):
                output += f"set {name} = {value}\n"
        
        elif elem.tag == "dictionary":
            output += "$[\n"
            for item in elem:
                name = item.get("name")
                value = item.text.strip()
                if validate_name(name):
                    output += f" {name} : {value},\n"
            output += "]\n"

        elif elem.tag == "comment":
            output += "{\n"
            output += f"{elem.text.strip()}\n"
            output += "}\n"

    return output

def main():
    input_data = sys.stdin.read()
    xml_root = parse_xml(input_data)
    output = translate_to_custom_language(xml_root)
    print(output)

if __name__ == "__main__":
    main()
