import requests
import os

def create_repo(repo_name):

	username = input("Enter Github Username: ")
	access_token = input("Enter Github access token: ")

	pwd = os.popen('pwd').readlines()[0]
	pwd = pwd.replace("\n", "")


	url = "https://api.github.com"

	payload = '{"name": "' + repo_name + '", "private": false }'


	headers = {
		"Authorization": "token " + access_token,
		"Accept": "application/vnd.github.v3+json"
	}

	try:

		r = requests.post(url+"/user/repos", data=payload, headers=headers)
		r.raise_for_status()

	except requests.exceptions.RequestException as err:
		raise SystemExit(err)

	try:
		os.system("mkdir " + repo_name)
		os.chdir(pwd + "/" + repo_name)
		os.system("git init")
		os.system("git remote add origin https://github.com/" + username + "/" + repo_name + ".git")
		os.system("echo '# " + repo_name + "' >> README.md")
		os.system("git add . && git commit -m 'Initial Commit' && git push origin master")
	except FileExistsError as err:
		raise SystemExit(err)


