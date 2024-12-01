import requests

def verify_token(token):
    valid=True
    try:
        if token is None:
            raise Exception("Missing token")    
    except Exception as e:
        print(e)
        valid=False
    return valid        