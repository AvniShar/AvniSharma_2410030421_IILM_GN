from flask import Flask, render_template, request

app = Flask(__name__)
bookings = []

@app.route('/')
def home():
    return render_template('index.html', bookings=bookings)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']

    for b in bookings:
        if b['date'] == date and b['time'] == time:
            return "❌ Slot already booked! <br><a href='/'>Go Back</a>"

    bookings.append({"name": name, "date": date, "time": time})
    return "✅ Booking Confirmed! <br><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)