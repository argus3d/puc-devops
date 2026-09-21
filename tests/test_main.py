import unittest
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):

    @patch("builtins.print")
    def test_mensagem_github_actions(self, mock_print):
        main.main()

        mock_print.assert_any_call(
            "GitHub Actions funcionando corretamente!"
        )

    @patch("builtins.print")
    def test_mensagem_continuous_integration(self, mock_print):
        main.main()

        mock_print.assert_any_call(
            "Teste de Continuous Integration realizado com sucesso."
        )

    @patch("builtins.print")
    def test_main_imprime_duas_mensagens(self, mock_print):
        main.main()

        self.assertEqual(mock_print.call_count, 2)

    @patch("builtins.print")
    def test_ordem_das_mensagens(self, mock_print):
        main.main()

        chamadas = mock_print.call_args_list

        self.assertEqual(
            chamadas[0].args[0],
            "GitHub Actions funcionando corretamente!"
        )

        self.assertEqual(
            chamadas[1].args[0],
            "Teste de Continuous Integration realizado com sucesso."
        )

    @patch("builtins.print")
    def test_main_retorna_none(self, mock_print):
        resultado = main.main()

        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()
