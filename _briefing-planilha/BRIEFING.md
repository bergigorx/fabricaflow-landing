# Briefing: página "Planilha de controle de produção grátis" (Marketing -> Landing)

Status: PARA PREVIEW. Nada vai para produção sem o "aprovado" do Igor (regra dele para o site).
Aprovado por ele: criar a página e mandar um resumo/print do resultado antes de publicar.

## Objetivo
Capturar quem busca "planilha de controle de produção" / "controle de produção" e ainda usa planilha ou WhatsApp, e levar à demonstração. As buscas por termos específicos (sistema para marcenaria, controle de produção para serralheria, fila de produção) têm volume muito baixo no Google Trends; o termo amplo e a planilha atraem mais gente. O arquivo é um ativo útil de verdade, sem propaganda dentro da planilha além de 1 linha na aba "Como usar".

## Arquivo
`_briefing-planilha/modelo-controle-de-producao-fabricaflow.xlsx` (gerado por `gerar_planilha.py`, na mesma pasta). Publicar em `/modelos/planilha-controle-de-producao/modelo-controle-de-producao-fabricaflow.xlsx`.
Abas: Como usar, Setores, Pedidos, Fila por setor, Estoque mínimo, Indicadores (a aba Listas fica oculta). Fórmulas conferidas por recálculo no LibreOffice. Dados de exemplo são fictícios e estão marcados "(exemplo)".
Não foi testada no Excel nem no Google Planilhas; não afirme compatibilidade além de "arquivo .xlsx".

## Página
- URL: `/modelos/planilha-controle-de-producao/` (index.html no padrão do site).
- Download direto, sem formulário nem cadastro (menos atrito e sem coleta de dados). Botão primário "Baixar a planilha (.xlsx)". Medir cliques com o Cloudflare Web Analytics se já houver evento; se não houver, não criar nada novo sem me avisar.
- Title (53): `Planilha de controle de produção grátis | FábricaFlow`
- Meta description (<=155): `Planilha grátis de controle de produção para fábrica pequena: pedidos, fila por setor, estoque mínimo e indicadores. Arquivo .xlsx, sem cadastro.`
- H1: `Planilha de controle de produção grátis para fábrica pequena`
- Resposta rápida (caixa no topo, padrão do site): "Esta planilha grátis controla pedidos, fila por setor, estoque mínimo e três indicadores da semana. Você preenche uma linha por pedido, escolhe o status em uma lista e vê quais setores estão sobrecarregados e quais insumos precisam ser pedidos. Funciona para fábrica pequena que ainda controla produção em papel, WhatsApp ou planilha solta."
- Seções (H2), nesta ordem:
  1. "O que vem na planilha" (lista das 5 abas, 1 linha cada):
     - Pedidos: uma linha por pedido, com prioridade (normal, alta, urgente), setor, status, prazo prometido e cálculo automático de atraso.
     - Fila por setor: quantos pedidos aguardam, estão em produção, parados ou prontos para o próximo setor, e a carga prometida contra a capacidade da semana.
     - Estoque mínimo: calcula estoque de segurança e ponto de reposição e avisa "Pedir agora".
     - Indicadores: entregas no prazo, carga do gargalo contra capacidade, pedidos parados e urgentes em aberto.
     - Setores: seus setores e as horas de capacidade de cada um (você edita).
  2. "Como usar em 4 passos" (os mesmos da aba Como usar).
  3. "As duas fórmulas do estoque mínimo": estoque de segurança = consumo por dia x atraso comum do fornecedor; ponto de reposição = consumo por dia x prazo de entrega + estoque de segurança. Link interno para o artigo /blog/estoque-minimo-fabrica/.
  4. "Quando a planilha deixa de bastar" (neutro, sem forçar): muitos pedidos ao mesmo tempo, várias pessoas editando, pedidos que chegam pelo WhatsApp e precisam ser digitados, perda de histórico. Aí o controle passa para um sistema: link para a home e para /#contato (demonstração de 20 minutos).
  5. Perguntas frequentes (3): "A planilha é grátis?" (Sim, sem cadastro e sem prazo.) / "Em que formato vem?" (.xlsx, formato aberto por Excel, LibreOffice e Google Planilhas.) / "Posso adaptar aos meus setores?" (Sim, edite os nomes e as horas na aba Setores; os dados de exemplo são fictícios e devem ser apagados.)
- Assinatura/rodapé padrão do site (Igor, CNPJ). Schema: WebPage + BreadcrumbList + FAQPage (as 3 perguntas). Sem Product/SoftwareApplication.
- Chamada final: "Quer ver isso dentro de um sistema? Agende uma demonstração de 20 minutos." (padrão do site).

## Regras de conteúdo (as mesmas do site)
Sem ERP/nota fiscal como funcionalidade nossa; chatbot não é citado aqui; não dizer que há clientes usando; nada de "o melhor"/"o único"; nada de oferta ou texto só para robôs.

## Integração
- Linkar a página no rodapé ou na seção de recursos/blog (onde fizer sentido) e a partir do artigo de estoque mínimo e do de controle de produção.
- sitemap.xml, llms.txt (seção Artigos ou nova seção "Modelos grátis"), cópia .md pelo script gerar_markdown.py, `<link rel="alternate" type="text/markdown">`.
- IndexNow só depois do aprovado.

## Entrega para o Igor aprovar
Em branch/preview (não em main). Commitar prints em `_previa/` no branch: desktop (1440px) e mobile (390px) da página inteira, mais um print da aba "Fila por setor" e da aba "Pedidos" da planilha aberta (pode ser o PDF/print do LibreOffice). Me avisar com o resumo; eu levo ao Igor.
