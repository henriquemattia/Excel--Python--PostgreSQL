import pandas as pd
import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(host=os.environ["DB_HOST"],
                              dbname=os.environ["DB_NAME"],
                              user=os.environ["DB_USER"],
                              password=os.environ["DB_PASS"])
cursor = conn.cursor()

#          INSERIR NOVOS DADOS NA TABELA

planilha = pd.read_excel("products.xlsx")

for i, DADOS in enumerate(planilha['id']):
    id = planilha.loc[i,"id"]
    category = planilha.loc[i,"category"]
    name = planilha.loc[i,"name"]
    price = planilha.loc[i,"price"]
    desc_price = planilha.loc[i,"desc_price"]
    sku = planilha.loc[i,"sku"]
    route = planilha.loc[i,"route"]
    img_main = planilha.loc[i,"img_main"]
    img_front = planilha.loc[i,"img_front"]
    img_right = planilha.loc[i,"img_right"]
    img_left = planilha.loc[i,"img_left"]
    img_back = planilha.loc[i,"img_back"]
    highlighs = planilha.loc[i,"highlighs"]
    is_available = planilha.loc[i,"is_available"]      
    
    comando = "insert into public.testes (id, category, name, price, desc_price, sku, route, img_main, img_front, img_right, img_left, img_back, highlights, is_available) VALUES "
    dados = f"({id}, '{category}', '{name}', {price}, {desc_price}, '{sku}', '{route}','{img_main}', '{img_front}', '{img_right}', '{img_left}', '{img_back}', {highlighs}, {is_available})"
    sql = comando + dados
    # print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        continue
    
conn.close()



#           ATUALIZAR DADOS NA TABELA


planilha = pd.read_excel("products.xlsx")

for i, DADOS in enumerate(planilha['id']):
    id = planilha.loc[i,"id"]
    category = planilha.loc[i,"category"]
    name = planilha.loc[i,"name"]
    price = planilha.loc[i,"price"]
    desc_price = planilha.loc[i,"desc_price"]
    sku = planilha.loc[i,"sku"]
    route = planilha.loc[i,"route"]
    img_main = planilha.loc[i,"img_main"]
    img_front = planilha.loc[i,"img_front"]
    img_right = planilha.loc[i,"img_right"]
    img_left = planilha.loc[i,"img_left"]
    img_back = planilha.loc[i,"img_back"]
    highlighs = planilha.loc[i,"highlighs"]
    is_available = planilha.loc[i,"is_available"]    
    
    
    i = f"id = {id}, "
    c = f"category = '{category}', "
    n = f"name = '{name}', "
    p = f"price = {price}, "
    d_p = f"desc_price = {desc_price}, "
    s = f"sku = '{sku}', "