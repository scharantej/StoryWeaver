 
# main.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adventure')
def adventure():
    # Get the user's choice from the query parameters
    choice = request.args.get('choice')

    # Determine the next scene or situation based on the user's choice
    if choice == 'option1':
        return render_template('adventure.html', scene='scene1')
    elif choice == 'option2':
        return render_template('adventure.html', scene='scene2')
    else:
        return render_template('adventure.html', scene='scene3')

@app.route('/end')
def end():
    # Get the user's choices from the query parameters
    choices = request.args.getlist('choices')

    # Determine the ending based on the user's choices
    if choices == ['option1', 'option2']:
        return render_template('end.html', ending='ending1')
    elif choices == ['option1', 'option3']:
        return render_template('end.html', ending='ending2')
    else:
        return render_template('end.html', ending='ending3')

if __name__ == '__main__':
    app.run()
