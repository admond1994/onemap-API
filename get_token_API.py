import requests

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

 
