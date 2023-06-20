import requests

access_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUG9zdG1hbl9BUEkiLCJpZCI6IjY0NzU5M2Q5ZTM3NzU2ZWI3YmIyYzc1ZCIsImludGVyZmFjZSI6ImFwaSIsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJiYW5pa2RhdmlkQGdtYWlsLmNvbSIsInBlcm1pc3Npb25zIjpbXSwiaWF0IjoxNjg2NzIyOTExLCJleHAiOjIxNjAwODY5MTF9.f39IxZF1FRj7dKiNiRp6fQw4IRrV_un0Eim9VutG4OU'


headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.freeconvert.com/v1/process/convert', headers = headers)

print(r.json())
