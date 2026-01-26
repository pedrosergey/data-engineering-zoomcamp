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
  project     = var.project
  region      = var.region
}

resource "google_bigquery_dataset" "homework_dataset" {
  dataset_id                  = var.bq_dataset_name
  location                    = var.bq_location
  default_table_expiration_ms = 3600000

}

resource "google_storage_bucket" "homework_bucket" {
  name          = var.cs_bucket_name
  location      = var.cs_location
  force_destroy = true
}