class  TestStringMethods ( unittest . TestCase):


    def test_00_media ( self ):
        r1 = pedidos . get ( "http://localhost:5000/?nota1=6¬a2=7" )
    
        if "6.5" não estiver em  r1 . texto :
            auto . fail ("a média de 6 com 7 deveria ter dado 6.5")

def runTests ():
    suíte  = teste_de_unidade . defaultTestLoader . loadTestsFromTestCase (TestStringMethods)
    teste_de_unidade . TextTestRunner (verbosidade = 2 , failfast = True). correr (suíte)

    executarTestes ()