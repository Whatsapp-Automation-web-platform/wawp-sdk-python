class Groups:
    def __init__(self, client):
        self.client = client

    def all(self) -> dict:
        return self.client.request('GET', 'groups')

    def detail(self, group_id: str) -> dict:
        return self.client.request('GET', f'groups/detail?groupId={group_id}')

    def create(self, name: str, participants: list) -> dict:
        return self.client.request('POST', 'groups/create', json={
            'name': name,
            'participants': participants
        })

    def join(self, invite_url: str) -> dict:
        return self.client.request('POST', 'groups/join', json={'url': invite_url})

    def leave(self, group_id: str) -> dict:
        return self.client.request('POST', f'groups/{group_id}/leave')

    def add_participants(self, group_id: str, participants: list) -> dict:
        return self.client.request('POST', f'groups/{group_id}/participants/add', json={'participants': participants})

    def remove_participants(self, group_id: str, participants: list) -> dict:
        return self.client.request('POST', f'groups/{group_id}/participants/remove', json={'participants': participants})
