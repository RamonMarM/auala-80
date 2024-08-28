import requests

def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox59e2363bd1af4261b42440f4c044d44a.mailgun.org/messages",
  		auth=("api", "8a399a332e3d31c60c580ba9e43d8927-2b91eb47-b8117fdb"),
  		data={"from": "Ramon Martins <mailgun@sandbox59e2363bd1af4261b42440f4c044d44a.mailgun.org>",
  			"to": ["ramonmendoncapiu@gmail.com"],
  			"subject": "Envio de email avaliacao 80",
  			"text": "Teste Teste Teste!"})
