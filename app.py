from flask import Flask, render_template

from infrastructure import EnvironmentManager


app = Flask('pastebin')


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/secret')
def secret():
    em = EnvironmentManager()
    return em.get('TEST_SECRET')


if __name__ == '__main__':
    app.run()
