#Python_CEH_TOOL_0001 START
import requests
import json 

#Defined login function with mail and password 
def login(mail, password):
    #request session for grabbing cookies
    s = requests.Session()
    payload = {
        'email': mail,
        'password': password
    }
    
    #post to login api here
    res = s.post('https://mail.protonmail.com/api/auth', json=payload)
    #s.headers.update({"authorization": json.loads(res.content)['token']})
    print(res.content)
    # return s the session object
    return s

session = login('deathcrows@Protonmail.com', 'This_Is_Not_My_D3@th_Cr0w_P@ssw0rd_98.')


#Python_CEH_TOOL_0001 END