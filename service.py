from api import API
import json


class SPService:
    """
    Conecta com o webservice do Detran-SP.
    """

    def __init__(self, **kwargs):
        """
        Construtor.
        """
        self.params = kwargs

        # Converte a placa para o modelo padrão, caso esteja no modelo Mercosul.
        plate_char = self.params["license_plate"][4]

        if plate_char.isalpha():
            with open("mercosul_plate_convertion.json", "r") as mp:
                mp = json.loads(mp.read())
                converted_num = mp[plate_char]
                self.params["license_plate"] = f"{self.params['license_plate'][:4]}{converted_num}{self.params['license_plate'][5:]}"

    def get_json_response(self, method):
        """
        Pega a resposta da requisição em json.
        """
        api = API(self.params["license_plate"], self.params["renavam"], method)
        return api.fetch()

    def debt_search(self):
        """
        Pega os débitos de acordo com a opção passada.
        """

        if self.params["debt_option"] == "ticket":
            response_json = self.get_json_response("ConsultaMultas")

        elif self.params["debt_option"] == "ipva":
            response_json = self.get_json_response("ConsultaIPVA")

        elif self.params["debt_option"] == "dpvat":
            response_json = self.get_json_response("ConsultaDPVAT")

        elif self.params["debt_option"] == "licensing":
            response_json = self.get_json_response("ConsultaLicenciamento")
            response_json = {
                "Licenciamento": {
                    "Exercicio": response_json.get("Exercicio"),
                    "TaxaLicenciamento": response_json.get("TaxaLicenciamento"),
                }
            }

        elif self.params["debt_option"] == "all":
            ticket_json = self.get_json_response("ConsultaMultas")
            ipva_json = self.get_json_response("ConsultaIPVA")
            dpvat_json = self.get_json_response("ConsultaDPVAT")
            licensing_json = self.get_json_response("ConsultaLicenciamento")

            response_json = {
                "Multas": ticket_json.get("Multas"),
                "IPVAs": ipva_json.get("IPVAs"),
                "DPVATs": dpvat_json.get("DPVATs"),
                "Licenciamento": {
                    "Exercicio": licensing_json.get("Exercicio"),
                    "TaxaLicenciamento": licensing_json.get("TaxaLicenciamento"),
                },
            }

        else:
            raise Exception("opção inválida")

        debts = {
            "IPVAs": response_json.get("IPVAs") or {},
            "DPVATs": response_json.get("DPVATs") or {},
            "Multas": response_json.get("Multas") or {},
            "Licenciamento": response_json.get("Licenciamento") or {},
        }

        for debt in debts:
            if debts[debt] == {}:
                debts[debt] = None

        return debts
