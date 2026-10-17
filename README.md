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
