class Labels:
    def __init__(self, client):
        self.client = client

    def all(self) -> dict:
        return self.client.request('GET', 'labels/all')

    def create(self, name: str, color: str = None) -> dict:
        data = {'name': name}
        if color: data['color'] = color
        return self.client.request('POST', 'labels/create', json=data)

    def delete(self, label_id: str) -> dict:
        return self.client.request('DELETE', f'labels/{label_id}/delete')

    def get_chats(self, label_id: str) -> dict:
        return self.client.request('GET', f'labels/{label_id}/chats')

    def add_chat(self, label_id: str, chat_id: str) -> dict:
        return self.client.request('POST', f'labels/{label_id}/chats/{chat_id}')

    def remove_chat(self, label_id: str, chat_id: str) -> dict:
        return self.client.request('DELETE', f'labels/{label_id}/chats/{chat_id}')
