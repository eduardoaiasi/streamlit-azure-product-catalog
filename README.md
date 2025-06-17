# 🛍️ Catálogo de Produtos com Streamlit e Azure

Este projeto demonstra uma aplicação web simples construída com **Streamlit** (Python) para gerenciamento de produtos, utilizando serviços de nuvem da **Microsoft Azure** para armazenamento de dados e imagens.
A aplicação permite que os usuários cadastrem novos produtos (com nome, preço, descrição e uma imagem) e visualizem a lista de produtos já cadastrados.

## ✨ Tecnologias Utilizadas

* **Frontend:**
    * [Streamlit](https://streamlit.io/) (Python Web Framework para Data Apps)
    * Python

* **Backend / Serviços de Nuvem (Microsoft Azure):**
    * **Azure SQL Database:** Para armazenamento dos dados estruturados dos produtos (nome, preço, descrição, URL da imagem).
    * **Azure Blob Storage:** Para armazenamento das imagens dos produtos.
    * **Azure Key Vault (Implícito/Recomendado):** Para gerenciar credenciais de forma segura. (Mencione se você usaria isso em um ambiente de produção).
    * **Azure Resource Group:** Para agrupar e gerenciar os recursos da aplicação.

* **Bibliotecas Python:**
    * `streamlit`
    * `azure-storage-blob`
    * `pymssql`
    * `python-dotenv`
    * `uuid`

## 🚀 Funcionalidades

* **Cadastro de Produtos:**
    * Nome do produto
    * Preço do produto
    * Descrição do produto
    * Upload de imagem do produto (salva no Azure Blob Storage)
* **Listagem de Produtos:**
    * Exibe todos os produtos cadastrados com seus detalhes e imagens.

## ⚙️ Configuração do Ambiente

Siga os passos abaixo para configurar e executar a aplicação localmente.

### Pré-requisitos

* **Python 3.x** instalado.
* Conta ativa no **Microsoft Azure**.
* **Git** instalado.

### 1. Clonar o Repositório

```bash
git clone https://github.com/xTsunammyx/streamlit-azure-product-catalog.git
cd streamlit-azure-product-catalog

### 2. Instalar Dependências
Bash

pip install -r requirements.txt
(Crie um arquivo requirements.txt com o conteúdo abaixo se ainda não tiver um)

Conteúdo de requirements.txt:

streamlit
azure-storage-blob
pymssql
python-dotenv

3. Configurar Recursos no Azure
Você precisará criar e configurar os seguintes recursos no Azure:

A. Azure SQL Database
Crie um servidor SQL do Azure:

Escolha um nome para o servidor (ex: sql.database.windows.net).
Defina um nome de usuário e senha de administrador para o servidor.
Crie um Banco de Dados SQL dentro do servidor:

Crie um banco de dados (ex: sqldevlab001).
Configure o Firewall do Servidor SQL:

No seu servidor SQL no Azure Portal, vá em "Rede" (Networking).
Em "Regras de firewall", adicione o seu endereço IP de cliente atual para permitir a conexão.
Se for implantar a aplicação no Azure, certifique-se de que a opção "Permitir que os serviços e recursos do Azure acessem este servidor" esteja habilitada.
Crie a Tabela Produtos:
Conecte-se ao seu Banco de Dados SQL usando o Azure Data Studio ou SQL Server Management Studio (SSMS) e execute o seguinte script SQL para criar a tabela Produtos:

SQL

CREATE TABLE Produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    descricao NVARCHAR(MAX),
    imagem_url NVARCHAR(MAX)
);

B. Azure Blob Storage
Crie uma Conta de Armazenamento (Storage Account):

No Azure Portal, crie uma "Conta de Armazenamento".

Escolha uma localização e um tipo de desempenho (Standard LRS ou GRS é geralmente suficiente).
Crie um Contêiner de Blob:
Dentro da sua Conta de Armazenamento, vá para "Contêineres" (Containers).
Crie um novo contêiner (ex: imagens-produtos).
Defina o nível de acesso para "Blob (acesso de leitura anônimo para blobs)" para que as imagens possam ser exibidas publicamente pela URL.
Obtenha a String de Conexão:
Na sua Conta de Armazenamento, vá para "Chaves de acesso" (Access keys).
Copie a "Cadeia de conexão" (Connection string) de key1.
4. Criar o Arquivo .env
Crie um arquivo chamado .env na raiz do seu projeto (no mesmo diretório de main.py) e preencha-o com suas credenciais e informações de conexão do Azure. NÃO COMPROMETA ESTE ARQUIVO EM REPOSITÓRIOS PÚBLICOS.

Snippet de código

BLOB_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=suacontadearmazenamento;AccountKey=sua_chave_aqui;EndpointSuffix=core.windows.net"
BLOB_CONTAINER_NAME="imagens-produtos"
BLOB_ACCOUNT_NAME="suacontadearmazenamento"

SQL_SERVER=""
SQL_DATABASE=""
SQL_USER=""
SQL_PASSWORD=""
(Substitua os valores entre aspas pelos seus próprios!)

5. Executar a Aplicação
Com o arquivo .env configurado, execute a aplicação Streamlit:

PowerShell

python -m streamlit run main.py
A aplicação será aberta automaticamente no seu navegador padrão, geralmente em http://localhost:8501.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
