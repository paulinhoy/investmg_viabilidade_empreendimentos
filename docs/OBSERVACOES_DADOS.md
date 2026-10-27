# Observações sobre os dados

Pontos encontrados na análise da extração de **2026-10-23 11:44** (`dados_brutos/manifesto.json`).
Estão registrados aqui para tratamento futuro: **nenhum deles foi corrigido no código ainda**.

## 1. Correção do empreendimento 100 não tem efeito (desativada)

`aplicar_correcao_empreendimento_100` fixa os cenários **1 a 4**, mas nos dados o empreendimento 100
só existe no **cenário 10** (receita com 30 anos e custo de 9,11 bi).

Efeito quando a correção está ligada:
- o cenário 10 do emp. 100 é calculado **sem** o custo e a receita da planilha de ferroviário de passageiros;
- são criadas linhas de receita para os cenários 1 a 4 sem custo correspondente, que o
  `preparar_fluxo_caixa` descarta silenciosamente (fluxo `NaN`).

Ou seja, hoje a correção não altera nada. Por isso está desligada em `tirm_peltmg.py`
(`APLICAR_CORRECAO_EMP_100 = False`). A decisão sobre aplicá-la ao cenário 10 ficou para depois.

## 2. Só existe o cenário 10 — ✅ resolvido (esperado)

`id_cenario = 10` é a **carteira recomendada do PELT-MG**, a única tratada neste trabalho.

As tabelas da infra (`tir_infra`, `receita_infra`) só tinham os cenários 1 a 4, e as colunas
`tirm_infra`, `diff` e `receita_seinfra` ficavam vazias. A comparação com a infra deixou de ser
necessária e foi **removida** das queries e do relatório.

## 3. Empreendimentos com receita mas sem custo (37)

Dos 201 empreendimentos com receita, **37 não têm custo** em `custo`. O fluxo deles fica `NaN`
e eles são excluídos do cálculo de VPL/TIRM (aparecem no relatório com `vpl` vazio quando estão
em `emps_esperados`).

## 4. Séries de receita fora do padrão

A maioria das séries tem 30 anos e começa entre 2022 e 2034. Fogem do padrão:

| Empreendimento | Anos | Nº de anos |
|---|---|---|
| 829 | 2018–2023 | 6 |
| 721 | 2028–2043 | 16 |
| 722 | 2031–2046 | 16 |
| 789 | 2022–2039 | 18 |
| 788 | 2022–2042 | 21 |

Também há séries que começam muito cedo: emp. **108 (1996)**, 842 (2007), 123 (2008),
104 e 1035 (2014).

Como o custo é abatido inteiro no primeiro ano (t=0), séries curtas ou muito antigas distorcem
VPL, TIRM e a contraprestação calculada. Na contraprestação, intervalos que passam do fim da
série não são calculados (ex.: `10-25` deixa de fora 721, 722, 788 e 789, com a coluna `observacao`).

## 5. Receitas negativas (3 linhas)

Existem 3 registros com `receita_ano < 0` na tabela `receita`, todos do **emp. 839**
(anos 2056 a 2058, entre -0,17 mi e -0,60 mi). **A investigar.**

## 6. Pontos sem problema (verificados)

- Cada empreendimento tem **um único modal**: não há mais de uma linha por (empreendimento, cenário, ano).
- Os anos de cada série são **contínuos** (sem buracos), então a posição no array usado pelo
  `npv`/`mirr` corresponde ao ano `t` correto.
- Nenhuma receita nula.

## 7. Resultado atual (sem correção do emp. 100)

- 226 linhas no relatório (`saida/resultados`), 164 com VPL calculada.
- **148 empreendimentos com VPL negativa** → candidatos à contraprestação.

## 8. Filtro geral da carteira (contraprestação e apresentação)

`contraprestacao.filtrar_carteira` mantém só **status 1 a 5** (Concepção, Estudo, Projeto,
Análise prévia, Em contratação; código vindo de `emp.status_empreendimento`) e **esfera estadual**.
Sobram **84 empreendimentos com VPL**, dos quais **83 com VPL negativa**, todos do setor **rodoviário**.

## 9. Receitas sem inflação: dois resultados

As receitas do banco estão em **moeda constante** (sem inflação). Por isso há dois resultados:
- **Moeda constante**: `fluxo`, `vpl`, `tirm_codemge` (como antes).
- **Com inflação**: `fluxo_corrigido = fluxo × (1 + INFLACAO_ANUAL)^t`, `vpl_corrigido`, `tirm_codemge_corrigido`.
  `INFLACAO_ANUAL = 3%` em `tirm_peltmg.py` (premissa, a confirmar). O ano 1 (t=0) não muda.

A contraprestação gera `contraprestacao_<a>-<b>` e `contraprestacao_<a>-<b>_inflacao`. Nos dois, o aporte é um valor
nominal constante descontado a 11,02%.

## 10. Custo distribuído ao longo da concessão (branch `custo-distribuido`)

`dados_brutos/custo_distribuido.csv` (separador `;`): custo anual (`valor = valor_capex + valor_opex`) de
**83 empreendimentos** (cenário 10), com `t` e `ano`. Usado com `USAR_CUSTO_DISTRIBUIDO = True` em `tirm_peltmg.py`;
os demais continuam com o custo inteiro no primeiro ano (coluna `custo_distribuido` no `fluxo_caixa`).

- O total por empreendimento bate com `custo_final` (diferença < R$ 0,01).
- O `t` do arquivo é contado a partir de ~2024 e é ignorado: o `t` do fluxo é recalculado (0 = primeiro ano do fluxo).
- **77 empreendimentos têm custo 1 ano depois do fim da receita** (ex.: emp. 36, receita 2034–2063, custo até 2064).
  Esse ano entra com receita 0 e a concessão passa a ter 31 anos.
- **3 empreendimentos têm custo antes da receita** (2 com 2 anos, 1 com 6 anos de antecedência). Nesses, o ano 1
  da concessão passa a ser o primeiro ano de custo.
- **CAPEX e OPEX parecem invertidos na tabela `capex_opex`**: no emp. 36 o arquivo tem CAPEX R$ 238,3 mi e OPEX R$ 43,9 mi;
  a `capex_opex` tem o contrário. A soma (custo total) é a mesma. O painel usa os valores do arquivo. **A confirmar.**
- A query que gerou o arquivo ainda não está em `extracao/queries.py`.
