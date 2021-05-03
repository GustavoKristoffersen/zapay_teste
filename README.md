# zapay_teste

Confira as instruções da atividade no arquivo "Instruções.pdf"

### Iniciar o projeto

--->> python main.py < debt_option > < license_plate > < renavam >

Onde:


debt_option = Informação a ser retornada, sendo:


       
       "ticket" - Multas do veículo
       
       "ipva" - IPVAs do veículo
       
       "dpvat" - DPVATs do veículo
       
       "licensing" - Licenciamento do veículo
       
       "all" - Tudo relacionado ao veículo
       
       
       
license_plate = Placa do carro, exemplo: "ABC1234" ou "ABC1C34"

renavam = Código renavam do veículo, exemplo: "11111111111"

Para testar, execute:

      python main.py all ABC1234 11111111111
      
      python main.py all ABC1C34 11111111111



### Testes

Para executar os testes, execute, na raíz do projeto:

              pytest tests.py
