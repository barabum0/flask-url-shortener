from flask import Flask, render_template, send_file, request, Response, redirect
import sqlite3
import yaml
import string
import os
from random import choice

app = Flask(__name__)
yamls = yaml.safe_load(open("config.yml", "r"))

def random_string(str_size, chars):
    return ''.join(choice(chars) for _ in range(str_size))

if not os.path.exists("links.db"):
    db = open("links.db", "w+").close()
con = sqlite3.connect("links.db")
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS links ('
                'code VARCHAR NOT NULL UNIQUE,'
                'link VARCHAR NOT NULL'
                ')')
con.commit()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/script.js')
def scriptjs():
    return send_file("templates/script.js")

@app.route('/genlink')
def genlink():
    check_unique = yamls.get("check_unique")
    con = sqlite3.connect("links.db")
    with con:
        link = request.headers.get("link")
        if link == None:
            return Response(
                "Link not found",
                400
            )
        cur = con.cursor()
        codel = random_string(yamls.get("link_length"), string.ascii_letters)
        if check_unique:
            if cur.execute(f"SELECT true FROM links WHERE link = '{link}'").fetchall():
                return cur.execute(f"SELECT code FROM links WHERE link = '{link}'").fetchall()[0][0]
            else:
                cur.execute(f"INSERT INTO links(code,link) VALUES('{codel}', '{link}')")
        else:
            cur.execute(f"INSERT INTO links(code,link) VALUES('{codel}', '{link}')")

        con.commit()

        return yamls.get("domain")+codel

@app.route('/<code>')
def getlink(code):
    con = sqlite3.connect("links.db")
    with con:
        cur = con.cursor()

        if cur.execute(f"SELECT link FROM links WHERE code = '{code}'").fetchall():
            link = cur.execute(f"SELECT link FROM links WHERE code = '{code}'").fetchall()[0][0]
            s = link
            if s.find("http://") != 0 and s.find("https://") != 0:
                link = "http://" + s
            return redirect(link), 302
        else:
            return render_template("no_link.html"), 404
# @app.route('/httptest')
# def test():
#     return "test ok! ✅"

if __name__ == '__main__':
    app.run()
