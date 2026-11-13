# Briefing: reforço do artigo "Estoque mínimo" (Marketing -> Landing)

Status: PARA PREVIEW em branch. Nada vai para main sem o "aprovado" do Igor.
URL: a mesma (/blog/estoque-minimo-fabrica/). Manter H1, os dois exemplos resolvidos, o gráfico, a tabela-resumo, o bloco da curva ABC, os erros comuns e o CTA. Só ACRESCENTAR/ajustar o que está abaixo.

## Por que
Search Console (26/10 a 10/11): a página aparece para "como calcular estoque mínimo" nas posições 85 e 96, perto de invisível. Quem ranqueia (Stone, Sienge, Nuvemshop, Yampi, PagBank, ContaAzul, Omie) é quase tudo varejo e e-commerce, com a fórmula básica "consumo médio diário x tempo de reposição", definição logo no topo e planilha. Lacunas do nosso artigo em relação a eles: sem caixa de resposta rápida, sem FAQ, sem "estoque máximo/médio" (buscas relacionadas), definição do estoque mínimo só depois do segundo parágrafo. Nosso diferencial é o ângulo industrial (consumo vem da produção, lote do fornecedor, validade) e a planilha grátis. Limite honesto: não medi o tamanho dos concorrentes, só li os resultados de busca; não prometemos posição.

## 1. Metadados
- Title (53): `Estoque mínimo: o que é e como calcular (com planilha)`
- Meta (133): `Estoque mínimo: o que é, fórmula, estoque de segurança e ponto de pedido, com exemplos de fábrica e planilha grátis para calcular.`
- "Publicado em 27/10 · Atualizado em <data da publicação>" visível; dateModified no JSON-LD.

## 2. Primeiro parágrafo (substituir o atual; a definição entra nas primeiras 100 palavras)
"Estoque mínimo é a quantidade de um material abaixo da qual você precisa comprar para não parar a produção. Material que acaba sem aviso é uma das formas mais caras de perder dinheiro na fábrica: a máquina para, o pedido atrasa, a compra sai às pressas e mais cara. O contrário também custa: estoque demais prende o caixa e ocupa espaço. O estoque mínimo existe para resolver esse equilíbrio."
Manter o parágrafo seguinte ("Neste guia você vai ver a fórmula...") como está.

## 3. Caixa "Resposta rápida" (padrão do site), logo depois do primeiro bloco de introdução
"Estoque mínimo = consumo médio diário x prazo de reposição + estoque de segurança. Exemplo: com consumo de 15 chapas por dia, prazo de 5 dias e 2 dias de segurança, o estoque mínimo é 15 x 5 + 15 x 2 = 105 chapas. Quando o saldo chegar a esse número, é hora de comprar. A planilha grátis desta página já traz a conta pronta."
(conferência: 75 + 30 = 105)

## 4. Nota de definição, no fim da seção "Estoque mínimo, estoque de segurança e ponto de pedido"
"Atenção: alguns materiais didáticos definem o estoque mínimo só como o consumo durante o prazo de reposição, sem a segurança. Aqui incluímos a segurança, porque é o que evita a parada quando o fornecedor atrasa."

## 5. Nova seção, depois de "A fórmula" e dos exemplos, antes de "Resumo dos exemplos": "E o estoque máximo? E o estoque médio?"
"O **estoque máximo** é o teto que o saldo pode atingir sem prender caixa nem ocupar espaço. Uma forma comum de calcular é estoque mínimo + lote de reposição, que é a quantidade comprada de cada vez. No exemplo da chapa de MDF, com estoque mínimo de 105 chapas e lote de compra de 150 chapas, o estoque máximo é de 255 chapas.
O **estoque médio** é (estoque no início do período + estoque no fim) ÷ 2. Ele mede quanto dinheiro fica parado em material, e não serve para decidir quando comprar. Se o saldo de MDF era de 200 chapas no começo do mês e de 120 no fim, o estoque médio é de 160 chapas."
(conferência: 105+150=255; (200+120)/2=160)

## 6. Nova seção, depois da curva ABC: "Estoque mínimo na indústria: o que muda em relação ao varejo"
Lista curta + exemplo:
- "**O consumo vem da produção, não das vendas.** Em vez de olhar só a média do passado, olhe o que as ordens de produção das próximas semanas vão consumir."
- "**O fornecedor vende em lote.** Bobina vem por carga e tinta por bombona; o lote mínimo de compra pesa no saldo."
- "**O prazo começa dentro de casa.** Conte o tempo de alguém perceber a falta e aprovar a compra."
- "**Alguns materiais vencem.** Cola e tinta têm validade; segurança demais vira perda."
- "**Um material serve vários produtos.** Some o consumo de todos os pedidos que usam o mesmo material."
Exemplo (marcar "Os números a seguir são fictícios..."): "As ordens da semana que vem usam 90 chapas de MDF em 6 dias de produção: 15 chapas por dia, o mesmo da média. Se entrar um pedido grande de 150 chapas, o consumo previsto passa a 240 chapas em 6 dias, ou 40 por dia. O estoque mínimo calculado pela média (105 chapas) fica curto: 40 x 5 + 40 x 2 = 280 chapas. Por isso a conta deve acompanhar as ordens de produção." Link para o modelo de ordem de produção (/modelos/ordem-de-producao/).
(conferência: 90/6=15; (90+150)/6=40; 40x5+40x2=280)

## 7. Seção "Perguntas frequentes" antes do CTA final (+ FAQPage JSON-LD idêntico)
1. O que é estoque mínimo? -> "É a quantidade de um material abaixo da qual é preciso comprar para não parar a produção. Ele cobre o consumo durante o prazo de reposição do fornecedor mais uma reserva de segurança."
2. Como calcular o estoque mínimo? -> "Multiplique o consumo médio diário pelo prazo de reposição em dias e some o estoque de segurança. Exemplo: 15 chapas por dia x 5 dias + 30 chapas de segurança = 105 chapas."
3. Qual a diferença entre estoque mínimo e estoque de segurança? -> "O estoque de segurança é só a reserva para imprevistos, como um atraso do fornecedor. O estoque mínimo, como calculamos aqui, é o consumo durante o prazo mais essa reserva."
4. Estoque mínimo e ponto de pedido são a mesma coisa? -> "Na prática da fábrica, sim: é o saldo em que a compra deve sair. Alguns autores chamam de estoque mínimo só a reserva de segurança; vale definir o termo que a sua equipe vai usar."
5. Como definir o estoque mínimo sem histórico? -> "Comece com uma estimativa do encarregado de consumo por dia e de prazo do fornecedor, use 2 a 5 dias de segurança e ajuste depois de um mês de lançamentos."
6. Existe planilha de estoque mínimo grátis? -> "Sim. A planilha de controle de produção grátis do FábricaFlow tem uma aba de estoque mínimo que calcula o estoque de segurança e o ponto de reposição e avisa 'Pedir agora'." (link /modelos/planilha-controle-de-producao/)

## 8. Links internos
Planilha (já existe no Resumo): manter e repetir na resposta rápida. Ordem de produção (seção 6). Controle de produção na pequena fábrica (já existe em "Leia também"). ERP ou MES (já existe).

## 9. Regras
As mesmas do site: sem afirmar clientes; sem "o melhor"; sem ERP/nota fiscal como função nossa; sem prometer posição no Google. Regenerar a cópia .md, sitemap lastmod, IndexNow só depois do aprovado. Tempo de leitura: atualizar (de 4 para cerca de 6 min).

## 10. Entrega
Em branch/preview; prints em `_previa/` (desktop 1440 e mobile 390) e resumo do que mudou. Eu levo ao Igor.
