
data "aws_vpc" "default" {
  default = true
}


resource "aws_security_group" "ansible_sg" {
  name        = "ansible_sg"
  description = "Security group for ansible instances"
  vpc_id      = data.aws_vpc.default.id

  
  dynamic "ingress" {
    for_each = var.port_number
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

 
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "ansible-sg"
  }
}


resource "aws_instance" "ansible" {
  for_each      = var.instance_type
  ami           = var.ami_id
  instance_type = each.value

  vpc_security_group_ids = [aws_security_group.ansible_sg.id]

  tags = {
    Name = each.key
  }
}
