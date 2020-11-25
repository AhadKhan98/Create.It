import requests

# github_token = input("Enter token")
# repo_name = input("Enter repo name")
url = "https://api.github.com"

payload = '{"name": "CreationHere"}'

headers = {
	"Authorization": "token " + "",
	"Accept": "application/vnd.github.v3+json"
}

r = requests.post(url+"/user/repos", data=payload, headers=headers)



