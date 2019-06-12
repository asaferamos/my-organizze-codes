from config import *
import base64

url = "https://api.organizze.com.br/rest/v2/"

auth_encode = (api_login + ':' + api_token).encode('ascii')
auth_encode = base64.b64encode(auth_encode).decode('ascii')

headers = {
  'Authorization': 'Basic ' + str(auth_encode)
}
