import pyqrcode
  
# String which represent the QR code 
s = input("Enter the url:")
id = input("Name of url:")

# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("id.png", scale = 8) 