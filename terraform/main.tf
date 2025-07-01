
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "example" {
  bucket = "infra-drift-bucket-example"
  acl    = "private"
  tags = {
    Environment = "Dev"
    Owner       = "DevOps"
  }
}

resource "aws_config_configuration_recorder" "recorder" {
  name     = "default"
  role_arn = aws_iam_role.config_role.arn
  recording_group {
    all_supported = true
  }
}

resource "aws_config_delivery_channel" "channel" {
  name           = "default"
  s3_bucket_name = aws_s3_bucket.example.bucket
  depends_on     = [aws_config_configuration_recorder.recorder]
}

resource "aws_iam_role" "config_role" {
  name = "aws-config-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "config.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "config_policy" {
  role       = aws_iam_role.config_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSConfigRole"
}
