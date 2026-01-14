import requests
import time
print("Welcome to our gender prediction system based on name")
print()
print("Enter your name below to predict")
name = input(":")

url = f"https://api.genderize.io?name={name}"
response = requests.get(url)
data = response.json()
print()
print("processing...")
time.sleep(1)
print("Analyzing data...")
time.sleep(2)
print("Almost done...")
time.sleep(1)
print("Name analyzed successfully!")
time.sleep(2)
print()
print(f"Your gender is: {data['gender']}")
print(f"Probability: {data['probability']*100}%")