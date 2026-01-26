# Terraform: Infrastructure as Code for GCP

This folder contains Terraform configurations to provision Google Cloud Platform (GCP) resources for data engineering workloads.

## 📁 Contents

- **`main.tf`** - Main Terraform configuration defining GCP provider and resources
- **`variables.tf`** - Variable definitions (⚠️ excluded from version control)
- **`terraform.tfstate`** - Current state of managed infrastructure (⚠️ excluded from version control)
- **`keys/`** - Directory for GCP service account credentials (⚠️ excluded from version control)

## 🎯 What gets provisioned

This Terraform configuration creates:
- **BigQuery Dataset** - Data warehouse for storing and querying large datasets
- Configurable dataset location (default: EU)
- Table expiration settings for automatic cleanup

## 🚀 Quick start

### Prerequisites

1. **GCP Account** with billing enabled
2. **Terraform CLI** installed ([Download](https://www.terraform.io/downloads))
3. **GCP Service Account** with appropriate permissions:
   - BigQuery Admin
   - Storage Admin (if working with GCS)

### Setup steps

1. **Create a service account key**
   - Go to GCP Console → IAM & Admin → Service Accounts
   - Create a new service account or use existing
   - Generate a JSON key file
   - Save it to `keys/my_creds.json`

2. **Create `variables.tf`** (template):

```terraform
variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset."
  type        = string
  default     = "your_dataset_name"
}

variable "bq_location" {
  description = "The location of the BigQuery dataset."
  type        = string
  default     = "EU"  # or "US"
}

variable "credentials" {
  description = "Path to the GCP credentials JSON file."
  type        = string
  default     = "./keys/my_creds.json"
}

variable "project_id" {
  description = "The GCP project ID."
  type        = string
  default     = "your-project-id"
}

variable "region" {
  description = "The GCP region."
  type        = string
  default     = "us-central1"  # or "europe-west1", etc.
}
```

3. **Initialize Terraform**

```bash
terraform init
```

4. **Review the plan**

```bash
terraform plan
```

5. **Apply the configuration**

```bash
terraform apply
```

## 🔑 Key Terraform concepts

### Core workflow
1. **`terraform init`** - Initialize working directory and download providers
2. **`terraform plan`** - Preview changes before applying
3. **`terraform apply`** - Create/update infrastructure
4. **`terraform destroy`** - Remove all managed resources

### State management
- **`terraform.tfstate`** - Tracks current infrastructure state
- **Never commit state files** - They contain sensitive information
- Consider using remote state (GCS bucket) for team collaboration

### Variables
- Define in `variables.tf` with type and default values
- Override with environment variables: `TF_VAR_project_id`
- Or use `.tfvars` files (also excluded from version control)

## 🛡️ Security best practices

✅ **Do**:
- Keep credentials in `keys/` folder (gitignored)
- Use service accounts with minimal required permissions
- Store state files securely (use remote backend for teams)
- Review `terraform plan` output before applying

❌ **Don't**:
- Commit `variables.tf` with real values to version control
- Commit credential files or state files
- Use overly permissive IAM roles
- Share your `.tfvars` or credential files publicly

## 📊 Managed resources

### BigQuery Dataset
```terraform
resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.bq_location
  default_table_expiration_ms = 3600000  # 1 hour
}
```

After applying, you can:
- Query the dataset from BigQuery Console
- Load data using `bq` CLI or Python libraries
- Create tables and views programmatically

## 🧹 Cleanup

When you're done experimenting:

```bash
terraform destroy
```

This will remove all resources created by Terraform (but double-check the plan first!).

## 💡 Tips

- Use `terraform fmt` to auto-format your `.tf` files
- Use `terraform validate` to check syntax
- Pin provider versions for reproducibility
- Consider using Terraform workspaces for multiple environments
- Use remote state with GCS for team collaboration

## 🔗 Additional resources

- [Terraform GCP Provider Docs](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [BigQuery Terraform Resources](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset)
- [GCP Best Practices](https://cloud.google.com/docs/terraform/best-practices-for-terraform)

---

**Next steps**: Use the provisioned BigQuery dataset to load and query data from your Docker-based ingestion pipeline!
