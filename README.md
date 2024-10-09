# QRCodeGenerator

This python script lets you generate QR codes however you want. 
It includes all 40 version that are part of the ISO/IEC 18004. Meaning any device compliant with this will be able to read the QR Codes and all their versions.
You can select which version you want. However should you enter too much text the script will automatically go to the next version that supports the amount of data.


In order for the script to work you need the following : 
qrcode : https://pypi.org/project/qrcode/
Pillow : https://python-pillow.org/
pyperclip : https://pypi.org/project/pyperclip/
TkInter : https://wiki.python.org/moin/TkInter (this should be a part of your python install)

The usage is very simple and should be self explanatory.      
1. Enter your text
2. Select your version you want 1-40 (Normed ISO/IEC 18004)
3. Generate your QR Code. (It will display in the window, if you want to copy it press the copy to clipboard button)
4. + and - buttons increase the size inside the window so its more readable.
