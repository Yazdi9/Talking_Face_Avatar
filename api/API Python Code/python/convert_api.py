import requests
import json 

url = "https://api.freeconvert.com/v1/process/convert?input"

payload = json.dumps({
  "input": "648973a1eb5fc978fc41933c",
  "input_format": "mp3",
  "output_format": "mp4"
})

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUG9zdG1hbl9BUEkiLCJpZCI6IjY0NzU5M2Q5ZTM3NzU2ZWI3YmIyYzc1ZCIsImludGVyZmFjZSI6ImFwaSIsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJiYW5pa2RhdmlkQGdtYWlsLmNvbSIsInBlcm1pc3Npb25zIjpbXSwiaWF0IjoxNjg2NzIyOTExLCJleHAiOjIxNjAwODY5MTF9.f39IxZF1FRj7dKiNiRp6fQw4IRrV_un0Eim9VutG4OU'
}

#r = requests.post('https://api.freeconvert.com/v1/process/convert', headers = headers)

response = requests.request("POST", url, headers=headers, data=payload)



print(response.text)

print(response.json())
