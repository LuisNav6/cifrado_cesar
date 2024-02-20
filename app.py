from flask import Flask, render_template, request, jsonify
from cifradoCesar import cifrar_cesar, descifrar_cesar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    #1
    """
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        clave = int(request.form['clave'])
        accion = request.form['accion']

        if accion == "cifrar":
            mensaje_procesado = cifrar_cesar(mensaje, clave)
        elif accion == "descifrar":
            mensaje_procesado = descifrar_cesar(mensaje, clave)

        return jsonify({"mensaje_procesado": mensaje_procesado})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
