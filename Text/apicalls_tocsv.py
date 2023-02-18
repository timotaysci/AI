  import csv
  import openai
  import os


  openai.api_key = "[API KEY]"
  model_engine = "davinci"

  # Define a function to generate responses for a given prompt
  def generate_response(prompt):
      response = openai.Completion.create(
          engine=model_engine,
          prompt=prompt,
          max_tokens=150,
      )
      return response.choices[0].text.strip()

  # Open the input CSV file in read mode
  with open('software_list.csv', mode='r') as csv_file:
      # Create a reader object
      csv_reader = csv.reader(csv_file)

      # Open the output CSV file in write mode
      with open('output_file.csv', mode='w', newline='') as output_file:
          # Create a writer object
          csv_writer = csv.writer(output_file)

          # Iterate over the rows and write data to the output CSV file
          for row in csv_reader:
              # Extract the prompt from the input CSV row (assuming it's in the second column)
              prompt = "What is " + row[0] + "?"

              # Generate a response using the DaVinci model
              response = generate_response(prompt)
              print(prompt)
              print(response)
              # Add the response as a new column to the row
              row.append(response.replace('\n', ' '))
              # Write the row to the output CSV file
              csv_writer.writerow(row)

