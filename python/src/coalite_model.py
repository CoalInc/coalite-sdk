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
    def __init__(self, url: str, public_key: str, signer_id: str):
        '''
            :param url: The coalite server url.
        '''
        self.__url = url
        self.__key = public_key
        self.__id = signer_id

    def claim_new_coalite(self) -> SimpleNamespace:
        '''
            Get newly emited coalite and claim it
        '''
        coal = self.__get_coalite()
        claim_request = self.__make_action_request(coal, CoaliteAction.CLAIM)
        result = requests.post(self.__url, json=claim_request)
        if result_is_not_good:
            return None

        return coal

    def mint_coalite(self, coalite: SimpleNamespace, payload: str):
        mint_request = self.__make_action_request(coalite, CoaliteAction.MINT, payload)

    def __get_coalite(self):
        resp = requests.get(self.__url)
        return json.loads(resp.text, object_hook=lambda d: SimpleNamespace(**d))

    def __make_action_request(self, coal: SimpleNamespace, action: CoaliteAction, payload: str = '') -> Request:
        # create signature
        # sign data (payload)
        # return Request
        pass
