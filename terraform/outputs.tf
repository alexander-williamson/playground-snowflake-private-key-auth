output "current_role" {
  description = "Primary role in use for the current Snowflake session"
  value       = data.snowflake_current_role.this.name
}

output "current_account" {
  description = "Current Snowflake account identifier"
  value       = data.snowflake_current_account.this.account
}

output "current_region" {
  description = "Current Snowflake region"
  value       = data.snowflake_current_account.this.region
}
