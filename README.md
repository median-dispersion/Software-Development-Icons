# Software Development Icons

<a href="./"><img alt="Software Development Icons Banner" src="./Assets/Banner.svg" style="width:100%"></a>

<p>
  <a href="./LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/median-dispersion/Software-Development-Icons?style=for-the-badge"></a>
</p>

A collection of icons for use in software development.

> [!NOTE]
> This repository is for keeping track of how to create the icons and make them consistent with each other. To use them, simply download the `Icons` folder and choose from the `Filled` or `Outlined` variants.

## ✨ Example

For a full list of all icons in this repository, view the `Example/index.html` file.

<p align="center">
<img src="Icons/Filled/Delete.svg" alt="Filled delete icon" width="50px">
<img src="Icons/Filled/DragAndDrop.svg" alt="Filled drag and drop icon" width="50px">
<img src="Icons/Filled/Radiation.svg" alt="Filled radiation icon" width="50px">
<img src="Icons/Filled/Settings.svg" alt="Filled settings icon" width="50px">
<img src="Icons/Filled/Brightness50.svg" alt="Filled brightness icon" width="50px">
<img src="Icons/Filled/User.svg" alt="Filled user icon" width="50px">
<img src="Icons/Filled/Copy.svg" alt="Filled copy icon" width="50px">
<img src="Icons/Filled/Light.svg" alt="Filled light icon" width="50px">
<img src="Icons/Filled/Dark.svg" alt="Filled dark icon" width="50px">
<img src="Icons/Filled/WiFiSignal50.svg" alt="Filled WiFi signal icon" width="50px">
<br><text style="font-weight:bold;">Filled icons</text>
</p>

<p align="center">
<img src="Icons/Outlined/Delete.svg" alt="Outlined delete icon" width="50px">
<img src="Icons/Outlined/DragAndDrop.svg" alt="Outlined drag and drop icon" width="50px">
<img src="Icons/Outlined/Radiation.svg" alt="Outlined radiation icon" width="50px">
<img src="Icons/Outlined/Settings.svg" alt="Outlined settings icon" width="50px">
<img src="Icons/Outlined/Brightness50.svg" alt="Outlined brightness icon" width="50px">
<img src="Icons/Outlined/User.svg" alt="Outlined user icon" width="50px">
<img src="Icons/Outlined/Copy.svg" alt="Outlined copy icon" width="50px">
<img src="Icons/Outlined/Light.svg" alt="Outlined light icon" width="50px">
<img src="Icons/Outlined/Dark.svg" alt="Outlined dark icon" width="50px">
<img src="Icons/Outlined/WiFiSignal50.svg" alt="Outlined WiFi signal icon" width="50px">
<br><text style="font-weight:bold;">Outlined icons</text>
</p>

## 📐 Guidelines

| Property      | Value     |
| ------------- | --------- |
| Software      | Inkscape  |
| Format        | SVG       |
| Units         | px        |
| Viewbox       | 512 px    |
| Margin        | 32 px     |
| Large icon    | 448 px    |
| Medium icon   | 288 px    |
| Tiny icon     | 224 px    |
| Line weight   | 32 px     |
| Line cap      | round     |
| Line join     | round     |
| Corner radius | 32 px     |
| Fill color    | #FFFFFFFF |

Copy the file `Assets/Templates/Master Template.svg` and use it as a starting point. It is already properly sized and has all the guides in place. For a visual representation of how to size the icon, view `Assets/Icon Sizing/Chart.svg`. The icon should ideally be of size large. For smaller icons, the medium size should be targeted. Tiny should only be used if the icon is enclosed in a border, e.g a circle, square or triangle that is of size large. No part of the icon should ever be inside the margin area. There should be a filled and outlined version of the icon. The outlined icon should have no filled polygons and should only consist of lines. The filled icon can contain or even be made up entirely from lines if it is unfeasible to fill it. For both versions of the icon, all stokes should be converted to paths. The icon should be exported as a singe path that has no strokes and is filled with a solid white.

<p align="center">
<img src="Assets/Sizing/Chart.svg" alt="Icon size chart" width="200px">
<img src="Assets/Sizing/Large.svg" alt="Example of a large icon" width="200px">
<img src="Assets/Sizing/Medium.svg" alt="Example of a medium icon" width="200px">
<img src="Assets/Sizing/Tiny.svg" alt="Example of a tiny icon" width="200px">
</p>

## 🛫 Export

The icon to export should just be a single path with no strokes, no groups or any other elements and filled with a solid white. The file should be saved using Inkscape's "Optimized SVG" format. This will use Scour, an SVG optimizing tool, to export the file.

### Scour [0.31+] Settings

#### Options
- Number of significant digits for coordinates: **5**
- [x] Shorten color values
- [x] Convert CSS attributes to XML attributes
- [x] Collapse groups
- [ ] Create groups for similar attributes
- [ ] Keep editor data
- [ ] Keep unreferenced definitions
- [x] Work around renderer bugs  

#### SVG Output
- [x] Remove the XML declaration
- [x] Remove metadata
- [x] Remove comments
- [ ] Embed raster images
- [ ] Enable viewboxing
- [ ] Format Output with line-breaks and indentation
- Indentation characters: **None**
- Depth of indentation: **0**
- [x] Strip the "xml:space" attribute from the root SVG element

#### IDs
- [x] Remove unused IDs
- [x] Shorten IDs
- Prefix shortened IDs with: 
- [ ] Preserve manually created IDs not ending with digits
- Preserve the following IDs:
- Preserve IDs stating with:

## 🧼 Cleaning

For cleaning the exported SVG files, use the tool found at `Tools/cleanSVG.py`. It will take all SVG files including those in subdirectory in the given folder and extract the SVG path values. It transplants them into a bare bones SVG template and overwrites the original file with it. A backup of the original file will be created before overwriting. 

Basic usage:
```bash
python cleanSVG.py "../Icons"
```

## 🔄 Updating the Example

To update the example page, simply execute the tool found at `Tools/updateExample.py`. It will automatically add all new icons in `Icons/Filled` and `Icons/Outlined` to the example list.
```bash
python updateExample.py
```