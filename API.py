# 1- API para consultar, criar, editar e excluir itens.
# 2- URL base - localhost
# 3- Endpoints -
        # localhost/agentes (GET)
        # localhost/agentes/id (GET)
        # localhost/agente/id (PUT)
        # localhost/agente/id (DELETE)
# 4- Quais recursos - agentes do R6

from flask import Flask, jsonify, request

app = Flask(__name__) #inicia o flask

agentes = [
        {
                'id': 1,
                'nome': 'Jordan Trace',
                'local': 'Plano, TX',
                'agente': 'Thermite',
                'gadgets': 'Carga Exotérmica',
                'especialidade': 'invasão, suporte',
                'esquadrao': 'REDHAMMER',
                'lado': 'ATACANTE',
                'dificuldade': '1',
                'velocidade': '2',
                'saude': '2'
        },
        {
                'id': 2,
                'nome': 'Sebastian Cote',
                'local': 'Montreal, QC',
                'agente': 'Buck',
                'gadgets': '12 espingarda acoplada',
                'especialidade': 'invasão, suporte',
                'esquadrao': 'REDHAMMER',
                'lado': 'ATACANTE',
                'dificuldade': '1',
                'velocidade': '2',
                'saude': '2'
        },
        {
                'id': 3,
                'nome': 'Ana Valentina Diaz',
                'local':'Zipaquira, Colombia',
                'agente': 'SOLIS',
                'gadgets': 'SPEC-IO Electro_Sensor',
                'especialidade': 'intel, suporte',
                'esquadrao': 'GHOSTEYES',
                'lado': 'DEFENSOR',
                'dificuldade': '3',
                'velocidade': '2',
                'saude': '2'
        }
]

# Consultar(todos)
@app.route('/agentes',methods=['GET'])
def obter_agentes():
        
        return jsonify(agentes)

# Consultar(id)
@app.route('/agentes/<int:id>',methods=['GET'])
def obeter_agente_por_id(id):
        for agente in agentes:
               if agente.get('id') == id:
                       
                       return jsonify(agente)
               
# Editar
@app.route('/agentes/<int:id>',methods=['PUT'])
def editar_agente_por_id(id):
        agente_alterado = request.get_json()
        for indice,agente in enumerate(agentes):
                if agente.get('id') == id:
                        agentes[indice].update(agente_alterado)
                        
                        return jsonify(agentes[indice])
             
# Criar
@app.route('/agentes',methods=['POST'])
def adicionar_agente():
           novo_agente = request.get_json()
           agentes.append(novo_agente)
           
           return jsonify(agentes)
   
# Excluir
@app.route('/agentes/<int:id>', methods=['DELETE'])
def excluir_agente(id):
        for indice, agente in enumerate(agentes):
                if agente.get('id') == id:
                        del agentes[indice]
                        
                        return jsonify(agentes)

app.run(port=5000,host='localhost',debug=True)