###### Pypi ##################


###### pip ##############
# pip3 install --upgrade pip
# pip3 list see the packages installed
# pip3 install requests==2.9.0
# pip3 install requests==2.9.* latest version in 2.9
# pip3 uninstall requests

import requests

response = requests.get("http://google.com")
print(response)
