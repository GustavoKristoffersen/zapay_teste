from service import SPService
from sp_parser import SPParser

#<----------------------- SERVICE TESTS ---------------------------------->

def test_service_with_paramater_all_should_return_all_api_items_available():
    service = SPService(
        license_plate="ABC1234", renavam="11111111111", debt_option="all"
    )
    response = service.debt_search()
    assert len(response) == 4
    assert response['Multas'] is not None
    assert response['IPVAs'] is not None
    assert response['DPVATs'] is not None
    assert response['Licenciamento'] is not None

def test_service_with_mercosul_plate_should_succeed():
    service = SPService(
        license_plate="ABC1C34", renavam="11111111111", debt_option="all"
    )
    response = service.debt_search()
    assert len(response) == 4
    assert response['Multas'] is not None
    assert response['IPVAs'] is not None
    assert response['DPVATs'] is not None
    assert response['Licenciamento'] is not None

def test_service_with_mercosul_plate_should_have_the_same_values_as_standard_plate():
    service_mercosul = SPService(
        license_plate="ABC1C34", renavam="11111111111", debt_option="all"
    )
    service_standard = SPService(
        license_plate="ABC1234", renavam="11111111111", debt_option="all"
    )

    response_mercosul = service_mercosul.debt_search()
    response_standard = service_standard.debt_search()

    assert len(response_mercosul) == 4
    assert len(response_standard) == 4
    assert response_mercosul['Multas'] == response_standard['Multas']
    assert response_mercosul['IPVAs'] == response_standard['IPVAs']
    assert response_mercosul['DPVATs'] == response_standard['DPVATs']
    assert response_mercosul['Licenciamento'] == response_standard['Licenciamento']

def test_service_with_paramater_ticket_should_return_only_ticket_api_items():
    service = SPService(
        license_plate="ABC1C34", renavam="11111111111", debt_option="ticket"
    )
    response = service.debt_search()
    assert len(response) == 4
    assert response['Multas']
    assert response['IPVAs'] == None
    assert response['DPVATs'] == None
    assert response['Licenciamento'] == None

def test_service_with_paramater_ipva_should_return_only_ipva_api_items():
    service = SPService(
        license_plate="ABC1C34", renavam="11111111111", debt_option="ipva"
    )
    response = service.debt_search()
    assert len(response) == 4
    assert response['IPVAs']
    assert response['Multas'] == None
    assert response['DPVATs'] == None
    assert response['Licenciamento'] == None

def test_service_with_paramater_dpvat_should_return_only_dpvat_api_items():
    service = SPService(
        license_plate="ABC1C34", renavam="11111111111", debt_option="dpvat"
    )
    response = service.debt_search()
    assert len(response) == 4
    assert response['DPVATs']
    assert response['IPVAs'] == None
    assert response['Multas'] == None
    assert response['Licenciamento'] == None

def test_service_with_paramater_licensing_should_return_only_licensing_api_items():
    service = SPService(
        license_plate="ABC1C34", renavam="11111111111", debt_option="licensing"
    )
    response = service.debt_search()
    assert len(response) == 4
    assert response['Licenciamento']
    assert response['DPVATs'] == None
    assert response['IPVAs'] == None
    assert response['Multas'] == None


#<----------------------- PARSER TESTS ---------------------------------->

def test_ipva_parser_values_should_succeed():
    service = SPService(
        license_plate="ABC1C34", renavam="11111111111", debt_option="ipva"
    )
    result = service.debt_search()
    parser = SPParser(data=result)

    response = parser.process_ipva_debts()

    assert type(response[0].get('amount')) == float
    assert response[0].get('description')
    assert response[0].get('title')
    assert response[0].get('type')
    assert response[0].get('year')
    assert response[0].get('year') == result.get('IPVAs').get('IPVA')[0].get('Exercicio')
    
