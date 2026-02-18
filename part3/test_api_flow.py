#!/usr/bin/env python3
import json, urllib.request, urllib.error, urllib.parse
BASE='http://127.0.0.1:5001'

def post(path, data, token=None):
    url=BASE+path
    b=json.dumps(data).encode('utf-8')
    req=urllib.request.Request(url, data=b, headers={'Content-Type':'application/json'})
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.getcode(), json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.load(e)
        except:
            return e.code, {'error': str(e)}
    except Exception as e:
        return None, {'error': str(e)}

if __name__ == '__main__':
    # 1 create user
    code, data = post('/api/v1/users/', {'first_name':'Test','last_name':'User','email':'test@example.com','password':'pass'})
    print('CREATE_USER:', code, data)

    # 2 login
    code, data = post('/api/v1/auth/login', {'email':'test@example.com','password':'pass'})
    print('LOGIN:', code, data)
    if code!=200 or 'access_token' not in data:
        print('Login failed, aborting')
        raise SystemExit(1)
    TOKEN=data['access_token']

    # 3 create place
    code, data = post('/api/v1/places/', {'title':'Test Place','description':'Nice','price':10,'latitude':0.0,'longitude':0.0}, token=TOKEN)
    print('CREATE_PLACE:', code, data)
    if code not in (200,201): raise SystemExit(1)
    PLACE_ID=data.get('id')

    # 4 post review
    code, data = post('/api/v1/reviews/', {'place_id': PLACE_ID, 'text':'Great stay'}, token=TOKEN)
    print('POST_REVIEW:', code, data)

    # 5 get reviews
    try:
        url=BASE+f"/api/v1/reviews/?place_id={urllib.parse.quote(PLACE_ID)}"
        with urllib.request.urlopen(url, timeout=10) as resp:
            reviews=json.load(resp)
            print('REVIEWS:', reviews)
    except Exception as e:
        print('REVIEWS_ERROR', e)
