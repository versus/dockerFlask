from flask import Flask
import sys
import optparse
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        args.port = "5000"
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
    
