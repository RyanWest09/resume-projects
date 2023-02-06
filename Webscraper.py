import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://www.urbandictionary.com/define.php?term=Fart')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
definition = soup.find_all(attrs = {'class' : 'break-words meaning mb-4'})
print(definition)
defin_list = []
for defin in definition: 
  seperate_definitions = defin.split('<br>')
  print(seperate_definitions)
  defin_list.append(seperate_definitions)
print(defin_list)






