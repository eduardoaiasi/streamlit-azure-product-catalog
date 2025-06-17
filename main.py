import streamlit as st
from azure.storage.blob import BlobServiceClient
import os 
import pymssql
import uuid
import json
from dotenv import load_dotenv
load_dotenv()



blobConnetionString = os.getenv('BLOB_CONNECTION_STRING')
blobContainerName = os.getenv('BLOB_CONTAINER_NAME')
blobAccountName = os.getenv('BLOB_ACCOUNT_NAME')

SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USER = os.getenv('SQL_USER')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')


#Formulário de cadastro de produtos
st.title('Cadastro de Produtos')

product_name = st.text_input('Nome do Produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format = '%.2f')
product_description = st.text_area('Descrição do Produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'png', 'jpeg'])

#Salvando imagem no blob
def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnetionString)
    container_client = blob_service_client.get_container_client(blobContainerName)
    blob_name = str(uuid.uuid4()) + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(),overwrite=True)
    image_url = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
    return image_url

#Inserindo produto
def insert_product(product_name, product_price, product_description, product_image):
    try:
        image_url = upload_blob(product_image)
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        insert_sql = f"INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES ('{product_name}', {product_price}, '{product_description}', '{image_url}')"
        cursor.execute(insert_sql)
        conn.commit()
        conn.close()

        return True
    except Exception as e:
        st.error(f'Erro ao inserir produto: {e}')
        return False

#listar produtos
def list_products():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produtos")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f'Erro ao listar produtos: {e}')
        return []
    
def list_products_screen():
    products = list_products()
    for product in products:
        st.write(f'Nome: {product[1]}')
        st.write(f'Preço: {product[2]}')
        st.write(f'Descrição: {product[3]}')
        st.image(product[4], width=200)

if st.button('Salvar Produto'):
    insert_product(product_name, product_price, product_description, product_image)
    return_message = 'Produto salvo com sucesso'

st.header('Produtos Cadastrados')

if st.button('Listar Produtos'):
    list_products_screen()
    return_message = 'Produtos listados com sucesso'