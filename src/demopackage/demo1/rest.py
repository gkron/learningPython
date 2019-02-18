import requests, json

# r = requests.get('https://github.com/timeline.json')
# print(r.status_code)
# # print(r.headers)
# # print(r.headers['Content-Type'])
# 
# github_url = "https://api.github.com/user/repos"
# data = json.dumps({'name':'test', 'description':'some test repo'})
# r = requests.post(github_url, data, auth=('user', '*****'))
#  
# print (r.json)


url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
 
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.content)