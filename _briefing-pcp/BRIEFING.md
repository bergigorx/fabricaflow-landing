# Briefing: novo artigo "PCP na pequena fábrica: o que é e como fazer" (Marketing -> Landing)

Status: PARA PREVIEW em branch. Nada vai para main sem o "aprovado" do Igor. O texto em ARTIGO.md (mesma pasta) foi aprovado por ele para virar prévia.

## Objetivo
Capturar buscas por "PCP" (maior volume do Google Trends entre os termos medidos) e ligar os conteúdos que já temos: controle de produção, planilha, ordem de produção, estoque mínimo, ERP x MES.

## O que fazer
- Criar `/blog/pcp-pequena-fabrica/` no padrão dos artigos (mesmo layout dos artigos de estoque mínimo e controle de produção), com o texto exato de ARTIGO.md: H1, caixa Resposta rápida, seções, tabela do exemplo (carga ÷ capacidade), cálculo do prazo, "Erros comuns", FAQ, Resumo e CTA de demonstração.
- Title (44): `PCP na pequena fábrica: o que é e como fazer` (+ " | FábricaFlow" se o padrão do site for esse e couber em 60). Meta (142): a que está no topo de ARTIGO.md.
- Autor com link para /sobre/, "Publicado em <data da publicação>", tempo de leitura (~1.500 palavras, cerca de 7 min).
- Dados estruturados: BlogPosting + BreadcrumbList + FAQPage com as 6 perguntas, idênticos ao texto visível.
- O exemplo traz números fictícios, com o aviso em itálico (manter).
- Links internos já estão no texto (estoque mínimo, controle de produção, ERP ou MES, planilha, ordem de produção, 3 segmentos). Adicionar, em sentido contrário, uma frase com link para este artigo no artigo de controle de produção (seção "Controle de produção ou PCP") e no de estoque mínimo ("Leia também").
- Item no topo do blog, sitemap, llms.txt (seção Artigos), cópia .md (gerar_markdown.py) e link alternate.
- Imagem de capa 1200x630 no padrão dos outros artigos. Se quiser um diagrama, só se for simples e sem texto novo.

## Regras
Mesmas do site: sem ERP/nota fiscal como função nossa; sem afirmar clientes; sem "o melhor/o único"; sem texto só para robôs. Não alterar o texto sem me avisar; se algo não couber no padrão, me diga o ajuste.

## Entrega
Em branch/preview. Prints em `_previa/` (desktop 1440 e mobile 390) e resumo do que mudou. Eu levo ao Igor. Depois do aprovado dele: publicar sem as pastas _briefing-pcp/ e _previa/, avisar o Bing (IndexNow) e me passar a URL.
