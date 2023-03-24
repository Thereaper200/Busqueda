from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.facturas

coleccion1 = db.facturas20_21
coleccion2 = db.facturas17_19


while True:
    serialnumber = input("Escribe el numero de serie del producto(Si quieres salir escribe 'Salida'): ")

    busqueda = coleccion1.find({'SerialNumber': serialnumber})

    for documento in busqueda:
        print(f"El {documento['Product']} se encuentra en la factura: {documento['factura']}")

    busqueda = coleccion2.find({'SerialNumber': serialnumber})

    for documento in busqueda:
        print(f"El {documento['Product']} se encuentra en la factura: {documento['factura']}")

    if serialnumber in ["Salida"]:
        break
