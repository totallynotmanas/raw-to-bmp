<pre> ====================================================================================================
 =       ======  =====  ====  ====  ===================================      ====  =====  ==       ==
 =  ====  ====    ====  ====  ====  ===================================  ===  ===   ===   ==  ====  =
 =  ====  ===  ==  ===  ====  ====  =============  ====================  ====  ==  =   =  ==  ====  =
 =  ===   ==  ====  ==  ====  ====  ============    ===   =============  ===  ===  == ==  ==  ====  =
 =      ====  ====  ==   ==    ==  ===        ===  ===     ==        ==      ====  =====  ==       ==
 =  ====  ==        ===  ==    ==  ==============  ===  =  ============  ===  ===  =====  ==  =======
 =  ====  ==  ====  ===  ==    ==  ==============  ===  =  ============  ====  ==  =====  ==  =======
 =  ====  ==  ====  ====    ==    ===============  ===  =  ============  ===  ===  =====  ==  =======
 =  ====  ==  ====  =====  ====  ================   ===   =============      ====  =====  ==  =======
 ====================================================================================================</pre>
<h1 align="center">🖼️ Raw to BMP Converter 🖼️</h1>

<p align="center">
<strong>A simple and efficient command-line utility to convert raw image files to the BMP image format.</strong>
<br><br>
<img src="https://img.shields.io/github/license/totallynotmanas/raw-to-bmp?style=for-the-badge" alt="license">
<img src="https://img.shields.io/github/issues/totallynotmanas/raw-to-bmp?style=for-the-badge&color=important" alt="issues">
<img src="https://img.shields.io/github/stars/totallynotmanas/raw-to-bmp?style=for-the-badge&color=yellow" alt="stars">
</p>

# ✨ Description

This project provides a lightweight but powerful tool for converting raw image data into the more common and widely supported BMP (Bitmap) image format. It's perfect for quickly viewing or processing raw image data from various sources, such as camera sensors or other imaging devices, without the need for heavy software.

# ✅ Key Features

- Fast Conversion: Quickly transforms raw image files into 24-bit BMP images.

- Command-Line Interface: Easy to use for scripting and automation.

- Cross-Platform: Compiles and runs smoothly on Linux, macOS, and Windows.

- Lightweight: No external dependencies needed, just a C++ compiler!

# 🚀 Getting Started

Follow these simple steps to get the script up and running on your local machine.

## 🔧 Prerequisites

    Python 3.6+

    pip (Python package installer)

It's highly recommended to use a virtual environment to manage dependencies.
Bash

## Create and activate a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## ⚙️ Installation

    Clone the repository:
    Bash

git clone https://github.com/totallynotmanas/raw-to-bmp.git
cd raw-to-bmp

Install the required packages:
(You'll need to create a requirements.txt file listing your dependencies, for example:)
Plaintext

## requirements.txt
Pillow
numpy

Then run the installer:
Bash

    pip install -r requirements.txt

# ▶️ Usage

To convert a file, run the Python script with the input file, output file, and the image dimensions.

Command Syntax

Bash

python main.py <input_file.raw> <output_file.bmp> <width> <height>

Argument	Description
<input_file.raw>	The path to the source raw image file.
<output_file.bmp>	The desired name for the output BMP file.
<width>	The width of the image in pixels.
<height>	The height of the image in pixels.

Example

Bash

python main.py my_image.raw converted_image.bmp 1920 1080

This command reads my_image.raw and creates a new 1920x1080 BMP file named converted_image.bmp.

# 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

    Fork the Project

    Create your Feature Branch (git checkout -b feature/AmazingFeature)

    Commit your Changes (git commit -m 'feat: Add some AmazingFeature')

    Push to the Branch (git push origin feature/AmazingFeature)

    Open a Pull Request

# 📜 License

This project is distributed under the MIT License. See the LICENSE file for more information.
