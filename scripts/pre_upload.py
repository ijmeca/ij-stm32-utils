import os
import subprocess
from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

# Caminho absoluto para o OpenOCD
OPENOCD = "/Users/ijmeca/.platformio/packages/tool-openocd/bin/openocd"
OPENOCD_SCRIPTS = "/Users/ijmeca/.platformio/packages/tool-openocd/openocd/scripts"

def disable_protection(source, target, env):
    print("Verificando proteção de leitura (ROP)...")

    openocd_command = [
        OPENOCD,
        "-f", f"{OPENOCD_SCRIPTS}/interface/stlink.cfg",
        "-f", f"{OPENOCD_SCRIPTS}/target/stm32f1x.cfg",
        "-c", "init",
        "-c", "reset halt",
        "-c", "stm32f1x unlock 0",  # Desbloqueia e apaga a Flash
        "-c", "reset halt",
        "-c", "exit"
    ]

    try:
        result = subprocess.run(openocd_command, capture_output=True, text=True)
        if result.returncode != 0:
            print("Erro ao desativar a proteção!")
            print(result.stderr)
            raise Exception("Falha ao desativar a proteção ROP.")
        else:
            print("Proteção desativada com sucesso.")
            print("Reiniciando o dispositivo para aplicar mudanças...")
            reset_command = [
                OPENOCD,
                "-f", f"{OPENOCD_SCRIPTS}/interface/stlink.cfg",
                "-f", f"{OPENOCD_SCRIPTS}/target/stm32f1x.cfg",
                "-c", "init",
                "-c", "reset run",
                "-c", "exit"
            ]
            subprocess.run(reset_command, capture_output=True, text=True)
            print("Dispositivo reiniciado. Pronto para o upload.")
    except Exception as e:
        print(f"Erro ao executar o OpenOCD: {e}")
        raise e

# Adicionar o hook para desativar a proteção antes do upload
env.AddPreAction("upload", disable_protection)
