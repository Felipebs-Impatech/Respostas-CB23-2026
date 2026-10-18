"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest
import numpy as np

from elevatoria.dados import (por_tag, contagem_por_tag, criar_conversores, ler_log, medir_memoria,
                              medir_tempos, serie, valida_tag)
from elevatoria.serie import SerieTemporal

class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])

# Abaixo mais um teste de elevatoria.dados
class TestContagemPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `contagem_por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, contagem_por_tag devolve um dicionário vazio."""
        self.assertEqual(contagem_por_tag([]), {})

# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #4 (escreva-os ANTES de corrigir o defeito e confirme que falham).

class TestSerieTemporal(unittest.TestCase):
    """Testes de regressão da issue #4."""

    def test_media_movel(self):
        """Médias móveis de janela 3."""
        s = SerieTemporal.de_lista([1, 2, 3, 4, 5])
        esperado = SerieTemporal.de_lista([2.0, 3.0, 4.0])
        resultado = s.media_movel(3)
        self.assertTrue(np.allclose(resultado, esperado), f"esperado {esperado}, obtido {resultado}")

    def test_variacao(self):
        """Diferenças entre pontos consecutivos."""
        s = SerieTemporal.de_lista([1, 3, 2, 5])
        esperado = SerieTemporal.de_lista([2.0, -1.0, 3.0])
        resultado = s.variacao()
        self.assertTrue(np.allclose(resultado, esperado), f"esperado {esperado}, obtido {resultado}")

if __name__ == "__main__":
    unittest.main()
