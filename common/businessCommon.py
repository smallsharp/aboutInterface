from common import mUtils
from common import mRequests
import readConfig as readConfig

localReadConfig = readConfig.ReadConfig()
localConfigHttp = mRequests.MyRequests()
localLogin_xls = mUtils.get_xls("userCase.xlsx", "login")
localAddAddress_xls = mUtils.get_xls("userCase.xlsx", "addAddress")


# login
def login():
    """
    login
    :return: token
    """
    # set url
    url = mUtils.get_url_from_xml('login')
    localConfigHttp.set_url(url)

    # set header
    token = localReadConfig.get_headers("token_v")
    header = {"token": token}
    localConfigHttp.set_headers(header)

    # set param
    data = {"email": localLogin_xls[0][3],
            "password": localLogin_xls[0][4]}
    localConfigHttp.set_data(data)

    # login
    response = localConfigHttp.post().json()
    token = mUtils.get_value(response, "member", "token")
    return token


# logout
def logout(token):
    """
    logout
    :param token: login token
    :return:
    """
    # set url
    url = mUtils.get_url_from_xml('logout')
    localConfigHttp.set_url(url)

    # set header
    header = {'token': token}
    localConfigHttp.set_headers(header)

    # logout
    localConfigHttp.get()


