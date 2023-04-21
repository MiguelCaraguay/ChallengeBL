import fitz

def generatePdf(path,file_name, order_information, transaction_information):

    logo = open('logoBanco.png', 'rb').read()

    title = 'SERVICIOS CORPORATIVOS'
    originator_title = 'INFORMACIÓN DEL ORDENANTE'
    transction_title = 'INFORMACIÓN DE LA TRANSACCIÓN'

    doc = fitz.open()
    pagina = doc.new_page(pno=-1,width=2100,height=2970)
    rect = fitz.Rect(0, 0, 500, 500)  

    pagina.insert_image(rect, stream=logo, keep_proportion=True)
    pagina.insert_text(fitz.Point(150,130), title, color=0, fontsize=30)
    pagina.insert_text(fitz.Point(170,160), originator_title, color=0, fontsize=30)
    pagina.insert_text(fitz.Point(270,160), order_information, color=0, fontsize=30)
    pagina.insert_text(fitz.Point(500,200), transction_title, color=0, fontsize=30)
    pagina.insert_text(fitz.Point(600,200), transaction_information, color=0, fontsize=30)
    
    path = path + "/"+file_name + ".pdf"
    print(path)
    doc.write()
    # Guardamos el archivo PDF
    doc.save(path , pretty=True)
    # Cerramos el documento
    doc.close()