// Copyright 2023 John Hurst
// John Hurst (john.b.hurst@gmail.com)
// 2023-06-05

terraform {
    required_providers {
        google = {
            source  = "hashicorp/google"
            version = "4.67.0"
        }
    }
}

provider "google" {
    project = "johnbhurst-ml-tones"
    # region  = "australia-southeast2"
}

variable "billing_account" {
    type = string
    sensitive  = true
}

resource "google_project" "johnbhurst_ml_tones_project" {
    name            = "johnbhurst-ml-tones"
    project_id      = "johnbhurst-ml-tones"
    billing_account = var.billing_account
#   org_id          = "" // enter your organization id here if applicable
}

resource "google_project_service" "johnbhurst_ml_tones_storage" {
    # project = google_project.johnbhurst_ml_tones_project.project_id
    service = "storage-component.googleapis.com"
    disable_on_destroy = false
}

resource "google_storage_bucket" "johnbhurst_ml_tones_dvc_bucket" {
    name     = "johnbhurst-ml-tones-dvc"
    location = "australia-southeast2"

    // Ensure that the bucket is globally unique
    force_destroy = true

    cors {
        origin           = ["*"]
        method           = ["GET", "HEAD"]
        response_header  = ["Content-Type"]
        max_age_seconds  = 3600
    }

    website {
        main_page_suffix = "index.html"
    }
}

resource "google_storage_bucket_iam_binding" "johnbhurst_ml_tones_dvc_bucket_public_read_binding" {
  bucket = google_storage_bucket.johnbhurst_ml_tones_dvc_bucket.name
  role   = "roles/storage.objectViewer"

  members = [
    "allUsers",
  ]
}

output "bucket_url" {
    value = "gs://${google_storage_bucket.johnbhurst_ml_tones_dvc_bucket.name}"
}
