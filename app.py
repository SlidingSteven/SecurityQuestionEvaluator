from flask import Flask, request, render_template
import newbs4
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        ruling = newbs4.checkURL(url)
        if ruling:
            return render_template('index.html', ruling = "SAFE")
        else:
            return render_template('index.html', ruling = "NOT SAFE")
        
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
