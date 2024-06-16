import os

input_dir = 'input'
output_dir = 'output'
valueRepeat = '[SPOTIFY-DOWNLOADER.COM] '
valueReplace = ''

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)


for filename in os.listdir(input_dir):
    if valueRepeat in filename:
        new_filename = filename.replace(valueRepeat, valueReplace)
        
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, new_filename)

        # Rename (move)
        os.rename(input_path, output_path)

print("Renaming complete!")