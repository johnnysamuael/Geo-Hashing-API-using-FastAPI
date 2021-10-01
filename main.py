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
