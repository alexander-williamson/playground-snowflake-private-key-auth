import snowflake.connector
import dotenv

config = dotenv.dotenv_values(".env")  # take environment variables

conn_params = {
    'account': config['ACCOUNT_IDENTIFIER'],
    'user': config['USER'],
    'authenticator': 'SNOWFLAKE_JWT',
    'private_key_file': 'rsa_key.p8',
    'private_key_file_pwd': config['PRIVATE_KEY_FILE_PASSWORD'],
    'warehouse': config['SNOWFLAKE_WAREHOUSE'],
    'database': config['SNOWFLAKE_DATABASE'],
    'schema': config['SNOWFLAKE_SCHEMA']
}

ctx = snowflake.connector.connect(**conn_params)
cs = ctx.cursor()

print(cs)
