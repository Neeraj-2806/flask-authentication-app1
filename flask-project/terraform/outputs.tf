output "rds_endpoint"{
    value = aws_db_instance.default.endpoint
}
output "vpc_id" {
    value = aws_vpc.first-vpc.id
}