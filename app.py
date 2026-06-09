from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def home():
    count = r.incr('visits')
    return f'''
    <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>System Health Monitor — Visit Tracker</h1>
            <h2>This page has been visited <span style="color: green;">{count}</span> times.</h2>
            <p>Deployed via Jenkins + Docker Compose</p>
            <p>Build: {os.environ.get("BUILD_NUMBER", "local")}</p>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    try:
        r.ping()
        return {"status": "healthy", "redis": "connected"}, 200
    except Exception as e:
        return {"status": "unhealthy", "redis": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
