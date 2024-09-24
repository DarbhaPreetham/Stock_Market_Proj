provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "stock_predictor" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI
  instance_type = "t2.micro"
  key_name      = var.key_name

  tags = {
    Name = "Stock Predictor"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo amazon-linux-extras install docker -y",
      "sudo service docker start",
      "sudo usermod -aG docker ec2-user",
      "sudo docker run -d -p 5000:5000 $DOCKER_HUB_USERNAME/stock-predictor-app"
    ]
  }

  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file(var.private_key_path)
    host        = aws_instance.stock_predictor.public_ip
  }
}

output "instance_ip" {
  value = aws_instance.stock_predictor.public_ip
}
