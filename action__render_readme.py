import datetime
import requests

response = requests.get("https://nuforc-sightings-database-api.herokuapp.com/sightings/today/random")
print(response.json()[0])

markdown_text_for_template = ''
markdown_text = open("./README.template.md", "r").read()

markdown_text_for_template += f"<sub>On this day in {response.json()[0][8]}, an anonymous witness in {response.json()[0][1]} ({response.json()[0][2]}) reported seeing craft that fit the description of some '{response.json()[0][3]}' over a period of approximately {response.json()[0][11]} - {response.json()[0][11]} minutes.</sub><blockquote><sub>{response.json()[0][-1]}</sub></blockquote><sub><sub><i>source: [{response.json()[0][-2]}]({response.json()[0][-2]})</i></sub></sub></sub><br>" 
print(markdown_text_for_template)

new_markdown_text = markdown_text.replace("{random_sighting}", markdown_text_for_template)

new_readme = open("README.md", "w")
new_readme.write(new_markdown_text)

timestamp_text = f'Last Updated: {datetime.datetime.now()}'

timestamp_for_last_update_markdown_text = markdown_text.replace("{timestamp_for_last_update}", markdown_text_for_template)

new_readme = open("README.md", "w")
new_readme.write(timestamp_for_last_update_markdown_text)

print(datetime.datetime.now())