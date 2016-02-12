import pycurl
import hashlib
from io import BytesIO
from bs4 import BeautifulSoup


class Mosenergosbyt:

    def __init__(self, login, password):
        self.balance = []
        self._cabinets = []
        self._email = login
        self._password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
        self._current_session = ''
        self._login()
        self._parseSessionId()
        self._loadLsList()
        self._loginWithLs()

    def _connect(self, url):
        self._response = BytesIO()
        try:
            c = pycurl.Curl()
            c.setopt(c.URL, url)
            c.setopt(c.CONNECTTIMEOUT, 10)
            c.setopt(c.TIMEOUT, 15)
            c.setopt(c.FAILONERROR, True)
            c.setopt(c.COOKIEFILE, '')
            c.setopt(c.COOKIEJAR, '')
            c.setopt(c.WRITEDATA, self._response)
            c.perform()
        except:
            return ConnectionError

    def _parseSessionId(self):
        soup = BeautifulSoup(self._response.getvalue(), 'xml')
        xmllist = soup.find_all('p')
        self._current_session = str(xmllist[7].string)

    def _login(self):
        url = ("https://lkkbyt.mosenergosbyt.ru/gate_lkk/do?process=login&type=1"
               "&ls=&pw_abn=%s&phone=&email=%s&api_version=5") % (self._password, self._email,)
        self._connect(url)

    def _refresh(self):
        url = "https://lkkbyt.mosenergosbyt.ru/gate_lkk/do?process=refresh&type=1&id_session=%s&api_version=5"\
            % (self._current_session,)
        self._connect(url)

    def _loadLsList(self):
        url = "https://lkkbyt.mosenergosbyt.ru/gate_lkk/do?process=lslistbymail&type=1&id_session=%s"\
                % (self._current_session,)
        self._connect(url)
        soup = BeautifulSoup(self._response.getvalue(), 'xml')
        bTag = soup.find_all('b')
        for i in bTag:
            self._cabinets.append(i.find_all('p')[0].string +\
                                  i.find_all('p')[1].string +\
                                  i.find_all('p')[2].string)

    def _loginWithLs(self):
        for ls in self._cabinets:
            url = ("https://lkkbyt.mosenergosbyt.ru/gate_lkk/do?process=login&type=1&"
                   "ls=%s&id_session=%s&phone=&api_version=5") % (ls, self._current_session)
            self._connect(url)
            self._parseSessionId()
            self._refresh()
            soup = BeautifulSoup(self._response.getvalue(), 'xml')
            b = soup.find('b')
            list = b.find_all('p')
            dict = {"Address": list[0].string,
                    "Full Name": list[2].string,
                    "Balance": list[14].string
                    }
            self.balance.append(dict)

if __name__ == "__main__":
    lgn = input("Email: ")
    pwd = input("Password :")
    a = Mosenergosbyt(lgn, pwd)
    print(a.balance)
