import os

class Messaging:
    def __init__(self, client):
        self.client = client

    def send_text(self, chat_id: str, message: str) -> dict:
        return self.client.request('POST', 'send/text', json={
            'chatId': chat_id,
            'message': message
        })

    def send_image(self, chat_id: str, url: str, caption: str = None) -> dict:
        data = {'chatId': chat_id, 'url': url}
        if caption: data['caption'] = caption
        return self.client.request('POST', 'send/image', json=data)

    def send_local_file(self, chat_id: str, file_path: str, media_type: str, caption: str = None) -> dict:
        files = {
            'file': (os.path.basename(file_path), open(file_path, 'rb'))
        }
        data = {'chatId': chat_id}
        if caption: data['caption'] = caption
        
        return self.client.request('POST', f'send/{media_type}', data=data, files=files)

    def mark_seen(self, chat_id: str) -> dict:
        return self.client.request('POST', 'send/seen', json={'chatId': chat_id})
