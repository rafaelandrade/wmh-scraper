import requests
from bs4 import BeautifulSoup


def main():
	url = "https://www.quintoandar.com.br/alugar/imovel/sao-paulo-sp-brasil/"
	request = requests.get(url=url)
	
	if request.status_code >= 200:
		pass


if __name__ == '__main__':
	main()
