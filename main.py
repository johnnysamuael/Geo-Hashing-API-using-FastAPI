from typing import Text
from fastapi import FastAPI
from fastapi.responses import FileResponse
#from deta import Drive,Deta 
import polyline
import qrcode
from PIL import Image
import base64

app = FastAPI()
#deta = Deta("c0xzui0l_hamVLxSFX5i42QHyTLGMGrT9H7ceTu94")
#drive = deta.Drive("images")

@app.get("/encode-latlon")
def encode_latlon(lat: float,lon: float,accuracy: int):
    
    return {"encodedvalue": polyline.encode([(lat,lon)],accuracy)}

@app.get("/decode-hash")
def encode_latlon(hashval: Text):
    
    return {"coordinates: ": polyline.decode(hashval)}

@app.get("/qr-generate")
def encode_latlon(lat: float,lon: float,accuracy: int):
   data = polyline.encode([(lat,lon)],accuracy)
   qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,)

   qr.add_data(data)
   qr.make(fit=True)
   img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
   img.save("sample.png")
   #image/png
   #drive.put('sample.png', img)
   #hello = drive.get('sample.png')
   #content = hello.read()
   #hello.close
   #content.save("sample.png")

   return FileResponse('sample.png')


    


