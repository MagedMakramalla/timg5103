import logging
import json
import os
from flask import request, url_for
import requests
import sys

def hello():
    print "test"    
    resp = requests.get('http://127.0.0.1:8005/listUsers')    
    return json.dumps({'status':'healthy'})



import requests
 
def get_user(name):
    resp = requests.get('http://127.0.0.1:8005/getUser?username=%s' % (name))        
    resp_data = resp.json()['user']
    print resp_data
    return resp_data


def find_connection():
    send_dict = {}
    username = None
    if 'username' in request.args:
        username = (request.args['username'])
        print username        
    else:
        send_dict['error'] = "param:username is required"
        return json.dumps(send_dict)    

    connection_username_single_user = None
    if 'connection' in request.args:
        connection_username = (request.args['connection'])
        print connection_username        
    else:
        send_dict['error'] = "param:connection is required"
        return json.dumps(send_dict)    
    
    send_dict['response'] = find_connection_internal(username,connection_username) 
    return json.dumps(send_dict)


def find_connection_internal(user,desired_contact):
        
    look_up_in = user
    
    i = 0       
    degree_of_seperation = 0
    contacts_in_link= []    
    stopping_value = 50    
    found  = False
    
    while not found:        
        user_data = get_user(look_up_in)            
        for each_connection in user_data['following']:            
            if each_connection['username'] == desired_contact:
                found = True
                break        
            i += 1        
        if not found:
            look_up_in = user_data['following'][0]['username']
            contacts_in_link.append(look_up_in)
            degree_of_seperation += 1
        if degree_of_seperation >= 3:
            break
        
                 
    if found:        
        if degree_of_seperation == 0:
            return 'This is a direct connection'
        else:
            return 'you found your contact with ' + str(degree_of_seperation) + ' degree of seperation.' + ' you can connect to ' +  desired_contact + ' through ' + ','.join(contacts_in_link)         
    else:
        return 'no connection found' 
     
