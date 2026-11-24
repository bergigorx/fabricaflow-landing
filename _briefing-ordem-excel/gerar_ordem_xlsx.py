import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule

out = sys.argv[1]
wb = Workbook()
ws = wb.active; ws.title = "Ordem de produção"
NAVY = "0F2A43"; ORANGE = "E89A2B"
thin = Side(style="thin", color="9AA9B8"); B = Border(left=thin, right=thin, top=thin, bottom=thin)
INP = PatternFill("solid", fgColor="FFF8E1"); HEAD = PatternFill("solid", fgColor="EEF2F6")
LAB = Font(size=8, color="5A6B7B", bold=True)
for k in "ABCDEFGH": ws.column_dimensions[k].width = 16

def merge(rng):
    if ":" in rng: ws.merge_cells(rng)

def label(rng, text):
    merge(rng); c = ws[rng.split(":")[0]]; c.value = text; c.font = LAB
    c.alignment = Alignment(vertical="bottom")

def field(rng, fmt=None, height=None, wrap=False):
    merge(rng)
    cells = ws[rng] if ":" in rng else ((ws[rng],),)
    for row in cells:
        for c in row: c.border = B; c.fill = INP
    first = ws[rng.split(":")[0]]
    first.alignment = Alignment(vertical="center", wrap_text=wrap, horizontal="left")
    if fmt: first.number_format = fmt
    if height: ws.row_dimensions[first.row].height = height

def section(row, text):
    merge(f"A{row}:H{row}")
    c = ws[f"A{row}"]; c.value = text; c.font = Font(bold=True, color="FFFFFF", size=10)
    for col in "ABCDEFGH": ws[f"{col}{row}"].fill = PatternFill("solid", fgColor=NAVY)
    ws.row_dimensions[row].height = 18

def head(rng, text):
    merge(rng)
    cells = ws[rng] if ":" in rng else ((ws[rng],),)
    for row in cells:
        for c in row: c.border = B; c.fill = HEAD
    c = ws[rng.split(":")[0]]; c.value = text; c.font = Font(bold=True, size=8, color=NAVY)
    c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")

# Título
merge("A1:E1"); ws["A1"] = "ORDEM DE PRODUÇÃO"; ws["A1"].font = Font(bold=True, size=20, color=NAVY)
merge("A2:E2"); ws["A2"] = "Documento interno da produção · sem valores · preencha as células amarelas"; ws["A2"].font = Font(size=9, color="5A6B7B")
ws.row_dimensions[1].height = 30
label("F1:H1", "Nº DA OP"); field("F2:H2")
label("F3:H3", "DATA DE EMISSÃO"); field("F4:H4", "dd/mm/yyyy")
for col in "ABCDEFGH": ws[f"{col}5"].border = Border(top=Side(style="medium", color=ORANGE))

# Dados do pedido
label("A6:C6", "CLIENTE"); label("D6:E6", "Nº DO PEDIDO"); label("F6:G6", "PRAZO PROMETIDO"); label("H6", "PRIORIDADE")
field("A7:C7", height=22); field("D7:E7"); field("F7:G7", "dd/mm/yyyy"); field("H7")
label("A8:E8", "PRODUTO / DESCRIÇÃO"); label("F8:H8", "QUANTIDADE")
field("A9:E9", height=22); field("F9:H9")
label("A10:H10", "ESPECIFICAÇÕES (medidas, material, cor, acabamento, arquivo ou desenho aprovado)")
field("A11:H13", wrap=True)

# Liberação
section(15, "LIBERAÇÃO · confira antes de produzir")
items = ["Pagamento ou sinal confirmado", "Desenho / arte aprovado", "Medidas conferidas", "Material disponível"]
cols = "ABCDEFGH"
for i, t in enumerate(items):
    a, b = cols[i*2], cols[i*2+1]
    merge(f"{a}16:{b}16"); ws[f"{a}16"] = t; ws[f"{a}16"].font = Font(size=9); ws[f"{a}16"].alignment = Alignment(horizontal="center", wrap_text=True)
    field(f"{a}17:{b}17"); ws[f"{a}17"].alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[16].height = 26; ws.row_dimensions[17].height = 20
label("A18:D18", "LIBERADO POR"); label("E18:H18", "DATA DA LIBERAÇÃO")
field("A19:D19", height=22); field("E19:H19", "dd/mm/yyyy")

# Material
section(21, "MATERIAL NECESSÁRIO")
head("A22:D22", "Material"); head("E22:F22", "Quantidade"); head("G22", "Unidade"); head("H22", "Em estoque?")
for rr in range(23, 27):
    field(f"A{rr}:D{rr}"); field(f"E{rr}:F{rr}"); field(f"G{rr}"); field(f"H{rr}")
    ws[f"H{rr}"].alignment = Alignment(horizontal="center", vertical="center")

# Etapas
section(28, "ETAPAS · cada setor preenche a sua linha")
head("A29", "Setor"); head("B29:C29", "Início (data/hora)"); head("D29:E29", "Fim (data/hora)"); head("F29", "Operador"); head("G29:H29", "Parou? Motivo (1 palavra)")
for rr in range(30, 35):
    field(f"A{rr}"); field(f"B{rr}:C{rr}", "dd/mm/yyyy hh:mm"); field(f"D{rr}:E{rr}", "dd/mm/yyyy hh:mm"); field(f"F{rr}"); field(f"G{rr}:H{rr}")

# Conferência
section(36, "CONFERÊNCIA FINAL E ENTREGA")
for i, t in enumerate(["Quantidade conferida", "Acabamento conferido", "Embalado / identificado", "Cliente avisado"]):
    a, b = cols[i*2], cols[i*2+1]
    merge(f"{a}37:{b}37"); ws[f"{a}37"] = t; ws[f"{a}37"].font = Font(size=9); ws[f"{a}37"].alignment = Alignment(horizontal="center")
    field(f"{a}38:{b}38"); ws[f"{a}38"].alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[38].height = 20
label("A39:C39", "DATA DE ENTREGA"); label("D39:F39", "ENTREGUE NO PRAZO? (automático)"); label("G39:H39", "DIAS DE ATRASO (automático)")
field("A40:C40", "dd/mm/yyyy", height=22)
for rng in ("D40:F40", "G40:H40"):
    merge(rng)
    for row in ws[rng]:
        for c in row: c.border = B
ws["D40"] = '=IF(OR(A40="",F7=""),"",IF(A40<=F7,"Sim","Não"))'; ws["G40"] = '=IF(OR(A40="",F7=""),"",MAX(0,A40-F7))'
for c in ("D40", "G40"): ws[c].font = Font(bold=True, color=NAVY); ws[c].alignment = Alignment(horizontal="center", vertical="center")
label("A41:H41", "OBSERVAÇÕES / RETRABALHO")
field("A42:H44", wrap=True)

# Assinaturas
for rng, t in (("A47:C47", "Liberação (gestor)"), ("D47:F47", "Responsável da produção"), ("G47:H47", "Conferência final")):
    merge(rng); c = ws[rng.split(":")[0]]; c.value = t; c.font = Font(size=8, color="5A6B7B"); c.alignment = Alignment(horizontal="center")
    for cc in ws[rng][0]: cc.border = Border(top=Side(style="thin", color=NAVY))
merge("A49:H49"); ws["A49"] = "Modelo grátis do FábricaFlow · fabricaflow.online/modelos/ordem-de-producao/"
ws["A49"].font = Font(size=8, color="7B8A99"); ws["A49"].alignment = Alignment(horizontal="center")

# Listas
dv_pri = DataValidation(type="list", formula1='"Normal,Alta,Urgente"', allow_blank=True); ws.add_data_validation(dv_pri); dv_pri.add("H7")
dv_sn = DataValidation(type="list", formula1='"Sim,Não"', allow_blank=True); ws.add_data_validation(dv_sn)
for rng in ("A17:H17", "A38:H38", "H23:H26"): dv_sn.add(rng)
ws.conditional_formatting.add("H7", FormulaRule(formula=['$H$7="Urgente"'], font=Font(bold=True, color="C00000")))
ws.conditional_formatting.add("D40:F40", FormulaRule(formula=['$D$40="Não"'], font=Font(bold=True, color="C00000")))

# Exemplo
ex = wb.create_sheet("Exemplo preenchido")
ex.column_dimensions["A"].width = 30; ex.column_dimensions["B"].width = 70
ex["A1"] = "Exemplo fictício de como preencher"; ex["A1"].font = Font(bold=True, size=14, color=NAVY)
rows = [("Nº da OP", "1001"), ("Cliente", "Cliente A (exemplo)"), ("Produto", "Produto 1 (exemplo)"), ("Quantidade", "20"),
        ("Prioridade", "Alta"), ("Prazo prometido", "14/11/2026"),
        ("Liberação", "Pagamento confirmado; desenho aprovado; medidas conferidas; material disponível"),
        ("Etapas", "Corte (3/11 08:00 a 3/11 15:00); Dobra (4/11 08:00 a 4/11 12:00); Solda (5/11 08:00 a 6/11 10:00)"),
        ("Parou?", "Solda: 'material' (1 dia)"), ("Entrega", "12/11/2026: Sim, no prazo; 0 dias de atraso")]
for i, (a, b) in enumerate(rows, 3):
    ex[f"A{i}"] = a; ex[f"A{i}"].font = Font(bold=True); ex[f"B{i}"] = b; ex[f"B{i}"].alignment = Alignment(wrap_text=True, vertical="top")
ex.merge_cells("A14:B16")
ex["A14"] = "Os valores deste exemplo são fictícios. Para cada pedido novo, copie a aba 'Ordem de produção' (clique com o botão direito na aba e escolha Mover ou copiar) e preencha uma ordem por pedido."
ex["A14"].alignment = Alignment(wrap_text=True, vertical="top"); ex["A14"].font = Font(italic=True, color="5A6B7B")

# Impressão
ws.page_setup.orientation = "portrait"; ws.page_setup.paperSize = ws.PAPERSIZE_A4
ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 1; ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_area = "A1:H49"; ws.page_margins.left = ws.page_margins.right = 0.4
ws.page_margins.top = ws.page_margins.bottom = 0.4
ws.sheet_view.showGridLines = False
wb.save(out)
