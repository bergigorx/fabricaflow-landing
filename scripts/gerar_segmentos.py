#!/usr/bin/env python3
"""Gera as páginas por segmento (segmentos/<slug>/index.html) a partir do index.html.

O index.html é a fonte: rode este script depois de editar a página principal.
Cada página tem endereço, título, H1, descrição e trechos próprios do segmento, para o Google
indexar separadamente buscas como "sistema de gestão para fábrica de móveis".
Uso: python3 scripts/gerar_segmentos.py
"""
import html
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SITE = "https://fabricaflow.online"

SEGMENTOS = [
    {
        "slug": "papel-e-embalagens",
        "nome": "Papel e embalagens",
        "titulo": "Sistema de gestão para fábricas de papel, papelão e embalagens | FábricaFlow",
        "descricao": "Plataforma de gestão industrial para fábricas de papel, papelão ondulado, papel cartão e embalagens: pedidos do WhatsApp, aprovação do gestor, produção por setor, estoque de bobinas e insumos e aviso ao cliente.",
        "h1": "Sistema de gestão para fábricas de papel, papelão e embalagens",
        "hero_sub": "Atendimento, aprovação, produção, estoque e aviso ao cliente conectados, para fábricas de papelão ondulado, papel cartão, papel e tissue e embalagens. Sem digitação manual, com aprovação do gestor.",
        "chips": ["Papelão ondulado", "Papel cartão", "Papel e tissue", "Caixas e embalagens", "Envelopes e sacolas"],
        "pedido": "Bom dia! Preciso de 2.000 caixas 40×30×20, onda B, kraft.",
        "orcamento": "Bom dia! Orçamento: 2.000 caixas 40×30×20, onda B kraft. Total R$ X.XXX,XX. Prazo de 7 dias úteis. Confirma?",
        "material": "Bobina, cola ou tinta que acabou sem ninguém perceber a tempo.",
        "setores": ["Onduladeira", "Impressão flexográfica", "Corte e vinco", "Colagem", "Máquina de papel", "Rebobinadeira", "Embalagem", "Expedição"],
        "formulario": "Papelão ondulado",
        "dores": [
            ("Pedido de medida e onda certas", "Medidas, onda, gramatura e quantidade ficam registradas no pedido, sem depender de mensagem perdida."),
            ("Bobina e cola sob controle", "Saldo de bobinas, chapas, cola e tinta com alerta antes de faltar e parar a onduladeira."),
            ("Fila por máquina", "Cada setor, da onduladeira à colagem, vê a própria fila e atualiza o andamento do pedido."),
        ],
    },
    {
        "slug": "moveis-e-marcenaria",
        "nome": "Móveis e marcenaria",
        "titulo": "Sistema de gestão para fábricas de móveis e marcenarias | FábricaFlow",
        "descricao": "Plataforma de gestão industrial para fábricas de móveis planejados, corporativos e marcenarias: pedidos do WhatsApp, aprovação do gestor, produção por setor, estoque de MDF e ferragens e aviso ao cliente.",
        "h1": "Sistema de gestão para fábricas de móveis e marcenarias",
        "dores": [
            ("Projeto e pedido no mesmo lugar", "Ambientes, medidas, acabamentos e prazos registrados no pedido, com o histórico de cada alteração."),
            ("Chapa e ferragem sem surpresa", "Saldo de MDF, fita de borda e ferragens com alerta de mínimo, antes de travar a montagem."),
            ("Do corte à montagem", "Fila por setor (corte, usinagem, borda, pintura, montagem) com o status atualizado pelo operador."),
        ],
    },
    {
        "slug": "metalurgia-e-serralheria",
        "nome": "Metalurgia e serralheria",
        "titulo": "Sistema de gestão para metalúrgicas e serralherias | FábricaFlow",
        "descricao": "Plataforma de gestão industrial para metalúrgicas, serralherias e fábricas de estruturas metálicas: pedidos do WhatsApp, aprovação do gestor, produção por setor, estoque de chapas e perfis e aviso ao cliente.",
        "h1": "Sistema de gestão para metalúrgicas e serralherias",
        "dores": [
            ("Desenho e pedido juntos", "Quantidade, material, acabamento e prazo registrados no pedido, sem depender de conversa solta."),
            ("Chapa, perfil e consumíveis", "Saldo de chapas, perfis, arame de solda e tinta com alerta antes de faltar."),
            ("Fila do corte à pintura", "Corte, dobra, solda, usinagem e pintura com fila própria e status atualizado pelo operador."),
        ],
    },
]


def segmentos_do_js():
    """Lê os textos de exemplo de móveis e metal do main.js (mesma fonte do ?seg=)."""
    js = (RAIZ / "main.js").read_text(encoding="utf-8")
    bloco = js[js.index("const SEGMENTOS = {") + len("const SEGMENTOS = "): js.index("};", js.index("const SEGMENTOS = {")) + 1]
    bloco = re.sub(r"^(\s*)(\w+):", r'\1"\2":', bloco, flags=re.M)  # chaves sem aspas -> JSON
    bloco = re.sub(r",(\s*[}\]])", r"\1", bloco)       # vírgulas finais
    dados = json.loads(bloco)
    chaves = {"heroSub": "hero_sub", "chips": "chips", "pedido": "pedido", "orcamento": "orcamento",
              "material": "material", "setores": "setores", "formulario": "formulario"}
    return {"moveis-e-marcenaria": {chaves[k]: v for k, v in dados["moveis"].items()},
            "metalurgia-e-serralheria": {chaves[k]: v for k, v in dados["metal"].items()}}


def trocar(s, padrao, novo, contagem=1):
    novo_s, n = re.subn(padrao, lambda _: novo, s, count=contagem, flags=re.S)
    if n == 0:
        raise SystemExit(f"Padrão não encontrado no index.html: {padrao}")
    return novo_s


def lista_li(itens):
    return "".join(f"<li>{html.escape(i)}</li>" for i in itens)


def gerar(base, seg):
    url = f"{SITE}/segmentos/{seg['slug']}/"
    e = html.escape
    s = base
    # Caminhos absolutos: a página fica em /segmentos/<slug>/
    for prefixo in ("style.css", "main.js", "img/", "fonts/", "video/"):
        s = s.replace(f'"{prefixo}', f'"/{prefixo}').replace(f", {prefixo}", f", /{prefixo}")
    s = trocar(s, r"<title>.*?</title>", f"<title>{e(seg['titulo'])}</title>")
    s = trocar(s, r'<meta name="description" content=".*?">', f'<meta name="description" content="{e(seg["descricao"])}">')
    s = trocar(s, r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{url}">')
    s = trocar(s, r'<link rel="alternate" hreflang="pt-BR" href=".*?">', f'<link rel="alternate" hreflang="pt-BR" href="{url}">')
    s = trocar(s, r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{url}">')
    s = trocar(s, r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{e(seg["h1"])} | FábricaFlow">')
    s = trocar(s, r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{e(seg["descricao"])}">')
    s = trocar(s, r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{e(seg["h1"])}">')
    s = trocar(s, r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{e(seg["descricao"])}">')
    migalhas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "FábricaFlow", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": seg["nome"], "item": url}]}
    s = s.replace("</head>", '<script type="application/ld+json">\n' + json.dumps(migalhas, ensure_ascii=False, indent=2) + "\n</script>\n</head>", 1)
    # Navegação: âncoras da página principal continuam na própria página
    s = s.replace('href="#inicio" aria-label="FábricaFlow, início"', 'href="/" aria-label="FábricaFlow, página inicial"')
    # Conteúdo do segmento
    s = trocar(s, r'<p class="sobretitulo">Plataforma de gestão industrial</p>\s*<h1>.*?</h1>',
               f'<p class="sobretitulo">Plataforma de gestão industrial · {e(seg["nome"])}</p>\n        <h1>{e(seg["h1"])}</h1>')
    s = trocar(s, r'<p class="hero-sub" id="hero-sub">.*?</p>', f'<p class="hero-sub" id="hero-sub">{e(seg["hero_sub"])}</p>')
    s = trocar(s, r'(<ul class="setores-hero" id="setores-hero" aria-label="Setores atendidos">\s*).*?(\s*</ul>)',
               f'<ul class="setores-hero" id="setores-hero" aria-label="Setores atendidos">\n          {lista_li(seg["chips"])}\n        </ul>')
    s = trocar(s, r'<p class="msg msg-cliente" id="conversa-pedido">.*?</p>', f'<p class="msg msg-cliente" id="conversa-pedido">{e(seg["pedido"])}</p>')
    s = trocar(s, r'<p class="msg msg-bot" id="conversa-orcamento">.*?</p>', f'<p class="msg msg-bot" id="conversa-orcamento">{e(seg["orcamento"])}</p>')
    s = trocar(s, r'<p id="calc-material">.*?</p>', f'<p id="calc-material">{e(seg["material"])}</p>')
    s = trocar(s, r'(<ul id="setores-config">).*?(</ul>)', f'<ul id="setores-config">\n          {lista_li(seg["setores"])}\n        </ul>')
    opcao = f"<option>{e(seg['formulario'])}</option>"
    if opcao not in s:
        raise SystemExit(f"Opção do formulário não encontrada: {seg['formulario']}")
    s = s.replace(opcao, f"<option selected>{e(seg['formulario'])}</option>", 1)
    # Bloco próprio do segmento logo depois do hero (conteúdo único para a página)
    dores = "\n".join(f"        <li><h3>{e(t)}</h3><p>{e(d)}</p></li>" for t, d in seg["dores"])
    bloco = f'''  <!-- Segmento: {e(seg["nome"])} -->
  <section class="secao" id="segmento">
    <div class="faixa">
      <header class="secao-cabeca">
        <p class="sobretitulo">Feito para a rotina de {e(seg["nome"].lower())}</p>
        <h2>O que muda na sua fábrica</h2>
      </header>
      <ul class="problemas">
{dores}
      </ul>
    </div>
  </section>

'''
    s = trocar(s, r"  <!-- 2\. O problema -->", bloco + "  <!-- 2. O problema -->")
    return s


def main():
    base = (RAIZ / "index.html").read_text(encoding="utf-8")
    do_js = segmentos_do_js()
    for seg in SEGMENTOS:
        seg = {**do_js.get(seg["slug"], {}), **seg}
        destino = RAIZ / "segmentos" / seg["slug"] / "index.html"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(gerar(base, seg), encoding="utf-8")
        print("gerada:", destino.relative_to(RAIZ))


if __name__ == "__main__":
    main()
