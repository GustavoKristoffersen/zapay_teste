# zapay_teste

Confira as instruções da atividade no arquivo "Instruções.pdf"

### Iniciar o projeto

--->> python main.py < debt_option > < license_plate > < renavam >

Onde:


debt_option = Informação a ser retornada, sendo:


       
       "ticket" - Multas do veículo
       
       "ipva" - Taxas de IPVA do veículo
       
       "dpvat" - Taxas de DPVAT do veículo
       
       "licensing" - Taxas de licenciamento do veículo
       
       "all" - Todas as taxas relacionadas ao veículo
       
       
       
license_plate = Placa do veículo, exemplo: "ABC1234"(formado padrão) ou "ABC1C34"(formado Mercosul)

renavam = Código renavam do veículo, exemplo: "11111111111"

Para fins de teste da atividade, execute:

      python main.py all ABC1234 11111111111
      
      python main.py all ABC1C34 11111111111
      
      python main.py licensing ABC1C34 11111111111



### Testes

Para executar os testes, execute, na raíz do projeto:

              pytest tests.py
