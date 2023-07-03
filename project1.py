# from pyyoutube import Client

# cli = Client(client_id="851864077615-iatk7dfl3l332neu6cqauk3luef9jird.apps.googleusercontent.com", client_secret="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")

# print(cli.get_authorize_url())

from pyyoutube import Api
import json

api = Api(api_key="AIzaSyAnarBmG-NnwVJl8IpJcE3A1XmebCspit0")
channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items)
channel_object = json.dumps(channel_by_id.items[0].to_dict(),indent=4)
print(channel_object)