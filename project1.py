# from pyyoutube import Client

# cli = Client(client_id="851864077615-iatk7dfl3l332neu6cqauk3luef9jird.apps.googleusercontent.com", client_secret="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")

# print(cli.get_authorize_url())

from pyyoutube import Api
import json
import sqlalchemy as db
import pandas as pd

api = Api(api_key="AIzaSyAnarBmG-NnwVJl8IpJcE3A1XmebCspit0")
channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items)
#channel_object = json.dumps(channel_by_id.items[0].to_dict(),indent=4)
channel_dict = channel_by_id.items[0].to_dict()
json_str = json.dumps(channel_dict, indent=4)
# print(type(channel_dict))
dataframe_name=pd.DataFrame.from_dict({'chan':json_str},orient='index')
engine = db.create_engine('sqlite:///data_base_name.db')
dataframe_name.to_sql('table_name', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name"))
   columns = query_result.keys()
   #print(columns)
   print(pd.DataFrame(query_result))


