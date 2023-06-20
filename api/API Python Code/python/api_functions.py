

import requests
import json 

#import files
def import_file():
    
    url="https://api.freeconvert.com/v1/process/import/url"

    payload = json.dumps({
        "url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/yoZ06aMxZJJ28mfd3POQ/1c4d417c-ba80-4de8-874a-a1c57987ea63.mp3",
        "filename": "1c4d417c-ba80-4de8-874a-a1c57987ea63.mp3"
        })


    headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUG9zdG1hbl9BUEkiLCJpZCI6IjY0NzU5M2Q5ZTM3NzU2ZWI3YmIyYzc1ZCIsImludGVyZmFjZSI6ImFwaSIsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJiYW5pa2RhdmlkQGdtYWlsLmNvbSIsInBlcm1pc3Npb25zIjpbXSwiaWF0IjoxNjg2NzIyOTExLCJleHAiOjIxNjAwODY5MTF9.f39IxZF1FRj7dKiNiRp6fQw4IRrV_un0Eim9VutG4OU'
            
            }

    response = requests.request("POST", url, headers=headers , data=payload)

    return response.json() 

#upload files
def upload_file():
    
   
    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUG9zdG1hbl9BUEkiLCJpZCI6IjY0NzU5M2Q5ZTM3NzU2ZWI3YmIyYzc1ZCIsImludGVyZmFjZSI6ImFwaSIsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJiYW5pa2RhdmlkQGdtYWlsLmNvbSIsInBlcm1pc3Npb25zIjpbXSwiaWF0IjoxNjg2NzIyOTExLCJleHAiOjIxNjAwODY5MTF9.f39IxZF1FRj7dKiNiRp6fQw4IRrV_un0Eim9VutG4OU'
   }

    r = requests.post('https://api.freeconvert.com/v1/process/import/upload', headers = headers)
    return r.json()
    
#convert
def convert():
    
    url = "https://api.freeconvert.com/v1/process/convert?input"
    
    
    payload = json.dumps({
    "input": "648b1d761b0adb184fe6108c",
    "input_format": "mp3",
    "output_format": "mp4"
    })

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUG9zdG1hbl9BUEkiLCJpZCI6IjY0NzU5M2Q5ZTM3NzU2ZWI3YmIyYzc1ZCIsImludGVyZmFjZSI6ImFwaSIsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJiYW5pa2RhdmlkQGdtYWlsLmNvbSIsInBlcm1pc3Npb25zIjpbXSwiaWF0IjoxNjg2NzIyOTExLCJleHAiOjIxNjAwODY5MTF9.f39IxZF1FRj7dKiNiRp6fQw4IRrV_un0Eim9VutG4OU'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return  response.json()

#export  files 

def export():
    
    payload = json.dumps({
  "input": "648b1d761b0adb184fe6108c",
  #"filename": "1c4d417c-ba80-4de8-874a-a1c57987ea63.mp3"
    })

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUG9zdG1hbl9BUEkiLCJpZCI6IjY0NzU5M2Q5ZTM3NzU2ZWI3YmIyYzc1ZCIsImludGVyZmFjZSI6ImFwaSIsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJiYW5pa2RhdmlkQGdtYWlsLmNvbSIsInBlcm1pc3Npb25zIjpbXSwiaWF0IjoxNjg2NzIyOTExLCJleHAiOjIxNjAwODY5MTF9.f39IxZF1FRj7dKiNiRp6fQw4IRrV_un0Eim9VutG4OU'
    }

    r = requests.post('https://api.freeconvert.com/v1/process/export/url', headers = headers,data=payload)

    return r.json() 

import_func=import_file()
print(import_func)

upload_func=upload_file()
print(upload_func)

convert_func=convert()
print(convert_func)

export_func=export()
print(export_func)
    
    
    
    