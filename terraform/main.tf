resource "local_file" "app_info" {
    filename="app_info.txt"
    content="ML API Project is ready"
}

resource "local_file" "env_config" {
    filename="env.txt"
    content="ENV=development\nPORT=8000"
}
resource "local_file" "api_config" {
  filename = "../config.json"
  content  = <<EOT
{
  "model": "logistic_regression",
  "version": "1.0",
  "port": 8000
}
EOT
}