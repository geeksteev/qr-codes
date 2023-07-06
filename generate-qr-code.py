import segno

qr_code = segno.make("Hello World!")
qr_code.save("hello-world.png", scale=10)
