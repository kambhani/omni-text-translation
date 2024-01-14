from google.cloud import translate_v2 as translate  # Import the translation API
import csv  # Import the CSV package

# Declare variables
text = 'Hello World!'  # The text to translate into all languages
filename = 'translations.csv'  # The name of the csv file to store the translations
headers = ['language_name', 'code', 'translation']  # The csv headers

# Create the translation client
translate_client = translate.Client()

# Get a list of all supported languages
languages = translate_client.get_languages()

# Open the csv file for writing
with open(filename, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)  # Create the csv writer
    csv_writer.writerow(headers)  # Write the headers to the csv file

    # Iterate over the supported languages and add each one to the csv file
    for language in languages:
        result = translate_client.translate(text, target_language=language.get('language'), format_='text')
        csv_writer.writerow([language.get('name'), language.get('language'), result.get('translatedText')])
