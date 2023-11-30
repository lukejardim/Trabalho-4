from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_fatorial(n):
    if n == 0:
        return 1
    return n * calcular_fatorial(n - 1)

def calcular_fibonacci(n):
    if n <= 1:
        return n
    return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

@app.route('/api/calculos', methods=['POST'])
def calcular():
    dados = request.get_json()

    if 'tipo' not in dados or 'valor' not in dados:
        return jsonify({'erro': 'Forneça o tipo (fatorial ou fibonacci) e o valor.'}), 400

    tipo = dados['tipo']
    valor = dados['valor']

    if tipo == 'fatorial':
        resultado = calcular_fatorial(valor)
    elif tipo == 'fibonacci':
        resultado = calcular_fibonacci(valor)
    else:
        return jsonify({'erro': 'Tipo inválido. Escolha entre fatorial ou fibonacci.'}), 400

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)