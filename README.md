# Textures Cutter

### [Русская версия README](https://github.com/proDreams/texture_cutter/blob/main/README-ru.md)

## Description:

A program for cutting an image/texture into individual elements at specified coordinates, with a given size and name of
the element.  
The cut images are saved in a separate directory with the name of the main file.

## Features:

Works with `DDS/PNG/TGA` textures when a valid XML file with coordinates is present.

## Example XML file (imageset):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Imageset Name="itemicons" Imagefile="media/ui/itemicons/itemicons.dds" NativeHorzRes="1024" NativeVertRes="768"
          AutoScaled="true">
    <Image Name="amulet8" XPos="0" YPos="0" Width="128" Height="192"/>
    <Image Name="portrait_zealot" XPos="128" YPos="0" Width="128" Height="128"/>
    <Image Name="portrait_sage" XPos="256" YPos="0" Width="128" Height="128"/>
</Imageset>
```

_Example XML file and texture file are available in the repository._

## Requirements for keys in the XML file:

_Case of keys is not important_

1. Root element:
    - The `Imagefile` key containing the texture file name. It should be in the same directory as the XML file.
2. Child elements:
    - The `Name` key defines the image name.
    - The `XPos` and `YPos` keys define the starting coordinates on the texture.
    - The `Width` and `Height` keys define the image size.

## Used external libraries:

- `Pillow`

## Launch:

1. Download the latest version: https://github.com/proDreams/texture_cutter/releases/latest
2. Drag and drop the XML file onto the exe file of the program.
3. A directory with the cut images will appear in the XML file directory.

## Author:

[Ivan "proDream" Ashikhmin](https://github.com/proDreams)
