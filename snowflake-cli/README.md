Using the Snowflake CLI with key-pair authentication.

See [Snowflake CLI installation](https://docs.snowflake.com/en/developer-guide/snowflake-cli/installation/installation).

## Install

On macOS:

```bash
brew tap snowflakedb/snowflake-cli
brew update
```

## Generate a key pair

Follow the [Snowflake key-pair authentication guide](https://docs.snowflake.com/en/user-guide/key-pair-auth).

I keep the keys in `~/.snowflake`:

```bash
openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out rsa_key.p8
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
```

Use a password to protect the private key.

## Configure the CLI connection

Create `~/.snowflake/connections.toml` and add a connection named `beans`:

```toml
[beans]
account = "example.eu-west-1"
user = "example@example.com"
database = "EXAMPLE_DATABASE"
schema = "EXAMPLE_SCHEMA"
warehouse = "EXAMPLE_WAREHOUSE"
role = "EXAMPLE_ROLE"
authenticator = "SNOWFLAKE_JWT"
private_key_path = "/Users/example/.snowflake/rsa_key.p8"
```

You do not have to store `private_key_password` in the file. You can pass it via an environment variable instead.

## Register the public key

Set the Snowflake user's `RSA_PUBLIC_KEY` property:

```sql
ALTER USER "example@example.com" SET RSA_PUBLIC_KEY='MIIB...QehOXLKlq2E8hwIDAQAB';
```

## Test the connection

```bash
snow connection test --connection beans
```