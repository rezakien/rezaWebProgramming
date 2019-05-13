import requests,json

url = "http://www.mocky.io/v2/5c7db5e13100005a00375fda"
response = requests.get(url)

if response.ok:
	text_to_decode = str(response.json()['result']).replace(" ", "_")
	data = dict(result=text_to_decode,method="GET",headers = dict(response.headers))
	with open("result.json", "w") as fp:
		json.dump(data, fp,indent=2)
