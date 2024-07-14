import pandas as pd
import pywhatkit as kit
import time
import pyautogui
import os
from datetime import datetime

# Carrega o arquivo de texto e adiciona os cabeçalhos
txt_file = 'lista.txt'
df_txt = pd.read_csv(txt_file, sep=';', header=None, names=['nome', 'telefone', 'cnpj'])

def activate_whatsapp_window():
    # Ativa a janela do WhatsApp Web usando pyautogui
    try:
        whatsapp_window = pyautogui.getWindowsWithTitle('WhatsApp')[0]
        print(f"Ativando a janela do WhatsApp: {whatsapp_window.title}")
        whatsapp_window.activate()
    except IndexError:
        print("Janela do WhatsApp não encontrada!")

def click_send_button():
    try:
        # Localiza a imagem do botão "Enviar" na tela
        button_location = pyautogui.locateOnScreen('send_button.png', confidence=0.8)
        if button_location is not None:
            print(f"Botão 'Enviar' encontrado: {button_location}")
            # Move o mouse para o botão e clica
            pyautogui.click(button_location)
        else:
            print("Botão 'Enviar' não encontrado!")
    except Exception as e:
        print(f"Erro ao localizar o botão 'Enviar': {e}")

def close_chrome_tab():
    try:
        # Comando AppleScript para fechar a aba atual do Google Chrome
        script = """
        tell application "Google Chrome"
            close active tab of window 1
        end tell
        """
        os.system(f"osascript -e '{script}'")
    except Exception as e:
        print(f"Erro ao fechar a aba do Chrome: {e}")

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Bom Dia"
    elif 12 <= current_hour < 20:
        return "Boa Tarde"
    else:
        return "Boa Noite"

# Loop para enviar as mensagens
for index, row in df_txt.iterrows():
    nome = row['nome'].split(' ')[0].capitalize()  # Pega apenas o primeiro nome
    telefone = str(row['telefone'])
    cnpj = str(row['cnpj'])
    
    # Valida o CNPJ e o telefone
    if len(cnpj) != 14 or not cnpj.isdigit():
        print(f"CNPJ inválido para {nome}: {cnpj}")
        continue
    if len(telefone) != 12 or not telefone.isdigit():
        print(f"Telefone inválido para {nome}: {telefone}")
        continue
    
    saudacao = get_greeting()
    
    # Formata a mensagem
    mensagem = f"{saudacao} {nome}, tudo bem? Esse contato é referente ao CNPJ: {cnpj}?"
    
    try:
        # Envia a mensagem via WhatsApp imediatamente
        kit.sendwhatmsg_instantly(f"+{telefone}", mensagem, 20)
        
        # Aguarda 15 segundos para que a mensagem seja digitada
        print("Aguardando 15 segundos para que a mensagem seja digitada...")
        time.sleep(15)
        
        # Verifica e alterna para a janela do WhatsApp Web diretamente
        activate_whatsapp_window()
        time.sleep(2)
        
        # Clica no botão "Enviar" para garantir que a mensagem seja enviada
        click_send_button()
        
    except Exception as e:
        print(f"Erro ao enviar mensagem para {telefone}: {e}")
    
    # Aguarda um tempo antes de enviar a próxima mensagem
    print("Esperando 5 segundos antes de enviar a próxima mensagem...")
    time.sleep(5)
    
    # Fecha a aba do Chrome após a ação ser concluída
    close_chrome_tab()
