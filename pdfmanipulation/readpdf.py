from PyPDF2 import PdfReader
  
# creating a pdf reader object
reader = PdfReader('factura.pdf')
  
# printing number of pages in pdf file
#print(len(reader.pages))
  
# getting a specific page from the pdf file
page = reader.pages[0]
  
# extracting text from page
text = page.extract_text()

def cortar_desde_saldo(texto_largo,palabra,position):
    
    indice_saldo = texto_largo.find(palabra)
    if position != 0:
        indice_saldo = position
        
    if indice_saldo != -1:  # Si la palabra "saldo" fue encontrada en el texto
        texto_cortado = texto_largo[indice_saldo:]  # Cortar desde la posición de "saldo" hasta el final
        return texto_cortado
    else:
        texto_cortado = texto_largo[indice_saldo:]  # Cortar desde la posición de "saldo" hasta el final
        return "La palabra 'saldo' no fue encontrada en el texto."

def cortar_hasta_fecha_emision(texto_cortado):
    palabra_buscada = "FECHA DE EMISION"
    indice_fecha_emision = texto_cortado.find(palabra_buscada)

    if indice_fecha_emision != -1:  # Si la palabra "FECHA DE EMISION" fue encontrada en el texto
        texto_final = texto_cortado[:indice_fecha_emision]  # Cortar hasta la posición de "FECHA DE EMISION"
        return texto_final
    else:
        # Manejar el caso en el que la palabra "FECHA DE EMISION" no fue encontrada
        return "La palabra 'FECHA DE EMISION' no fue encontrada en el texto."

resultado = cortar_desde_saldo(text,"NPE",0)
texto_final = cortar_hasta_fecha_emision(resultado)
texto_final = cortar_desde_saldo(texto_final,"TOTAL A PAGAR ",18)
text_without_spaces = texto_final.replace(" ", "")
print(text_without_spaces)



