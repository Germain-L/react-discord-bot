output "ressource_group_name" {
  value = azurerm_resource_group.rg.name
}
  
output "cognitive_service_name" {
  value = azurerm_cognitive_account.cognitive.name
}
  
output "acr_name" {
  value = azurerm_container_registry.acr.name
}

output "container_group_name" {
  value = azurerm_container_group.containers.name
}



