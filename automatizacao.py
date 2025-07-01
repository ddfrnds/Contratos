from docxtpl import DocxTemplate

doc = DocxTemplate("contrato_rinp_modelo.docx.docx")
context = { 
    "NOME_COMPLETO" : "DAINARA FERNANDA DE SOUSA" }

doc.render(context)
doc.save("contrato_preenchido.docx")
print ("Contrato gerado!")
