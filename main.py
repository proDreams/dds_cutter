import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image

# Получение пути до файла из "Drag'n'Drop" на exe с программой
droppedFile = sys.argv[1]
xml_file = Path(droppedFile)

# Получение пути до файла из консоли
# xml_file = Path(input("Введите путь до xml-файла: "))

file_path = xml_file.cwd()

# открытие xml-файла и парсинг
tree = ET.parse(xml_file)
root = tree.getroot()

dds_file = root.attrib.get("Imagefile").split("/")[-1]

file_name, file_ext = dds_file.split(".")

# Создание папки для нарезанных файлов, если её не существует
result_dir = f"{file_path}/{file_name}"
if not os.path.exists(result_dir):
    Path(result_dir).mkdir()

# Открытие текстуры полученного из xml-файла
image_file_path = Path(file_path / dds_file)
image_file = Image.open(image_file_path)

# Проходимся по всем изображениям в текстуре и нарезаем
for child in root:
    name = child.attrib.get("Name")
    x_pos = int(child.attrib.get("XPos"))
    y_pos = int(child.attrib.get("YPos"))
    width = int(child.attrib.get("Width"))
    height = int(child.attrib.get("Height"))
    im_crop = image_file.crop((x_pos, y_pos, x_pos + width, y_pos + height))
    im_crop.save(f"{result_dir}/{name}.{file_ext}", quality=100)
