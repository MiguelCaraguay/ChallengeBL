import fitz

def generatePdf(path,file_name, order_information, transaction_information):

    logo = open('logoBanco.png', 'rb').read()

    title = 'SERVICIOS CORPORATIVOS\nCOMPROBANTE DE TRANSACCION\nTRANSFERENCIA INTERBANCARIA'
    originator_title = 'INFORMACIÓN DEL ORDENANTE'
    transction_title = 'INFORMACIÓN DE LA TRANSACCIÓN'

    x=30
    x1= 595
    y1= 842
    fontsize =10
    doc = fitz.open()
    size = fitz.paper_size("A4")
    print(size)
    pagina = doc.new_page(width= size[0], height=size[1])
    rect = fitz.Rect(x, 0, 300, 100)  


    pagina.insert_image(rect, stream=logo)

    pagina.insert_textbox(fitz.Rect(x, 90, x1, y1),title, fontsize=12, align=1)
    pagina.insert_textbox(fitz.Rect(x, 160, x1, y1), originator_title, color=0, fontsize=12, align=0)
    pagina.insert_textbox(fitz.Rect(x, 180, x1, y1), order_information, color=0, fontsize=fontsize, align=0)
    pagina.insert_textbox(fitz.Rect(x, 380, x1, y1), transction_title, color=0, fontsize=12, align=0)
    pagina.insert_textbox(fitz.Rect(x, 400, x1, y1), transaction_information, color=0, fontsize=fontsize, align=0)

    path = path + "/"+file_name + ".pdf"
    print(path)
    doc.write()
    # Guardamos el archivo PDF
    doc.save(path , pretty=True)
    # Cerramos el documento
    doc.close()