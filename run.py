from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import pandas as pd

app = Flask(__name__)
bootstrap = Bootstrap(app)
questions = [
    {'question': 'What is the name of your store?', 'field_name': 'name'},
    {'question': 'What is the balance left on your gift card?', 'field_name': 'balance'},
    {'question': 'What price are you selling at ?', 'field_name': 'price'},
    {'question': 'Which network would you like to receive funds at?',
        'field_name': 'network'},
    {'question': 'What’s your email address?', 'field_name': 'email'}
]

data = pd.DataFrame(columns=[question['field_name'] for question in questions])


@app.route('/results', methods=['GET', 'POST'])
def display():
    return data.to_html()


@app.route('/', methods=['GET', 'POST'])
def survey():
    global len_df
    if request.method == 'POST':
        # Save data and print to console
        user_data = request.form.to_dict()
        idx = int(user_data['question_index'])
        field = questions[idx]['field_name']
        print("field", field, user_data[field])
        if idx == 0:
            data.loc[len_df] = None
        data.loc[len_df, field] = user_data[field]
        print("Fields for question ", user_data['question_index'])

        # Render next question or finish survey
        question_index = int(user_data['question_index'])
        print(data)
        if question_index == len(questions) - 1:

            data.to_csv('data.csv', index=False)
            len_df += 1
            return 'Thank you for taking the survey!'
        else:
            question_index += 1
            return render_template('survey.html', question=questions[question_index]['question'], field_name=questions[question_index]['field_name'], question_index=question_index)
    else:
        # Clear the "dirty" attribute of the form
        return render_template('survey.html', question=questions[0]['question'], field_name=questions[0]['field_name'], question_index=0)


@app.route('/survey')
def survey_page():
    return render_template('survey.html')


@app.route('/leave')
def leave():
    print('user left')
    # return render_template('survey.html')


@app.route('/results')
def results():
    data = pd.read_csv('data.csv')
    return render_template('results.html', data=data)


if __name__ == '__main__':
    try:
        data = pd.read_csv('data.csv')
        len_df = len(data)
    except:
        data = pd.DataFrame(
            columns=['name', 'balance', 'price', 'network', 'email'])
        len_df = 0
    app.run(debug=True, host='0.0.0.0', port=5001)
