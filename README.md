# Landing page do FábricaFlow

Página estática (HTML, CSS e JS puros, sem build). Para ver localmente:

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

## Configurar o envio do formulário (Zapier)

O formulário envia para o Zap do Igor (gatilho **Webhooks by Zapier → Catch Hook**). A URL fica em `ENDPOINT_FORMULARIO`, no topo do `main.js`. Para trocar de Zap, mude só essa linha.

Se o envio falhar, o visitante vê uma mensagem e o botão do WhatsApp com a mensagem já pronta.

### Filtro anti-spam no Zap (recomendado)

Logo depois do gatilho **Catch Hook**, adicione a etapa **Filter by Zapier** com três condições (todas obrigatórias):

| Campo | Condição | Valor |
|---|---|---|
| `origem` | (Text) Exactly matches | `landing-fabricaflow-v1` |
| `consentimento_lgpd` | (Text) Exactly matches | `sim` |
| `tempo_preenchimento_s` | (Number) Greater than | `3` |

O gatilho e o filtro não consomem tarefas do Zapier. Assim, uma chamada falsa direta no webhook é descartada antes de gastar tarefas ou de cair na planilha e no e-mail.

O envio é um `POST` em `application/x-www-form-urlencoded` (sem pré-verificação CORS). Campos enviados:

`nome`, `empresa`, `cargo`, `email`, `whatsapp`, `cidade`, `segmento`, `funcionarios`, `principal_dor`, `mensagem`, `consentimento_lgpd`, `custo_mensal_estimado` (se o visitante usou a calculadora), `utm_source`, `utm_medium`, `utm_campaign`, `pagina`, `origem`, `tempo_preenchimento_s`, `enviado_em`.

Dica para os e-mails em lote: use links com UTM, por exemplo `...?utm_source=email&utm_campaign=lote-1`, para saber de onde veio cada pedido.

## SEO e buscas por IA

- **Fonte única:** edite o `index.html` e rode `python3 scripts/gerar_segmentos.py` para regerar as páginas de `segmentos/` (papel e embalagens, móveis e marcenaria, metalurgia e serralheria). Cada uma tem endereço, título, H1 e trechos próprios, para o Google indexar buscas como "sistema de gestão para fábrica de móveis". O `?seg=` dos e-mails continua funcionando na página principal.
- **Dados estruturados (JSON-LD):** Organization, WebSite, SoftwareApplication, VideoObject e FAQPage no `<head>`; BreadcrumbList nas páginas de segmento. As perguntas frequentes visíveis e o JSON-LD devem dizer a mesma coisa.
- **`robots.txt`** libera buscadores e robôs de IA (ChatGPT, Claude, Gemini, Perplexity) e aponta o `sitemap.xml`. Ao criar página nova, inclua no sitemap.
- **`llms.txt`:** resumo do produto para assistentes de IA. Mantenha em dia com a página.
- **IndexNow:** o arquivo `a17806be07edc96b189f28b540d06687.txt` na raiz autoriza avisar Bing e Yandex de páginas novas ou alteradas (o ChatGPT busca pelo índice do Bing):
  `curl -s -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json' -d '{"host":"fabricaflow.online","key":"a17806be07edc96b189f28b540d06687","urlList":["https://fabricaflow.online/"]}'`
- **Imagens de compartilhamento:** `img/og-fabricaflow.jpg` (1200×630), `img/logo-fabricaflow.png`, `favicon.svg`, `apple-touch-icon.png`.

## Segurança

Veja [SECURITY.md](SECURITY.md).

## Arquivos

- `index.html`, `style.css`, `main.js`: a página.
- `fonts/`: Archivo e Inter em WOFF2, servidas pelo próprio site (licença SIL OFL 1.1 nos arquivos `OFL-*.txt`).
- `.well-known/security.txt`: contato para relatar falhas de segurança.
- `img/`: prints reais do app em WebP (1440 px e 800 px), sem o selo "Edit with Lovable". Gerados pelo script `landing-fabricaflow/scripts/preparar_imagens.py` do repositório `bergigorx/estudos`.
- `video/fabricaflow-demo.mp4`: vídeo narrado (1min52s) reduzido para 1280 px, cerca de 3 MB.

## Publicação

No ar em **https://fabricaflow.online**, pelo GitHub Pages, a partir do branch `main`, pasta raiz (`/`). O domínio está no arquivo `CNAME`.

DNS na Hostinger: registro `A` em `@` para `185.199.108.153` e `CNAME` em `www` para `bergigorx.github.io`. O painel da Hostinger não aceitou os outros três IPs do GitHub (`185.199.109.153`, `185.199.110.153`, `185.199.111.153`); eles servem só de redundância. O arquivo `.nojekyll` faz o GitHub servir os arquivos como estão.
