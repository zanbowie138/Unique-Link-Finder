import requests
from bs4 import BeautifulSoup

starting_website = "https://www.github.com/"

def add_to(arr,input):
  output = ""
  sorted_arr = sorted(arr.items(), key=lambda x: x[1], reverse=True)
  if not input in arr:
    arr[input] = 1
    f = open("websites.txt","w")
    for link in sorted_arr:
      output+=link[0] + ": " + str(link[1]) + "\n"
    f.write(output)
    f.close()
  else:
    arr[input]+=1
    
def print_to_file(input,file):
  f = open(file,"w")
  f.write(str(input))
  f.close()
  
def read_file(input):
  f = open(input,"r")
  output = f.read()
  f.close()
  return output

unique_urls = {}
url_num = 0

if (len(unique_urls) == 0):
  unique_urls[starting_website] = 1
while (url_num < len(unique_urls)):
  url = list(unique_urls)[url_num]
  print("Searching " + str(url_num) + ": " + list(unique_urls)[url_num])
  try:
    reqs = requests.get(url)
  except:
    url_num+=1
    print("Skipping website because of error")
    continue
  soup = BeautifulSoup(reqs.text, 'html.parser')
  for link in soup.find_all('a'):
    lk = link.get('href')
    if lk != None and lk != "":
      if lk[:8] == "https://":
        add_to(unique_urls,lk[0:lk.find("/",8)+1])
  url_num+=1
print("Stopped!")