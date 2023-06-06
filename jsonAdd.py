import os
import json

directory = './json'  # Replace with the path to your directory

for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r+') as file:
            data = json.load(file)
            
            # Add 'keyword' field to each record in the JSON file
            for record in data:
                record['keyword'] = filename
            
            # Move file pointer to the beginning of the file
            file.seek(0)
            
            # Write the updated data back to the file
            json.dump(data, file, indent=4)
            
            # Truncate any remaining content after the updated data
            file.truncate()
            
        print(f'Updated {filename} with the "keyword" field.')

