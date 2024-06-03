from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '06140818',
    'host': 'localhost',
    'database': 'avaliacoes_site'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT nome, avaliacao, comentario, data FROM avaliacoes ORDER BY data DESC')
    reviews = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', reviews=reviews)

@app.route('/add_review', methods=['POST'])
def add_review():
    nome = request.form['nome']
    avaliacao = int(request.form['avaliacao'])
    comentario = request.form['comentario']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO avaliacoes (nome, avaliacao, comentario) VALUES (%s, %s, %s)', (nome, avaliacao, comentario))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

@app.route('/sinopse')
def sinopse():
    return render_template('sinopse.html')

@app.route('/personagens')
def personagens():
    return render_template('personagens.html')

if __name__ == '__main__':
    app.run(debug=True)