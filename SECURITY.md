# Política de Segurança -- PixelVault

## Versões Suportadas

| Versão | Suportada |
| ------ | --------- |
| 2.0.x  | sim       |
| 1.x    | não       |

## Reportando

1. **Não** abra uma issue pública
2. Envie email ao mantenedor
3. Inclua: descrição, passos para reproduzir, impacto

## Tempo de Resposta

- Recebimento: 48h
- Avaliação: 7 dias
- Correção: 30 dias

## Dados Sensíveis

PixelVault publica assets via GitHub + CDN. Nunca commite:

- Chaves de API do Looker Studio
- Service account keyfiles
- Tokens do GitHub (em ~/.netrc, .git-credentials ou variáveis de ambiente exportadas no repo)

## Escopo

- Código em `scripts/` e `main.py`
- Workflow de CI
- Scripts de instalação

## Fora do Escopo

- Vulnerabilidades em `requests`, `PyJWT`, `cryptography` (reporte upstream)
- Disponibilidade do jsDelivr CDN
