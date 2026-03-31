import requests #connect different websites
import json #convert random texts into Machine understandable text
import pandas as pd #to work with datasets

api = "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"
model = "openai-community/gpt2"
url = f"https://api-inference.huggingface.co/models/{model}"
headers = {"Authorization":f"Bearer {api}"}

def load_data(file_path):
  df=pd.read_csv(file_path)
  return df['Text'].tolist()
custom_data = load_data("Text.csv")

def query(prompt):
  payload = {"inputs":prompt}
  response = requests.post(url,headers=headers,json=payload)
  return response.json()

results = []
for text in custom_data:
  response = query(text)
  results.append(response)

output = pd.DataFrame({"Input": custom_data,"Response": results})
output.to_csv("output.csv",index=False)