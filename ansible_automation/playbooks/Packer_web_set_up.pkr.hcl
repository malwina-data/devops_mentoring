packer {
  required_plugins {
    ansible = {
      version = ">= 1.0.0"
      source = "github.com/hashicorp/ansible"
    }
  }
}

variable "region" {}
variable "vpc_id" {}
variable "web_subnet_id" {}
variable "security_group_id" {}
variable "db_instance_id" {}

source "amazon-ebs" "web" {
  region                  = var.region
  instance_type           = "t3.micro"
  ami_name                = "web-ami"
  source_ami              = "ami-04eeb630f180cea95"
  ssh_username            = "ec2-user"
  associate_public_ip_address = true
  vpc_id                  = var.vpc_id
  subnet_id               = var.web_subnet_id
  security_group_ids      = [var.security_group_id]

  tags = {
    Name = "WebInstance"
  }
}

build {
  sources = ["source.amazon-ebs.web"]

  provisioner "ansible" {
    playbook_file = "web_playbook.yml"
  }
}
