import hashlib
import hmac
import json
import requests

secret = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "Matthew Cann",
    "email": "matthewcameroncann@gmail.com",
    "resume": "",       # URL to your resume
    "location": "Calgary, AB",     # e.g. "New York, NY"
    "linkedin": "www.linkedin.com/in/matthew-cann",
    "codeLink": "",     # URL to the repo/gist containing THIS script
    "yearsPython": 6,
    "yearsDjango": 1,
    "repos": "https://mattcann1.github.io/mattcann1/",
    "notes": "I wish more companies did this! This is so much fun!"
}

body = json.dumps(payload)
signature = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()

resp = requests.post(
    endpoint,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-HMAC-Signature": signature,
    },
)
print(resp.status_code, resp.json())
