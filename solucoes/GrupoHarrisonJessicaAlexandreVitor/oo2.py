import pandas as pd
from opencage.geocoder import OpenCageGeocode
import json
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

class Preparador:
    def __init__(self, dataset):
        self.df = pd.read_csv(dataset, sep='\n', delimiter=';')
        self.fields = list(self.df)
        self.n_lines = len(self.df)

    # Para cada coluna identique a quantidade de linhas com dados faltantes (em alguns casos,
    # o dado faltante é uma string vazia, em outros casos é uma string contendo algum valor do tipo:
    # "sem informação"). Faça um método que retorna a média de dados faltantes por coluna
    def search_nan(self):
        count = {}
        for field in self.fields:
            count[field] = sum(
                [1 if value == "" or value == "Sem Informações" else 0 for value in self.df[field]]) / self.n_lines
        return count

    # Para cada item identifique até qual nível taxônomico a ocorrência foi identificada.

    def n_tax(self):
        count = {}
        for i in range(self.n_lines):
            count[i] = ""
            for field in reversed(['Reino', 'Filo', 'Classe', 'Ordem', 'Familia', 'Genero', 'Especie']):
                if self.df.loc[i,field] != "Sem Informações" and self.df.loc[i,field] != "":
                    count[i] = field
                    break
        return count

    # Monte filtros de ocorrências por estados, nome de espécie (nome exato ou parte do nome)
    #  e categoria de ameaça, e outros filtros que julgar relevante.

    def filter(self):
        pass

    # Crie uma funcionalidade para avaliar se a informação de longitude e latitude corresponde
    #  a informação presente na localização

    def verify_lat_long(self, city, lat, long):
        key = '65b25c705a5349ad99c824ca809363b7'
        geocoder = OpenCageGeocode(key)
        results = geocoder.reverse_geocode(lat, long)
        try:
            r_city = results[0]['components']['city']
        except Exception as identifier:
            try:
                r_city = results[0]['components']['island']
            except Exception as identifier:
                r_city = ""
        self.pbar.update(1)
        return r_city == city

    def call(self):
        futures = {}
        count = {}
        self.pbar = tqdm(total=len(self.df))
        with ThreadPoolExecutor(max_workers=100) as executor:
            for i, (lat, long, city) in enumerate(zip(self.df['Latitude'], self.df['Longitude'], self.df['Municipio'])):
                futures[i] = executor.submit(self.verify_lat_long, city, lat, long)

        for i, f in futures.items():
            count[i] = f.result()
        return count

preparador = Preparador('portalbio_export_16-10-2019-14-39-54.csv')
print(preparador.n_lines)
print(preparador.call())
# key = '65b25c705a5349ad99c824ca809363b7'
# geocoder = OpenCageGeocode(key)
# results = geocoder.reverse_geocode(44.8303087, -0.5761911)
# print(results[0]['components']['city'])