import snowflake.connector
import dotenv
import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
config = dotenv.dotenv_values(script_dir / ".env")  # take environment variables

def debug(message: str) -> None:
    print(f"DEBUG: {message}", file=sys.stderr)

conn_params = {
    'account': config['ACCOUNT_IDENTIFIER'],
    'user': config['USER'],
    'authenticator': 'SNOWFLAKE_JWT',
    'login_timeout': 5,
    'private_key_file': str(script_dir.parent / 'rsa_key.p8'),
    'private_key_file_pwd': config['PRIVATE_KEY_FILE_PASSWORD'],
    'warehouse': config['SNOWFLAKE_WAREHOUSE'],
    'database': config['SNOWFLAKE_DATABASE'],
    'schema': config['SNOWFLAKE_SCHEMA']
}

ctx = None
cs = None

try:
    debug(f"env_file={script_dir / '.env'}")
    debug(f"account={conn_params['account']}")
    debug(f"user={conn_params['user']}")
    debug(f"private_key_file={conn_params['private_key_file']}")
    debug(f"warehouse={conn_params['warehouse']!r}")
    debug(f"database={conn_params['database']!r}")
    debug(f"schema={conn_params['schema']!r}")

    ctx = snowflake.connector.connect(**conn_params)
    cs = ctx.cursor()
    cs.execute("SELECT CURRENT_USER()")
    print(cs.fetchone()[0])
except Exception as exc:
    print(f"Snowflake request failed: {exc}", file=sys.stderr)
    raise SystemExit(1)
finally:
    if cs is not None:
        cs.close()
    if ctx is not None:
        ctx.close()
