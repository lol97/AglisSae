import pyqrcode

code = pyqrcode.create("lakad matatag2")
code.png("hasil.png",scale=6)