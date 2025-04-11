# playground-snowflake-private-key-auth

Here's an example in Python that uses a Private Key File and unlock password to connect to Snowflake. The password is used to unlock the Private Key File before it is used.

## Steps to get this example working
1. Ensure you've got a Python 3 environment
   ```
   brew install pyenv
   pyenv install 3
   pyenv local 3
   exec "$SHELL"
   python --version
   ```
2. Use a Virtual Env:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install the Snowflake Python Connector from `requirements.txt`
   ```
   pip install -r requirements.txt
   ```
4. Copy the values from `.env.example` into `.env` file
5. Update the values in the configuration file. Use your private key which has been given to you from your admin.
6. Run `python main.py`. You should see a successful connection with the cursor dumped into the console.

```
> python main.py

<snowflake.connector.cursor.SnowflakeCursor object at 0x104aca990>
```

Any errors mean something is wrong. A JWT error means your Private Key / Public Key (stored in Snowflake) as mismatched - talk to your admin.

## Validating your key and password

Run this command (change `rsa_key.p8` to point to your `.p8` private key file):

```
openssl pkcs8 -in rsa_key.p8 -inform PEM -outform PEM > /dev/null
```

You'll be prompted for your password. Enter it (or try pasting into your console etc). It will be hidden. The output will also be hidden. 

You will get a blank result if success, or an error if the password was wrong.

## Useful Links
- Generating Private Key Pairs in Snowflake https://docs.snowflake.com/en/user-guide/key-pair-auth
- Validate p8 password https://stackoverflow.com/questions/59416711/is-there-an-openssl-command-that-checks-the-validity-of-a-p8-certificate