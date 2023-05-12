import pytest

#chama a função main do arquivo main.py e executa os testes. Com os seguintes argumentos: -v: exibe informações verbosas sobre o teste. -s: exibe informações de saída durante o teste. --cov: Opções para medir a cobertura dos testes usando o pacote coverage. --cov=. --cov-report=html: especifica o diretório raiz para a cobertura e --cov-report=html gera um relatório de cobertura em formato HTML..

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--cov=.", "--cov-report=html"])