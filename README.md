# 🔳 QR Code Generator

A simple Python project that generates a QR code from a given URL or text and saves it as an image.

## 📌 About

This project uses the **Python `qrcode` library** to convert data such as a website URL into a QR code.

The generated QR code is:

* Saved as a `.png` image
* Automatically opened after generation
* Easy to customize for different URLs or text

## ✨ Features

* 🔗 Generate QR codes from URLs
* 📝 Generate QR codes from text
* 💾 Save the QR code as a PNG image
* 🖼️ Automatically display the generated QR code
* 🐍 Simple Python implementation

## 🛠️ Technologies Used

* **Python**
* **qrcode** library

## 📂 Project Structure

```text
QR-Code-Generator/
│
├── qr_code_generator.py
├── my_qr_code1.png
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Navigate to the project folder

```bash
cd QR-Code-Generator
```

### 3. Install the required library

```bash
pip install qrcode
```

## ▶️ How to Run

Run the Python file:

```bash
python qr_code_generator.py
```

The program will generate a QR code and save it as:

```text
my_qr_code1.png
```

The image will also open automatically after it is generated.

## 💻 Code

```python
import qrcode

data = "https://leetcode.com/"

img = qrcode.make(data)

img.save("my_qr_code1.png")

img.show()
```

## 🔄 How It Works

```text
Enter URL / Text
       ↓
qrcode.make()
       ↓
QR Code Generated
       ↓
Save as PNG
       ↓
Display QR Code
```

## 🧪 Example

For the input:

```text
https://leetcode.com/
```

the program generates a QR code that can be scanned to open the LeetCode website.

## 🔧 Customization

You can generate a QR code for any URL or text by changing the `data` variable:

```python
data = "https://github.com/"
```

or:

```python
data = "Hello, World!"
```

You can also change the output filename:

```python
img.save("github_qr.png")
```

## 🚀 Future Improvements

Possible improvements for this project:

* Add user input instead of hardcoding the URL
* Add customizable QR colors
* Add custom QR sizes
* Create a simple GUI
* Allow users to generate multiple QR codes
* Add support for QR codes containing Wi-Fi credentials or contact information

## 📚 What I Learned

* Installing and using a Python package
* Importing external libraries
* Generating QR codes programmatically
* Saving images using Python
* Working with simple file operations
              - REHANA FATHIMA M
