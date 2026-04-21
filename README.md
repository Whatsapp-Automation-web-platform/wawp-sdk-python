# Wawp Python SDK 🐍

The official Python client for the **Wawp WhatsApp Automation Platform**. Build powerful WhatsApp bots and automation scripts with ease.

## 🌟 Features
- **Resource-Based API**: Clean syntax like `client.messaging.send_text()`.
- **Full V2 Support**: Messaging, Groups, Channels, Labels, and more.
- **Webhook Security**: Built-in methods to verify HMAC signatures.
- **Synchronous & Powerful**: Optimized for quick automation and AI integration.

## 📦 Installation
```bash
pip install wawp-sdk
```

## ⌨️ Quick Start
```python
from wawp_sdk import WawpClient

# Initialize the client
client = WawpClient(instance_id='YOUR_ID', access_token='YOUR_TOKEN')

# Send a text message
client.messaging.send_text('201234567890@c.us', 'Hello from the Python SDK!')

# Check session status
info = client.session.info()
print(f"Session Status: {info['status']}")
```

## 🏗️ The Wawp Ecosystem
- **[JS/TS SDK](https://www.npmjs.com/package/@wawp/sdk)**: For Node.js environments.
- **[PHP SDK](https://github.com/Whatsapp-Automation-web-platform/wawp-sdk-php)**: For PHP & Laravel.
- **[Live API Docs](https://api.wawp.net)**: Test endpoints interactively.

---
© 2026 Wawp API. All rights reserved.
