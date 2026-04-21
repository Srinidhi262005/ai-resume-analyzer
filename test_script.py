import requests, re
session = requests.Session()
try:
    res = session.get('http://127.0.0.1:5000/auth/register')
    token = re.search(r'name="csrf_token" type="hidden" value="([^"]+)"', res.text)
    csrf = token.group(1)
    data = {
        'csrf_token': csrf,
        'username': 'testytest12345',
        'email': 'testy12345@test.com',
        'password': 'password123',
        'confirm_password': 'password123',
        'submit': 'Register'
    }
    res2 = session.post('http://127.0.0.1:5000/auth/register', data=data)
    
    res3 = session.get('http://127.0.0.1:5000/auth/login')
    token_login = re.search(r'name="csrf_token" type="hidden" value="([^"]+)"', res3.text)
    login_data = {'csrf_token': token_login.group(1), 'email': 'testy12345@test.com', 'password': 'password123', 'submit': 'Login'}
    res4 = session.post('http://127.0.0.1:5000/auth/login', data=login_data)
    
    # Try ATS Check
    res_ats = session.get('http://127.0.0.1:5000/ats-check')
    token_ats = re.search(r'name="csrf_token" type="hidden" value="([^"]+)"', res_ats.text)
    ats_data = {'csrf_token': token_ats.group(1), 'resume_text': 'I am a python developer with sql', 'submit': 'Check'}
    res_ats_post = session.post('http://127.0.0.1:5000/ats-check', data=ats_data)
    print('ATS POST STATUS:', res_ats_post.status_code)
    
    if 'ATS Score' in res_ats_post.text:
        print("SUCCESS! 'ATS Score' found in response.")
    else:
        print("FAILED: 'ATS Score' not found. It probably redirected or failed validation silently.")
        
    # Let's see if there are form errors in the HTML
    errors = re.findall(r'<div class="flash-message.*?>(.*?)</div>', res_ats_post.text)
    if errors:
        print("FLASH MESSAGES:", errors)
        
except Exception as e:
    print('Error:', e)
