import pyautogui
import keyboard
import time

# Lista com 30 pesquisas sobre mercado financeiro
pesquisas = [
    "o que é mercado financeiro",
    "como investir em ações" 
    '''
    "o que é renda fixa",
    "o que é renda variável",
    "como funciona a bolsa de valores",
    "o que é day trade",
    "o que é swing trade",
    "fundos imobiliários o que são",
    "tesouro direto como funciona",
    "o que é inflação",
    "taxa selic hoje",
    "como montar uma carteira de investimentos",
    "diversificação de investimentos",
    "análise técnica ações",
    "análise fundamentalista ações",
    "o que são dividendos",
    "como investir em fundos de investimento",
    "mercado financeiro para iniciantes",
    "como investir com pouco dinheiro",
    "riscos do mercado financeiro",
    "o que é liquidez",
    "o que é volatilidade",
    "como funciona o mercado de câmbio",
    "o que é dólar futuro",
    "criptomoedas mercado financeiro",
    "bitcoin vale a pena",
    "o que é índice bovespa",
    "como funciona o home broker",
    "o que são ETFs",
    "Fim" 
    '''
]


time.sleep(2)
# Abrir o navegador sozinho

pyautogui.press('win')  # tecla windows
pyautogui.write("edge")  # nome do navegador
pyautogui.press('enter')


time.sleep(2)

for pesquisa in pesquisas:
    # Foca a barra de endereços
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)

    # Digita a pesquisa
    #pyautogui.write(pesquisa, interval=0.05)
    keyboard.write(pesquisa)
    time.sleep(1)

    # Pressiona Enter
    pyautogui.press('enter')

    # Aguarda alguns segundos antes da próxima pesquisa
    time.sleep(5)