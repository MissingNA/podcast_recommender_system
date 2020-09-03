# imports 
import numpy as np
import pickle 
from flask import Flask, Response, request, render_template, jsonify

# initialize the flask app 
app = Flask('my_app')

# route 1: welcome page
@app.route('/')
def home():
    #return a simple string
    return render_template('welcome to my podcast app!.html')

    # add an enter button 

#route 2: show a form to the user 
@app.route('/gen_rec')
def form():
    # use flaks's render_template function to display a html page 
    return render_template('form.html')

    # search bar that allows user to find podcast from a drop down menu

    # generate recommendation

    # if podcast name searched does not show up. 

    # suggest generate based on unseen data option

@app.route('/new_gen_rec')
def new_form():
    # field to enter in new podcast title, description and category [drop down menu]

    # generate prediction 

# route 3: return the results 
@app.route('/submit')
def submit():
    data = request.args # form data
    # load in the form data from the incoming request
    X_test = np.array([
        int(data['OverallQual'])
    ]).reshape(1, -1) 
    #manipulate data into a format that we pass to our model

    model = pickle.load(open('code/model.p', 'rb'))

    return render_template('results.html', recommendations=recs) 

# call app.run(debug=True) when python script is called 
if __name__ == '__main__': # if we run 'python_app.py' in the terminal 
    app.run(debug=True) 