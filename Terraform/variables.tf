variable "aws_region" {
  description = "The AWS region to deploy in"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.medium"
}


variable "key_name" {
  description = "SSH key name to access the EC2 instance"
  type        = string
}

variable "ami_id" {
  description = "AMI ID for the instance"
  type        = string
  default     = "ami-02d26659fd82cf299" 
}