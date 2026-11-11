import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter

out = sys.argv[1]
wb = Workbook()
NAVY = "0F2A43"
hdr_fill = PatternFill("solid", fgColor=NAVY)
hdr_font = Font(bold=True, color="FFFFFF", name="Calibri", size=11)
inp_fill = PatternFill("solid", fgColor="FFF8E1")
thin = Side(style="thin", color="BFC9D4")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

def header(ws, row, labels, widths=None):
    for i, t in enumerate(labels, 1):
        c = ws.cell(row=row, column=i, value=t)
        c.fill = hdr_fill; c.font = hdr_font; c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 32
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w

# ---------- Como usar ----------
ws = wb.active; ws.title = "Como usar"
ws.column_dimensions["A"].width = 110
lines = [
 ("Modelo grátis de controle de produção", "title"),
 ("Feito pelo FábricaFlow para a pequena fábrica que recebe pedidos (inclusive pelo WhatsApp) e quer saber, todo dia, o que está em cada setor.", None),
 ("", None),
 ("Como usar, em 4 passos", "h"),
 ("1. Aba 'Setores': escreva os nomes dos seus setores (corte, dobra, solda, montagem, pintura...) e a capacidade de horas de cada um na semana.", None),
 ("2. Aba 'Pedidos': uma linha por pedido. Preencha as colunas amarelas. Prioridade, setor e status são listas: clique na célula e escolha.", None),
 ("3. Aba 'Fila por setor': mostra sozinha quantos pedidos há em cada situação e se a carga prometida passa da capacidade (célula vermelha = acima de 100%).", None),
 ("4. Aba 'Estoque mínimo': informe consumo por dia, prazo do fornecedor e atraso comum. A planilha calcula o ponto de reposição e avisa 'Pedir agora'.", None),
 ("", None),
 ("Regras simples que fazem funcionar", "h"),
 ("• Só entra na fila o pedido que pode ser feito: desenho aprovado, medidas conferidas, material disponível e prazo registrado. Se faltar algo, use o status 'Aguardando liberação'.", None),
 ("• Quem executa atualiza: o operador muda o status e, se parar, escreve o motivo em uma palavra. O gestor só olha.", None),
 ("• Reveja os três números toda segunda-feira (aba 'Indicadores'): entregas no prazo, carga contra capacidade e tempo de espera.", None),
 ("", None),
 ("Os valores que já estão preenchidos são exemplos fictícios. Apague e use os seus.", "note"),
 ("Quando a planilha deixar de dar conta (muitos pedidos, vários usuários), o FábricaFlow faz esse controle no sistema: fabricaflow.online", "note"),
]
for r, (t, kind) in enumerate(lines, 1):
    c = ws.cell(row=r, column=1, value=t)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    if kind == "title": c.font = Font(bold=True, size=16, color=NAVY)
    elif kind == "h": c.font = Font(bold=True, size=12, color=NAVY)
    elif kind == "note": c.font = Font(italic=True, color="5A6B7B")

# ---------- Setores ----------
st = wb.create_sheet("Setores")
header(st, 1, ["Setor (edite os nomes)", "Capacidade na semana (horas)"], [34, 28])
setores = [("Corte", 40), ("Dobra", 30), ("Solda", 32), ("Acabamento", 24), ("Expedição", 16)]
for i, (n, h) in enumerate(setores, 2):
    st.cell(row=i, column=1, value=n).fill = inp_fill
    st.cell(row=i, column=2, value=h).fill = inp_fill
    for col in (1, 2): st.cell(row=i, column=col).border = border
# lists
lst = wb.create_sheet("Listas")
for i, v in enumerate(["Normal", "Alta", "Urgente"], 1): lst.cell(row=i, column=1, value=v)
stat = ["Aguardando liberação", "Aguardando", "Em produção", "Parado", "Pronto para o próximo setor", "Entregue"]
for i, v in enumerate(stat, 1): lst.cell(row=i, column=2, value=v)
lst.sheet_state = "hidden"

# ---------- Pedidos ----------
pd = wb.create_sheet("Pedidos", 1)
cols = ["Nº do pedido", "Data do pedido", "Cliente", "Produto", "Quantidade", "Prioridade", "Setor atual",
        "Status", "Motivo da parada (1 palavra)", "Horas estimadas", "Prazo prometido", "Data de entrega",
        "Entregue no prazo?", "Dias de atraso"]
header(pd, 1, cols, [12, 14, 24, 28, 12, 13, 16, 26, 26, 12, 15, 15, 15, 12])
import datetime as dt
ex = [
 (1001, dt.date(2026,11,3), "Cliente A (exemplo)", "Produto 1 (exemplo)", 20, "Normal", "Solda", "Em produção", "", 12, dt.date(2026,11,14), None),
 (1002, dt.date(2026,11,4), "Cliente B (exemplo)", "Produto 2 (exemplo)", 8, "Urgente", "Corte", "Aguardando", "", 6, dt.date(2026,11,10), None),
 (1003, dt.date(2026,11,5), "Cliente C (exemplo)", "Produto 3 (exemplo)", 50, "Alta", "Dobra", "Parado", "material", 18, dt.date(2026,11,17), None),
 (1004, dt.date(2026,10,28), "Cliente D (exemplo)", "Produto 4 (exemplo)", 10, "Normal", "Expedição", "Entregue", "", 9, dt.date(2026,11,6), dt.date(2026,11,5)),
 (1005, dt.date(2026,10,29), "Cliente E (exemplo)", "Produto 5 (exemplo)", 4, "Normal", "Expedição", "Entregue", "", 5, dt.date(2026,11,6), dt.date(2026,11,9)),
]
N = 500
for r in range(2, N+1):
    for c in range(1, 13):
        cell = pd.cell(row=r, column=c); cell.border = border; cell.fill = inp_fill
    pd.cell(row=r, column=2).number_format = "dd/mm/yyyy"
    pd.cell(row=r, column=11).number_format = "dd/mm/yyyy"
    pd.cell(row=r, column=12).number_format = "dd/mm/yyyy"
    m = pd.cell(row=r, column=13, value=f'=IF(L{r}="","",IF(L{r}<=K{r},"Sim","Não"))')
    n = pd.cell(row=r, column=14, value=f'=IF(L{r}="","",MAX(0,L{r}-K{r}))')
    for c in (m, n): c.border = border; c.alignment = Alignment(horizontal="center")
for i, row in enumerate(ex, 2):
    for c, v in enumerate(row, 1):
        if v is not None: pd.cell(row=i, column=c, value=v)
dv1 = DataValidation(type="list", formula1="=Listas!$A$1:$A$3", allow_blank=True)
dv2 = DataValidation(type="list", formula1="=Setores!$A$2:$A$11", allow_blank=True)
dv3 = DataValidation(type="list", formula1="=Listas!$B$1:$B$6", allow_blank=True)
for dv, col in ((dv1, "F"), (dv2, "G"), (dv3, "H")):
    pd.add_data_validation(dv); dv.add(f"{col}2:{col}{N}")
pd.freeze_panes = "C2"
pd.auto_filter.ref = f"A1:N{N}"
red = PatternFill("solid", bgColor="F8CBAD", fgColor="F8CBAD")
pd.conditional_formatting.add(f"A2:N{N}", FormulaRule(formula=['$F2="Urgente"'], font=Font(bold=True, color="C00000")))
pd.conditional_formatting.add(f"H2:H{N}", FormulaRule(formula=['$H2="Parado"'], fill=red))
pd.conditional_formatting.add(f"M2:M{N}", FormulaRule(formula=['$M2="Não"'], fill=red))

# ---------- Fila por setor ----------
fl = wb.create_sheet("Fila por setor", 2)
header(fl, 1, ["Setor", "Aguardando", "Em produção", "Parado", "Pronto p/ próximo", "Carga prometida (h)", "Capacidade (h/semana)", "Carga ÷ capacidade"],
       [24, 14, 14, 12, 18, 20, 22, 20])
for i in range(2, 12):
    s = i
    fl.cell(row=i, column=1, value=f'=IF(Setores!A{s}="","",Setores!A{s})')
    fl.cell(row=i, column=2, value=f'=IF($A{i}="","",COUNTIFS(Pedidos!$G$2:$G${N},$A{i},Pedidos!$H$2:$H${N},"Aguardando"))')
    fl.cell(row=i, column=3, value=f'=IF($A{i}="","",COUNTIFS(Pedidos!$G$2:$G${N},$A{i},Pedidos!$H$2:$H${N},"Em produção"))')
    fl.cell(row=i, column=4, value=f'=IF($A{i}="","",COUNTIFS(Pedidos!$G$2:$G${N},$A{i},Pedidos!$H$2:$H${N},"Parado"))')
    fl.cell(row=i, column=5, value=f'=IF($A{i}="","",COUNTIFS(Pedidos!$G$2:$G${N},$A{i},Pedidos!$H$2:$H${N},"Pronto para o próximo setor"))')
    fl.cell(row=i, column=6, value=f'=IF($A{i}="","",SUMIFS(Pedidos!$J$2:$J${N},Pedidos!$G$2:$G${N},$A{i},Pedidos!$H$2:$H${N},"<>Entregue"))')
    fl.cell(row=i, column=7, value=f'=IF($A{i}="","",Setores!B{s})')
    c = fl.cell(row=i, column=8, value=f'=IF(OR($A{i}="",G{i}="",G{i}=0),"",F{i}/G{i})')
    c.number_format = "0%"
    for col in range(1, 9):
        fl.cell(row=i, column=col).border = border
        if col > 1: fl.cell(row=i, column=col).alignment = Alignment(horizontal="center")
fl.conditional_formatting.add("H2:H11", FormulaRule(formula=['AND(ISNUMBER(H2),H2>1)'], fill=PatternFill("solid", bgColor="F4B084", fgColor="F4B084"), font=Font(bold=True, color="9C0006")))
fl.conditional_formatting.add("D2:D11", FormulaRule(formula=['AND(ISNUMBER(D2),D2>0)'], fill=red))
fl.cell(row=13, column=1, value="Célula vermelha em 'Carga ÷ capacidade' = mais trabalho prometido do que o setor consegue fazer na semana. Antes de prometer novo prazo, decida: renegociar, terceirizar ou hora extra.").alignment = Alignment(wrap_text=True)
fl.merge_cells("A13:H14")
fl.cell(row=13, column=1).font = Font(italic=True, color="5A6B7B")

# ---------- Estoque mínimo ----------
es = wb.create_sheet("Estoque mínimo", 3)
header(es, 1, ["Insumo", "Unidade", "Consumo médio por dia", "Prazo do fornecedor (dias)", "Atraso comum (dias)",
               "Estoque de segurança", "Ponto de reposição", "Saldo atual", "Situação"], [28, 10, 16, 18, 16, 16, 16, 14, 16])
exe = [("Insumo 1 (exemplo)", "kg", 120, 5, 3, 1200), ("Insumo 2 (exemplo)", "kg", 18, 7, 4, 150), ("Insumo 3 (exemplo)", "un", 4, 10, 5, 70)]
for i in range(2, 102):
    for c in range(1, 6): es.cell(row=i, column=c).fill = inp_fill
    es.cell(row=i, column=8).fill = inp_fill
    es.cell(row=i, column=6, value=f'=IF(OR(C{i}="",E{i}=""),"",C{i}*E{i})')
    es.cell(row=i, column=7, value=f'=IF(OR(C{i}="",D{i}="",F{i}=""),"",C{i}*D{i}+F{i})')
    es.cell(row=i, column=9, value=f'=IF(OR(G{i}="",H{i}=""),"",IF(H{i}<=G{i},"Pedir agora","OK"))')
    for c in range(1, 10): es.cell(row=i, column=c).border = border
for i, row in enumerate(exe, 2):
    for c, v in enumerate(row[:5], 1): es.cell(row=i, column=c, value=v)
    es.cell(row=i, column=8, value=row[5])
es.conditional_formatting.add("I2:I101", FormulaRule(formula=['$I2="Pedir agora"'], fill=red, font=Font(bold=True, color="9C0006")))
es.freeze_panes = "B2"
es.cell(row=104, column=1, value="Estoque de segurança = consumo por dia × atraso comum do fornecedor. Ponto de reposição = consumo por dia × prazo de entrega + estoque de segurança. Quando o saldo chega ao ponto de reposição, o pedido de compra sai no mesmo dia.").alignment = Alignment(wrap_text=True)
es.merge_cells("A104:I106")
es.cell(row=104, column=1).font = Font(italic=True, color="5A6B7B")

# ---------- Indicadores ----------
ind = wb.create_sheet("Indicadores", 4)
ind.column_dimensions["A"].width = 46; ind.column_dimensions["B"].width = 20; ind.column_dimensions["C"].width = 70
header(ind, 1, ["Indicador da semana", "Valor", "Como ler"])
rows = [
 ("Entregas no prazo", f'=IFERROR(COUNTIF(Pedidos!M2:M{N},"Sim")/(COUNTIF(Pedidos!M2:M{N},"Sim")+COUNTIF(Pedidos!M2:M{N},"Não")),"")', "0%",
  "Porcentagem de pedidos entregues até a data prometida. Para cada atraso, anote em que setor o pedido ficou parado."),
 ("Carga do gargalo ÷ capacidade", "=IFERROR(MAX('Fila por setor'!H2:H11),\"\")", "0%",
  "A maior carga entre os setores. Acima de 100%, não prometa novo prazo antes de decidir o que fazer com o excesso."),
 ("Pedidos parados agora", f'=COUNTIF(Pedidos!H2:H{N},"Parado")', "0",
  "Pedidos com status 'Parado'. Veja o motivo na aba Pedidos e resolva o mais frequente primeiro."),
 ("Pedidos urgentes em aberto", f'=COUNTIFS(Pedidos!F2:F{N},"Urgente",Pedidos!H2:H{N},"<>Entregue",Pedidos!A2:A{N},"<>")', "0",
  "Se passar de um ou dois por dia, a urgência virou regra e a fila perde o sentido."),
 ("Tempo de espera entre setores (horas) - preencha à mão", None, "0",
  "Quanto tempo o pedido ficou pronto, esperando o próximo setor. Se a espera é maior do que o tempo de trabalho, o problema é a fila, não a máquina."),
]
for i, (n, f, fmt, how) in enumerate(rows, 2):
    ind.cell(row=i, column=1, value=n)
    c = ind.cell(row=i, column=2, value=f); c.number_format = fmt
    if f is None: c.fill = inp_fill
    ind.cell(row=i, column=3, value=how).alignment = Alignment(wrap_text=True, vertical="top")
    for col in (1, 2, 3): ind.cell(row=i, column=col).border = border
    ind.row_dimensions[i].height = 46
    ind.cell(row=i, column=2).alignment = Alignment(horizontal="center", vertical="center")
    ind.cell(row=i, column=1).alignment = Alignment(vertical="center", wrap_text=True)
wb.move_sheet("Setores", offset=-(wb.sheetnames.index("Setores") - 1))
wb.save(out)
