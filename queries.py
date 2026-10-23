# ==========================================
# QUERIES SQL (fonte única: usadas por baixar_dados.py e tirm_peltmg.py)
# ==========================================
QUERIES = {
    "receita": """
        SELECT vrf.id_empreendimento, vrf.id_cenario, vrf.ano_corrente, vrf.receita_ano, 'Ferro' AS modal
        FROM cenario_recomendado_2.vw_receita_ferro vrf 
        UNION ALL
        SELECT vrr.id_empreendimento, vrr.id_cenario, vrr.ano_corrente, vrr.receita_ano, 'Rodo' AS modal
        FROM cenario_recomendado_2.vw_receita_rodo vrr 
        UNION ALL
        SELECT vrh.id_empreendimento, vrh.id_cenario, vrh.ano_corrente, vrh.receita_ano, 'Hidro' AS modal
        FROM cenario_recomendado_2.vw_receita_hidro vrh;
    """,
    "custo": """
        SELECT vc.id_empreendimento, vc.id_cenario, SUM(vc.valor_adotado) as custo_final
        FROM cenario_recomendado_2.vw_custo_economico vc
        GROUP BY vc.id_empreendimento, vc.id_cenario
    """,
    "emps_esperados": """
        SELECT vc.id_empreendimento, 
        10 as id_cenario
        FROM carteira.vw_empreendimento ve 
        JOIN cenarios.mvw_cenario_otimizado_3 vc ON ve.id_empreendimento = vc.id_empreendimento 
        WHERE ve.id_setor in (1,2,3) and ve.status_empreendimento <= 8 
          AND ve.id_grupo_modelagem in (1,2) 
          AND ve.ids_intervencoes && array[6, 49, 25, 37, 44, 14]
          AND NOT (ve.id_setor = 2 AND ve.id_nat_empreendimento = 1)
          AND ve.id_empreendimento NOT in (1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1993, 1995) -- light 
    """,
    "tir_infra": """
        SELECT id_empreendimento, id_cenario, tirm
        FROM financeiro.resumo_financeiro
    """,
    "emp": """
        SELECT * FROM carteira.vw_empreendimento
    """,
    "capex_opex": """
        SELECT  
            vf.id_empreendimento, vf.id_cenario,
            SUM(CASE WHEN vf.id_custo_economico = 1 THEN vf.valor_adotado ELSE 0 END) AS capex,
            SUM(CASE WHEN vf.id_custo_economico = 2 THEN vf.valor_adotado ELSE 0 END) AS opex
        FROM cenario_recomendado_2.vw_custo_economico vf
        GROUP BY vf.id_empreendimento, vf.id_cenario
    """,
    "receita_infra": """
        SELECT * FROM financeiro.vw_e06a_receita_ferro
        UNION ALL
        SELECT * FROM financeiro.vw_e06b_receita_hidro
        UNION ALL
        SELECT * FROM financeiro.vw_e06d_receita_rodo;
    """,
    "receita_codemge": """
        SELECT id_empreendimento, id_cenario, SUM(receita_ano) as receita_global_codemge
        FROM cenario_recomendado_2.vw_receita_ferro
        GROUP BY id_empreendimento, id_cenario
        UNION ALL
        SELECT id_empreendimento, id_cenario, SUM(receita_ano) as receita_global_codemge
        FROM cenario_recomendado_2.vw_receita_rodo
        GROUP BY id_empreendimento, id_cenario
        UNION ALL
        SELECT id_empreendimento, id_cenario, SUM(receita_ano) as receita_global_codemge
        FROM cenario_recomendado_2.vw_receita_hidro
        GROUP BY id_empreendimento, id_cenario;
    """,
    "ferroviario_passageiro": """
    SELECT 
  def.id_empreendimento,
  def.id_cenario,
  ve.nome_empreendimento,
  ve.id_setor,
  ve.setor,
  ve.natureza_empreendimento,
  ve.numero_obras,
  ve.descr_status_empreendimento,
  ve.esfera_acao,
  ve.intervencao_principal,
  ve.grupo_modelagem,
  ve.data_inicio,
  ve.data_conclusao,
  NULL AS vpl,
  NULL AS tirm_infra,
  def.tir*100 AS tirm_codemge,
  NULL AS diff,
  def.capex,
  def.opex,
  NULL AS receita_seinfra,
  def.receita AS receita_codemge
FROM carteira.vw_empreendimento ve 
LEFT JOIN financeiro.dados_externos_financeiros def  ON ve.id_empreendimento = def.id_empreendimento 
WHERE ve.id_nat_empreendimento = 1 and ve.id_setor = 2 AND def.id_empreendimento IS NOT NULL and tir IS NOT NULL 
    """,
    "aero_duto": """
    select
  def.id_empreendimento,
  def.id_cenario,
  ve.nome_empreendimento,
  ve.id_setor,
  ve.setor,
  ve.natureza_empreendimento,
  ve.numero_obras,
  ve.descr_status_empreendimento,
  ve.esfera_acao,
  ve.intervencao_principal,
  ve.grupo_modelagem,
  ve.data_inicio,
  ve.data_conclusao,
  NULL AS vpl,
  NULL AS tirm_infra,
  def.tir*100 AS tirm_codemge,
  NULL AS diff,
  def.capex,
  def.opex,
  NULL AS receita_seinfra,
  def.receita AS receita_codemge
FROM carteira.vw_empreendimento ve 
LEFT JOIN financeiro.dados_externos_financeiros def  ON ve.id_empreendimento = def.id_empreendimento 
WHERE ve.id_setor in (5,6) AND def.id_empreendimento IS NOT NULL and tir IS NOT NULL 
    """,
    "concessao_light": """
    SELECT 
  def.id_empreendimento,
  def.id_cenario,
  ve.nome_empreendimento,
  ve.id_setor,
  ve.setor,
  ve.natureza_empreendimento,
  ve.numero_obras,
  ve.descr_status_empreendimento,
  ve.esfera_acao,
  ve.intervencao_principal,
  ve.grupo_modelagem,
  ve.data_inicio,
  ve.data_conclusao,
  NULL AS vpl,
  NULL AS tirm_infra,
  def.tir*100 AS tirm_codemge,
  NULL AS diff,
  def.capex,
  def.opex,
  NULL AS receita_seinfra,
  def.receita AS receita_codemge
FROM carteira.vw_empreendimento ve 
LEFT JOIN financeiro.dados_externos_financeiros def  ON ve.id_empreendimento = def.id_empreendimento 
WHERE def.id_empreendimento in (1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1993, 1995)
    """
}
