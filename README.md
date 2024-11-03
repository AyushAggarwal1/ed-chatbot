# ed-chatbot
Chatbot is to be deployed as subject tutors

To install dependencies use
```pip install -r requirements.txt```

To run the project locally use
```uvicorn main:app --reload``` 

# Chatbot Deployment Guide

This README provides a step-by-step guide on how to host and deploy your chatbot on Microsoft Teams and Google Chat. 

## Table of Contents

- [Prerequisites](#prerequisites)
- [Hosting on Microsoft Teams](#hosting-on-microsoft-teams)
  - [Step 1: Create a Microsoft Teams App](#step-1-create-a-microsoft-teams-app)
  - [Step 2: Register Your Bot with Azure Bot Service](#step-2-register-your-bot-with-azure-bot-service)
  - [Step 3: Set Up Your Bot's Endpoint](#step-3-set-up-your-bots-endpoint)
  - [Step 4: Test Your Bot in Microsoft Teams](#step-4-test-your-bot-in-microsoft-teams)
- [Hosting on Google Chat](#hosting-on-google-chat)
  - [Step 1: Create a Google Cloud Project](#step-1-create-a-google-cloud-project)
  - [Step 2: Enable Google Chat API](#step-2-enable-google-chat-api)
  - [Step 3: Deploy Your Bot](#step-3-deploy-your-bot)
  - [Step 4: Test Your Bot in Google Chat](#step-4-test-your-bot-in-google-chat)
- [Conclusion](#conclusion)

## Prerequisites

- An active account with Microsoft Azure.
- An active Google Cloud account.
- Basic understanding of how to work with APIs and webhooks.
- Your chatbot code deployed and accessible over the internet (e.g., using services like Heroku, AWS, or ngrok for local testing).

## Hosting on Microsoft Teams

### Step 1: Create a Microsoft Teams App

1. Go to the [Microsoft Teams Developer Portal](https://dev.teams.microsoft.com/) and sign in.
2. Click on **Apps** and select **Create a new app**.
3. Fill in the app details (name, description, icons).
4. Add **Bot** as a capability and configure your bot settings.

### Step 2: Register Your Bot with Azure Bot Service

1. Visit the [Azure Portal](https://portal.azure.com/).
2. Search for **Bot Services** and create a new bot registration.
3. Enter your bot’s name, messaging endpoint, and select the appropriate pricing tier.
4. Save the **App ID** and generate a **password** (client secret) for authentication.

### Step 3: Set Up Your Bot's Endpoint

1. Ensure your bot's server is deployed and accessible.
2. Update the messaging endpoint in Azure Bot Service with your bot’s URL (e.g., `https://<your_ngrok_subdomain>.ngrok.io/chat`).

### Step 4: Test Your Bot in Microsoft Teams

1. Use the **App Studio** in Microsoft Teams to add your bot to a team or a chat.
2. Send messages to your bot and check its responses.
3. Monitor logs in your bot’s server for any errors.

## Hosting on Google Chat

### Step 1: Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on **Select a Project** and then **New Project**.
3. Name your project and enable billing.

### Step 2: Enable Google Chat API

1. In your Google Cloud project, navigate to **APIs & Services** > **Library**.
2. Search for **Google Chat API** and enable it for your project.

### Step 3: Deploy Your Bot

1. Navigate to **APIs & Services** > **Credentials**.
2. Create credentials for a **Service Account** and generate a private key (JSON format).
3. Use Google Cloud Functions or App Engine to deploy your chatbot code. Ensure that the webhook endpoint is properly set.

### Step 4: Test Your Bot in Google Chat

1. Go to Google Chat and invite your bot to a chat room or start a direct message with it.
2. Test the bot by sending messages and verifying its responses.
3. Check your server logs for any issues.

## Conclusion

You have successfully hosted your chatbot on both Microsoft Teams and Google Chat. Make sure to continuously monitor and improve your bot based on user feedback. For further enhancements, explore additional capabilities provided by both platforms.
