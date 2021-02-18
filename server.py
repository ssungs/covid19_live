from flask import Flask, render_template
from covid19_live_data import Covid19_live_data


app = Flask(__name__)

@app.route('/')
def index():
    title = 'Covid19 Live in Korea.'
    return render_template('index.html', title=title)

@app.route('/covid19-live')
def show_item():
    data = Covid19_live_data()
    return render_template('covid19-live.html', Covid19_live_data=data)

if __name__=='__main__':
    app.run(host='localhost', port=8019, debug=True)
