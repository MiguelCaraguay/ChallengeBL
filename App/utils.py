# set Report parameters
def generateReportFile(row):    

    data=row.split("\t")

    batch=data[0]
    nombre_cliente=data[1]
    identificacion=data[2]
    cta_debito=data[3]
    comision=data[4]
    nro_transaccion_por_cuenta=data[5]
    aprobadores=data[6]
    nombre_beneficiario=data[7]
    identificacion_beneficiario=data[8]
    institucion_financiera_receptora=data[9]
    cta_credito=data[10]
    valor=data[11]
    referencia_transaccion=data[12]
    fecha_ingreso=data[13]
    fecha_aprobacion=data[14]
    observaciones=data[15]
    estado_transaccion=data[16]

    
    order_information =("Nombre del Cliente:\n\t%s\n"
                       +"Identificacion:\n\t%s\n"
                       +"Cuenta débito:\n\t%s\n"
                       +"Comisión:\n\t%s\n"
                       +"Nro. de transacción por cuenta:\n\t%s\n"
                       +"Aprobadores:\n\t%s\n")%(nombre_cliente, cta_debito,identificacion, comision,nro_transaccion_por_cuenta, aprobadores)
    order_information.upper()

    transaction_information =("Nombre del Beneficiario:\n\t%s\n"+
                             "Identificacion:\n\t%s\n"+
                             "Institucion Financiera Receptora:\n\t%s\n"+
                             "Cuenta crédito:\n\t%s\n"+
                             "Valor:\n\t%s\n"+
                             "Referencia de la transacción:\n\t%s\n"+
                             "Fecha de Ingreso:\n\t%s\n"+
                             "Fecha de aprobación:\n\t%s\n"+
                             "Observaciones:\n\t%s\n"+
                             "Estado de la transacción:\n\t%s\n")%(nombre_beneficiario,identificacion_beneficiario, 
                             institucion_financiera_receptora, cta_credito, valor, referencia_transaccion, 
                             fecha_ingreso, fecha_aprobacion,observaciones, estado_transaccion)
    transaction_information.upper()

    file_name = ("%s %s")% (batch,nombre_cliente)



    return (file_name, order_information, transaction_information)


