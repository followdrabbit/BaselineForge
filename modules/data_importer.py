import re
import json
import pandas as pd
from pathlib import Path

def extract_json_blocks(markdown_text: str) -> list:
    """
    Localiza blocos de código JSON em um texto Markdown (```json ... ```),
    converte cada bloco para objetos Python (listas/dicionários),
    e retorna todos os objetos em uma única lista.
    
    Se existirem múltiplos blocos, os elementos de cada bloco serão concatenados.
    """
    # Expressão regular para capturar o conteúdo entre ```json e ```
    pattern = r"```json(.*?)```"
    matches = re.findall(pattern, markdown_text, flags=re.DOTALL | re.IGNORECASE)
    
    all_data = []
    for match in matches:
        candidate = match.strip()
        try:
            parsed_json = json.loads(candidate)
            if isinstance(parsed_json, list):
                all_data.extend(parsed_json)
            else:
                all_data.append(parsed_json)
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
    
    return all_data

def load_markdown_as_dataframe(md_file_path: str) -> pd.DataFrame:
    """
    Lê um arquivo Markdown, extrai os blocos JSON e retorna um DataFrame
    com as entradas encontradas.
    
    Parâmetros:
        md_file_path (str): Caminho para o arquivo Markdown.
    
    Retorno:
        pd.DataFrame: DataFrame com os dados extraídos. Se não houver dados,
                      retorna um DataFrame vazio.
    """
    file_path = Path(md_file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {md_file_path}")
    
    markdown_text = file_path.read_text(encoding="utf-8")
    data_list = extract_json_blocks(markdown_text)
    
    if not data_list:
        return pd.DataFrame()  # Retorna DataFrame vazio se nenhum dado for encontrado
    
    return pd.DataFrame(data_list)

if __name__ == "__main__":
    # Exemplo de uso: ajusta os caminhos conforme necessário
    control_refiner_file = "controlgen_unificado_ControlRefiner.md"
    risk_evaluator_file = "controlgen_unificado_RiskEvaluator.md"
    
    df_controls = load_markdown_as_dataframe(control_refiner_file)
    df_risks = load_markdown_as_dataframe(risk_evaluator_file)
    
    print("DataFrame - ControlRefiner:")
    print(df_controls.head())
    
    print("\nDataFrame - RiskEvaluator:")
    print(df_risks.head())
