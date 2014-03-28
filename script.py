
import sys
import requests
 
def get_user(name):
    resp = requests.get('http://127.0.0.1:9010/getUser?username=%s' % (name))
        
    resp_data = resp.json()
    return resp_data



def find_connection():
        
    user = 'vignesh'
    desired_contact = 'asdsad'
    look_up_in = user
    
    i = 0       
    degree_of_seperation = 0
    contacts_in_link= []    
    stopping_value = 50    
    found  = False
    
    while not found:        
        user_data = get_user(look_up_in)            
        for each_connection in user_data['connections']:            
            if each_connection['name'] == desired_contact:
                found = True
                break        
            i += 1        
        if not found:
            look_up_in = user_data['connections'][0]['name']
            contacts_in_link.append(look_up_in)
            degree_of_seperation += 1
        if i >= stopping_value:
            break
        
                 
    if found:
        print 'you found your contact with ' + str(degree_of_seperation) + ' degree of seperation'
        if degree_of_seperation == 0:
            print 'This is your direct connection'
        else:
            print 'you can connect to ' +  desired_contact + ' through ' + ','.join(contacts_in_link)         
    else:
        print 'no connection found' 
     
         
find_connection()

