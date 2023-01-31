resource "azurerm_resource_group" "rg" {
  name = var.ressource_group_name
  location = var.location
}

resource "azurerm_cognitive_account" "cognitive" {
  name = "translator"
  location = var.location
  resource_group_name = azurerm_resource_group.rg.name
  kind = "TextTranslation"

  sku_name = "F0"
}

resource "azurerm_container_registry" "acr" {
  name                = "reactgifbotacr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_container_registry_task" "build" {
  name                  = "build-bot-task"
  container_registry_id = azurerm_container_registry.acr.id
  platform {
    os = "Linux"
  }
  docker_step {
    dockerfile_path      = "Dockerfile"
    context_path         = var.github_repository
    context_access_token = var.GITHUB_ACCESS_TOKEN
    image_names          = ["bot:latest"]
  }
}

resource "azurerm_container_registry_task_schedule_run_now" "run" {
  container_registry_task_id = azurerm_container_registry_task.build.id
}

resource "azurerm_container_group" "containers" {
  name                = "containers"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  ip_address_type     = "None"
  os_type             = "Linux"

  image_registry_credential {
    server   = azurerm_container_registry.acr.login_server
    username = azurerm_container_registry.acr.admin_username
    password = azurerm_container_registry.acr.admin_password
  }

  container {
    name  = "bot"
    image = "${azurerm_container_registry.acr.login_server}/bot:latest"
    cpu   = "1"
    memory = "1.5"

    environment_variables = {
      "TENOR_KEY" = var.TENOR_KEY
      "GIPHY_KEY" = var.GIPHY_KEY
      "MICROSOFT_TRANSLATOR" = azurerm_cognitive_account.cognitive.primary_access_key
      "MICROSOFT_LOCATION" = azurerm_cognitive_account.cognitive.location
      "DISCORD_KEY" = var.DISCORD_KEY
    }
  }

  depends_on = [
    azurerm_container_registry_task_schedule_run_now.run
  ]
}