services:
  - type: web
    name: ml-flask-api
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startcommand: "gunicorn app:app --bind 0.0.0.0:$PORT"
    autodeploy: false  #we'll triggere deploys via Github action