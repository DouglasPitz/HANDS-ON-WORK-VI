import psycopg2

# Configurações do banco de dados
POSTGRESQL_IP = "localhost"  # Nome do serviço Docker
POSTGRESQL_LOGIN = "postgres"
POSTGRESQL_PASSWORD = "postgrespw"
POSTGRESQL_DATABASE = "postgres"
POSTGRESQL_PORT = 5435  # Porta padrão do PostgreSQL no Docker


# Função de conexão com o banco de dados
def get_db_connection():
    connection = psycopg2.connect(
        host=POSTGRESQL_IP,
        user=POSTGRESQL_LOGIN,
        password=POSTGRESQL_PASSWORD,
        database=POSTGRESQL_DATABASE,
        port=POSTGRESQL_PORT
    )
    return connection
