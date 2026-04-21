import requests
from typing import Optional, Dict, Any, Union
from .resources.messaging import Messaging
from .resources.session import Session
from .resources.webhooks import Webhooks
from .resources.chats import Chats
from .resources.groups import Groups
from .resources.contacts import Contacts
from .resources.channels import Channels
from .resources.labels import Labels
from .resources.profile import Profile
from .resources.status import Status

class WawpClient:
    def __init__(self, instance_id: str, access_token: str, base_url: str = 'https://api.wawp.net/v2/'):
        self.instance_id = instance_id
        self.access_token = access_token
        self.base_url = base_url.rstrip('/') + '/'
        
        # Initialize resources
        self.messaging = Messaging(self)
        self.session = Session(self)
        self.webhooks = Webhooks(self)
        self.chats = Chats(self)
        self.groups = Groups(self)
        self.contacts = Contacts(self)
        self.channels = Channels(self)
        self.labels = Labels(self)
        self.profile = Profile(self)
        self.status = Status(self)

    def request(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        url = self.base_url + path.lstrip('/')
        
        headers = kwargs.get('headers', {})
        headers['Authorization'] = f'Bearer {self.access_token}'
        headers['X-Instance-ID'] = self.instance_id
        
        kwargs['headers'] = headers
        
        response = requests.request(method, url, **kwargs)
        
        if not response.ok:
            try:
                error_data = response.json()
                message = error_data.get('message', response.text)
            except:
                message = response.text
            raise Exception(f"Wawp API Error ({response.status_code}): {message}")
            
        return response.json()
