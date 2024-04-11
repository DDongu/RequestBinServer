from flask import Flask, request, render_template
import queue
from datetime import datetime
import ssl

app = Flask(__name__)
requests = queue.Queue(maxsize=10)

@app.route('/')
def index():
  
    # HTTP 요청 정보 저장
    request_info = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'method': request.method,
        'path': request.path,
        'headers': dict(request.headers),
        'data': request.data.decode('utf-8'),
        'args': request.args.to_dict(),
        'form': request.form.to_dict(),
        'files': request.files.to_dict(),
        'cookies': request.cookies.to_dict(),
        'remote_addr': request.remote_addr,
    }

    if requests.qsize() == 10:
        requests.get()
    requests.put(request_info)

    return "Request received successfully!"

@app.route('/requestbin')
def requestbin():
    return render_template('requestbin.html', request_info=list(requests.queue)[::-1])


if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000, ssl_context=('../ssl/server.crt', '../ssl/server.key'), debug=False)
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
