# Terraform + Snowflake (Key-Pair Auth)

This example uses the latest Snowflake Terraform provider from `snowflakedb/snowflake` and authenticates with a local `.p8` private key.

It reads live session data from Snowflake and outputs:

- Current role (`CURRENT_ROLE()` via `snowflake_current_role`)
- Current account
- Current region

## Files

- `main.tf`: provider and data source configuration
- `variables.tf`: required inputs
- `outputs.tf`: values that prove connectivity/authentication
- `terraform.tfvars.example`: example local values

## Prerequisites

1. Terraform `>= 1.6.0`
2. Snowflake user configured for key-pair auth
3. Local private key file available (for example `../rsa_key.p8` from this folder)

## Usage

From this folder:

```bash
tfswitch 1.6.0
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform plan
terraform apply -auto-approve
```

Expected outputs include `current_role`, `current_account`, and `current_region`.

## Notes

- `terraform.tfvars` is ignored in `.gitignore` so secrets stay local.
- The `snowflake_current_role` data source is currently preview in the provider, so this example enables:

```hcl
preview_features_enabled = [
  "snowflake_current_role_datasource", 
  "snowflake_current_account_datasource"
]
```

