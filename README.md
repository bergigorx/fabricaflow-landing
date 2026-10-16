# Landing page do FábricaFlow

Página estática (HTML, CSS e JS puros, sem build). Para ver localmente:

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

## Configurar o envio do formulário (Zapier)

1. No Zapier, crie um Zap com o gatilho **Webhooks by Zapier → Catch Hook** e copie a URL.
2. Em `main.js`, troque o valor de `ENDPOINT_FORMULARIO` (primeira linha de configuração) por essa URL.
3. Envie um pedido de teste pela página para o Zapier reconhecer os campos.

Enquanto o valor de exemplo estiver lá, o formulário não envia nada: mostra ao visitante uma mensagem e o botão do WhatsApp com a mensagem já pronta.

O envio é um `POST` em `application/x-www-form-urlencoded` (sem pré-verificação CORS). Campos enviados:

`nome`, `empresa`, `cargo`, `email`, `whatsapp`, `cidade`, `segmento`, `funcionarios`, `principal_dor`, `mensagem`, `consentimento_lgpd`, `custo_mensal_estimado` (se o visitante usou a calculadora), `utm_source`, `utm_medium`, `utm_campaign`, `pagina`, `enviado_em`.

Dica para os e-mails em lote: use links com UTM, por exemplo `...?utm_source=email&utm_campaign=lote-1`, para saber de onde veio cada pedido.

## Arquivos

- `index.html`, `style.css`, `main.js`: a página.
- `img/`: prints reais do app em WebP (1440 px e 800 px), sem o selo "Edit with Lovable". Gerados pelo script `landing-fabricaflow/scripts/preparar_imagens.py` do repositório `bergigorx/estudos`.
- `video/fabricaflow-demo.mp4`: vídeo narrado (1min52s) reduzido para 1280 px, cerca de 3 MB.

## Publicação

Publicada pelo GitHub Pages a partir do branch `main`, pasta raiz (`/`). O arquivo `.nojekyll` faz o GitHub servir os arquivos como estão.
