import pyqrcode

code = pyqrcode.create("https://aglistech.blogspot.com/2018/11/cara-membuat-qrcode-di-python.html")
code.png("hasil.png",scale=6)
code.show()