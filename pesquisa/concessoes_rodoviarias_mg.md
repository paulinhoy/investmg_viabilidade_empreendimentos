# Concessões rodoviárias estaduais de Minas Gerais: como o estudo de viabilidade modela a receita

Data da pesquisa: 23/10/2026. Pesquisa em fontes abertas (notícias oficiais, relatórios de rating, prospecto de debêntures, demonstrações financeiras, dissertações). Os estudos originais (EVTEA, cadernos de tráfego e modelo econômico-financeiro) ficam em data room do BDMG e em páginas da Seinfra que estavam bloqueadas (HTTP 403) ou fora do ar; portanto **nenhum caderno de estudo foi lido diretamente**. Tudo o que segue sobre modelagem vem de fontes secundárias.

Convenção: **[D]** = dado documentado na fonte citada; **[I]** = inferência minha; "não encontrado" = não localizado.

---

## 1) Resumo executivo

1. O programa mineiro (a partir de 2021) estrutura lotes de ~30 anos com apoio do BNDES (Fábrica de Projetos; consórcio Future ATP, LOGIT, JGP e Queiroz Maluf, contratado em maio/2020) e do BDMG/BID (Ouro Preto). [D] [S1][S2]
2. Leiloados até hoje: Triângulo (ago/2022), Sul de Minas (ago/2022), Varginha-Furnas (mai/2023) e Ouro Preto-Mariana "Via Liberdade" (set/2025). Os três primeiros foram vencidos por Equipav+Perfin (hoje EPR), sem concorrência no Triângulo e em Varginha-Furnas. [D]
3. Os lotes nomeados na demanda "Rota Sul de Minas", "Mucuri/Jequitinhonha" e "Sete Lagoas" **não foram encontrados** como lotes estaduais. Existem Vetor Norte (suspenso pelo TCE-MG), Zona da Mata (em estruturação), Noroeste (edital revogado em 13/02/2026) e Quadrilátero Ferrífero (em espera). [D]
4. Receita: nos lotes de concessão comum, a receita é **tarifa × tráfego em eixos equivalentes**, com tarifa básica (categoria 1) reajustada anualmente por IPCA (fórmula TP = TBP × IRT, IRT = IPCA_t / IPCA_0, base out/2021 no Triângulo). Tráfego e demanda são **risco do concessionário**, sem banda de compartilhamento no contrato do Triângulo, segundo o prospecto. [D]
5. Nos lotes PPP (Sul de Minas, Via Liberdade), a receita soma pedágio e contraprestação do Estado. A disputa é por **menor contraprestação** (deságio sobre um teto). A contraprestação do Sul de Minas é reembolso de investimentos concluídos, corrigido por IPCA (R$ 371,1 mi contratados); a da Via Liberdade foi de R$ 1,702 bi (teto R$ 1,961 bi), com R$ 2 bi do Novo Acordo de Mariana. [D]
6. O caso MG-050 (2007) é o único com **banda de tráfego documentada**: faixa de ±10% sem reequilíbrio; acima disso, repartição 50%/50%. Contraprestação adicional à tarifa (CAT) com teto de R$ 2.916.666,67/mês, ligada a indicadores de desempenho (QID). [D]
7. Moeda: o estudo trabalha em **reais constantes de uma data-base** e a tarifa é indexada ao IPCA desde essa data. Isso é compatível com fluxo real descontado a taxa real. Esta é uma inferência minha sobre o modelo, apoiada na cláusula de reajuste (a data-base) e em nota do prospecto que diz "valores nominais EVTEA". [D]+[I]
8. Taxa de retorno do estudo: só apareceu "retorno estimado de 11,2%" para a Via Liberdade (Agência iNFRA), sem dizer se é real ou nominal. Para os demais lotes, TIR/WACC regulatória: **não encontrado**. [D]
9. O tráfego real do Sul de Minas ficou abaixo do esperado em 2025 (+7,2% em nove meses contra ~10% projetado pela S&P, que é projeção da agência, não do EVTEA). O Triângulo tem comparação "realizado versus EVTEA" no prospecto, mas só em gráfico sem números extraíveis. [D]
10. Lição central para o PELT-MG: o modelo de mercado separa investimento por ciclos (serviços iniciais, recuperação, ampliação, manutenção), em vez de abater tudo no ano 1, e usa tráfego em eixos equivalentes com rampa de maturação. Ver seção 6.

---

## 2) Tabela das concessões

| Lote | Leilão | Rodovias / km | Prazo | Vencedor | Critério e resultado | Tarifa (TBP) | Praças | CAPEX / OPEX | Aporte público | Estruturador |
|---|---|---|---|---|---|---|---|---|---|---|
| MG-050 "Nascentes das Gerais" (PPP, caso antigo) | edital 2006; contrato jul/2007 [S20] | MG-050 e trechos BR-265/BR-491, 372 km [S20][S21] | 25 anos [S20] | não encontrado na pesquisa | menor contraprestação (CAT) [S21] | ~R$ 3,00 por automóvel/eixo (estimada no edital) [S20] | 6 [S20] | investimento total ~R$ 645 mi, ~R$ 320 mi nos 5 primeiros anos [S21] | CAT máxima R$ 2.916.666,67/mês (~R$ 35 mi/ano); garantidor CODEMIG [S20][S21] | DER/MG; estudo TECTRAN 2005 [S21] |
| Lote 1 Triângulo Mineiro | 08/08/2022; contrato nov/2022 [S3][S4] | BR-452, BR-365, CMG-452, CMG-462, LMG-782, LMG-798, LMG-812, MG-190, MG-427; 627,4 km [S3] | 30 anos | Consórcio Infraestrutura MG (Equipav+Perfin), único proponente [S3] | desconto na tarifa (0,1%): R$ 11,48115 contra teto R$ 11,49397 [S3]. Versões divergem sobre outorga (ver nota A) | R$ 11,48115 (base do leilão) [S3] | 8 [S11] | CAPEX R$ 3,17 bi (R$ 1,4 bi nos 8 primeiros anos); OPEX R$ 2,8 bi [S3]. EPR cita CAPEX previsto R$ 3,1 bi [S11] | sem contraprestação [S3] | BNDES [S1] |
| Lote 2 Sul de Minas (PPP) | 17/08/2022 [S5] | BR-459, MG-290, MG-173, MG-295, MG-459, MG-455, LMG-877, CMG-146; 454,3 km [S5] | 30 anos | Infraestrutura MG (concorreu também Monte Rodovias) [S5] | desconto sobre a contraprestação: 14,9% (Agência Brasil) ou 13,87% (F&A); ver nota B | teto R$ 8,32 [S5]; R$ 8,30 após revisão de 2025 [S9] | 8 (7 com cobrança tradicional e 1 free flow, <5% da arrecadação) [S12] | CAPEX R$ 3,1 bi + manutenção R$ 1,4 bi = R$ 4,5 bi (S&P) [S12] | contraprestação ~R$ 377 mi (leilão) [S5]; R$ 371,1 mi no balanço de 2023 [S13] | BNDES [S1] |
| Lote 3 Varginha-Furnas | 25/05/2023 [S6] | MG-167, BR-265, LMG-863, MGC-491, BR-146, MGC-369; 432,8 km [S6] | 30 anos | Infraestrutura MG, único proponente [S6] | menor tarifa: R$ 13,17966 contra teto R$ 13,20343 (-0,18%) e piso R$ 10,56274 [S6] | R$ 13,17966 | 6 [S6][S14] | R$ 2,6 bi em 30 anos, R$ 1,3 bi nos 8 primeiros [S6] | não encontrado (concessão comum) | BNDES [S1] |
| Lote 7 Ouro Preto-Mariana "Via Liberdade" (PPP) | 18/09/2025 [S7] | BR-356, MG-262, MG-329; 190,1 km [S7] | 30 anos | Consórcio Rota da Liberdade (Metropolitana e outras 5) [S15] | menor contraprestação: R$ 1.702.476.148,74, deságio 13,2% sobre teto de R$ 1,961 bi; concorrente Houer: 0,02% [S7][S15] | TBP R$ 5,58 (pista simples) e R$ 7,81 (pista dupla) segundo a imprensa [S16] | não encontrado (há menção a free flow [S15]) | CAPEX R$ 3,69 bi; OPEX ~R$ 1,5 bi; receita acumulada até R$ 7,5 bi; tráfego médio 13,63 mi veículos/ano [S16] | contraprestação do Estado; R$ 2 bi vindos do Novo Acordo de Mariana [S7][S15] | BDMG com apoio do BID [S1] |
| Lote 8 Vetor Norte | edital suspenso desde abr/2025 [S17] | MG-010, MG-424, LMG-800; 123,4 km, 12 pórticos [S17] | não encontrado | sem leilão | TCE-MG mandou interromper por suspeita sobre cálculo da tarifa e consulta aos municípios [S17] | não encontrado | 12 pórticos | não encontrado | não encontrado | não encontrado |
| Lote Noroeste | edital 21/01/2026; leilão marcado para 20/03/2026; **edital revogado em 13/02/2026** [S17][S18] | BR-365, CMG-496, MG-408, MG-181; 767 km [S18] | 30 anos | sem leilão | revogado porque o Ministério dos Transportes negou a delegação dos trechos federais da BR-365 [S18] | não encontrado | não encontrado | R$ 7,5 bi em 30 anos [S18] | concessão "pura", sem aporte ou contraprestação [S19] | BNDES, com padronização das concessões federais [S18] |
| Lote 9 Zona da Mata | previsto 2º semestre de 2026 [S17] | 1.176 km, 47 municípios [S19] | 30 anos | sem leilão | não encontrado | não encontrado | free flow como lógica geral dos projetos [S19] | R$ 8,6 bi (R$ 5,4 bi CAPEX e R$ 3,2 bi OPEX), preliminar [S19] | não encontrado | não encontrado |
| Quadrilátero Ferrífero | em espera [S17] | 506 km, 15 rodovias [S17] | não encontrado | sem leilão | secretário não tem certeza de que concessão seja o caminho [S17] | | | | | |

Notas:
- **Nota A (outorga do Triângulo).** Diário do Comércio e Exame reportam outorga de R$ 446,68 mi ao Fundo Estadual de Desenvolvimento de Transportes e critério híbrido (desconto de até 15% na tarifa, depois maior outorga). Já a Seinfra, em trecho citado numa busca, diz que o julgamento combinava menor tarifa e maior outorga e que "não houve proposta de valor de outorga". Não consegui conciliar. [D, divergente] [S3][S22]
- **Nota B (desconto do Sul de Minas).** 14,9% (Agência Brasil) contra 13,87% (Fusões & Aquisições, proposta de R$ 378 mi). Divergência não resolvida. [S5][S23]
- Os nomes "Rota Sul de Minas", "Mucuri/Jequitinhonha" e "Sete Lagoas" sugeridos na demanda **não apareceram** nas fontes. "Sul de Minas" é o Lote 2; "Rota das Gerais" é uma concessão federal (EcoRodovias, 31/03/2026, 19% de desconto), fora do escopo.
- O prospecto da EPR afirma que o Estado tem 6 concessões sob supervisão da Seinfra: Eco135, Via Nascentes, Rodoanel BH, EPR Triângulo, EPR Sul de Minas e EPR Vias do Café. [D] [S11] A concessionária da MG-050 é "Nascentes das Gerais" segundo a Agência Minas (resultado de busca); não verifiquei se "Via Nascentes" do prospecto é o mesmo ativo.
- Fitch descreve o Triângulo como "nove rodovias" e a S&P descreve o Sul de Minas com oito trechos; não há inconsistência com a tabela.

---

## 3) Como a receita é modelada (seção principal)

### 3.1 O que foi possível documentar sobre o método de demanda

**Documentado**
- Os estudos do programa (BNDES/consórcio Future ATP, LOGIT, JGP, Queiroz Maluf) cobrem "demanda de tráfego em horizonte de 30 anos, avaliação econômico-financeira, impactos socioambientais e minutas de edital e contrato". [D] [S2] (descrição de imprensa; o conteúdo metodológico dos cadernos **não foi lido**.)
- A EPR descreve a demanda do Triângulo com os mesmos elementos que se esperam de um estudo de tráfego: tráfego medido em **veículos equivalentes**, fluxo dominante (Uberlândia-Patrocínio responde por 41% dos veículos equivalentes), análise de **rotas alternativas** (Eco050 e Concebra são vistas como integradoras, não concorrentes), análise de **modais concorrentes** (ferrovia com impacto estimado em no máximo 1% do tráfego de pesados, por engenheiros independentes) e **sazonalidade** mensal por classe (leves e pesados, com fatores como 1,12 para leves em janeiro e 0,83 para pesados em janeiro). Tarifa por km comparada: Triângulo R$ 0,16, Concebra R$ 0,07, Eco050 R$ 0,06. [D] [S11]
- No prospecto há um gráfico de "Tráfego Realizado vs Edital (Veículo Diário Médio)" e um gráfico "OPEX EVTEA x realizado" (de 44 contra 40 e 25 contra 19, em R$ mi, ordens de grandeza lidas em gráfico). O texto diz que a demanda está "já em linha com estudos em termos de diversificação e volumes". Não consegui extrair valores do gráfico de tráfego com segurança. [D, parcial] [S11]
- A fonte da modelagem de demanda mais completa que consegui para um lote mineiro é o relatório da Fitch (Triângulo): linha de base em **eixos equivalentes** (25,4 mi no ano 2 da concessão, 26,1 mi no ano 3, 26,8 mi no ano 4, depois **CAGR de 2,6%**; cenário de rating: 25,4, 25,9, 26,5 e CAGR 2,1%). [D] [S10] **Atenção: são projeções da Fitch, não do EVTEA.** Fitch descreve elasticidade-preço "moderada" e 73% de tráfego pesado.
- A S&P projeta o Sul de Minas ligando o crescimento do tráfego ao PIB com **múltiplo de 1,0x a 1,5x** durante a concessão (PIB de 1,7% em 2026, 2,1% em 2027 e 2,2% de 2028 em diante). Também é método da agência, não do EVTEA. [D] [S12]
- MG-050 (2006): estudo de viabilidade com contagens, pesquisa origem-destino (TECTRAN, 2005), pesquisa de opinião sobre pedágio (56% favoráveis desde que a rodovia estivesse em boas condições), **cálculo de rotas de fuga**, tarifa definida com base na **elasticidade-preço da demanda** e projeção de tráfego para 25 anos publicada no Anexo XV do edital e vinculante para as propostas. O gráfico da projeção (milhares de veículos/ano, soma de automóveis e caminhões, convertida em eixos por praça) exibe os rótulos 17.181, 19.295, 21.737, 24.362, 27.201 e 30.248; não consegui associar cada rótulo ao ano exato, mas a série vai de ~17 mi no início a ~30 mi no ano 25. [D] [S20][S21]

**Não encontrado:** a metodologia dos cadernos de tráfego dos lotes 1, 2, 3 e 7 (modelo de 4 etapas ou não, tipo de pesquisa OD, calibração, elasticidade-preço adotada, taxa de crescimento por classe, rampa de maturação, fuga de praças). Isso exige baixar os cadernos do data room do BDMG.

### 3.2 Conversão de tráfego em receita

| Elemento | O que está documentado |
|---|---|
| Unidade de tráfego | **Eixos equivalentes** ("quantidade de eixos pagantes de cada veículo"), usada pela EPR Vias do Café e pela Fitch no Triângulo. [D] [S10][S14] |
| Tarifa básica (TBP) | Valor para a Categoria 1 (automóvel, caminhonete, furgão, com ou sem semirreboque/reboque). Demais categorias seguem multiplicadores por eixos, **cuja tabela não encontrei**. [D] [S11] |
| Tarifa média | A EPR Vias do Café reporta tarifa média líquida de R$ 13,29 em 2025, para tarifa básica entre R$ 14,30 e R$ 15,00 no período. A diferença reflete mix de categorias, descontos e arredondamentos; a decomposição não é divulgada. [D] [S14] |
| Fórmula de receita (reporte) | Receita de pedágio = eixos equivalentes × tarifa média. Ex.: Vias do Café 2025, 19,4 mi de eixos equivalentes (9,9 mi leves e 9,5 mi pesados) e receita de serviços prestados de R$ 257,9 mi. [D] [S14]. A razão 257,9/19,4 = R$ 13,3 por eixo equivalente é cálculo meu e bate com a tarifa média informada. [I] |
| Tarifa por km | Não é a base do cálculo (a cobrança é por praça); a EPR usa a tarifa quilométrica só para comparar com rotas vizinhas. [D] [S11] |
| Free flow | Sul de Minas tem uma praça free flow (P8), <5% da arrecadação total. [D] [S12] Vetor Norte previa 12 pórticos. [D] [S17] Agência iNFRA diz que os projetos de rodovia seguem a lógica de free flow, "sem praças tradicionais" (Zona da Mata, em projeto). [D] [S19] |
| Desconto de Usuário Frequente (DUF) | Até 80% de desconto para veículos de passeio com TAG, a partir da 2ª passagem pela mesma praça, no mesmo sentido e mês, em pista automática (Triângulo). [D] [S24] A Revisão Anual **compensa** o DUF: em 2025, R$ 3,67 mi (Vias do Café, 2º sem./2024), R$ 56 mil (Triângulo, out-dez/2023) e R$ 203 mil (Sul de Minas), corrigidos por IPCA. [D] [S9] |
| Inadimplência e evasão | Sul de Minas não tinha contas de pedágio em atraso em 31/12/2023 e não constituiu provisão. [D] [S13] Parâmetro de evasão/inadimplência no EVTEA: **não encontrado**. |
| Ramp-up | A Vias do Café saiu de 8,5 mi de eixos (cobrança a partir de 26/07/2024, ano parcial) para 19,4 mi em 2025. [D] [S14] Rampa do EVTEA: não encontrada. Início da cobrança nos lotes depende de marcos de obra (Triângulo: 28/10/2023; Via Liberdade: pedágio só após as intervenções do 1º ano). [D] [S11][S7] |
| Receitas acessórias | Contrato prevê contratos de receita acessória, e a Revisão Anual considera "as Receitas Acessórias, com base nos valores faturados, para apuração do valor a ser revertido para a modicidade tarifária". [D] [S11] O TCE-MG investiga por que a 3ª Revisão do Sul de Minas concluiu que **não existem** receitas acessórias. [D] [S25] Percentual de partilha: **não encontrado**. |

### 3.3 Reajuste e relação com a moeda do modelo

- Cláusula 34 do contrato do Triângulo: **TP = TBP × IRT**, com IRT = IPCA_t / IPCA_0, onde IPCA_0 é o de **outubro de 2021** e IPCA_t o do segundo mês anterior à data de reajuste. A Concessionária pode praticar a nova TP a partir do 5º dia da data-base se o regulador não manifestar objeção. [D] [S11]
- O mesmo IRT atualiza a "verba de segurança no trânsito", verba de desapropriação, ônus de fiscalização e garantia de execução. [D] [S11]
- Cláusula 31, Revisão Anual: ocorre por ocasião do reajuste e inclui diferença de receita entre datas, receitas acessórias, verba de segurança e compensação do DUF. [D] [S11]
- Evidência empírica da indexação (Triângulo): tarifa básica de passeio R$ 13,30 → R$ 14,00 (a partir de 22/10/2025) → R$ 14,50 (22/10/2026, +3,57%). [D] [S24][S26] A TBP do leilão foi R$ 11,48. [D] [S3] Ou seja, a tarifa praticada é a TBP corrigida por IPCA acumulado desde a data-base. [I]
- Para o Sul de Minas, TBP de R$ 8,30 (revisão de 2025) e tarifa praticada de R$ 10,10 → R$ 10,60 (+4,95%) em 09/10/2026. [D] [S9][S25]
- Para Varginha-Furnas: R$ 14,30 → R$ 15,00 em 26/07/2025, após "redução técnica" de R$ 0,04 na TBP. [D] [S9] A data-base de Varginha-Furnas é diferente da do Triângulo (a razão 15,00/13,18 é bem menor que a do Triângulo); data exata: **não encontrada**. [I]
- Debêntures e custos também são IPCA: a S&P diz que O&M, salários, serviços e materiais são ajustados anualmente por inflação e que as debêntures são indexadas ao IPCA. [D] [S12]

**Leitura sobre moeda [I]:** o estudo de viabilidade foi montado em **valores constantes da data-base** (out/2021 no Triângulo) com tarifa e custos indexados ao mesmo índice. Isso é o que se espera se o fluxo é em moeda real descontado a taxa real. O prospecto indica que os valores de OPEX do EVTEA usados na comparação com o realizado são "nominais, considerando a mensalização dos anos de concessão" (isto é, conversão para valores correntes para comparar com o realizado). [D] [S11] Não vi o EVTEA para confirmar que o fluxo de caixa regulatório é real.

### 3.4 Mecanismos de risco de demanda

| Caso | Mecanismo documentado |
|---|---|
| MG-050 (2007) | Projeção do DER/MG (Anexo XV/XVI) é a referência. Riscos de procura compartilhados **50%/50%**. Faixa de ±10% sobre o volume projetado: variação a menor fica com a concessionária e a maior reverte integralmente à concessionária (sem reequilíbrio). Acima de +10%: partilha de benefícios 50/50. Abaixo de -10%: reequilíbrio considerando a repartição 50/50. Verificação anual com dados acumulados desde o início da cobrança. [D] [S21] |
| Triângulo (2022) | Prospecto: "a variação de demanda ou volume de tráfego da malha em desacordo com as projeções elaboradas para o projeto ... são riscos de responsabilidade da Companhia" (risco de demanda 100% privado, sem banda). Reequilíbrio só para riscos alocados ao Poder Concedente (alteração de tarifas, de investimentos, de prazo, ou combinações). [D] [S11] |
| Sul de Minas (PPP, 2022) | S&P observa que o projeto "possui a possibilidade de requerer um reequilíbrio", já que o principal impacto vem da **contagem de tráfego inicial** (ou seja, uma linha de base de tráfego que pode ser contestada). Não vi cláusula. [D] [S12] |
| Todos | Revisões anuais, quinquenais e extraordinárias; aportes de recursos vinculados mensais; DUF. [D] [S11] Marcos de desempenho condicionam o reajuste (Fitch). [D] [S10] Desconto de reequilíbrio / Fator D: **não encontrado** nos lotes mineiros (nem confirmado como inexistente). |

---

## 4) Taxa de desconto, moeda (real × nominal) e indicadores

| Item | Dado | Fonte |
|---|---|---|
| Retorno estimado Via Liberdade | 11,2% (a imprensa não diz se é real ou nominal; nem se é TIR do projeto ou do acionista) | [S27] |
| TIR/WACC regulatória dos lotes 1, 2 e 3 | **não encontrado** | |
| "Equity regulatório" do Triângulo | R$ 81 mi (R$ 250 mi aportados até o prospecto) | [S11] |
| Custo da dívida das concessionárias | Triângulo: 2ª emissão R$ 1,3 bi, IPCA + 7,32%, venc. 2041, rating A+(bra) Fitch. Sul de Minas: 2ª emissão R$ 500 mi, IPCA + 8,1584%, venc. out/2044, brAA- (S&P). Vias do Café: 2ª emissão R$ 800 mi, IPCA + 8,47%, venc. mar/2041 | [S10][S12][S28] |
| Índices de cobertura | Triângulo: DSCR médio 1,2x (cenário de rating) e abaixo de 1,0x em 2027-2030 por causa do CAPEX. Sul de Minas: ICSD mínimo 1,42x em 2040, mediano 1,54x | [S10][S12] |
| Taxa de desconto de referência de mercado | Debêntures **reais** (IPCA + cupom), o que mostra que o custo de capital de mercado desses ativos é referido em termos reais | [S10][S12] |

**Real versus nominal [I]:** com tarifa indexada ao IPCA desde a data-base, o equilíbrio econômico-financeiro do contrato é naturalmente expresso em reais constantes dessa data-base e descontado a taxa real. A taxa de 11,02% do PELT-MG precisa ser conferida: se for real, está acima do cupom real das dívidas (7,3% a 8,5%), mas um WACC de equity-heavy exigido pelo acionista pode chegar a esse patamar; se for nominal, a comparação com taxa real exige deflacionar. Não afirmo qual é o caso do PELT-MG.

---

## 5) Aporte público e contraprestação nos lotes mineiros

| Lote | Aporte / contraprestação | Observação |
|---|---|---|
| MG-050 | CAT teto R$ 2.916.666,67/mês; paga conforme nota do QID (operacional 60-70%, ambiental, financeira e social 10-20%); garantidor CODEMIG, com recursos da participação em lucros da CBMM | [S20][S21]. As duas fontes divergem nos pesos do QID (60/20/10/10 contra 70/10/10/10) |
| Triângulo | Sem contraprestação | [S3] |
| Sul de Minas | Contraprestação ~R$ 377 mi no leilão, corrigida por IPCA; a EPR reconhece R$ 371,1 mi como direito a receber da Seinfra "como reembolso para determinados investimentos". Em 2023, recebeu R$ 37,2 mi e reconheceu R$ 180,9 mi. Contas a receber de R$ 180,9 mi em 31/12/2023 | [S5][S13]. Imprensa afirma que a outorga do Triângulo financiaria a contraprestação do Sul de Minas [S23] |
| Varginha-Furnas | Sem aporte nas fontes | |
| Via Liberdade | Contraprestação vencedora R$ 1,702 bi (teto R$ 1,961 bi). R$ 2 bi do Novo Acordo de Mariana citados como aporte. Regra: deságio acima de R$ 600 mi exige depósito de garantia. Retorno estimado de 11,2%. Valor do contrato no portal PPP-MG: R$ 2,88 bi, assinatura em 13/01/2026 (divergência com R$ 1,7 bi: não conciliada) | [S7][S15][S27] |
| Noroeste | Modelo "puro", sem aporte ou contraprestação | [S19] |

**Leitura [I]:** nos lotes mineiros recentes, a contraprestação é **desembolsada em função de investimentos concluídos** (Sul de Minas: primeiros dois anos, reembolso) e não como anuidade constante ao longo de 30 anos, como o modelo do PELT-MG supõe. Na MG-050 era mensal e condicionada ao desempenho. Isso deve ser conferido nas minutas (não lidas).

---

## 6) Lições para o modelo do PELT-MG [inferências minhas, salvo indicação]

1. **CAPEX no ano 1.** Os lotes mineiros dividem o investimento em ciclos: Triângulo, serviços iniciais (R$ 275 mi, ano 1), recuperações (R$ 332 mi, a partir do ano 2), ampliação até o 8º ano (R$ 454 mi), outras intervenções (R$ 643 mi) e manutenção (R$ 1.380 mi até o ano 30) [D, S11]. Fitch projeta CAPEX anual nos anos 2, 3 e 4-9 [S10]. Abater CAPEX+OPEX inteiros no ano 1 **superestima o custo em valor presente** e distorce VPL e TIRM. Sugestão: distribuir CAPEX por cronograma de obras e OPEX por ano.
2. **Receita não é constante.** Há rampa de maturação (Vias do Café: 8,5 mi para 19,4 mi de eixos entre 2024 e 2025) e crescimento do tráfego ligado ao PIB (S&P: múltiplo 1,0-1,5x; Fitch: CAGR de 2,1%-2,6%). Modelar receita = tráfego_t × tarifa média_t, com tráfego crescendo por elasticidade ao PIB.
3. **Receita real.** Se o fluxo é em moeda constante, a tarifa deve ser constante em termos reais (porque o contrato a reajusta por IPCA), e a taxa de desconto deve ser real. Ponto de atenção: a taxa 11,02% e o aporte constante têm que estar na mesma base monetária.
4. **Tarifa média < tarifa básica.** A tarifa média líquida da Vias do Café foi cerca de 11% abaixo da tarifa básica (R$ 13,29 contra R$ 14,30-15,00) [D+I]. Convém aplicar um fator de mix/desconto (DUF, categorias, isenções) sobre a TBP.
5. **Contraprestação** em lotes recentes do Estado não é anuidade constante; no Sul de Minas é reembolso por marcos de obra, no MG-050 era mensal condicionada ao desempenho. O objetivo do PELT-MG (aporte que zera o VPL) deve decidir se a contraprestação é equalizada em anuidade ou ligada a marcos.
6. **Risco de demanda.** Em Minas, o risco é do concessionário (Triângulo) ou com banda ±10% e partilha 50/50 (MG-050). Se o PELT-MG quer testar robustez, vale rodar cenários de tráfego de -10%/+10%.
7. **Receitas acessórias** e DUF reduzem/ajustam a tarifa; no mínimo incluir um parâmetro de receita acessória (percentual da receita) como sensibilidade.
8. **Tributos e outorga:** o ISSQN é pago aos municípios (R$ 19 mi no Sul de Minas, 2026) [D, S25]; PIS/COFINS aparecem como imposto sobre receita nas demonstrações [D, S14]. Confirmar o tratamento no PELT-MG.

---

## 7) Lacunas e documentos a baixar

- **Data room BDMG** (estudos de viabilidade dos lotes 1 a 6): cadernos de estudo de tráfego, modelo econômico-financeiro, EVTEA, caderno de engenharia, PER. Páginas relevantes (HTTP 403 na pesquisa): [S29][S30][S31].
- **Contrato de concessão, Anexos** (cláusulas 30 a 35: risco, revisões, reajuste, DUF, receitas acessórias) dos lotes 1, 2, 3 e 7. Portal PPP-MG (certificado inválido): [S32].
- **Edital do Lote 7** (critério, teto de contraprestação, mecanismo de pagamento, free flow) e consulta pública (27/11 a 26/12/2024). [S7][S33]
- **Edital do Lote Noroeste** (publicado 21/01/2026, ainda disponível mesmo revogado) e do **Vetor Norte** (tarifa questionada pelo TCE-MG, relatório pode trazer a metodologia da tarifa).
- **Processos do TCE-MG** sobre Vetor Norte e sobre a 3ª Revisão do Sul de Minas (fluxo de caixa, receitas acessórias). [S17][S25]
- **Formulário de Referência da EPR** (seções de fatores de risco e de contrato) e prospectos de debêntures de Sul de Minas e Vias do Café: trazem premissas de tráfego e relatório do engenheiro independente. O prospecto do Triângulo (agosto/2024) foi lido. [S11]
- Relatórios de rating completos da Fitch/S&P para Vias do Café (não localizados).
- Confirmar: critério/outorga do Triângulo (Nota A); desconto do Sul de Minas (Nota B); data-base do Varginha-Furnas; contraprestação teto do Sul de Minas.
- MG-050: contrato SETOP 007/2007 e Anexos XV e XVI (projeções de tráfego). Vencedor do leilão de 2006: não encontrado na pesquisa.

---

## 8) Fontes

Estruturação e programa
- [S1] BNDES/Agência Minas, estruturação (via Okai): https://okai.com.br/noticia/2022-08-17/com-projetos-do-bndes-governo-de-minas-gerais-conclui-leilao-de-4543-km-de-rodovias (acesso via resumo de busca)
- [S2] Descrição do consórcio contratado em maio/2020 (resultado de busca citando Agência Minas): https://www.agenciaminas.mg.gov.br/noticia/governo-publica-edital-do-terceiro-lote-do-programa-de-concessoes-rodoviarias

Leilões
- [S3] Diário do Comércio, Triângulo: https://diariodocomercio.com.br/economia/consorcio-vence-leilao-de-lote-rodoviario-no-triangulo/ ; Exame: https://exame.com/brasil/sem-concorrentes-consorcio-infraestrutura-mg-vence-leilao-de-rodovias-no-triangulo-mineiro/ ; Agência Brasil: https://agenciabrasil.ebc.com.br/economia/noticia/2022-08/consorcio-infraestrutura-mg-vence-leilao-de-lote-rodoviario-em-minas
- [S4] Agência Minas, assinatura dos contratos: https://www.agenciaminas.mg.gov.br/noticia/governo-de-minas-assina-concessao-de-rodovias-do-triangulo-mineiro-e-sul-do-estado-115093
- [S5] Agência Brasil, Sul de Minas: https://agenciabrasil.ebc.com.br/economia/noticia/2022-08/consorcio-infraestrutura-mg-arremata-rodovias-do-lote-sul-de-minas
- [S6] Diário do Comércio, Varginha-Furnas: https://diariodocomercio.com.br/economia/governo-leiloa-3o-lote-de-rodovias-e-grupo-vence-mais-uma-vez/
- [S7] Agência Minas, Via Liberdade: https://www.agenciaminas.mg.gov.br/noticia/consorcio-rota-da-liberdade-vence-leilao-do-lote-rodoviario-ouro-preto-mariana-127622 ; B3: https://www.b3.com.br/pt_br/noticias/governo-do-estado-de-minas-gerais-realiza-leilao-na-b3-para-concessao-rodoviaria-do-lote-ouro-preto-mariana-via-liberdade.htm
- [S9] O Fator, 1ª Revisão Anual (jul/2025): https://ofator.com.br/informacao/os-novos-valores-de-pedagio-tres-rodovias-estaduais-minas/

Modelagem, rating e financeiro
- [S10] Fitch, 2ª emissão EPR Triângulo (29/08/2024): https://eprtriangulo.com.br/wp-content/uploads/2024/08/Fitch-Assigns-Rating-Abra-to-the-2nd-Issuance-of-Debentures-of-EPR-Triangulo.pdf
- [S11] Prospecto preliminar, 2ª emissão Rodovias do Triângulo (Santander, 19/08/2024), slides do projeto, cláusulas 31 e 34 do contrato: https://cms.santander.com.br/sites/WPS/documentos/arq-EPR-prospectoII/24-08-20_011847_deb.+tri%C3%A2ngulo+i+prospecto+preliminar+atualizado+(19.08.2024).pdf
- [S12] S&P, análise atualizada Rodovias do Sul de Minas (29/01/2026): https://filemanager-cdn.mziq.com/published/d2b808ee-0df5-429f-813a-07119e8a4cdf/77946d9e-2364-4175-90ca-a20b44ac52a8_eprsuldeminas_2026jan.pdf
- [S13] Demonstrações financeiras 2023, Sul de Minas: https://eprsuldeminas.com.br/wp-content/uploads/2024/04/DFs-Sul-de-Minas_Dez2023_VF.pdf
- [S14] Relatório da Administração 2025, Rodovias do Café: https://api.mziq.com/mzfilemanager/v2/d/41494f5a-6b15-4502-a348-ca9a59f06cf4/4d251e61-9e88-2a07-9052-757f5664b61f?origin=2
- [S15] InfoMoney / Terra, Via Liberdade: https://www.terra.com.br/economia/consorcio-rota-da-liberdade-arremata-concessao-entre-ouro-preto-e-mariana-com-desagio-de-13,75ec3d6eef755cc6a9702c5c5221958d4fqe4ixn.html
- [S16] UNA Connect, Lote 7: https://unaconnect.com.br/concessao-do-sistema-rodoviario-lote-7-ouro-preto/ (dados de imprensa especializada; não conferidos no edital)

Status dos demais lotes
- [S17] O Tempo, "Plano de concessões rodoviárias de Romeu Zema fica pelo caminho" (26/01/2026): https://www.otempo.com.br/politica/2026/1/26/plano-de-concessoes-rodoviarias-de-romeu-zema-fica-pelo-caminho
- [S18] Itatiaia, revogação do Noroeste (13/02/2026): https://www.itatiaia.com.br/politica/zema-revoga-edital-para-concessao-que-foi-questionado-pelo-dnit/ ; edital do Noroeste: https://www.agenciaminas.mg.gov.br/noticia/governo-de-minas-publica-edital-de-concessao-do-lote-rodoviario-noroeste
- [S19] Agência iNFRA, seis leilões em 2026 (21/10/2025): https://agenciainfra.com/blog/governo-de-mg-projeta-seis-leiloes-para-o-primeiro-semestre-de-2026/

MG-050
- [S20] Dissertação PUC-Rio, cap. 6 "O Projeto da MG-050": https://www.maxwell.vrac.puc-rio.br/14180/14180_7.PDF
- [S21] Dissertação (Univ. de Lisboa), "As Parcerias Público-Privadas no setor rodoviário no Brasil: caso da MG-050": https://scholar.tecnico.ulisboa.pt/api/records/mzvoR7jTBmV8rxxiJdF6sIYxv_60i5o1iqU3/file/af74bff38fd606b32e203b0928c15d7d8af37bc8ec77dcf7c287689b4e7f4caa.pdf

Outras
- [S22] Conflito sobre outorga do Triângulo (resultado de busca citando Seinfra): https://guiadoinvestidor.com.br/?p=140120
- [S23] Fusões & Aquisições, Sul de Minas: https://fusoesaquisicoes.com/acontece-no-setor/consorcio-formado-por-equipav-e-perfin-vence-leilao-rodoviario/
- [S24] ARTEMIG, reajuste Triângulo (22/10/2025): https://artemig.mg.gov.br/noticias/reajuste-tarifario-entra-em-vigor-nas-rodovias-do-triangulo-mineiro/
- [S25] Diário do Comércio, TCE-MG suspende reajuste Sul de Minas: https://diariodocomercio.com.br/legislacao/suspensao-pedagio-sul-minas/
- [S26] Moon BH / O Tempo, reajuste Triângulo 2026: https://moonbh.com.br/bh-news/2026/10/18/pedagio-triangulo-minas-14-50-epr-2026/ ; https://www.otempo.com.br/cidades/2026/10/20/a-partir-desta-quinta-22-pedagio-ficara-mais-caro-em-rodovias-do-triangulo-mineiro-veja-tarifas
- [S27] Agência iNFRA, PPP Via Liberdade (retorno 11,2%, regra de R$ 600 mi): https://agenciainfra.com/blog/ppp-via-liberdade-dois-consorcios-disputam-lote-rodoviario-em-mg/
- [S28] Ratings do Grupo EPR: https://ri.grupoepr.com.br/ratings/
- [S29] https://www.infraestrutura.mg.gov.br/component/gmg/page/2482-concorrencia-internacional-n-003-2022-lote-varginha-furnas (403)
- [S30] https://www.infraestrutura.mg.gov.br/component/gmg/page/2450-concorrencia-internacional-n-002-2021-lote-triangulo (403)
- [S31] https://www.infraestrutura.mg.gov.br/component/gmg/page/2572-consulta-publica-lote-7-ouro-preto-mariana (403)
- [S32] http://www.ppp.mg.gov.br/projetos/projetos-em-estruturacao/rodovias?id=779:lote-7-ouro-preto (certificado inválido)
- [S33] Agência Minas, edital do Lote 7 (28/03/2025): https://www.agenciaminas.mg.gov.br/noticia/ouro-preto-a-mariana-governo-de-minas-publica-edital-de-concessao-do-lote-via-liberdade-com-investimentos-de-r-6-bilhoes-125678
- Fusões (financiamento das SPEs, Tauil & Chequer, 14/02/2023: debêntures de R$ 700 mi no Triângulo e R$ 200 mi no Sul de Minas): https://www.mayerbrown.com/pt/news/2023/02/tauil-and-chequer-advogados-advises-on-project-finance-concessions-totaling-uss-174-million
