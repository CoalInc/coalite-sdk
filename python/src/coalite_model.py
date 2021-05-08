import datetime
import enum
import json
from types import SimpleNamespace
import requests
from Crypto.PublicKey import RSA

class CoaliteAction(enum.Enum):
    EMIT = 'EMIT'
    PUBLISH = 'PUBLISH'
    CLAIM = 'CLAIM'
    TRANSFER = 'TRANSFER'
    ACCEPT = 'ACCEPT'
    MINT = 'MINT'
    BURN = 'BURN'


class CoaliteIfce:
    def __init__(self, url: str):
        '''
            :param url: The coalite server url.
        '''
        self.__url = url

    def claim_new_coalite(self, payload: str) -> SimpleNamespace:
        '''
            Get newly emited coalite and claim it
        '''
        coal = self.__get_coalite()
        claim_request = self.__make_action_request(coal, CoaliteAction.CLAIM, payload)
        result = requests.post(self.__url, json=claim_request)

    def __get_coalite(self):
        resp = requests.get(self.__url)
        return json.loads(resp.text, object_hook=lambda d: SimpleNamespace(**d))

    def __make_action_request(self, coal: SimpleNamespace, action: CoaliteAction, payload: str, public_key: str, signer_id: str):
        return "request"
