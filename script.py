import sys



def main():
    
    
    user = maged
    desired_contact = vignesh
    num_of_connections = 5
    
    i = 0
    
    degree_of_seperaation=0
    
    contacts_in_link= []
    
    stopping_value = 10000
    
    searched_in = user  
    
    not_found = false
    found  = true
    
    for num1 in [0,stopping_value]:
        
        if found==true:
            break
        
        if not_found==true:
            searched_in = searched_in.friends(i)
            contact_in_link[degree_of_seperaation] = searched_in
            i++
            
            not_found==false
            
        for num2 in [0, searched_in.numoffriends]:
            if searched_in.friends(num2) == desired_contact:
                found = true
                break 
         
        not_found==true
         
        if i == searched_in.numoffriends:
            i=0
            degree_of_seperaation++
         
    
    if found==true:
        print 'you found your contact with' + degree_of_seperation + 'degree of seperation'
        
        print 'you can connect to' +  desired_contact + 'through' + contact_in_link
        
    else:
        print 'no contact found' 
    
        
