import shutil
from PIL import Image
import requests
import json
import base64
import os


pixabay_api = "85f13dc" # https://pixabay.com/api/docs/
def pixabay_image_operation(command):
  if not os.path.exists('img'):
    os.makedirs('img')
  try:
    image_list = requests.get(f'https://pixabay.com/api/?key={pixabay_api}&q={command.replace(" ","+")}&image_type=photo&pretty=true')
    img_soup = image_list.json()['hits']
    img_list = []
    for x in img_soup:
      img_list.append(x['webformatURL'])
    if len(img_list) > 5:
      img_choice = choice([0,1,2,3,4,5])
    else:
      img_choice = 0
    headers_fox = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    response = requests.get(img_list[img_choice], stream=True, headers=headers_fox)
    local_file = open('img/' + command + '.jpg', 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, local_file)
    im = Image.open('img/' + command + '.jpg')
    resized_im = im.resize((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    resized_im.save('img/' + command + '.jpg')
  except:
    pass

test = pixabay_image_operation('Red roses')
print(test)