import requests

headers = {"Authorization": "Bearer aaaaaaa"}
result = []

for i in range(1,6):
  endpoint = "https://api.github.com/search/repositories?q=language:python+stars:>5000&sort=stars&order=desc&per_page=100&page=" + str(i)
  res = requests.get(endpoint, headers=headers).json()
  items = res.get('items')
  result = result + items

for repo in result:
  print(repo.get('name') + " - " + str(repo.get("stargazers_count")))

print("***********")
print("Total repositorios: " + str(len(result)))
