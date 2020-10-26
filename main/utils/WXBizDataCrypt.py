import base64
import json
from Crypto.Cipher import AES


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)

        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)).decode('utf-8'))

        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

if __name__ == '__main__':
    appId="wx28a93f4b755e759a"
    sessionKey = 'ji3i2yCX10LreEWRi7SkgA=='
    iv = 'rPtIiKOIRY43ISuDQSxkVQ=='
    encryptedData = 'kni+uXBns4plHSwwodpDCPtfWst+R1Xc1OZjUPLsc87g3qavl1DCr93oGFiZONfYohi8R47c+mmS74kqv4yVVPel+o1AW4Ph55QDLuEvtKmzUyWNcfG6D5qvRwJwP+4RP5YIO2y8LL5diYsBSO06rXmZHavoie7Scu+vhptLIUP3IMm3yrXyX7M8/KpWflUMe/8S82BtHJKPflCaWx2ShA=='
    # def get_phone(sessionKey, encryptedData, iv):
    pc = WXBizDataCrypt(appId, sessionKey)
    print(pc.decrypt(encryptedData, iv))
