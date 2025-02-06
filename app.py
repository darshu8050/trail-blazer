from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health/v2/system', methods=['GET'])
def health_check():
    return jsonify({"status": "Running smoothly"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)

