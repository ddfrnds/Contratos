from docxtpl import DocxTemplate

doc = DocxTemplate("contrato_rinp_modelo.docx")
context = { 
    "NOME_COMPLETO" : "DAINARA FERNANDA DE SOUSA",
     "nacionalidade" : "brasileira",
     "profissão" : "estagiária",
     "estado_civil" : "solteira", 
     "cpf" : "118.616.000-00", 
     "RG": "019.770.000", 
     "nome_da_rua" : "Rua Tal", 
     "n_da_casa" : "175", 
     "bairro" : "Cidade Nova", 
     "cidade" : "Gov. Valadares", 
     "estado" : "MG", 
     "email" : "dainarafs@gmail.com", 
     "numero_telefone" : "3398890-1052",
     "valor" : "12.000,00 ",
     "valor_extenso" : "vinte mil reais",
     "forma de pagamento" : "mil vezes no cartão, parcelado 12x",
     "dia" : "10",
     "mes" : "maio"}

doc.render(context)
doc.save("contrato_preenchido.docx")
print ("Contrato gerado!")
