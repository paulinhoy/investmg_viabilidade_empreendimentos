# Viabilidade dos empreendimentos do PELT-MG

VPL/TIRM da carteira recomendada do PELT-MG (cenário 10) e cálculo da **contraprestação do Estado**:
o valor anual, pago num intervalo de anos da concessão, que leva a VPL a zero.

## Estrutura

```
extracao/            roda no servidor com acesso ao banco (leve a pasta inteira)
  baixar_dados.py      baixa as tabelas e gera dados_brutos.zip
  queries.py           dicionário com as queries SQL
  config.exemplo.py    modelo de config.py (host, banco, caminho da planilha) — config.py não é versionado
tirm_peltmg.py       Fluxo 1: fluxo de caixa, VPL e TIRM -> saida/fluxo_caixa, saida/resultados
contraprestacao.py   Fluxo 2: contraprestação por intervalo de anos -> saida/contraprestacao_<a>-<b>[_inflacao]
gerar_apresentacao.py  gera apresentacao/painel_contraprestacao.html a partir do template
apresentacao/        painel_template.html (o HTML gerado, com dados, não é versionado)
docs/                OBSERVACOES_DADOS.md: problemas e premissas encontrados nos dados
pesquisa/            pesquisa sobre estudos de viabilidade de concessões rodoviárias
```

Pastas locais, fora do Git: `dados_brutos/` (extração), `saida/` (resultados), `apresentacao_ref/`.

## Como rodar

1. No servidor: copie `extracao/`, crie `config.py` a partir de `config.exemplo.py` e rode
   `python baixar_dados.py`. Traga o `dados_brutos.zip` e extraia em `dados_brutos/` na raiz do projeto.
2. Na raiz do projeto, com o `.venv`:
   ```
   .venv\Scripts\python tirm_peltmg.py
   .venv\Scripts\python contraprestacao.py 1-5
   .venv\Scripts\python gerar_apresentacao.py
   ```

## Premissas principais

- Taxa de desconto e de financiamento 11,02% a.a.; reinvestimento 15% a.a. (TIRM).
- Ano 1 da concessão = primeiro ano do fluxo (t = 0); custo (CAPEX + OPEX) abatido inteiro no ano 1.
- Aporte do Estado constante em valor nominal nos anos escolhidos.
- Dois resultados: receitas em moeda constante (como vêm do banco) e corrigidas por `INFLACAO_ANUAL` (3% a.a.).
- Contraprestação e painel: só esfera estadual e status 1 a 5 (Concepção a Em contratação).
