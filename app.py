# Import Flask and other required modules
from flask import Flask, request, render_template, g, redirect, url_for
import sqlite3
import csv
from io import StringIO


app = Flask(__name__)
app.config['DATABASE'] = 'history.db'
app.config['TEMPLATES_AUTO_RELOAD'] = True


def init_db():
    """Initialize the database by executing the SQL commands in schema.sql."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.execute('''CREATE TABLE IF NOT EXISTS history (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         expression TEXT,
                         result REAL)''')
    db.commit()


def get_db():
    """Create and return a connection to the database."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Close the database connection at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    """Handle requests to the main page."""
    init_db()
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            result = eval(expression)
            db = get_db()
            db.execute("INSERT INTO history (expression, result) VALUES (?, ?)", (expression, result))
            db.commit()
        except Exception:
            result = "Invalid expression"
        return render_template('index.html', result=result, expression=expression)
    else:
        return render_template('index.html')


@app.route('/history')
def history():
    """Handle requests to the history page."""
    db = get_db()
    rows = db.execute("SELECT * FROM history").fetchall()
    return render_template('history.html', rows=rows)


@app.route('/export')
def export():
    """Handle requests to export the history as a CSV file."""
    db = get_db()
    rows = db.execute("SELECT * FROM history").fetchall()

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Expression', 'Result'])
    for row in rows:
        writer.writerow(row)

    response = app.response_class(
        content_type='text/csv',
        headers=[('Content-Disposition', 'attachment; filename="history.csv"')])
    response.data = output.getvalue().encode('utf-8')
    return response


@app.route('/clear', methods=['POST'])
def clear():
    db = get_db()
    db.execute('DELETE FROM history')
    db.commit()
    return redirect(url_for('history'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
