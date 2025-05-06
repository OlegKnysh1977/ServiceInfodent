import os

INFODENT_CENTRAL = os.getenv("infodent.central", "")
INFODENT_VO = os.getenv("infodent.central", "")
INFODENT_SAVUSHKINA = os.getenv("infodent.central", "")
INFODENT_KUPCHINO = os.getenv("infodent.central", "")
INFODENT_VODETSTVO = os.getenv("infodent.central", "")
INFODENT_BALTPERL = os.getenv("infodent.central", "")
INFODENT_PARNAS = os.getenv("infodent.central", "")

RABBIT = os.getenv("rabbit", "")
RABBIT_VIRTUAL_HOST = os.getenv("rabbit.virtual_host", "")
RABBIT_EXCHANGE = os.getenv("rabbit.exchange", "")
RABBIT_ROUTING_KEY = os.getenv("rabbit.routing_key", "")
LIST_OF_TOKENS = os.getenv("list_of_tokens", "").split(",")

WORKINGPATH = os.getcwd()

