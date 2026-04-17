# Changelog

## [2.0.0] - 2026-04-16

### Mudado
- Projeto renomeado de `imagens_ux_ui` para `PixelVault` (sprint S18 do portfólio)
- Substituída última referência a "Glyph-Vault" em `scripts/gerenciador.py`

### Adicionado
- `pyproject.toml` com deps pinadas, ruff e pytest
- `tests/test_gerenciador.py` com 9 testes cobrindo sanitizar_nome, montar_nome_arquivo, extrair_metadados_nome
- `.github/workflows/ci.yml` (ruff + pytest)
- `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.mailmap`
- `CHANGELOG.md`

## [1.0.0] - 2025-03-23

### Adicionado
- Gerenciador CLI de assets visuais para Looker Studio
- Organização automática com padrão `{programa}_{tipo}[_{variante}].{ext}`
- Catálogo JSON rastreável
- URLs raw e jsDelivr CDN geradas automaticamente
- Menu interativo
- Instalação automatizada (install.sh/install.bat)
