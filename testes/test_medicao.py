"""Seus testes do Marco 2 (veja a seção 5 do ENUNCIADO_MARCO2.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual, math.isclose ou
np.allclose, a não ser que a igualdade exata seja justamente o que você quer testar.
"""
import unittest

from elevatoria.acumuladores import AcumuladorIngenuo, AcumuladorKahan


class TestAcumuladorIngenuoExemplo(unittest.TestCase):
    """Exemplo do formato. `AcumuladorIngenuo` é código existente da base."""

    def test_sem_parcelas(self):
        """Sem nenhuma parcela, o total é zero."""
        self.assertEqual(AcumuladorIngenuo().total, 0.0)


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #7 (escreva-os ANTES de corrigir o defeito e confirme que falham).

class TestAcumuladorKahan(unittest.TestCase):
    """Testes de regressão da issue #7."""
    
    def test_soma_1000x1e_6(self): # não deixam usar "-" no nome de função, então usei "_"
        """Soma 1000 parcelas de 1e-6 com AcumuladorKahan e compara com o resultado exato."""
        acumulador = AcumuladorKahan()
        for _ in range(1000):
            acumulador.adicionar(1e-6)
        self.assertAlmostEqual(acumulador.total, 1e-3, places=10)

    def test_soma_um_milhao_de_decimos(self):
        """Soma um milhão de parcelas de 0,1 e verifica a compensação do erro."""
        acumulador = AcumuladorKahan()
        for _ in range(1_000_000):
            acumulador.adicionar(0.1)
        self.assertAlmostEqual(acumulador.total, 100_000.0, places=9)

    def test_soma_dez_mil_de_decimos(self):
        """Soma dez mil parcelas de 0,1 e detecta erro de arredondamento acumulado."""
        acumulador = AcumuladorKahan()
        for _ in range(10_000):
            acumulador.adicionar(0.1)
        self.assertAlmostEqual(acumulador.total, 1_000.0, places=12)

if __name__ == "__main__":
    unittest.main()
