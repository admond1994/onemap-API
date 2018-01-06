# 'requests' is a Python library
# This gets the access token from C:\Users\Admond\Desktop\SMRT Intern (Jalan)\onemap (API)\authentication_module_for_Windows_x64-master\authentication_module\auth.exe
import subprocess
import requests

#------------------------------------------------------------------------------
def get_access_token(file_path):
    '''
    This function executes auth.exe to generate a valid access token for API 
    DOWNLOAD THE FOLDERS: authentication_module_for_Windows_x64
    FROM (https://github.com/sla-onemap/authentication_module_for_Windows_x64/tree/master/authentication_module)
    ** This function is built to execute auth.exe in Window OS **
        
    Other operating system --> MacOS & Linux (https://github.com/sla-onemap)
    
    Input -> path of auth.exe in the computer
    Output -> access_token
    
    '''
    p = subprocess.Popen(file_path, stdout=subprocess.PIPE) # execute auth.exe given the file path
    text = p.stdout.read()  # read the text from the terminal 
    
    access_token = text # will put in some conditions to extract access token once we are registered as the authorized user 
    
    # Suppose we have text as the access token as string
    return access_token
#------------------------------------------------------------------------------
## MAIN SCRIPT (METHOD 1 - Temporary Solution)
#file_path = r'C:\Users\Admond\Desktop\SMRT Intern (Jalan)\onemap (API)\authentication_module_for_Windows_x64-master\authentication_module\auth.exe'
#access_token = get_access_token(file_path) # get the access token as string format

# Token is obtained directly from the website (https://www.onemap.sg/main/v2/trafficquery)
# webpage url
url = r'https://developers.onemap.sg/publicapi/cp/getAllCarparks'
access_token = r'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMsInVzZXJfaWQiOjMsImVtYWlsIjoicHVibGljQXBpUm9sZUBzbGEuZ292LnNnIiwiZm9yZXZlciI6ZmFsc2UsImlzcyI6Imh0dHA6XC9cL29tMi5kZmUub25lbWFwLnNnXC9hcGlcL3YyXC91c2VyXC9zZXNzaW9uIiwiaWF0IjoxNTA5Nzg1MjMyLCJleHAiOjE1MTAyMTcyMzIsIm5iZiI6MTUwOTc4NTIzMiwianRpIjoiOGQwM2ZmNmNjZTI5MTUwODZhM2YwZWFhNGVhNjdmYzQifQ.abeLxkqpjMDDBFZlJHhzxgbNJ-Xat8zwoXBmoFi-R1M'
parameter = {'token':access_token}  # input the access token here as the parameter

# ping the website or portal for information (get the webpage)
# send get request to the url
#r = requests.get(url, params=parameter) # use 'r' to store the request response  
#print('The token is collected manually here')
#print('status code:{} \n'.format(r))  # status code should be 200-400 
#print('url:{} \n'.format(r.url))
#print('response status code:{}'.format(r.status_code)) 
#data = r.json()  # return a dictionary that stores all the output 
#
#print('--- The Carpark content (from manual token) is --- \n')
#for count,carpark in enumerate(data['CARPARKS'],1):
#    print('Carpark:{} \n {} \n'.format(count,carpark))    
#------------------------------------------------------------------------------
## MAIN SCRIPT (METHOD 2)

# Access the URL for public API session ID 
# Collect token from there in real time (test it after 3 days)

url_public_id = r'https://developers.onemap.sg/publicapi/publicsessionid'
url_get_carpark = r'https://developers.onemap.sg/publicapi/cp/getAllCarparks'

r_public_id = requests.get(url_public_id)
print('The token is collected from url_1 automatically here')
print('status code (public id):{} \n'.format(r_public_id))
print('url_public_id:{} \n'.format(r_public_id.url))
print('response status code (public id):{}'.format(r_public_id.status_code)) 
dic = r_public_id.json() # retrieve token and expiry time stamp 

token = dic['access_token'] #return token in string format
parameter_get_carpark = {'token':token}
r_get_carpark = requests.get(url_get_carpark, params=parameter_get_carpark)
data_get_carpark = r_get_carpark.json() 

print('--- The Carpark content (from public id token) is --- \n')
for count,carpark_1 in enumerate(data_get_carpark['CARPARKS'],1):
    print('Carpark:{} \n {} \n'.format(count,carpark_1))  
#/////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////
# TESTING PURPOSE...
# THIS uses one of the APIs available on onemap.sg 
#URL = 'https://www.onemap.sg/nearby-api/getAllBusStops' 
#
## location given here (input to the parameters)
#latitude = 1.33587701539134
#longitude = 103.848418629367
# 
## defining a params dict for the parameters to be sent to the API
#PARAMS = {'lat':latitude, 'lon':longitude}
# 
## sending get request and saving the response as response object
#r = requests.get(url = URL, params = PARAMS)
# 
## extracting data in json format
#data = r.json()
 
 
