Página: https://fabricaflow.online/blog/estoque-minimo-fabrica/

[Início](https://fabricaflow.online/) [Blog](https://fabricaflow.online/blog/)

Controle de estoque

# Como calcular o estoque mínimo dos materiais da fábrica (com exemplo)

A fórmula, os três números de que você precisa e dois exemplos resolvidos, para nunca mais parar a máquina por falta de material.

Por [Igor Bergara](https://fabricaflow.online/sobre/) · Publicado em 27 de outubro de 2026 · Atualizado em 13 de novembro de 2026 · 7 min de leitura

Estoque mínimo é a quantidade de um material abaixo da qual você precisa comprar para não parar a produção. Material que acaba sem aviso é uma das formas mais caras de perder dinheiro na fábrica: a máquina para, o pedido atrasa, a compra sai às pressas e mais cara. O contrário também custa: estoque demais prende o caixa e ocupa espaço. O estoque mínimo existe para resolver esse equilíbrio.

Neste guia você vai ver a fórmula, os dados necessários e dois exemplos resolvidos, um de papelão e um de móveis.

Resposta rápida

Estoque mínimo = consumo médio diário × prazo de reposição + estoque de segurança. Exemplo: com consumo de 15 chapas por dia, prazo de 5 dias e 2 dias de segurança, o estoque mínimo é 15 × 5 + 15 × 2 = 105 chapas. Quando o saldo chegar a esse número, é hora de comprar. A [planilha de controle de produção grátis](https://fabricaflow.online/modelos/planilha-controle-de-producao/) já traz a conta pronta.

## Estoque mínimo, estoque de segurança e ponto de pedido

Os três termos costumam ser usados como se fossem a mesma coisa. Vale separar:

- **Estoque de segurança:** a reserva para imprevistos, como um consumo acima do normal ou um fornecedor que atrasa.
- **Ponto de pedido:** o saldo em que você precisa fazer a compra. É o consumo durante o prazo de entrega do fornecedor mais o estoque de segurança.
- **Estoque mínimo:** no dia a dia da fábrica, é o número que dispara o alerta de compra. Na prática, o mais útil é usar o ponto de pedido como estoque mínimo, e é isso que este guia ensina a calcular.

**Atenção:** alguns materiais didáticos definem o estoque mínimo só como o consumo durante o prazo de reposição, sem a segurança. Aqui incluímos a segurança, porque é o que evita a parada quando o fornecedor atrasa.

![Gráfico do saldo de um material ao longo do tempo: o saldo cai até o estoque mínimo, a compra é feita, o saldo continua caindo durante o prazo de reposição e sobe quando o material chega; a faixa de estoque de segurança cobre um consumo acima do normal.](https://fabricaflow.online/blog/img/estoque-minimo-grafico.svg)

Como o estoque mínimo funciona: a compra sai no ponto de pedido e o material chega antes de acabar.

## Os três números de que você precisa

1. **Consumo médio diário:** quanto do material sai por dia de produção. Some as saídas dos últimos 2 ou 3 meses e divida pelos dias trabalhados no período.
2. **Prazo de reposição:** quantos dias de produção passam entre fazer o pedido e o material estar disponível na fábrica. Inclua o tempo de aprovação da compra, não só o frete.
3. **Variação:** qual foi o maior consumo diário e o maior atraso do fornecedor no período. É daqui que sai o estoque de segurança.

Se você ainda não tem esses dados registrados, comece com uma estimativa do encarregado e ajuste depois de um mês de lançamentos.

## A fórmula

**Estoque mínimo** = consumo médio diário × prazo de reposição + estoque de segurança

E para o estoque de segurança, use um destes dois métodos:

- **Método simples (dias de cobertura):** estoque de segurança = consumo médio diário × dias extras de proteção. Para a maioria dos materiais, de 2 a 5 dias resolvem.
- **Método do pior caso:** estoque de segurança = (consumo máximo diário × prazo máximo) − (consumo médio diário × prazo médio). Use para materiais críticos ou fornecedores pouco confiáveis.

## Exemplo 1: bobina de papel kraft em uma fábrica de papelão

Dados dos últimos três meses:

- consumo médio: 1,2 tonelada por dia;
- maior consumo em um dia: 1,6 tonelada;
- prazo médio do fornecedor: 10 dias úteis; maior atraso registrado: 14 dias úteis.

Como a bobina para a onduladeira inteira, vale usar o método do pior caso:

1. Consumo durante o prazo: 1,2 × 10 = **12 toneladas**.
2. Estoque de segurança: (1,6 × 14) − (1,2 × 10) = 22,4 − 12 = **10,4 toneladas**.
3. Estoque mínimo: 12 + 10,4 = **22,4 toneladas**.

Ou seja: quando o saldo de bobina kraft chegar a 22,4 toneladas, é hora de comprar.

## Exemplo 2: chapa de MDF em uma fábrica de móveis planejados

- consumo médio: 15 chapas por dia;
- prazo de reposição: 5 dias úteis, fornecedor pontual;
- proteção desejada: 2 dias de consumo.

1. Consumo durante o prazo: 15 × 5 = **75 chapas**.
2. Estoque de segurança (método simples): 15 × 2 = **30 chapas**.
3. Estoque mínimo: 75 + 30 = **105 chapas**.

## E o estoque máximo? E o estoque médio?

O **estoque máximo** é o teto que o saldo pode atingir sem prender caixa nem ocupar espaço. Uma forma comum de calcular é estoque mínimo + lote de reposição, que é a quantidade comprada de cada vez. No exemplo da chapa de MDF, com estoque mínimo de 105 chapas e lote de compra de 150 chapas, o estoque máximo é de 255 chapas.

O **estoque médio** é (estoque no início do período + estoque no fim) ÷ 2. Ele mede quanto dinheiro fica parado em material, e não serve para decidir quando comprar. Se o saldo de MDF era de 200 chapas no começo do mês e de 120 no fim, o estoque médio é de 160 chapas.

## Resumo dos exemplos

| Material | Consumo médio/dia | Prazo | Segurança | Estoque mínimo |
| --- | --- | --- | --- | --- |
| Bobina kraft | 1,2 t | 10 dias | 10,4 t (pior caso) | 22,4 t |
| Chapa de MDF | 15 chapas | 5 dias | 30 chapas (2 dias) | 105 chapas |

## Tenho centenas de materiais. Por onde começo?

Não é preciso calcular tudo no primeiro dia. Use a lógica da curva ABC:

- **Comece pelos materiais que param a produção** quando faltam, como bobina, chapa, resina, cola e tinta. Em geral são de 10 a 20 itens.
- **Depois, os de maior valor**, em que errar para mais prende muito dinheiro.
- **Para o resto**, um estoque mínimo aproximado já resolve. Revise quando houver falta.

![Tela de estoque do FábricaFlow com o saldo de cada material, o estoque mínimo e o alerta de estoque baixo.](https://fabricaflow.online/img/estoque-800.webp)

Saldo de cada material contra o estoque mínimo, com alerta, no FábricaFlow (dados de demonstração).

## Estoque mínimo na indústria: o que muda em relação ao varejo

- **O consumo vem da produção, não das vendas.** Em vez de olhar só a média do passado, olhe o que as ordens de produção das próximas semanas vão consumir.
- **O fornecedor vende em lote.** Bobina vem por carga e tinta por bombona; o lote mínimo de compra pesa no saldo.
- **O prazo começa dentro de casa.** Conte o tempo de alguém perceber a falta e aprovar a compra.
- **Alguns materiais vencem.** Cola e tinta têm validade; segurança demais vira perda.
- **Um material serve vários produtos.** Some o consumo de todos os pedidos que usam o mesmo material.

*Os números a seguir são fictícios e servem só para mostrar o raciocínio.* As ordens da semana que vem usam 90 chapas de MDF em 6 dias de produção: 15 chapas por dia, o mesmo da média. Se entrar um pedido grande de 150 chapas, o consumo previsto passa a 240 chapas em 6 dias, ou 40 por dia. O estoque mínimo calculado pela média (105 chapas) fica curto: 40 × 5 + 40 × 2 = 280 chapas. Por isso a conta deve acompanhar as ordens de produção. Se ainda não usa ordem de produção, baixe o [modelo grátis de ordem de produção](https://fabricaflow.online/modelos/ordem-de-producao/).

## Erros comuns

- **Calcular com o saldo errado:** se as saídas não são lançadas, o alerta dispara tarde. Estoque mínimo só funciona com saldo confiável.
- **Esquecer o tempo interno:** o prazo de reposição começa quando alguém percebe a necessidade, não quando o pedido chega ao fornecedor.
- **Nunca revisar:** consumo e prazos mudam com a época do ano e com novos clientes. Revise os materiais críticos a cada trimestre.
- **Depender da memória de uma pessoa:** o alerta precisa aparecer para quem compra, sem ninguém ter que conferir a planilha.

## Resumo

Estoque mínimo = consumo médio diário × prazo de reposição + estoque de segurança. Para materiais críticos, calcule a segurança pelo pior caso; para os demais, alguns dias de cobertura bastam. Comece pelos itens que param a produção, mantenha o saldo atualizado e revise a cada trimestre. Se o saldo do ERP e o da fábrica não batem, vale entender a [diferença entre ERP e MES](https://fabricaflow.online/blog/erp-ou-mes-qual-usar-na-fabrica/). As duas fórmulas já vêm prontas na [planilha de controle de produção grátis](https://fabricaflow.online/modelos/planilha-controle-de-producao/).

## Perguntas frequentes

### O que é estoque mínimo?

É a quantidade de um material abaixo da qual é preciso comprar para não parar a produção. Ele cobre o consumo durante o prazo de reposição do fornecedor mais uma reserva de segurança.

### Como calcular o estoque mínimo?

Multiplique o consumo médio diário pelo prazo de reposição em dias e some o estoque de segurança. Exemplo: 15 chapas por dia × 5 dias + 30 chapas de segurança = 105 chapas.

### Qual a diferença entre estoque mínimo e estoque de segurança?

O estoque de segurança é só a reserva para imprevistos, como um atraso do fornecedor. O estoque mínimo, como calculamos aqui, é o consumo durante o prazo mais essa reserva.

### Estoque mínimo e ponto de pedido são a mesma coisa?

Na prática da fábrica, sim: é o saldo em que a compra deve sair. Alguns autores chamam de estoque mínimo só a reserva de segurança; vale definir o termo que a sua equipe vai usar.

### Como definir o estoque mínimo sem histórico?

Comece com uma estimativa do encarregado de consumo por dia e de prazo do fornecedor, use 2 a 5 dias de segurança e ajuste depois de um mês de lançamentos.

### Existe planilha de estoque mínimo grátis?

Sim. A [planilha de controle de produção grátis](https://fabricaflow.online/modelos/planilha-controle-de-producao/) do FábricaFlow tem uma aba de estoque mínimo que calcula o estoque de segurança e o ponto de reposição e avisa “Pedir agora”.

## Receba o alerta antes de faltar material

No FábricaFlow, cada entrada, saída e ajuste fica registrado e o saldo é atualizado na hora. Quando um material chega ao estoque mínimo, o gestor é avisado. Em 20 minutos, por vídeo, mostramos como funciona com os materiais da sua fábrica.

[Agendar demonstração de 20 min](https://fabricaflow.online/#contato)

Leia também: [controle de produção na pequena fábrica](https://fabricaflow.online/blog/controle-de-producao-pequena-fabrica/) · [papel e embalagens](https://fabricaflow.online/segmentos/papel-e-embalagens/) · [móveis e marcenaria](https://fabricaflow.online/segmentos/moveis-e-marcenaria/)

---

FábricaFlow · Plataforma de gestão industrial

Igor Bergara · igorbergara@fabricaflow.online · (11) 97874-6889

FábricaFlow é um produto da I.F.A. Bergara Tecnologia · CNPJ 47.035.146/0001-36 · São Paulo/SP
