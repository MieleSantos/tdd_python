from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_retorna_22(self):
        
        entrada = "13/03/2000" #Given-COntexto
        esperado = 24
        funcionario_teste = Funcionario("teste",entrada,2000) 
        
        #when-ação
        resultado = funcionario_teste.idade()
        print(resultado)
        # Then-desfecho
        assert esperado == resultado
        
    
    def test_quando_sobrenome_recebe_lucas_carvalho_retorna_carvalho(self):
        
        entrada = " lucas carvalho "
        esperado = "carvalho"
        
        lucas = Funcionario(entrada,"11/11/2000",1111)
        
        resultado = lucas.sobrenome()
        
        assert resultado==esperado