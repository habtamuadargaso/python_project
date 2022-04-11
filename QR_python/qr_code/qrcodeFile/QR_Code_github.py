import qrcode
data = "https://github.com/habtamuadargaso/Java/commit/bfba65a863230ab40236f4e1acfe79680b2416b5"
QRCodefile = "My_githube_File.png"
QRimage =qrcode.make(data)
QRimage.save(QRCodefile)