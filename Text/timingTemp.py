
import csv
import openai
import os
import time
import numpy as np
import random
reps = [1,2,3,4,5,6,7,8,9,10]
x =  np.arange(0.1,1.1,0.05)
xr = []
y = []

openai.api_key = "APIKey"
model_engine = "davinci"

def generate_response(prompt,temperature):
      response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      temperature = temperature,
      max_tokens=50
      )
      return response.choices[0].text.strip()


for k in x:
    for p in reps:
          t0=time.time()
          response = generate_response('What is the weather like today?',k)




          t1 = time.time()
          y.append(t1-t0)
          xr.append(k)

with open('AL4500.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Temprture', 'Time (s)'])
    for x, y in zip(xr, y):
        writer.writerow([x, y])
