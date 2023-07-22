import json

consumer_detail={"name":"vijay",
                 "reading":[1110,1220,1330,1440,1500]}

consumer_json=json.dumps(consumer_detail)
print(consumer_json)

