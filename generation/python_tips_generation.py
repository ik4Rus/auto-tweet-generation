# Prepare env
import os
import ipdb

import openai
import json

# Parameters
GENERATION_PROMPT = \
    "Generate a list of 183 unique and advanced Python tips and tricks, each tip or trick should be a short sentence " \
    "or phrase and should be suitable for intermediate or advanced Python programmers. The tips and tricks should cover" \
    " a wide range of topics, including but not limited to data manipulation, coding style, performance optimization, " \
    "debugging, and software engineering best practices."
MAX_TOKENS = 3_000
openai.api_key = os.getenv("OPENAI_KEY")

# Let GPT-3 generate the tips and tricks
print("Start creation")
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=GENERATION_PROMPT,
    temperature=0.7,
    max_tokens=MAX_TOKENS,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

tips = response.choices[0].text

# Split the tips into a list
tips_list = tips.split('\n')

ipdb.set_trace()

# Create a list of tuples containing the index and tip
tips_with_index = [(index, tip) for index, tip in enumerate(tips_list)]

# Convert the list of tuples to a JSON object
tips_json = json.dumps(tips_with_index)

# Open a new file in write mode
with open('tips.json', 'w') as f:
  # Write the JSON object to the file
  f.write(tips_json)

if __name__ == "__main__":
    print(response)
