#!/bin/env python

import qrcode
import os
import sys
import time
from PIL import Image

def CreateQrCode(text, export="genqrcode.png", logo=""):
    qr = qrcode.QRCode(version=2,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 1
        )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")
    img_w, img_h = img.size
    print(img_w, img_h)

    if logo != ""   and os.path.isfile(logo):
      icon = Image.open(logo)
      factor = 4
      size_w = int(img_w / factor)
      size_h = int(img_h / factor)

      icon_w, icon_h = icon.size
      print(icon_w, icon_h)
      if icon_w > size_w:
        icon_w = size_w
      if icon_h > size_h:
        icon_h = size_h
      
      print(icon_w, icon_h)
      icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

      w = int((img_w - icon_w) / 2)
      h = int((img_h - icon_h) / 2)
      print(w, h)

      icon = icon.convert("RGBA")
      img.paste(icon, (w, h), icon)
    if export == "":
      export = "genqrcode.png"
    if os.path.exists(export):
      if os.path.isdir(export):
        export = export + "genqrcode.png"
      else:
        export = os.path.dirname(export) + time.strftime("%Y%m%d%H%M%S.png", time.gmtime())
    else:
      if export[len(export)-1] == '/' or export[len(export)-1] == '\\':
        os.makedirs(export)
      else:
        if not os.path.dirname(export) == "":
          os.makedirs(os.path.dirname(export))
        try:
          if export.rindex('.png') or export.rindex('.jpg') or export.rindex('.gif'):
            pass
        except Exception as e:
          print(e)
          export = export + '.png'

    img.save(export)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print("usage: genQrCode.py <text> <export path> <logo>")
  if len(sys.argv) == 2:
    text = sys.argv[1]
    CreateQrCode(text)
  if len(sys.argv) == 3:
    text = sys.argv[1]
    export = sys.argv[2]
    CreateQrCode(text, export)
  if len(sys.argv) == 4:
    text = sys.argv[1]
    export = sys.argv[2]
    logo = sys.argv[3]
    CreateQrCode(text, export, logo)
