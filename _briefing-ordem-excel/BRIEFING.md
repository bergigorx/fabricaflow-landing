# Briefing: versão em Excel do modelo de ordem de produção (Marketing -> Landing)

Status: PARA PREVIEW em branch. Nada vai para main sem o "aprovado" do Igor (ele aprovou a criação da versão em Excel).

## Por quê
Search Console (26/10 a 22/11): a página /modelos/ordem-de-producao/ é a mais vista (46 impressões, 5 cliques, posição média 3,7; posição 1 para "modelo ordem de produção"). "ordem de produção pdf" aparece na posição 40. Quem busca modelo costuma querer também a versão editável em Excel. Aproveitar o impulso sem mudar o que já funciona.

## Arquivo
`_briefing-ordem-excel/modelo-ordem-de-producao-fabricaflow.xlsx` (gerado por gerar_ordem_xlsx.py, na mesma pasta). Publicar em `/modelos/ordem-de-producao/modelo-ordem-de-producao-fabricaflow.xlsx`.
- Aba "Ordem de produção": mesma estrutura do PDF (cliente, pedido, prazo, prioridade em lista, produto, quantidade, especificações, 4 itens de liberação em lista Sim/Não, material, 5 linhas de etapas, conferência final, entrega, observações, assinaturas). Impressão em A4, 1 página.
- Cálculo automático de "entregue no prazo?" e "dias de atraso" a partir de prazo prometido e data de entrega (testado por recálculo no LibreOffice: prazo 14/11 e entrega 17/11 dão "Não" e 3 dias).
- Aba "Exemplo preenchido": exemplo fictício (marcado), com a instrução de copiar a aba para cada pedido.
- Não testado no Excel nem no Google Planilhas; não afirmar compatibilidade além de ".xlsx".

## Mudanças na página /modelos/ordem-de-producao/ (manter o resto)
- Title (49): `Modelo de ordem de produção grátis (PDF e Excel)` (+ " | FábricaFlow" se o padrão do site couber em 60; se passar, manter sem).
- Meta (141): `Modelo grátis de ordem de produção em PDF para imprimir e em Excel para preencher: liberação, material, etapas por setor e entrega. Sem cadastro.`
- Linha fina: "PDF para imprimir e planilha em Excel para preencher no computador. Download direto, sem cadastro."
- Resposta rápida: acrescentar ao fim da frase do modelo "Há uma versão em PDF para imprimir e outra em Excel para preencher no computador."
- Dois botões lado a lado (mesmo estilo): "Baixar o modelo (PDF)" e "Baixar em Excel (.xlsx)". O botão do PDF continua o principal; o do Excel pode ser secundário.
- Seção "O que vem no modelo": após a imagem, um parágrafo: "A versão em Excel tem a mesma estrutura, com listas para prioridade e para as conferências (Sim ou Não) e cálculo automático de entrega no prazo e dias de atraso. Uma aba traz um exemplo preenchido, com dados fictícios. Para cada pedido novo, copie a aba e preencha uma ordem por pedido."
- FAQ "Posso editar o modelo?": trocar a resposta por: "Sim. Além do PDF para imprimir e preencher à mão, há uma versão em Excel (.xlsx) para preencher no computador. Para acompanhar vários pedidos ao mesmo tempo, use também a planilha de controle de produção." (link para /modelos/planilha-controle-de-producao/). Atualizar o FAQPage JSON-LD igual ao texto visível.
- Bloco final "Baixe também": incluir o Excel.
- Nova pergunta (4ª) no FAQ e no JSON-LD: "Em que formato vem o modelo?" -> "Em PDF de uma página para imprimir e em arquivo Excel (.xlsx) para preencher no computador. Os dois são grátis, sem cadastro."
- dateModified/atualizado em: data da publicação.

## Integração
Página da planilha: frase com link já existente, acrescentar "(PDF ou Excel)". llms.txt (seção Modelos grátis): citar as duas versões. Cópia .md, sitemap lastmod. IndexNow só depois do aprovado.

## Regras
Mesmas do site: sem afirmar clientes, sem "o melhor", sem ERP/nota fiscal como função nossa, sem texto só para robôs.

## Entrega
Em branch/preview, prints em `_previa/` (desktop 1440 e mobile 390) e, se possível, uma captura da planilha aberta (aba "Ordem de produção"). Eu levo ao Igor.
