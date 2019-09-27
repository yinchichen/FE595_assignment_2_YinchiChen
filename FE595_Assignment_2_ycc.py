from bs4 import BeautifulSoup
import requests
from requests import Response

male_list = []
female_list = []

for i in range(50):
    response = requests.get(url = 'https://theyfightcrime.org/')
    content = BeautifulSoup(response.content, "html.parser")

    text = content.find("td")
    text_strip = text.text.strip()
    text_split = text_strip.split("They fight crime!")[0]

    male_sentence = text_split.split('She')[0]
    female_sentence = 'She' + text_split.split('She')[1]

    male_list.append(str(male_sentence))
    female_list.append(str(female_sentence))

with open('/Users/yinchichen/Desktop/FE595/hw/Assignment_2/he.txt', mode='wt') as file_1:
    file_1.write('\n'.join(male_list))
with open('/Users/yinchichen/Desktop/FE595/hw/Assignment_2/she.txt', mode='wt') as file_2:
    file_2.write('\n'.join(female_list))





