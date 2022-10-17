import hashlib  # Se utiliza para calcular el hash de un bloque
import json  # Utilizado en el método de hash
from time import time  # Utilizado para dar marca temporal a los bloques


class Blockchain(object):

    # Método utilizado en python para inicializar los atributos del objeto
    # https://www.geeksforgeeks.org/__init__-in-python/
    def __init__(self):
        self.chain = []  # Esta lista representa la cadena de bloques
        self.transacciones_pendientes = []  # Lista con las transacciones que aún no han sido añadidas a un bloque,
        # vacía por defecto

        # Definimos el primer bloque con un hash arbitrario
        # https://coingeek.com/the-mystery-of-the-genesis-block/
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.",
                       proof=100)

    def new_block(self, proof, previous_hash=None):
        # TAREA 1: Definir diccionario block
        block = {
            'index': len(self.chain) + 1,  # Longintud de self.chain + 1
            'timestamp': time(),
            'transactions': self.transacciones_pendientes,  # Se le asigna el valor de self.pending_transactions
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            # Le pasamos a self.hash() el último bloque de la cadena self.chain
        }
        # TAREA 2: Vaciar self.transacciones_pendientes, ya que ahora estas transacciones pendientes se han asociado
        # al nuevo bloque
        self.transacciones_pendientes = []
        # TAREA 3: Insertar bloque al final de la lista self.chain
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        # TAREA 4: Devolver el último bloque de la cadena self.chain
        return self.chain[-1]

    def new_transaction(self, emisor, receptor, cantidad):
        # TAREA 5: definir diccionario de transacción
        transaction = {
            'emisor': emisor,
            'receptor': receptor,
            'cantidad': cantidad
        }
        # TAREA 6: insertar la transacción en la lista self.transacciones_pendientes
        self.transacciones_pendientes.append(transaction)
        # TAREA 7: Devolver el índice del último bloque incrementado en 1
        return self.chain[-1]["index"] + 1

    # Devolvemos un hash del bloque convertido a texto previamente
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


# Creamos la blockchain
blockchain = Blockchain()

# Realizamos 3 transacciones
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
# Creamos un nuevo bloque
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
t5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
t6 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
blockchain.new_block(6789)

# Imprimimos la cadena
print("Genesis block: ", blockchain.chain)
