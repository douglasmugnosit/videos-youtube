import random
import time
from datetime import datetime

def funcao_a_ser_retried():
    if random.random() < 0.9:
        raise Exception("Algo deu errado!")  # Simula uma exceção aleatória
    return "Operação bem-sucedida"

def retry(funcao, max_tentativas, espera_segundos):
    tentativa = 0
    while tentativa < max_tentativas:
        try:
            resultado = funcao()
            return resultado  # Se a função for bem-sucedida, retornamos o resultado
        except Exception as e:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Tentativa {tentativa + 1} falhou: {str(e)}")
            tentativa += 1
            time.sleep(espera_segundos)  # Espera um tempo antes de tentar novamente
    raise Exception(f"Até {max_tentativas} tentativas, todas falharam")

# Exemplo de uso
try:
    resultado = retry(funcao_a_ser_retried, max_tentativas=5, espera_segundos=1)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Resultado: {resultado}")
except Exception as e:
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Erro final: {str(e)}")
