from toggl.api_client import TogglClientApi

settings = {
    'token': '4c2e7a7083b4434da3fda4fef989f353',
    'user_agent': 'toggl',
    'workspace_id': '2429477'
}
toggle_client = TogglClientApi(settings)

response = toggle_client.get_workspaces()

print (response)