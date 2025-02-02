import unittest
from apps.validators import Validators


class TesteValidadores(unittest.TestCase):

    def setUp(self):
        self.validador = Validators()

    def test_identificadores_validos(self):
        ids_validos = ["teste", "_valido", "Var123", "a1b2c3", "_sublinhado"]
        for identificador in ids_validos:
            with self.subTest(identificador=identificador):
                self.assertTrue(self.validador.check_valid_identifier(identificador))

    def test_identificadores_invalidos(self):
        ids_invalidos = ["1nvalido", "$imbolo", "ob", "palavreadomuitogrande", "@caractere"]
        for identificador in ids_invalidos:
            with self.subTest(identificador=identificador):
                self.assertFalse(self.validador.check_valid_identifier(identificador))

    def test_emails_validos(self):
        emails_validos = ["teste@teste.com", "usuario.nome@qqcoisa.coun", "valido_123@sub.qqcoisa.net"]
        for email in emails_validos:
            with self.subTest(email=email):
                self.assertTrue(self.validador.check_email(email))

    def test_emails_invalidos(self):
        emails_invalidos = ["enderecoqualquer", "@usuario.com", "usuario@.com", "usuario@dominio,com"]
        for email in emails_invalidos:
            with self.subTest(email=email):
                self.assertFalse(self.validador.check_email(email))

    def test_palavras_reservadas_python(self):
        palavras_chave = ["if", "else", "while", "return", "class"]
        for palavra in palavras_chave:
            with self.subTest(palavra=palavra):
                self.assertTrue(self.validador.check_keywords_python([palavra]))

    def test_nao_palavras_reservadas_python(self):
        palavras_normais = ["ola", "mundo", "python", "funcao", "validar"]
        for palavra in palavras_normais:
            with self.subTest(palavra=palavra):
                self.assertFalse(self.validador.check_keywords_python([palavra]))

    def test_senhas_validas(self):
        senhas_validas = ["Senha1@forte", "Forte@1", "Senhatop_1@pipi"]
        for senha in senhas_validas:
            with self.subTest(senha=senha):
                self.assertEqual(self.validador.check_password(senha), 0)

    def test_senhas_invalidas(self):
        senhas_invalidas = ["curta", "SemNumero@", "minusculas1@", "MAIUSCULAS1@", "SemEspec123"]
        for senha in senhas_invalidas:
            with self.subTest(senha=senha):
                self.assertEqual(self.validador.check_password(senha), -1)

    def test_idade_para_trabalho(self):
        casos_idade = [(15, "Não Empregar"), (17, "Empregado Parcial"), (30, "Empregado Integral"),
                       (101, "Empregado Múmia")]
        for idade, esperado in casos_idade:
            with self.subTest(idade=idade):
                self.assertEqual(self.validador.check_age_for_work(idade), esperado)

if __name__ == '__main__':
    unittest.main()
