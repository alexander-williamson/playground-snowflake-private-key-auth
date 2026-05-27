variable "organization_name" {
  description = "Snowflake organization name"
  type        = string
}

variable "account_name" {
  description = "Snowflake account name"
  type        = string
}

variable "user" {
  description = "Snowflake username"
  type        = string
}

variable "role" {
  description = "Role to use for the provider session"
  type        = string
}

variable "warehouse" {
  description = "Warehouse to use for the provider session"
  type        = string
}

variable "private_key_path" {
  description = "Path to the local Snowflake private key (.p8)"
  type        = string
}

variable "private_key_passphrase" {
  description = "Passphrase for the private key"
  type        = string
  sensitive   = true
  nullable    = true
  default     = null
}
