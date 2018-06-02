import os
from flask import Flask, redirect, render_template, request
from random import choice
import json

app = Flask(__name__)


welcome_messages = ["Hi", "Hello", "Bonjour", "Ciao", "Hola", "Annyeonghaseyo"]

def load_list(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = f.read()
            items = json.loads(data)
    else:
        items = []
        
    return items
    
def save_list(filename, items):
    with open(filename, "w") as f:
        data = json.dumps(items)
        f.write(data)
    


@app.route("/")
def get_index():
    items = load_list("data/list.json")    
    welcome = choice(welcome_messages)
    return render_template('index.html', msg=welcome, tasks=items)

@app.route("/new_task", methods=['POST'])
def create_a_task():
    task = request.form['task_to_do']
    
    items = load_list("data/list.json")
    items.append(task)
    save_list("data/list.json", items)
    
    return redirect("/")


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)