variable "cidr_block" {
}
variable "cidr_public_subnet" {
}
variable "cidr_public_subnet2" {
}
variable "cidr_private_subnet" {
}
variable "cidr_private_subnet2" {}
variable "subnet_ids" {
    type = list(string)
}
variable "cluster_name" {}
variable  "db_username" {}
variable "db_password" {}
variable "db_name" {}
variable "vpc_id" {}
variable "public_subnet_ids"{
    type = list(string)
}