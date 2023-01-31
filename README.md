# React Discord Bot

This project is a Discord bot written in Python using the discord.py library. It uses the Giphy and Tenor APIs to search for GIFs, and the Microsoft Translator Text API to translate messages.

This project also includes a Terraform configuration to deploy the bot to Azure.

## Prerequisites

- Python 3.11
- Giphy API Key
- Tenor API Key
- Microsoft Translator Text API Key
- Discord API Key

## Installation

Clone the repository:

`git clone https/github.com/Germain-L/react-discord-bot.git`

Install the dependencies:

`pip install -r requirements.txt`

Create a .env file in the root of the project and add the API keys:

```
GIPHY_KEY=<your_giphy_key>
TENOR_KEY=<your_tenor_key>
MICROSOFT_TRANSLATOR=<your_microsoft_translator_key>
MICROSOFT_LOCATION=<your_microsoft_location>
DISCORD_KEY=<your_discord_key>
```

Run the application:

`python main.py`


## Terraform
This file contains the Terraform configuration to deploy the bot to Azure. It includes the following resources:

 - azurerm_resource_group: Creates a resource group to store the resources.
 - azurerm_cognitive_account: Creates a Cognitive Services account for the Microsoft Translator Text API.
 - azurerm_container_registry: Creates a container registry to store the Docker image.
 - azurerm_container_registry_task: Creates a container registry task to build the Docker image.
 - azurerm_container_registry_task_schedule_run_now: Creates a container registry task schedule to run the task immediately.
 - azurerm_container_group: Creates a container group to run the Docker image.

The configuration also includes environment variables for
 - Giphy
 - Tenor
 - Discord API keys
 
These keys must be added to the `terraform.tfvars` file before running the Terraform commands.

