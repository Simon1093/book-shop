from datetime import datetime
from bson import ObjectId

from flask import Flask, render_template, redirect, request

from repositories import PasteBinRepository
from models import PasteBin


app = Flask('pastebin')

pastebin_repo = PasteBinRepository()


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return redirect('/')
    attrs = {}
    title = request.form.get('title')
    attrs['title'] = title if title != '' else 'No title'
    attrs['data'] = request.form.get('data')
    attrs['datetime'] = datetime.now()
    if len(attrs['data']) == 0:
        return redirect('/')
    pastebin = PasteBin(attrs)
    result = pastebin_repo.insert_one(pastebin)
    return redirect(f'/pastebin/{result}')


@app.route('/pastebin/<pastebin_id>')
def pastebin(pastebin_id):
    try:
        pastebin_id = ObjectId(pastebin_id)
    except:
        return redirect('/')
    result = pastebin_repo.find_one({'_id': pastebin_id})
    if result is None:
        return redirect('/')
    return render_template('pastebin.html', result=result.to_json())


if __name__ == '__main__':
    app.run()
