# Concessões rodoviárias federais em Minas Gerais: como a ANTT modela a receita (EVTEA)

Pesquisa realizada em 23/10/2026 para o PELT-MG (CODEMGE / Invest MG).

Convenções deste documento:
- **[DOC]** = dado lido em documento ou página oficial (com link).
- **[IMPR]** = dado de imprensa/terceiros, não confirmado em fonte oficial.
- **[INF]** = inferência minha, não documentada.
- "não encontrado" = procurei e não localizei.
- Todos os links estão na seção 8, referenciados como [F#].

---

## 1) Resumo executivo

1. Minas Gerais já concluiu praticamente todo o ciclo de leilões federais recentes: BR-381 (Nova 381, 2024), BR-040 BH–Juiz de Fora (2024), BR-040 BH–Cristalina (Rota dos Cristais, 2024), BR-262 Uberaba–Betim (Rota do Zebu, 2024), BR-153/262 (Rota Sertaneja, 2025), BR-116/251 (Rota das Gerais, 31/03/2026) e Fernão Dias (processo competitivo, dez/2025). Uma notícia indica que a Rota das Gerais fecha o ciclo em MG [IMPR, F27].
2. O critério de julgamento é, em todos os casos achados, **maior desconto sobre a Tarifa Básica de Pedágio (TBP)**. Na BR-381 há ainda **aporte de "Recursos Vinculados" exigido quando o desconto passa de 18%** [DOC, F10, F14].
3. A **TBP é o resultado do modelo**: o EVTEA ajusta a tarifa quilométrica (R$/km, pista simples e pista dupla) para que a **TIR do fluxo não alavancado (FCFF) seja igual ao WACC regulatório** (VPL = 0, sem outorga mínima) [DOC, F13, F16, F18].
4. O fluxo é modelado **em termos reais (valores constantes, data-base da tarifa)**, deflacionado pelo IPCA projetado, com taxa de desconto **real**. Exemplos: 8,47% (BR-040 Concer, 2021), 9,20% (BR-364/365, 2016), 9,22% (Rota dos Sertões, 2025), 11,97% (BR-381, 2024) [DOC, F13, F18, F9, F10].
5. O WACC regulatório vem da Resolução ANTT 6.003/2022 (e 6.002/6.004): **TIR = taxa de longo prazo de referência + spread por classe de risco CR0 a CR3**. Spreads vigentes: 2,09% / 3,52% / 4,94% / 6,37%. Há revisão em audiência pública em 2026 [DOC, F10, F20].
6. A receita é **Receita Tarifária = tráfego em eixos equivalentes (VDMA equivalente) por praça x tarifa da praça x multiplicador de categoria**. O tráfego vem de contagens, pesquisas OD e preferência declarada, e é projetado por correlação com o PIB, com perdas por fuga/desvio via modelos logit [DOC, F17, F18].
7. Os contratos da 5ª etapa trazem **compartilhamento de risco de demanda (Anexo 14)** com bandas de 5% e fator de 80% na BR-381, **descontos de usuário frequente (DUF), desconto de 5% para TAG, degraus/reclassificações tarifárias ligados a obras e free flow** [DOC, F9, F14].
8. Dados abertos úteis da ANTT: **volume de tráfego por praça (2010 a 2026)**, **tráfego equivalente**, **receita por praça (2019 a 2025)**, cadastro de praças, custos operacionais e investimentos. **Não há dataset de tarifas** na lista que verifiquei (seção 5).
9. Para o PELT-MG: o desenho da ANTT (CAPEX distribuído no tempo, receita com ramp-up/PIB, tarifa como incógnita, tributos, WACC real por risco) difere do nosso fluxo (CAPEX+OPEX inteiro no ano 1, desconto 11,02%, aporte constante). A seção 6 lista os ajustes.
10. Lacunas: não encontrei no ar os EVTEA completos de BH–Juiz de Fora, Rota dos Cristais e Rota das Gerais, nem o texto final do Anexo 14 (bandas por contrato), nem o valor numérico do WACC regulatório vigente em 2026.

---

## 2) Concessões federais com trechos em MG

Todas com prazo de 30 anos, salvo indicação. "Desconto" é sobre a TBP.

| Projeto / trecho | Km | Leilão / situação | Vencedor e desconto | Critério | Tarifa básica (R$/km) | CAPEX / OPEX | TIR (WACC) | Fonte |
|---|---|---|---|---|---|---|---|---|
| **BR-381/MG** (BH–Gov. Valadares; Nova 381) | 303,4 | 1ª tentativa nov/2023 sem propostas; leilão 29/08/2024; contrato assinado 23/01/2025 | 4UM Investimentos, 0,94% (outro licitante: Opportunity, 0,10%) | Maior desconto + curva de aporte (Recursos Vinculados se desconto > 18%) | PS 0,18380; PD 0,25732 (voto) ; página ANTT cita 0,1821 / 0,2549 (data-base jan/23) | CAPEX R$ 5,5 bi; OPEX R$ 3,7 bi (página ANTT). Voto: CAPEX R$ 5,57 bi, OPEX R$ 3,68 bi | **11,97%** (CR3). Tentativa anterior: 9,88% (e 8,47% na AP de 2022) | F10, F14, F1, F11 |
| **BR-040/MG BH–Juiz de Fora** (Via Mineira / EPR) | 232 | Leilão 11/04/2024 (1º da relicitação) | Consórcio Infraestrutura MG (EPR), 11,21% (rivais: 0% e 1%) | Maior desconto | não encontrado | "mais de R$ 9 bi" de investimento (imprensa, edital 2023) | não encontrado | F2, F3, F25 |
| **BR-040/GO/MG BH–Cristalina** (Rota dos Cristais / Via Cristais) | 594,8 | Leilão 26/09/2024; operação desde 10/03/2025 | Vinci Highways, 14,32% (BTG 7,50%; 4UM+Opportunity 9,09%; CCR 1,75%) | Maior desconto | PS 0,12405 (imprensa, valor possivelmente já reajustado; ver nota) | CAPEX R$ 6,4 bi; OPEX R$ 5,6 bi [IMPR] | 9,21% (estimativa do Safra, terceiro) [IMPR]; oficial não encontrado | F4, F5, F6, F12 |
| **BR-262/MG Uberaba–Betim** (Rota do Zebu) | 438,9 | Leilão out/2024 | Consórcio Kinea / Way (15,3% na fase viva-voz, contra BTG) [IMPR] | Maior desconto | PS 0,13969; PD 0,18160 (data-base jul/23) | CAPEX R$ 4,40 bi; OPEX R$ 4,10 bi | 9,21% | F9 (tabela), F21 |
| **BR-153/262 GO/MG** (Rota Sertaneja; Way-153) | 530 | Leilão 06/11/2025; homologado 17/12/2025; contrato pendente na última informação | Way Concessões, 24,80% (Rota do Cerrado 20,36%; Vinci 20,11%) [IMPR] | Maior desconto | PS 0,1086; PD 0,1521 (data-base jan/22) | CAPEX R$ 5,30 bi; OPEX R$ 4,10 bi | 9,22% | F9 (tabela), F21 |
| **BR-116/251 MG** (Rota das Gerais; Ecovias das Gerais) | ~735 | Leilão 31/03/2026; contrato 03/06/2026 | EcoRodovias, 19% (viva-voz; antes 13,5%, 13,7% e 0,01%) | Maior desconto; DBT-TAG 5%, DUF até 50%, moto isenta | não encontrado | "mais de R$ 13 bi" (ANTT, CAPEX+OPEX?); pré-leilão: CAPEX ~R$ 7,2 bi, OPEX ~R$ 5,2 bi [IMPR] | não encontrado | F7, F8, F22 |
| **BR-116/465/493 RJ/MG** (Rio–Gov. Valadares; EcoRioMinas) | 726,9 | Leilão 20/05/2022; operação desde 22/09/2022 | EcoRodovias, 3,11% (teto de desconto 17,5%) [IMPR] | Maior desconto | não encontrado | não encontrado | não encontrado | F23 |
| **BR-364/365 GO/MG** (Ecovias do Cerrado) | 437 | Concessão em operação (EVTEA original PMI 2016) | não pesquisado | Menor tarifa | Tarifa quilométrica R$ 10,098 por 100 km (ou R$ 0,10098/km; data-base jul/2016) | não extraído | 9,20% | F15 |
| **BR-050 GO/MG** (Eco050 / Ecovias Minas Goiás) | 436,6 | Leilão 18/09/2013; operação jan/2014 | Consórcio Planalto, 42,38% (tarifa R$ 0,04534/km; teto R$ 0,0787/km) [IMPR] | Menor tarifa | ver coluna do vencedor | Investimento realizado >R$ 2,5 bi [IMPR] | não encontrado | F24 |
| **BR-381 SP/MG Fernão Dias** (Autopista Fernão Dias / Motiva Minas SP) | 562 | Processo competitivo 11/12/2025; contrato até 2040; transferência Arteris para Motiva autorizada em 26/03/2026 | Motiva, 17,05% (EPR 11,25%; Arteris 0%) [IMPR] | Maior desconto | não encontrado | ~R$ 14,8 bi em uma década [IMPR] | não encontrado | F26 |

Notas:
- A BR-381/262 MG/ES (tentativa de 2021 a 2022) não foi a leilão com sucesso; o projeto foi reformulado como BR-381/MG [DOC, F10]. A TIR subiu de 8,47% para 9,88% em jul/2022 [IMPR, F11] e depois para 11,97% em 2024 [DOC, F14].
- O PELT-MG deve tratar a Rota dos Cristais com cautela: a notícia [F12] diz "tarifa básica de R$ 0,12405 para trechos de pista simples" após aprovação da ANTT e cita reajuste IRT 1,067. Não consegui saber se 0,12405 é o valor com ou sem reajuste.
- A planilha de praças da ANTT (maio/2026) lista também Concer e Elovias (BR-040, Rio–BH/ Juiz de Fora) e Ecovias Minas Goiás, Ecovias Rio Minas, Motiva Minas SP, Nova 381, Via Cristais, Way 153 e Way 262 com praças ativas em MG [DOC, F28]. A BR-040 Concer (BH–RJ) foi o objeto do EVTEA de 2021 (data-base jan/2021), cuja TIR real foi 8,47% [DOC, F13].
- Os valores de receita bruta anual por concessionária nas praças de MG (2025) que calculei dos dados abertos estão na seção 5 (não confirmados contra balanços).

---

## 3) Como a receita é modelada nos EVTEA da ANTT

### 3.1 Estrutura do estudo

Cada EVTEA é composto por seis produtos: Estudo de Tráfego, Estudos de Engenharia, Modelo Operacional, Estudos Econômico-Financeiros, Relatório Executivo e PER (Programa de Exploração da Rodovia) [DOC, F13]. O produto econômico-financeiro usa o tráfego como entrada e entrega a **Tarifa Básica de Pedágio** para pista simples e dupla, "que possibilita valor mínimo de outorga equivalente a zero" [DOC, F13].

Ponto importante (citação do estudo da Concer): o modelo "reflete apenas cenário indicativo para definição das Tarifas de Pedágio" e não capta alterações ex-post (aportes adicionais, mudanças de demanda, receitas extraordinárias), que são tratadas via contrato e reequilíbrio [DOC, F13].

### 3.2 Projeção de tráfego (produto 1)

Documentado no Estudo de Tráfego da BR-101/SC (2019), que é um bom proxy do método padrão da ANTT/consultorias [DOC, F17]:

1. **Coleta primária**: contagens volumétricas e classificatórias (CVC), por 7 dias de 24 horas nos postos principais, expandidas com fatores sazonais; pesquisas Origem-Destino (OD); pesquisas de **preferência declarada** (PD) para estimar fuga e valor do tempo. Dados secundários: praças de pedágio das concessões vizinhas (por exemplo, praça 05 de Palhoça da ALS), DNIT/PNCT [DOC, F17].
2. **Unidade de demanda**: VDMA em **eixos equivalentes tarifários** (veículos leves = 1 eixo base; comerciais ponderados pelo número de eixos), e VDMA equivalente por praça. Eixos suspensos: usou 4,1% sobre eixos pedagiados, valor arbitrado pela ANTT em reequilíbrio de outra concessionária [DOC, F17].
3. **Matrizes de viagens** por classe de veículo, zoneamento de tráfego, e rede de simulação com rotas alternativas [DOC, F17].
4. **Crescimento "normal" sem pedágio** por correlação com o **PIB Brasil** (única variável macro com projeção de longo prazo). Foram ajustadas funções polinomiais separadas para leves, pesados e eixos equivalentes. Exemplos documentados [DOC, F17]:
   - Leves: Tdemanda = 2,1*TPIB^2 + 0,66*TPIB + 0,04 (R2 = 0,90)
   - Pesados: Tdemanda = 369,85*TPIB^3 - 18,14*TPIB^2 + 1,90*TPIB - 0,01 (R2 = 0,96)
   - Eixos equivalentes: Tdemanda = 331,38*TPIB^3 - 16,97*TPIB^2 + 1,46*TPIB (R2 = 0,95)
   - Taxas de eixos equivalentes mostradas: 2,50% para PIB e 3,11% para tráfego em 2021 a 2023 (quadro 31 do estudo)
   - Tendo em vista a forma polinomial, a "elasticidade" varia com o PIB (não é constante). Não vi um valor único de elasticidade no documento.
5. **Perdas por fuga, desvio, mudança modal e desistência**: processo **iterativo** entre tráfego e tarifa. Calculam-se fugas com modelos **logit** (calibrados em PD), por classe de veículo, nas rotas alternativas; a nova demanda altera a receita, que altera a tarifa de equilíbrio, que altera a fuga, até convergir [DOC, F17]. O estudo de localização das praças (3 cenários na BR-101/SC) usa o critério de minimizar fuga como critério preponderante [DOC, F17].
6. **Premissas macro do PIB**: o EVTEA da BR-364/365 (2016) usa Focus do Banco Central nos 5 primeiros anos e **PIB de 2,5% a.a.** e inflação 4,0% depois [DOC, F15]. No estudo da Concer (2021), IPCA 4,52%, 5,15%, 3,64%, 3,25% e 3,25% de 2025 em diante [DOC, F13].
7. Saída para a Rota dos Sertões (BR-116/BA/PE): **95 mil Veq/dia no ano 1 a 170 mil Veq/dia no ano 30** (o parecer escreve "Veq/ano" no fim da frase, provável erro de digitação), média de 141 mil veículos/dia [DOC, F9]. Isto é crescimento total de ~79% em 30 anos, ~2% a.a. [INF, cálculo meu].
8. Rampa de crescimento (ramp-up) e cenários: não encontrei descrição de ramp-up específica nem de cenários otimista/pessimista no EVTEA lido. O ano 1 já parte da demanda observada/projetada, e a perda por pedágio aparece como fuga (no caso de rodovia sem pedágio, o risco de tráfego é maior; a ANTT usa bandas de 5% na BR-381 por isso [DOC, F14]).

### 3.3 Tarifa

- **Tarifa quilométrica** (R$/km) por tipo de pista: PS e PD, com PD cerca de 40% acima da PS na BR-381 (0,25732 / 0,18380 = 1,40) [DOC, F14]. Rota dos Sertões: 0,0892 PS e 0,1159 PD [DOC, F9].
- **Tarifa da praça** = tarifa quilométrica x extensão do Trecho de Cobertura de Praça (TCP). Na BR-364/365, tarifa única = R$ 0,10098 x 437 km / 7 praças = R$ 6,30 [DOC, F15].
- **Multiplicadores por categoria** (exemplo da BR-364/365): automóveis 1,0; automóvel com semirreboque 1,0 (categoria 2); com reboque 1,5; comerciais de 2 eixos 2,0; 3 eixos 3,0; 4 eixos 4,0 etc. [DOC, F15, tabela com formatação confusa no PDF; confira no original].
- **TBP resolve o VPL = 0**: "A Receita foi projetada utilizando-se a tarifa encontrada para que a TIR atingisse o valor de 9,2% a.a." [DOC, F15].
- **Critério de leilão**: menor tarifa = maior desconto sobre a TBP. No modelo "híbrido" da BR-381, o desconto acima de 18% exige **aporte de Recursos Vinculados** em valor proporcional ao deságio, curva calculada com base no edital do Lote 1 do Paraná e simulada no MEF (quanto cada ponto percentual de deságio representa em perda de receita) [DOC, F14]. O valor numérico da curva de aporte não consta no voto que li.
- **Descontos de tarifa**: DBT (Desconto Básico de Tarifa) de 5% para pagamento por TAG e DUF (Desconto de Usuário Frequente) **progressivo ao longo de um mês** [DOC, F9]; na Rota das Gerais, DUF de até 50% e isenção para motociclistas [DOC, F8]. Não encontrei como a ANTT modela o efeito desses descontos na receita média (percentual médio de usuários beneficiados).
- **Degraus tarifários / reclassificações**: tarifa condicionada à entrega de pacotes de obras na fase de transição e depois à execução de ampliações (duplicação/faixas adicionais); o TCU pediu mudanças sobre o cálculo PS/PD e reclassificação após duplicação na Rota das Gerais [DOC, F9; IMPR, F29]. Na Rota das Gerais, o pedágio só começa após melhorias iniciais ("Plano de 100 dias") [DOC, F8].
- **Free flow**: a modelagem da Rota dos Sertões prevê cobrança por livre passagem [DOC, F9]. Não encontrei como a evasão é parametrizada no EVTEA (valor percentual).
- **Reajuste tarifário**: anual pelo IPCA (ex.: IRT de 1,067 entre jul/2023 e mar/2025, reajuste de 6,70% na Rota dos Cristais [IMPR, F12]); as tarifas de BR-381 e Rota dos Sertões têm data-base explícita (jan/23 e abr/23) [DOC, F9, F10].
- **Reajuste e revisão ordinária**: Fatores A, D e E (paramétricos de reequilíbrio) e Fator C (compensação financeira) ligados ao desempenho do PER; no modelo da 5ª etapa, os efeitos incidem sobre a **alíquota de Recursos Vinculados**, não diretamente sobre a tarifa, com reversão do saldo a cada 3 anos à modicidade tarifária [DOC, F14].

### 3.4 Receitas acessórias e extraordinárias

- A Receita da Concessionária no EVTEA da BR-364/365 é "composta especificamente pela Receita Tarifária"; no da Concer há também "Receitas Acessórias" (apenas a tributação é citada na tabela: PIS 1,65% e COFINS 7,60% para acessórias, ISS 5%) [DOC, F13, F15].
- Não encontrei valores percentuais de receita acessória no EVTEA (nas fontes lidas). Receitas extraordinárias "não constam" do modelo, porque são tratadas ex-post [DOC, F13].

### 3.5 Tributos e descontos sobre a receita (efeito no fluxo)

Na Concer (2021) [DOC, F13]: PIS 0,65% e COFINS 3,00% (cumulativo) sobre receita tarifária; ISS até 5%; IRPJ 15% + 10% adicional; REIDI 3,65% aplicado sobre CAPEX; outorga variável de 4% da receita bruta; verba de fiscalização ANTT 1,5% do VPL da receita bruta (anualizada); RDT 0,25%; verba de segurança R$ 170/km/mês; seguros e garantias (0,15%, 0,20%, 0,0594% e 0,25% conforme o tipo). No BR-364/365: ISS 5%, PIS+COFINS 3,65%, IR 15% + 10%, CSLL 9% [DOC, F15].

### 3.6 Compartilhamento de risco de demanda e outros mecanismos

- **Contratos da 5ª etapa** (a partir da Rota dos Cristais) migraram do mecanismo de compartilhamento do **risco de receita** para o de **risco de demanda** (tráfego como variável de acompanhamento) [DOC, F14].
- **Anexo 14 (Mecanismo de Compartilhamento do Risco de Demanda)**: na BR-381, **bandas de compartilhamento de 5% e fator de compartilhamento de 80%** durante toda a vigência do contrato (por ser trecho sem histórico de pedágio e obras do DNIT) [DOC, F14]. A ANTT justificou que o mecanismo evita caducidade/relicitação ao dar suporte financeiro em caso de frustração de tráfego, e pediu que não seja condicionado ao índice de execução contratual [DOC, F14].
- Para os demais contratos, as faixas de proposta de 2022 foram: bandas de 10% a 15%, 15% a 20% e acima de 20%, com compartilhamento de 25%, 50% e 75% (existentes), com proposta de elevar o compartilhamento; no texto final, não confirmei os valores [IMPR, F30]. Nota: esse trecho é de notícia sobre proposta, não de contrato assinado.
- **Conta vinculada e Recursos Vinculados**: a Rota dos Sertões usa "contas vinculadas para a constituição de reserva de contingência" e fatores paramétricos sobre a alíquota de recursos vinculados [DOC, F9]. Na BR-381 a alíquota de recursos vinculados caiu de 3% (R$ 771 mi) para 1% (R$ 259 mi) na reformulação [DOC, F14].
- **Risco cambial**: o parecer do MF lista "cambial" entre os riscos alocados na matriz [DOC, F9]. Não encontrei o detalhe de mecanismo de proteção cambial. O EVTEA da Concer inclui o ressarcimento do EVTEA em dólares (US$ 2.177.780,38) [DOC, F13].
- **Risco geotécnico**: BR-381 tem waiver de 2 anos para a concessionária levantar riscos geotécnicos [DOC, F14].
- **Obras do DNIT**: alguns trechos têm obras a cargo do DNIT (Rota dos Sertões, BR-381), e a concessionária só conserva depois [DOC, F9, F14].

### 3.7 Estrutura de CAPEX e OPEX no fluxo (para comparar com o nosso modelo)

- Horizonte: 30 anos. CAPEX **distribuído no tempo** (Rota dos Sertões: maior volume até o 7º ano; Rota dos Cristais: 58% do ano 1 ao 7 [IMPR, F31]; Rota das Gerais: obras entre o 3º e o 10º ano [DOC, F8]).
- Rota dos Sertões: CAPEX R$ 3,18 bi (40,92% em TI, restauração e manutenção; 38,96% em ampliação), OPEX R$ 4,0 bi (62,12% em sistemas de operação, 27,80% em conservação) [DOC, F9].
- Financiamento: no EVTEA da BR-364/365, BNDES financia 50% dos investimentos financiáveis, custo financeiro 11,0% a.a. (TJLP 7,0% + spread do setor 1,9% + spread do banco 2,1%) [DOC, F15]. Isto vale para FCFE/FCFD, não para o FCFF.
- Resultados: FCFF Rota dos Sertões passa a ser positivo no 8º ano; payback de 15 anos (projeto) e 16 anos (acionista); TIR projeto = 9,22%, FCFE 13,37%, DDM 12,44% [DOC, F9]. (Observação: o item 13 do parecer fala em 12,44% para o "projeto alavancado (FCFE)" e o item 31 diz 13,37% para FCFE e 12,44% para o acionista; confira no original.)

---

## 4) WACC, moeda (real x nominal) e indicadores

### 4.1 Moeda

- O modelo é construído em **moeda constante (real)**, na data-base (ex.: "Todos os valores estão apresentados em Reais a valores constantes na data base de julho de 2016, ou seja, não foram ajustados pela inflação" [DOC, F15]). Também há fluxos nominais (inflacionados), em abas separadas ("FCProjReal", "FinanciamentoReal", "FCAcionReal" etc.) [DOC, F15]. Na Concer: "ajustes de deflação... para a projeção em termos reais", usando IPCA projetado [DOC, F13].
- A **taxa de desconto é real** ("taxa interna de retorno sobre o fluxo de caixa em Reais da Base 0, sem inflação, em uma operação não alavancada") [DOC, F15].
- A depreciação fiscal é calculada em função da curva de VDM equivalente (amortização pela curva de tráfego), e deflacionada para o fluxo real [DOC, F13, F15].
- Tarifa reajustada pelo IPCA no contrato; ou seja, receita real constante ao longo do tempo (aparte o crescimento de tráfego) [INF, coerente com os documentos].

### 4.2 Metodologia do WACC regulatório

- Resoluções ANTT 6.002, 6.003 e 6.004 de 22/12/2022 (WACC com classes de risco CR0 a CR3, spreads), alterada pela Res. 6.048/2024 [DOC, F9, F20]. Histórico: Res. 3.651/2011, 4.075/2013, 4.903/2015 (Monte Carlo), 6.003/2022 [DOC, F20].
- **Fórmula (BR-381, mar/2024)**: TIR = taxa de longo prazo de referência (TLPT-2, jan/24) de **5,60%** + spread por CR. Com spread CR2 (4,94%) = 10,54%. A diretoria elevou o projeto para **CR3 (spread 6,37%) = 11,97%** [DOC, F14]. Nota: o voto rotula a conta de 10,54% como "TIR para CR1" mas usa o spread de CR2; é inconsistência do texto.
- **Spreads vigentes** (Res. 6.004/2022): CR0 2,09%; CR1 3,52%; CR2 4,94%; CR3 6,37% [DOC, F20]. Spreads "esperados" na revisão proposta em jun/2026 (simulação, não valores finais): CR0 2,39%; CR1 2,97% ; CR2 3,60%; CR3 4,35% (os valores aparecem em duas colunas no PDF extraído, atribuição por CR é minha leitura [INF]; confira em F20).
- Revisão em 2026 (audiência pública de 30/06 a 13/08/2026, prazo possivelmente alterado): mediana anual de preços para equity, janela comum desde 2011, **cópulas** para dependência entre variáveis, beta regulatório central de **1,10 alavancado**, retornos logarítmicos, custo de dívida setorial ponderado (com debêntures incentivadas), CRs por quantis (P50, P60...) [DOC, F20, F19]. Não afeta leilões já realizados [DOC, F19].
- Projetos com mais CAPEX tendem a ter CR maior (proposta de 2024) [DOC, F32].
- A ANTT usa o WACC como taxa de desconto (a) no EVTEA, (b) no Fluxo de Caixa Marginal para reequilíbrio, (c) para definir CRs [DOC, F20]. Nos reequilíbrios, mantém-se a taxa de desconto originalmente usada no FCM projetado [IMPR, F33 (MPF), não confirmado como norma vigente].

### 4.3 Valores observados do WACC/TIR real nos EVTEA

| Projeto | Ano / base | TIR (WACC real, FCFF) | Fonte |
|---|---|---|---|
| BR-364/365 GO/MG (PMI) | 2016 | 9,20% | F15 (nota STN/SEAE/MF) |
| BR-040 MG/RJ + BR-495 (Concer) | data-base jan/2021 | 8,47% (Ofício 131/2020/SFPP) | F13 |
| BR-381/262 MG/ES e BR-381/MG (1ª fase) | 2022 | 8,47% elevado a 9,88% | F11 [IMPR] |
| BR-381/MG (versão do leilão) | mar/2024 | 11,97% (CR3) | F14 |
| BR-262/MG Rota do Zebu | data-base jul/23 | 9,21% | F9 (tabela) |
| BNDES lotes Centro-Oeste e Norte 1 | data-base jan/24 | 9,08% | F9 (tabela) |
| BR-153/262 GO/MG Rota Sertaneja | data-base jan/22 | 9,22% | F9 (tabela) |
| BR-116/BA/PE Rota dos Sertões | abr/23 (tarifa); AP 2024 | 9,22% (CR1) | F9 |
| Rota dos Cristais BR-040 | 2024 | 9,21% (estimativa de terceiro) | F6 [IMPR] |

Não encontrei o WACC das concessões Rota das Gerais, BH–Juiz de Fora (data-base 2023/2024) nem o valor "vigente" de 2026. Pela fórmula, um valor para CR1 em 2024/2025 ficou em torno de 9,1% a 9,2% (5,60% a 5,70% + 3,52%) [INF].

### 4.4 Indicadores usados

TIR do projeto não alavancado (= WACC), TIR do acionista (DDM/FCFE), payback (15 e 16 anos na Rota dos Sertões), data em que o FCFF vira positivo (ano 8), capital social mínimo, receita tarifária anual média (BR-381: R$ 853 milhões), FCFF negativo acumulado, VPL zero com outorga mínima nula [DOC, F9, F14].

---

## 5) Dados abertos da ANTT úteis

Portal: https://dados.antt.gov.br (CKAN, licença Creative Commons Atribuição; 106 conjuntos na listagem). Todos os links são dos datasets (consulte a página para baixar CSV/JSON).

| Dataset | Link | Formato / periodicidade | Período | Uso para calibrar receita em MG |
|---|---|---|---|---|
| Volume de Tráfego por Praça (veículos por categoria/mês) | https://dados.antt.gov.br/dataset/volume-trafego-praca-pedagio | CSV e JSON; anual 2010-2023, diário e mensal 2024-2026; atualiz. mensal (última 30/09/2026) | 2010 a 2026 | Tráfego real por praça, sentido, tipo de cobrança (manual, TAG, OCR/placa), categoria/eixos e tipo de veículo; campos: concessionaria, mes_ano, sentido, praca, Tipo de Cobrança, categoria_eixo, tipo_de_veiculo, volume_total (dicionário PDF). Calibra crescimento, sazonalidade, mix leves/pesados e ramp-up em concessões novas (Via Mineira, Via Cristais, Nova 381) |
| Volume de Tráfego **Equivalente** por Praça | https://dados.antt.gov.br/dataset/volume-trafego-equivalente-praca-pedagio | CSV e JSON; anual 2010-2024, diário/mensal 2024-2026; mensal (28/09/2026) | 2010 a 2026 | Base de receita: o VDMA em eixos equivalentes é a base que multiplica a tarifa. Arquivo de 2024 de ~705 MB |
| Receita por Praça (mensal) | https://dados.antt.gov.br/dataset/receita-por-praca | CSV e JSON; anual | 2019 a 2025 | Receita mensal por praça, com UF, rodovia, km, município, coordenadas (campos: Concessionaria, Praca_de_pedagio, UF, Rodovia, Km_m, Mes_ano, Receita_Praca_de_Pedagio). Dividida pelo tráfego dá **receita média por veículo (tarifa efetiva)**, que embute categorias, DUF, TAG e evasão |
| Receita de Pedágio (por concessionária/ano) | https://dados.antt.gov.br/dataset/receita-pedagio | CSV e JSON; anual | histórico (anos não conferidos) | Total anual por concessionária (campos: concessionaria, ano, valor) |
| Praças de Pedágio (cadastro) | https://dados.antt.gov.br/dataset/praca-de-pedagio | CSV, JSON, KMZ; mensal (arquivo 6/2026) | posição atual | 277 praças; 46 em MG. **Sem tarifa**. Concessionárias com praça em MG no arquivo: Concer, Ecovias do Cerrado, Ecovias Minas Goiás, Ecovias Rio Minas, Elovias, EPR Via Mineira, Motiva Minas SP, Nova 381, Via Cristais, Way 153, Way 262 |
| Tráfego de Veículos SAT (contagem automática por concessionária) | https://dados.antt.gov.br/dataset/volume-sat | CSV; mensal; 102 recursos (inclui Eco050, Ecovias do Cerrado, Via 040, Via Mineira, Autopista Fernão Dias) | variável | Contagens nos pontos SAT (complementa praças); não conferi o dicionário |
| Volume Radar | https://dados.antt.gov.br/dataset/volume-radar | não conferido | n/c | Volume em radares; não conferido |
| Custos Operacionais | https://dados.antt.gov.br/dataset/custos-operacionais | CSV/JSON; anual | n/c | Benchmark de OPEX por concessionária |
| Investimentos / Autorização de Investimentos / Cadastros / Inexecução | https://dados.antt.gov.br/dataset/investimentos ; /autorizacao-investimento ; /cadastros-investimentos ; /inexecucao | CSV/JSON; anual ou mensal | n/c | CAPEX realizado vs previsto (benchmark para CAPEX por km) |
| ISS arrecadado | https://dados.antt.gov.br/dataset/iss-arrecadado | CSV/JSON; anual | n/c | Proxy de receita bruta tributável por município |
| Acidentes (rodovias e por km) | https://dados.antt.gov.br/dataset/acidentes-rodovias ; /acidentes-quilometro-rodovias | CSV por concessionária | n/c | Segurança viária (não receita) |
| Trecho concedido, Infraestrutura rodoviária (tipo de pavimento, faixa, pista principal etc.) | https://dados.antt.gov.br/dataset/trecho-concedido ; /infraestrutura-rodoviaria | CSV/JSON; anual | n/c | Cadastro físico, extensão por trecho, PS/PD |
| Projetos de Concessão de Rodovias | https://dados.antt.gov.br/dataset/projeto-concessao-rodovias | n/c | n/c | Lista de projetos em PPCS ainda não licitados |
| Vale-Pedágio Obrigatório | https://dados.antt.gov.br/dataset/vale-pedagio-obrigatorio | mensal | n/c | Uso de VPO (carga) |
| Taxa de fiscalização | https://dados.antt.gov.br/dataset/taxa-de-fiscalizacao | n/c | n/c | Verba de fiscalização |

**O que fazer com eles para calibrar receita em MG** [INF]:
1. Calcular receita por veículo equivalente por praça (receita mensal / VDM equivalente) e comparar com a tarifa de face x multiplicador: mostra o "desconto efetivo" (TAG 5%, DUF, isentos, evasão).
2. Estimar crescimento e sazonalidade do tráfego (2010 a 2026) das praças de MG e testar contra PIB (correlação, como faz a ANTT) para uma regra de crescimento do PELT-MG.
3. Estimar ramp-up/queda de tráfego após o início da cobrança em concessões novas em MG (Via Mineira desde 2024, Via Cristais desde mar/2025, Nova 381 e Way-262 a partir de 2025): comparar contagem SAT/DNIT pré-pedágio com o tráfego pedagiado.
4. Usar custos operacionais e investimentos para benchmark de OPEX/km e CAPEX/km.

**Resultado de um cálculo meu** (receita mensal somada das praças em MG, arquivo 2025; nº de meses com dado entre parênteses; valores brutos, **não auditados**; algumas concessionárias com poucos meses, e as da fase inicial de operação): Via Cristais R$ 523,4 mi (10); Via Mineira R$ 404,8 mi (12); Autopista Fernão Dias R$ 412,1 mi (11); Eco050 R$ 330,7 mi (12); Ecovias do Cerrado R$ 176,5 mi (12); Concebra R$ 160,3 mi (12); Elovias R$ 23,9 mi (2). Fonte: https://dados.antt.gov.br/dataset/receita-por-praca (arquivo receita_por_praca_2025.csv). Recomendo validar (o filtro por UF "Minas Gerais" pode pegar praças da rodovia em MG sem separar o tráfego em outros estados).

Observação: **não existe dataset de tarifas** entre os 106 conjuntos listados. As tarifas de face aparecem em Deliberações/Portarias de reajuste anuais da ANTT e nos sites das concessionárias [INF; não verificado].

---

## 6) Lições para o modelo do PELT-MG

Nosso fluxo: CAPEX+OPEX inteiro abatido no ano 1, receitas em moeda constante, desconto de 11,02% e aporte constante do Estado. Comparação com a prática da ANTT e recomendações. Itens "[DOC]" referem-se ao que a ANTT faz; as recomendações são inferências minhas.

1. **CAPEX no ano 1** [INF]. A ANTT distribui o CAPEX no tempo (Sertões: maior volume até o ano 7; Cristais: 58% do ano 1 ao 7; Gerais: obras entre ano 3 e 10) e o fluxo vira positivo só no ano 8. Concentrar tudo no ano 1 superestima o custo financeiro e, portanto, a contraprestação necessária. Recomendação: usar o cronograma de obras do PER/EVTEA por empreendimento, em valor constante.
2. **OPEX no ano 1** [INF]. Na ANTT, OPEX é anual, com rubricas (sistemas de operação 62%, conservação 28% no Sertões) e atrelado a receita (outorga variável, fiscalização 1,5% do VPL da receita, RDT 0,25%, seguros). Recomendação: OPEX anual por km, e rubricas % da receita separadas.
3. **Taxa de desconto** [INF]. 11,02% é compatível com as taxas mais altas já usadas pela ANTT em projetos muito arriscados (BR-381, 11,97% real, CR3), mas bem acima do WACC real de projetos de risco médio (9,2% a 9,22%) e do mínimo histórico (8,47%). Fórmula: referência de longo prazo + spread por classe de risco. Recomendação: rodar o PELT com 8,5%, 9,2% e 11,97% como sensibilidade, e declarar se a 11,02% é real ou nominal. Se for nominal, converter (ex.: 11,02% nominal com IPCA 4% equivale a ~6,8% real [INF, cálculo meu]), pois a ANTT desconta fluxo real a taxa real.
4. **TIR do projeto = WACC** [DOC]. A ANTT dimensiona a tarifa (ou o aporte) para que o VPL a esse WACC seja zero. Nosso exercício é equivalente (contraprestação que zera VPL), mas a ANTT resolve a **tarifa**; só há aporte quando o desconto do leilão excede um limite (18% na BR-381) ou nos projetos patrocinados (PPP), onde não se considera participação do governo na concessão plena [DOC, F15].
5. **Aporte constante do Estado** [INF]. Na ANTT o aporte (Recursos Vinculados) é exigido do vencedor, não pago pelo poder concedente, e é proporcional ao deságio. Para um aporte público (PPP/concessão patrocinada), a analogia mais próxima é o aporte em fase de obras (curva atrelada ao cronograma) e contraprestação após a entrega. Recomendação: considerar aporte durante a obra + contraprestação pós-obra, em vez de série constante.
6. **Receita em moeda constante** [DOC/INF]. Está alinhado com a ANTT (valores constantes na data-base, tarifa reajustada por IPCA). O que falta: **crescimento de tráfego** (a ANTT usa PIB: ~2% a.a. de crescimento total na Rota dos Sertões; PIB 2,5% a.a. de longo prazo em estudos antigos) e **tarifa por categoria** (multiplicadores por eixo e conversão para eixos equivalentes).
7. **Receita = tráfego x tarifa x multiplicador** [DOC]. Recomendação: modelar por trecho/praça em Veq/dia, com tarifa quilométrica (R$/km) x TCP, e usar os dados abertos (seção 5) para calibrar receita por Veq em MG.
8. **Fuga/evasão e descontos** [DOC]. Aplicar um redutor de receita (TAG 5%, DUF, isentos, evasão em free flow) calibrado com receita/Veq real do dataset de receita por praça. O fator não consta nos EVTEA lidos, então a calibração empírica é a opção.
9. **Risco de demanda** [DOC]. Se o Estado quiser replicar a ANTT, usar banda de 5% e fator de 80% (BR-381, trecho sem histórico) como cenário; a faixa tradicional em outros contratos [IMPR] tinha banda de 10 a 15% e compartilhamento de 25%/50%/75%. Isso transforma a contraprestação em função do tráfego realizado.
10. **Tributos** [DOC]. PIS+COFINS 3,65% sobre receita, ISS 5%, IRPJ 15%+10%, CSLL 9%, REIDI 3,65% de redução do CAPEX. Se nosso modelo é antes de tributos, a contraprestação sai subestimada.
11. **Cenários** [INF]. Rodar o tráfego com 3 cenários (PIB baixo/base/alto) e com a fuga quando a tarifa sobe, como a ANTT faz iterativamente.
12. **Metodologia de reequilíbrio (FCM)** [DOC/IMPR]. Se o Estado quiser prever reequilíbrios, usar fluxo de caixa marginal com a taxa de desconto do projeto.

---

## 7) Lacunas e documentos para baixar

| Item | Onde procurar | Observação |
|---|---|---|
| EVTEA, planilha do MEF (xlsx), caderno de demanda e PER da **BR-381/MG** | https://www.gov.br/antt/pt-br/assuntos/rodovias/novos-projetos-em-rodovias/br-381-mg (links SharePoint de "Andamento dos Estudos" e "Histórico e Estudos"); AP 07/2022 no Participa ANTT | Links do SharePoint listados em F10; não consegui abrir. Voto DGS 029/2024 (F14) foi lido |
| EVTEA de **BH–Juiz de Fora (BR-040 MG)** | gov.br/antt, página do projeto BR-040/MG | tarifa, TIR, CAPEX/OPEX não encontrados |
| EVTEA e MEF da **Rota dos Cristais** (BR-040 GO/MG) | gov.br/antt, página do projeto; Voto de aprovação do edital | TIR oficial não encontrada |
| EVTEA e MEF da **Rota das Gerais** (BR-116/251 MG) | gov.br/antt e briefing do Ministério (https://www.gov.br/transportes/pt-br/assuntos/concessoes/BriefingCGORRotaGerais.pdf, falhou ao baixar como PDF) | tarifa, TIR e demanda não encontrados |
| **Rota do Zebu** e **Rota Sertaneja** (EVTEA completos) | gov.br/antt, páginas dos projetos | só a tabela comparativa do parecer do MF (F9) |
| **Anexo 14** do contrato 5ª etapa (bandas, fatores e cálculo do mecanismo de demanda) | Contrato da Rota dos Cristais, BR-381 ou Rota das Gerais em gov.br/antt (arquivos para download) | só os valores da BR-381 (5% e 80%) foram vistos |
| **Texto das Resoluções 6.002, 6.003, 6.004/2022 e 6.048/2024** (fórmula e spreads) | Datalegis/ANTTlegis (https://anttlegis.antt.gov.br) | valores de spread lidos no Voto DAB (F20); falta o valor da taxa de longo prazo vigente em 2026 |
| Resultado da **audiência pública de 2026 sobre WACC** | participantt.antt.gov.br | nova metodologia ainda em consulta |
| Resolução do **Fluxo de Caixa Marginal** e RCR (Res. 6.000, 6.032/2023; IN 33/2024) | ANTTlegis | não li o texto |
| **Estudo de Tráfego** completo de uma concessão em MG (ex.: Rota dos Cristais, Rota do Zebu) | gov.br/antt, aba de estudos; caderno de demanda | usei o da BR-101/SC (F17) como modelo de método. Coeficientes da correlação com PIB são específicos daquele corredor e não devem ser usados em MG |
| Valores de **evasão, DUF médio e receita acessória** nos EVTEA | cadernos econômico-financeiros dos lotes | não encontrado |
| Tarifas de face atuais por praça de MG | Deliberações/Portarias de reajuste da ANTT | não encontrado em dados abertos |
| Resultado e termos do leilão **BR-153/262 (Way)**, assinatura do contrato | gov.br/antt | última informação: homologado em 17/12/2025 |
| Dicionário do dataset de tráfego equivalente e SAT | links de recursos nos datasets | não conferidos |

---

## 8) Fontes

Documentos oficiais e técnicos:
- F1. ANTT, página BR-381/MG: https://www.gov.br/antt/pt-br/assuntos/rodovias/novos-projetos-em-rodovias/br-381-mg
- F7. B3, leilão Rota das Gerais: https://www.b3.com.br/pt_br/noticias/ministerio-dos-transportes-e-antt-realizam-leilao-na-b3-para-a-concessao-do-sistema-rodoviario-br-251-mg-e-br-116-mg.htm
- F8. ANTT, resultado Rota das Gerais: https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias/ecorodovias-vence-primeiro-leilao-rodoviario-federal-de-2026-com-19-de-desconto-e-assume-735-km-em-minas-gerais
- F9. Ministério da Fazenda, Parecer SEI 123/2025 (BR-116/BA/PE Rota dos Sertões; tabela comparativa com Rota do Zebu e Rota Sertaneja): https://www.gov.br/fazenda/pt-br/composicao/orgaos/secretaria-de-reformas-economicas/manifestacoes-em-consultas-publicas-de-orgaos-reguladores/2025/agencia-nacional-de-transportes-terrestres-antt/sei_47574434_parecer_123.pdf
- F10. ANTT, página BR-381/MG (mesmo que F1; dados de TIR, tarifa, datas)
- F13. ANTT, Estudos Econômico-Financeiros, BR-040 MG/RJ e BR-495 RJ (Concer, data-base jan/2021): https://portal.antt.gov.br/documents/20122/3435657/Lote+3+-+Estudos+Econ%C3%B4mico-Financeiros+R2.pdf/be3c77cd-178c-8233-d7e2-4084e8a8f0cc?t=1640948657110
- F14. ANTT, Voto DGS 029/2024 (BR-381/MG): https://portal.antt.gov.br/documents/498202/0/Voto+DGS+029-2024+(1).pdf/1e878da9-e5ba-c6b0-260f-a72e4a2882bc?t=1715952052400
- F15. ANTT, Estudos Econômico-Financeiros BR-364/365 GO/MG (Ecovias do Cerrado): https://www.gov.br/antt/pt-br/assuntos/rodovias/concessionarias/lista-de-concessoes/ecovias-do-cerrado/documentos-de-gestao/processo-de-licitacao/edital-de-concessao-no-01-2019-1/arquivos/estudos-de-viabilidade/estudos-economico-financeiros.pdf
- F17. ANTT, Produto 1 Estudos de Tráfego, BR-101/SC: https://portal.antt.gov.br/documents/359170/710124/Estudos+de+Tr%C3%A1fego.pdf/7c264949-2f2a-a0d6-152d-3021c0338384?t=1592842079107
- F18. ANTT, Relatório Executivo (BR-101/SC): https://portal.antt.gov.br/documents/359170/710124/Relat%C3%B3rio+Executivo.pdf/28e892bf-37e9-f2d2-8391-7da935429626?t=1592842078567 (não consegui extrair o texto; citado só como fonte de pesquisa)
- F19. Agência iNFRA, revisão do WACC (jun/2026): https://agenciainfra.com/blog/antt-propoe-revisao-de-calculo-de-taxa-wacc-de-concessoes-rodoviarias/
- F20. ANTT, Voto DAB (SEI 43366523, 22/06/2026) sobre revisão do WACC: https://agenciainfra.com/blog/wp-content/uploads/2026/06/SEI_ANTT-43366523-Voto-DAB.pdf
- F28. Dados abertos ANTT, praças de pedágio: https://dados.antt.gov.br/dataset/praca-de-pedagio
- F34. Dados abertos ANTT, volume de tráfego por praça: https://dados.antt.gov.br/dataset/volume-trafego-praca-pedagio (dicionário: https://dados.antt.gov.br/dataset/5bf70ec3-b24e-4f73-99a0-78b200f5e915/resource/5cec4e90-24d4-4a43-84e1-121a422bbcd5/download/dicionario_dados_surod_volume-de-trafego-nas-pracas-de-pedagio.pdf)
- F35. Dados abertos ANTT, tráfego equivalente: https://dados.antt.gov.br/dataset/volume-trafego-equivalente-praca-pedagio
- F36. Dados abertos ANTT, receita por praça: https://dados.antt.gov.br/dataset/receita-por-praca
- F37. Dados abertos ANTT, receita de pedágio: https://dados.antt.gov.br/dataset/receita-pedagio
- F38. Dados abertos ANTT, catálogo: https://dados.antt.gov.br/dataset

Imprensa e terceiros:
- F2. Itatiaia, vitória do Consórcio Infraestrutura MG na BR-040 BH–JF: https://www.itatiaia.com.br/politica/consorcio-infraestrutura-mg-vence-leilao-e-assume-gestao-da-br-040-entre-bh-e-juiz-de-fora/
- F3. Poder360, relicitação BR-040: https://www.poder360.com.br/infraestrutura/governo-inicia-relicitacao-da-br-040-com-leilao-nesta-5a-feira/
- F4. InfoMoney, Vinci vence Rota dos Cristais: https://www.infomoney.com.br/?p=2613144
- F5. Poder360, edital da Rota dos Cristais: https://www.poder360.com.br/infraestrutura/antt-aprova-edital-de-concessao-da-rota-dos-cristais/
- F6. Safra, análise do leilão Rota dos Cristais: https://oespecialista.safra.com.br/leilao-de-rodovias-rota-dos-cristais/
- F11. Agência iNFRA, TIR da BR-381 (jul/2022): https://agenciainfra.com/blog/antt-amplia-taxa-de-retorno-e-atualiza-data-base-de-orcamentos-para-tentar-licitar-br-381-mg/
- F12. Diário do Transporte, início da cobrança na Rota dos Cristais: https://diariodotransporte.com.br/2025/02/27/antt-autoriza-inicio-da-cobranca-de-pedagio-na-rota-dos-cristais-rodovia-br-040-go-mg/
- F16. Agência iNFRA, ANTT leva a consulta proposta de WACC (2024): https://agenciainfra.com/blog/antt-leva-a-consulta-proposta-que-pode-ampliar-taxa-de-retorno-em-concessoes-com-grandes-obras/
- F21. B3 / Atlas Público, Rota Sertaneja: https://www.b3.com.br/pt_br/noticias/ministerio-dos-transportes-e-antt-realizam-leilao-na-b3-para-a-concessao-da-rota-sertaneja.htm ; https://atlaspublico.com.br/noticias/antt-homologa-concessao-da-br-153-262-rota-sertaneja-a-way-20443 ; Rota do Zebu: https://istoedinheiro.com.br/rotas-do-brasil-vence-leilao-da-br-262-conhecida-como-rota-do-zebu
- F22. Ecorodovias, vitória na Rota das Gerais: https://www.ecorodovias.com.br/noticias/ecorodovias-vence-leilao-da-rota-das-gerais-e-abre-agenda-de-concessoes-rodoviarias-federais-de-2026/ ; Poder360: https://www.poder360.com.br/poder-infra/leilao-das-rotas-gerais-sera-em-31-de-marco/
- F23. Suno, EcoRioMinas (Rio–Gov. Valadares): https://www.suno.com.br/noticias/?p=260390 ; Diário do Transporte: https://diariodotransporte.com.br/2023/12/19/ecoriominas-passa-a-cobrar-pedagio-em-sao-francisco-do-gloria-mg-na-br-116-a-partir-de-29-de-dezembro/
- F24. Tribuna do Sertão, leilão BR-050 (2013): https://www.tribunadosertao.com.br/brasil/2013/09/18/149602-consorcio-planalto-oferece-a-menor-tarifa-e-vence-leilao-da-br-050
- F25. Poder360, edital BR-040 BH–JF: https://www.poder360.com.br/infraestrutura/antt-aprova-edital-da-br-040-mg-de-belo-horizonte-a-juiz-de-fora/
- F26. Diário do Transporte, Motiva e Fernão Dias: https://diariodotransporte.com.br/2025/12/11/motiva-vence-leilao-da-br-381-fernao-dias-e-assume-concessao-ate-2040/ ; https://diariodotransporte.com.br/2026/03/27/motiva-assume-concessao-da-br-381-fernao-dias-da-arteris-com-aval-da-antt/
- F27. Diário do Comércio, Rota das Gerais fecha o ciclo em MG: https://diariodocomercio.com.br/economia/leilao-da-rota-das-gerais-em-2026-deve-fechar-ciclo-de-leiloes-de-rodovias-federais-em-minas-diz-diretor-da-antt/
- F29. Agência iNFRA, TCU e Rota das Gerais: https://agenciainfra.com/blog/tcu-pede-mudancas-para-licitacao-da-br-116-251-mg-a-rota-das-gerais/
- F30. Agência iNFRA, risco de demanda (AP 13/2022): https://agenciainfra.com/blog/?p=11489 ; https://agenciainfra.com/blog/?p=11873
- F31. Poder360, Rota dos Cristais: https://www.poder360.com.br/poder-infra/governo-leiloa-rota-dos-cristais-entre-minas-e-goias-nesta-5a/
- F32. (mesmo que F16)
- F33. MPF, texto sobre regras de FCM (norma não identificada): https://biblioteca.mpf.mp.br/repositorio/bitstreams/ebfb27ea-9f3c-4bc6-8303-fbfc24a196ce/download
