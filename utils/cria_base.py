from langchain.schema import Document

def cria_documentos():
    textos_sim = [
        """
        A parte Autora é beneficiária da Previdência Social, sendo tal sua única fonte de renda.  
        Portanto, por ser aposentada pelo INSS, a parte autora fica vulnerável a ter em sua folha  de pagamento, 
        descontos indevidos, como aqueles oriundos de Empréstimos  Consignados, e todos os demais, que podem ser 
        realizados em folha, mediante a simples  posse dos dados cadastrais do Requerente.  Ocorre que a parte 
        Requerente, ao analisar sua folha de pagamento, pode perceber que,  vem lhe sendo descontado, valores 
        referentes a empréstimo consignado que sequer tem  conhecimento e muito menos utilizou, conforme informações 
        abaixo extraídas do portal  MEU INSS:
        """,
        """
        A parte Autora é titular do benefício previdenciário de nº 194.285.875-0 e, de acordo com extrato fornecido pelo 
        INSS (doc. em anexo), o referido benefício vem sofrendo descontos em razão de empréstimo consignado supostamente 
        efetuado pela parte autora. O referido contrato de n° 507904789 foi averbado com os seguintes dados:  Contudo, 
        a parte autora informa ter sido vítima de golpes fraudulentos, pois além de analfabeta, a parte requerente reside 
        na zona rural e possui pouco conhecimento sobre instituições financeiras.
        """,
        """
        A parte autora, pessoa sem leitura, é titular de um benefício previdenciário que é a fonte do sustento seu e de sua família. 
        Com o fim de aclarar a quantidade e natureza dos descontos que vem experimentando em seu benefício, procurou ajuda profissional 
        para que fossem feitos os requerimentos administrativos e demais investigações por um profissional especializado e de sua confiança.  
        Nesta oportunidade, e em observância ao extrato fornecido pela Previdência Social (doc. em anexo), foi constatado que seu benefício 
        sofreu e/ou vem sofrendo descontos por parte da requerida em decorrência de empréstimo consignado, com os seguintes contratos: 
        NOME: LUZIA BATISTA DA SILVA BANCO REQUERIDO: BANCO BRADESCO S.A. ? 1º Contrato n°386039739, no valor mensal fixo de R$150,77, 
        com vigência de 11/02/2020 - 30/01/2024, com o total de 48 parcelas pagas até a presente data, totalizando o valor de R$7236,96
        """
    ]
    
    textos_nao = [
        """DOS FATOS A parte autora tomou empréstimo de valores com a requerida. 
        No entanto, esta última em seu contrato de adesão impôs juros exorbitantes que superam múltiplas 
        vezes a média de mercado, endividando a parte autora de maneira desproporcional, 
        impondo demasiado desequilíbrio contratual entre as partes. As parcelas são descontadas 
        diretamente na conta corrente da requerente. Veja-se o profundo prejuízo: Ardilosamente o 
        empréstimo realizado pela Ré se reveste das mesmas características e garantias do “empréstimo consignado”, 
        contudo, sem a necessidade de atenção as normas legais que delimitam esta modalidade de empréstimo, 
        possibilitando à Ré agir de forma abusiva em contrato de adesão, tomando boa parte do seu benefício 
        previdenciário, reduzindo-a a condição de miserabilidade. Para conferir o original, acesse o site informe o 
        processo 1012023-81.2025.8.26.0196 e código U51COoIY.  6"""
    ]


    documentos_sim = [Document(page_content=text, metadata={"label": "SIM"}) for text in textos_sim]
    documentos_nao = [Document(page_content=text, metadata={"label": "NAO"}) for text in textos_nao]
    
    return documentos_sim, documentos_nao