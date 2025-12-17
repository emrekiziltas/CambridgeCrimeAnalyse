from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # simulator2.html içeriğini oku
    with open('templates/simulator2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    return render_template('simulator.html', preview_content=content)


if __name__ == '__main__':
    app.run(debug=True, port=5000)