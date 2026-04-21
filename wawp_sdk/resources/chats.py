class Chats:
    def __init__(self, client):
        self.client = client

    def all(self) -> dict:
        return self.client.request('GET', 'chats')

    def overview(self, chat_id: str) -> dict:
        return self.client.request('GET', f'chats/overview?chatId={chat_id}')

    def archive(self, chat_id: str) -> dict:
        return self.client.request('POST', 'chats/archive', json={'chatId': chat_id})

    def unarchive(self, chat_id: str) -> dict:
        return self.client.request('POST', 'chats/unarchive', json={'chatId': chat_id})

    def delete(self, chat_id: str) -> dict:
        return self.client.request('DELETE', 'chats/delete', json={'chatId': chat_id})

    def clear(self, chat_id: str) -> dict:
        return self.client.request('POST', 'chats/clear', json={'chatId': chat_id})

    def mark_read(self, chat_id: str) -> dict:
        return self.client.request('POST', 'chats/read', json={'chatId': chat_id})

    def mark_unread(self, chat_id: str) -> dict:
        return self.client.request('POST', 'chats/unread', json={'chatId': chat_id})
