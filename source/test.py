from requests import get
from urllib.parse import unquote

url = 'https://accounts.google.com/o/oauth2/auth?redirect_uri=storagerelay%3A%2F%2Fhttps%2Ffap.fpt.edu.vn%3Fid%3Dauth511049&response_type=permission%20id_token&scope=email%20profile%20openid&openid.realm=&include_granted_scopes=true&client_id=183063314780-0j6vj5ddfm7j3lsledglk2egnk18up7f.apps.googleusercontent.com&ss_domain=https%3A%2F%2Ffap.fpt.edu.vn&fetch_basic_profile=true&gsiwebsdk=2'

print(unquote(url))

# get(url=url)