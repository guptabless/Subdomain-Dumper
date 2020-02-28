from googlesearch import search

print("------------------------------------------------")
print("Code BY ::  NG")
print("------------------------------------------------")
url = input("Enter URL which Subdomain we want to find by using GOOGLE dork Functionality ")
print(url)

if(url.startswith("https://")):
  new_url = url.replace("https://", "*.")
else:
  new_url = url.replace("http://", "*.")

surl = new_url
surl= "site:" + new_url

try:
    from googlesearch import search
except ImportError:
    print("Not found")

limit = int(input("Please enter the limit how much SubDomain you want to fetch"))

for u in search(surl, tld="com", num=10, stop=limit, pause=2):
  print(u)


