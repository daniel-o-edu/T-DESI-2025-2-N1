from flask import Flask, render_template

app = Flask(__name__)

# Rota principal (Controller)
@app.route('/')
def index():
    # Fonte de Dados (Simulação de Banco de Dados)
    musicJ = [
        {
            "titulo": "Bohemian Rhapsody",
            "artista": "Queen",
            "estilo": "Rock",
            "fileName": "bohemian_rhapsody.mp3",
            "duracao": "5:55"
        },
        {
            "titulo": "Smells Like Teen Spirit",
            "artista": "Nirvana",
            "estilo": "Grunge",
            "fileName": "smells_like.mp3",
            "duracao": "5:01"
        },
        {
            "titulo": "Shape of You",
            "artista": "Ed Sheeran",
            "estilo": "Pop",
            "fileName": "shape_of_you.mp3",
            "duracao": "3:53"
        }
    ]
    
    # Injeção de Dependência Visual (Context Passing)
    # Passamos a variável musicJ para o template 'playlist.html'
    return render_template('playlist.html', musicJ=musicJ)

if __name__ == '__main__':
    app.run(debug=True)
