class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)

    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        return url.split()

    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise (ValueError, "ERRO: A URL inserida está vazia.")

    def get_url_base(self):
        """Retorna a base da url."""
        interrogacao = self.url.find("?")
        return self.url[:interrogacao]

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        interrogacao = self.url.find("?")
        return self.url[interrogacao + 1:]

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
