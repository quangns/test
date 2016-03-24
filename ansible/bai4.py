from flask import Flask
from flask import request
import redis
import time


app = Flask(__name__)
pool = redis.ConnectionPool(host='0.0.0.0', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


@app.route("/")
def main():
    date = time.strftime("%d-%m-%Y")
    user_agent = request.headers.get('User-Agent')
    r.execute_command('PFADD', date, user_agent)
    count = r.execute_command('PFCOUNT', date)
    return "%s: %s" % (date, count)


if __name__ == "__main__":
    app.run(host="192.168.33.10", port=8080, debug=True)
