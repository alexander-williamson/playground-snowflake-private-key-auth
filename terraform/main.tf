terraform {
  required_version = ">= 1.6.0"

  required_providers {
    snowflake = {
      source  = "snowflakedb/snowflake"
      version = "~> 2.16"
    }
  }
}

provider "snowflake" {
  organization_name = var.organization_name
  account_name      = var.account_name
  user              = var.user
  role              = var.role
  warehouse         = var.warehouse

  authenticator          = "SNOWFLAKE_JWT"
  private_key            = file(var.private_key_path)
  private_key_passphrase = var.private_key_passphrase

  preview_features_enabled = [
    "snowflake_current_role_datasource", 
    "snowflake_current_account_datasource"
  ]
}

data "snowflake_current_role" "this" {}
data "snowflake_current_account" "this" {}
