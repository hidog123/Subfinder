from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
file1=open('suby.txt', 'r')
f=open('resulte.txt', 'w') 
for line in file1:
  url="https://"+line 
  print(url)
  req = Request(url)
  try:
    response = urlopen(req,timeout=5)
  except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
  except URLError as e:
    continue
  else:
     print("(---------------------------Found------------------------------)")
     print (url)
     f.write(url)

