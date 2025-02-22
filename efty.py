echo "from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send', methods=['GET'])
def send_message():
    number = request.args.get('n')
    message = request.args.get('m')

    if not number or not message:
        return jsonify({
            'status': 'failed',
            'error': 'Missing parameters',
            'owner': '@Efty67'
        }), 400

    api_url = f'https://sktelecoms.xyz/eftyget.php?n={number}&m={message}'
    response = requests.get(api_url)

    if response.status_code == 200:
        return jsonify({
            'status': 'success',
            'data': response.text,
            'owner': '@Efty67'
        })
    else:
        return jsonify({
            'status': 'failed',
            'error': 'API request failed',
            'owner': '@Efty67'
        }), 500

if __name__ == '__main__':
    app.run()" > app.py
