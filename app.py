# animated_qrcode.py

import segno

data = "https://github.com/iMatheusHenrique"

slts_qrcode = segno.make_qr(data)
slts_qrcode.save("qrcode.png",scale=10,border=1)

