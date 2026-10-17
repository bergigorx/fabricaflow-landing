# Segurança

## Como relatar um problema

Encontrou uma falha de segurança na página https://fabricaflow.online? Escreva para **igorbergara99@gmail.com** com a descrição e os passos para reproduzir. Por favor, não abra uma issue pública antes de o problema ser corrigido.

## O que já está protegido

- **Site estático no GitHub Pages:** não há servidor, banco de dados nem login para invadir. O GitHub entrega a página por uma CDN com proteção contra DDoS e HTTPS obrigatório.
- **Content-Security-Policy:** a página só carrega scripts, estilos, fontes, imagens e vídeo do próprio domínio e só envia dados para `hooks.zapier.com`. Isso bloqueia scripts injetados e envios para outros endereços.
- **Sem dependências de terceiros:** nenhuma biblioteca externa. As fontes são servidas pelo próprio site (sem Google Fonts), o que também evita enviar o IP do visitante ao Google (LGPD).
- **Formulário:**
  - campo isca invisível e tempo mínimo de 3 segundos, para descartar robôs simples;
  - limite de um envio por minuto por navegador;
  - textos limpos antes do envio: sem caracteres de controle, com tamanho máximo, e com fórmulas de planilha (`=`, `+`, `-`, `@`) neutralizadas;
  - campo `origem` para o Zap descartar chamadas que não vieram do formulário.
- **Links externos** abrem com `rel="noopener"`, e a política de referência não envia a URL completa a outros sites.

## Limites conhecidos

- A URL do webhook do Zapier aparece no código, como em qualquer formulário de site estático. As proteções do navegador reduzem o abuso, mas quem chamar a URL direto consegue passar por elas. A defesa final é o **filtro no Zap** (descrito no README).
- O GitHub Pages não permite configurar cabeçalhos HTTP. Por isso, `frame-ancestors` (proteção contra a página ser exibida dentro de outro site) não está ativo. O risco aqui é baixo: a página não tem login nem ações sensíveis.
