terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project_id
  region      = var.region
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = var.bq_dataset_name
  location                    = var.bq_location
  default_table_expiration_ms = 3600000

}