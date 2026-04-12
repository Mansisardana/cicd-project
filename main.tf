provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_instance" "devops" {
  ami           = "ami-0f8faa29480e7e6de"
  instance_type = "t3.micro"

  tags = {
    Name = "cicd-project-server"
  }
}
