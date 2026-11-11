# Briefing 2: página "Modelo de ordem de produção grátis" (PDF para imprimir)

Status: PARA PREVIEW em branch. Nada vai para main sem o "aprovado" do Igor.
Mesma estrutura e padrão da página /modelos/planilha-controle-de-producao/ (já publicada).

## Arquivos (nesta pasta)
- `modelo-ordem-de-producao-fabricaflow.pdf`: PDF A4, 1 página, para imprimir e preencher à mão. Publicar em `/modelos/ordem-de-producao/modelo-ordem-de-producao-fabricaflow.pdf`.
- `previa-ordem.png`: imagem da página do PDF para usar na página (copiar para /img/ em .webp otimizado, com alt descritivo).
- `ordem.html`: fonte do PDF (para ajustes futuros).

## Página
- URL: `/modelos/ordem-de-producao/` (index.html no padrão do site). Download direto, sem formulário. Botão "Baixar o modelo (PDF)".
- Title (54): `Modelo de ordem de produção grátis (PDF para imprimir)`
- Meta (131): `Modelo grátis de ordem de produção em PDF para imprimir: liberação, material, etapas por setor e entrega. Uma página, sem cadastro.`
- H1: `Modelo de ordem de produção grátis para fábrica pequena`
- Linha fina: "PDF de uma página para imprimir e preencher. Download direto, sem cadastro."
- Resposta rápida: "Ordem de produção (OP) é o documento que leva o pedido para o chão de fábrica: diz o que produzir, em que quantidade, com que especificação, para quando e por quais setores. Este modelo grátis, em PDF de uma página para imprimir, tem campos de liberação, material necessário, etapas por setor, conferência final e entrega, sem valores."
- Seções (H2), nesta ordem:
  1. "O que é uma ordem de produção" (2 a 3 frases; mesmo conceito do artigo pilar).
  2. "O que deve ter uma ordem de produção" (lista: número da OP e data; cliente e pedido; produto, quantidade e especificações; prioridade e prazo; critérios de liberação (pagamento, desenho aprovado, medidas, material); material necessário; etapas por setor com início, fim, operador e motivo de parada; conferência final e entrega; observações e retrabalho).
  3. "O que vem no modelo" com a imagem previa-ordem e legenda "Modelo de ordem de produção do FábricaFlow, em PDF de uma página."
  4. "Como usar em 5 passos": 1) emita uma OP por pedido, com o número do pedido; 2) confira os quatro itens de liberação antes de produzir e assine; 3) liste o material e confira o estoque; 4) cada setor preenche a sua linha de etapa (início, fim, operador e, se parou, o motivo em uma palavra); 5) na conferência final, registre a entrega e se foi no prazo.
  5. "Ordem de produção e pedido de venda são a mesma coisa?" -> "Não. O pedido de venda é o registro comercial do que o cliente comprou, com valores. A ordem de produção é o documento interno da fábrica, sem valores, que diz como produzir. Uma OP nasce de um pedido já aprovado."
  6. "Quando o papel deixa de bastar" (neutro): muitas OPs ao mesmo tempo, perda de folhas, ninguém sabe onde está cada pedido, digitar de novo o que chegou pelo WhatsApp. "No FábricaFlow, a ficha do pedido sai em PDF a partir do pedido registrado (cliente, produto, quantidade, setor, prazo, prioridade e observações, sem valores), e a fila por setor se atualiza sozinha. Agende uma demonstração de 20 minutos." (link /#contato)
  7. Perguntas frequentes (3): "O modelo é grátis?" (Sim, sem cadastro e sem prazo.) / "Posso editar o modelo?" (É um PDF para imprimir e preencher à mão. Para registrar no computador, use a planilha de controle de produção, com link.) / "Ordem de produção e pedido de venda são a mesma coisa?" (a resposta acima, resumida).
- Schema: WebPage + FAQPage (3 perguntas) + BreadcrumbList. Sem Product.
- Rodapé padrão com CNPJ.

## Integração
Links: da página da planilha (frase "Precisa da ordem de produção para imprimir? Baixe o modelo"), do artigo pilar de controle de produção (seção "Ordem de produção", ver Briefing 1), do índice do blog/modelos. Sitemap, llms.txt (seção "Modelos grátis"), cópia .md, link alternate, IndexNow só depois do aprovado.

## Regras
Sem afirmar clientes; sem "o melhor"; não afirmar que o PDF é igual ao do sistema (é um modelo de papel); só dizer sobre o FábricaFlow o que o llms.txt já diz (ficha do pedido em PDF, sem valores).

## Entrega
Em branch/preview, prints em `_previa/` (desktop 1440 e mobile 390). Eu levo ao Igor.
