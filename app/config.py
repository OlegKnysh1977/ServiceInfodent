import os

def load_db_param(str):

    db_params = {
        "database": "",
        "user": "",
        "password": ""
        }
    
    lst_param = str.split(";")

    for sub_str in lst_param:
        pos_div_sumbol = sub_str.find("=")
        if pos_div_sumbol > -1:
            cur_param = sub_str[pos_div_sumbol + 1:]
            name_param = sub_str[:pos_div_sumbol].upper()
            match name_param:
                case "DBNAME":
                    db_params["database"] = cur_param
                case "UID":
                    db_params["user"] = cur_param
                case "PWD":
                    db_params["password"] = cur_param

    return db_params

INFODENT_CENTRAL = load_db_param(os.getenv("infodent.central", ""))
INFODENT_VO = load_db_param(os.getenv("infodent.central", ""))
INFODENT_SAVUSHKINA = load_db_param(os.getenv("infodent.central", ""))
INFODENT_KUPCHINO = load_db_param(os.getenv("infodent.central", ""))
INFODENT_VODETSTVO = load_db_param(os.getenv("infodent.central", ""))
INFODENT_BALTPERL = load_db_param(os.getenv("infodent.central", ""))
INFODENT_PARNAS = load_db_param(os.getenv("infodent.central", ""))

RABBIT = os.getenv("rabbit", "")
RABBIT_VIRTUAL_HOST = os.getenv("rabbit.virtual_host", "")
RABBIT_EXCHANGE = os.getenv("rabbit.exchange", "")
RABBIT_ROUTING_KEY = os.getenv("rabbit.routing_key", "")
LIST_OF_TOKENS = os.getenv("list_of_tokens", "").split(",")

WORKINGPATH = os.getcwd()

try:
    SERVICE_INFODENT_PORT = int(os.getenv("service.infodent.port", "8080"))
except ValueError:
    SERVICE_INFODENT_PORT = 8080
