terraform {
  backend "s3" {
    bucket  = "danit-bogdan-tfstate-340822112160"
    key     = "eks/terraform.tfstate"
    region  = "eu-central-1"
    encrypt = true
  }
}
