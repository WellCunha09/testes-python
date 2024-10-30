# 1) Importar a classe 'calculadora'
from calculadora import  calculadora

# 2) Importar o pacote de testes unitarios
import unittest 

# 3) Criar a classe de testes unitarios
class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
    self.calc = calculadora()    # Criando o teste do metodo 'soma'
    
    def test_soma(self):
    self.assertEqual(self.calc.soma(10, 10), 20, "Deve somar dois numeros")


# Executar a classe de testes unitarios
if __name__ == "__main__":
    unittest.main()