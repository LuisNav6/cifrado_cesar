from flask import Flask, render_template, request
from cifradoCesar import cifrar_cesar, descifrar_cesar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    mensaje = request.form['mensaje']
    clave = int(request.form['clave'])
    modulo = int(request.form['modulo'])
    accion = request.form['accion']
    
    if accion == "cifrar":
        mensaje_procesado = cifrar_cesar(mensaje, clave, modulo)
    elif accion == "descifrar":
        mensaje_procesado = descifrar_cesar(mensaje, clave, modulo)
    
    return render_template('resultado.html', mensaje_procesado=mensaje_procesado)

if __name__ == '__main__':
    app.run(debug=True)
