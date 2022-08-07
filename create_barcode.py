import random
from barcode import EAN13
import barcode
from barcode.writer import ImageWriter
def generation_ean_code():
    n = list(range(0,10))
    numberEAN = random.choices(n,k=12)
    # chcange to string and first 0
    numberEAN = '0' + ''.join([str(i) for i in numberEAN])
    return numberEAN

def create_ean13(path):
    numberEAN = generation_ean_code()
    #if I want to save svg
    EAN_code = str(EAN13(numberEAN))
    #EAN_code.save(f"barcode/{EAN_code}")
    #if I want save png
    img = ImageWriter()
    ean = barcode.get('ean13', EAN_code, writer=img)
    ean.save(f"{path}/{EAN_code}")
    return EAN_code



