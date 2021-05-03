# zapay_teste

Confira as instruções no arquivo "Instruções.pdf"

### Iniciar o projeto

--->> python main.py <info_to_check> <vehicle_plate> <vehicle_renavam>

Onde:


info_to_check = Informação a ser retornada, sendo:


       
       "ticket" - Multas do veículo
       
       "ipva" - IPVAs do veículo
       
       "dpvat" - DPVATs do veículo
       
       "licensing" - Licenciamento do veículo
       
       "all" - Tudo relacionado ao veículo
       
       
       
vehicle_plate = Placa do carro, exemplo: "ABC1234" ou "ABC1C34"

vehicle_renavam = Renavam do veículo, exemplo: "11111111111"

Para teste, execute:

      python main.py all ABC1234 11111111111
      
      python main.py all ABC1C34 11111111111
