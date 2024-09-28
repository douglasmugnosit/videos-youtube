import random
import time
from datetime import datetime

def funcao_a_ser_retried():
    if random.random() < 0.9:
        raise Exception("Algo deu errado!")  # Simula uma exceção aleatória
    return "Operação bem-sucedida"

def retry(funcao, max_tentativas, espera_inicial):
    tentativa = 0
    espera_atual = espera_inicial

    while tentativa < max_tentativas:
        try:
            resultado = funcao()
            return resultado  # Se a função for bem-sucedida, retornamos o resultado
        except Exception as e:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} - Tentativa {tentativa + 1} falhou: {str(e)}")
            tentativa += 1
            if tentativa < max_tentativas:
                time.sleep(espera_atual)
                espera_atual *= 2  # Aumenta o tempo de espera exponencialmente

    raise Exception(f"Até {max_tentativas} tentativas, todas falharam")

# Exemplo de uso
try:
    resultado = retry(funcao_a_ser_retried, max_tentativas=5, espera_inicial=1)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} - Resultado: {resultado}")
except Exception as e:
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} - Erro final: {str(e)}")
