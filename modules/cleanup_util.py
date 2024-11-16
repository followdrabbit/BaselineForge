import os
import shutil
import streamlit as st

def cleanup_generated_files(session_directory: str):
    """
    Remove todos os arquivos e diretórios gerados durante a execução de uma sessão específica.

    Args:
        session_directory (str): Caminho para o diretório onde os artefatos da sessão estão armazenados.
    """
    try:
        if os.path.exists(session_directory):
            st.write(f"Removendo todos os arquivos e diretórios da sessão: {session_directory}")
            # Remove o diretório e todo o seu conteúdo
            shutil.rmtree(session_directory)
            st.success("Arquivos e diretórios da sessão removidos com sucesso!")
        else:
            st.warning(f"O diretório da sessão {session_directory} não foi encontrado.")
    except Exception as e:
        st.error(f"Erro ao limpar os arquivos da sessão: {e}")
