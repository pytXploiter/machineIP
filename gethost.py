import socket
from requests import get


def getLAN():
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		ip = s.getsockname()[0]
		s.close()
		return ip

def getWAN():
		ip = get('https://api.ipify.org').text
		return ip