import pandas as pd

regiao_centro = [
    'Abrantes','Aguiar da Beira','Águeda','Albergaria-a-Velha','Alcanena','Alcains',
    'Alcobaça','Alenquer','Almeida','Alvaiázere','Alvôco da Serra','Ansião',
    'Arganil','Arruda dos Vinhos','Aveiro','Batalha','Belmonte','Bombarral',
    'Cadaval','Caldas da Rainha','Cantanhede','Carregal do Sal','Castanheira de Pera',
    'Castelo Branco','Castro Daire','Celorico da Beira','Coimbra','Condeixa-a-Nova',
    'Constância','Covilhã','Entroncamento','Estarreja','Ferreira do Zêzere',
    'Figueira da Foz','Figueira de Castelo Rodrigo','Figueiró dos Vinhos','Fornos de Algodres',
    'Fundão','Góis','Gouveia','Guarda','Idanha-a-Nova','Ílhavo','Lafões','Lardosa',
    'Leiria','Lourinhã','Lousã','Mação','Mangualde','Manteigas','Marinha Grande',
    'Mealhada','Mêda','Mira','Miranda do Corvo','Monsanto','Montemor-o-Velho',
    'Mortágua','Murtosa','Nazaré','Nelas','Óbidos','Oleiros','Oliveira de Frades',
    'Oliveira do Bairro','Oliveira do Hospital','Ourém','Ovar','Pamplihosa da Serra',
    'Penacova','Penamacor','Penela','Penha Garcia','Penalva do Castelo','Peniche',
    'Pinhel','Pombal','Porto de Mós','Proença-a-Nova','Rosmaninhal','Sabugal',
    'Santa Comba Dão','Sardoal','Sarzedas','Sátão','Seia','Sever do Vouga',
    'Sobral de Monte Agraço','Sobreira Formosa','Soure','São Miguel de Acha',
    'São Pedro do Sul','São Vicente da Beira','Tábua','Tomar','Tondela',
    'Torres Novas','Torres Vedras','Trancoso','Vagos','Vila Nova da Barquinha',
    'Vila Nova de Paiva','Vila Nova de Poiares','Vila Velha de Ródão','Vila de Rei',
    'Viseu','Vouzela','Zebreira',"Lisboa"
    ]

regiao_centro_upper = [m.upper() for m in regiao_centro]

df = pd.read_excel('contactos_contabilistas.xlsx')

df_filtered = df[~df['Morada2'].str.upper().apply(lambda x: any(region in x for region in regiao_centro_upper))]

df_filtered.to_excel('contactos_contabilistas(centro-removed).xlsx',index=False)