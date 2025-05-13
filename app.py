from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulated in-memory storage
reservations = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    data = request.json
    name = data.get('name')
    train = data.get('train')
    date = data.get('date')

    if not name or not train or not date:
        return jsonify({'status': 'error', 'message': 'Missing reservation fields'}), 400

    reservation = {'name': name, 'train': train, 'date': date}
    reservations.append(reservation)

    return jsonify({'status': 'success', 'message': f'Reservation confirmed for {name} on train {train} for {date}.'})

if __name__ == '__main__':
    app.run(debug=True)
