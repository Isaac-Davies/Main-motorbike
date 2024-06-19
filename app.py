from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') #This "/" stands for the Main.html file
def hello_world():  # put application's code here
   return render_template('Main.html')


@app.route('/data')
def go_to_database():  # this defines a function
   return render_template('data.html')

@app.route('/base')
def go_to_base():  # this defines a function
   return render_template('base.html')


if __name__ == '__main__':
    app.run()
