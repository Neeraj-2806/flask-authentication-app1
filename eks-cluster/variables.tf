variable "cluster_name" {
  default = "blackforge-eks-cluster"
}

variable "region" {
  default = "us-east-1"
}

variable "vpc_id" {
  description = "Your default VPC ID"
  default     = "vpc-0ca1a3369eecd7f57" # your default VPC
}
variable "subnet_ids" {
  default = [
    "subnet-03952ce4f9e8ca19d",  # us-east-1a ✅
    "subnet-0b267de0db1c3eb11",  # us-east-1d ✅
    "subnet-0af2aca06e8d475bc"   # us-east-1c ✅
  ]
}

