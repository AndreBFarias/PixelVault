"""Testes para scripts.gerenciador."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.gerenciador import (
    extrair_metadados_nome,
    montar_nome_arquivo,
    sanitizar_nome,
)


def test_sanitizar_nome_converte_para_snake_case():
    assert sanitizar_nome("Minha Marca") == "minha_marca"


def test_sanitizar_nome_remove_acentos():
    assert sanitizar_nome("Educação Básica") == "educacao_basica"


def test_sanitizar_nome_remove_caracteres_especiais():
    assert sanitizar_nome("bolsa-escola!@#$") == "bolsa_escola"


def test_sanitizar_nome_colapsa_underscores():
    assert sanitizar_nome("a---b...c   d") == "a_b_c_d"


def test_montar_nome_arquivo_sem_variante():
    assert montar_nome_arquivo("FUNDEB", "logo", None, ".png") == "fundeb_logo.png"


def test_montar_nome_arquivo_com_variante():
    assert montar_nome_arquivo("PNLD", "icon", "colorido", "svg") == "pnld_icon_colorido.svg"


def test_extrair_metadados_nome_completo():
    resultado = extrair_metadados_nome("fundeb_logo_azul.png")
    assert resultado == {
        "programa": "fundeb",
        "tipo": "logo",
        "variante": "azul",
    }


def test_extrair_metadados_nome_sem_variante():
    resultado = extrair_metadados_nome("pnld_icon.svg")
    assert resultado == {
        "programa": "pnld",
        "tipo": "icon",
        "variante": None,
    }


def test_extrair_metadados_nome_invalido_retorna_none():
    assert extrair_metadados_nome("arquivo_aleatorio.png") is None
    assert extrair_metadados_nome("semseparador.png") is None
