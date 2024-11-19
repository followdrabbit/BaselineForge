import os
import shutil
import streamlit as st

def cleanup_generated_files(file_list: list, session_directory: str):
    """
    Remove os arquivos gerados durante a execução atual e o diretório da sessão, se aplicável.

    Args:
        file_list (list): Lista dos caminhos completos dos arquivos a serem removidos.
        session_directory (str): Caminho do diretório da sessão.
    """
    # Remover os arquivos rastreados
    for file_path in file_list:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            st.error(f"Erro ao remover o arquivo {file_path}: {e}")
    
    # Tentar remover o diretório da sessão
    try:
        if os.path.exists(session_directory) and not os.listdir(session_directory):
            os.rmdir(session_directory)
        elif os.path.exists(session_directory):
            # Caso ainda tenha arquivos, forçar a remoção com shutil.rmtree
            shutil.rmtree(session_directory)
    except Exception as e:
        st.error(f"Erro ao remover o diretório da sessão: {e}")
