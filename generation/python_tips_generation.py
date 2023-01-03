# Prepare env
import os

import ipdb

import openai
import re
import json

# Parameters
# LIST_TIPS_PROMPT = \
#     "Generate a list of 183 unique and advanced Python tips and tricks, each tip or trick should be a short sentence " \
#     "or phrase and should be suitable for advanced Python programmers. The tips and tricks should cover" \
#     " a wide range of topics, including but not limited to data manipulation, coding style, performance optimization, " \
#     "debugging, and software engineering best practices."
MAX_TOKENS = 300
openai.api_key = os.getenv("OPENAI_KEY")

with open('../data/areas_python_tips.json') as f:
    python_tip_areas = json.load(f)

final_tips_list = []

for area in python_tip_areas[:2]:
    print(f"Generating tips for '{area.get('area')}'")
    area_prompt = \
        f"Generate a list of {area.get('count')} advanced Python tips and tricks for the area '{area.get('area')}'. " \
        f"Each tip or trick should be a short sentence, advanced, very specific and they need to be mutually exclusive."

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=area_prompt,
        temperature=0.7,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    tips = response.choices[0].text

    # Split the tips into a list
    tips_list = tips.split('\n')
    tips_list = [re.sub(r'^[0-9]*\.*', '', tip).strip() for tip in tips_list if tip != '']

    final_tips_list = final_tips_list + [{"tip": tip, "area": area.get('area')} for tip in tips_list]

for idx, tip in enumerate(final_tips_list):
    print(f"{idx + 1} of {len(final_tips_list)}")
    tweet_prompt = f'''
    I write daily tweets for advanced Python tips and tricks. I follow these three principles: 
    - I use hashtags and never use more than 280 characters
    - I'm specific and try to visualize the content so it is easy to learn
    - I am engaging and interesting
    
    A tweet for the following tip: 'tip.get('tip')'
    '''

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=tweet_prompt,
        temperature=0.7,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    tips = response.choices[0].text
    ipdb.set_trace()
    # Split the tips into a list
    tips_list = tips.split('\n')
    tips_list = [re.sub(r'^[0-9]*\.*', '', tip).strip() for tip in tips_list if tip != '']

    final_tips_list = final_tips_list + [{"tip": tip, "area": area.get('area')} for tip in tips_list]

with open('../data/python_tips.json', 'w+') as f:
    json.dump(final_tips_list, f)

for tip in final_tips_list:
    print(tip)

ipdb.set_trace()

sum([x.get('count') for x in python_tip_areas])

ipdb.set_trace()

# Let GPT-3 generate the tips and tricks
print("Start creation")

ipdb.set_trace()

# Create a list of tuples containing the index and tip
tips_with_index = [{"index": index,
                    "tip": tip} for index, tip in enumerate(tips_list)]

# Convert the list of tuples to a JSON object
tips_json = json.dumps(tips_with_index)

# Open a new file in write mode
with open('tips.json', 'w') as f:
    # Write the JSON object to the file
    f.write(tips_json)

if __name__ == "__main__":
    print(response)
