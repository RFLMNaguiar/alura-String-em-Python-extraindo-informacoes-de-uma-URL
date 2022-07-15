import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

    def sanitiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if not self.url:
            raise (ValueError, "ERRO: A URL inserida está vazia.")

        padrao = re.compile("(http(s)?://)?(www.)?(bytebank.com)(.br)?(/cambio)")
        match = padrao.match(self.url)
        if not match:
            raise (ValueError, "ERRO: A URL não é válida.")

    def get_url_base(self):
        interrogacao = self.url.find("?")
        return self.url[:interrogacao]

    def get_url_parametros(self):
        interrogacao = self.url.find("?")
        return self.url[interrogacao + 1:]

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"URL: {self.url}\n URL BASE:{self.get_url_base()}\n PARÂMETROS: {self.get_url_parametros()}"

    def __eq__(self, other):
        return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    total = float(quantidade) / VALOR_DOLAR
    print(f"O valor de R${quantidade} é ${total}.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    total = float(quantidade) * VALOR_DOLAR
    print(f"O valor de ${quantidade} é R${total}.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
