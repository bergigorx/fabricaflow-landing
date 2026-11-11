"""Gera uma cópia em Markdown (index.md) de cada página listada no llms.txt.

O conteúdo vem do próprio HTML da página (o mesmo texto que o visitante vê):
tudo o que está em <main>, mais a assinatura do rodapé. Nada é escrito à mão aqui.
Uso: python3 scripts/gerar_markdown.py   (rode depois de gerar_segmentos.py)
"""
import re
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify

SITE = "https://fabricaflow.online"
PAGINAS = [
    "index.html", "sobre/index.html", "privacidade/index.html", "termos/index.html",
    "segmentos/papel-e-embalagens/index.html", "segmentos/moveis-e-marcenaria/index.html",
    "segmentos/metalurgia-e-serralheria/index.html",
    "blog/index.html",
    "blog/erp-ou-mes-qual-usar-na-fabrica/index.html",
    "blog/implantacao-sistema-gestao-fabrica-checklist/index.html",
    "blog/pedido-whatsapp-industria/index.html",
    "blog/estoque-minimo-fabrica/index.html",
    "blog/controle-de-producao-pequena-fabrica/index.html",
]


def absoluto(url, base):
    if not url or url.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return url
    if url.startswith("#"):
        return base + url
    if url.startswith("/"):
        return SITE + url
    return base + url


def gerar(caminho):
    html = Path(caminho).read_text(encoding="utf-8")
    sopa = BeautifulSoup(html, "html.parser")
    pasta = caminho[: -len("index.html")]
    base = f"{SITE}/{pasta}"
    main = sopa.find("main")
    # O que não é texto de leitura: scripts, ícones, campos de formulário e o formulário de contato.
    for tag in main.find_all(["script", "style", "svg", "input", "select", "textarea", "output", "button", "noscript"]):
        tag.decompose()
    for tag in main.select('[aria-hidden="true"], form#formulario'):
        tag.decompose()
    for video in main.find_all("video"):
        fonte = video.find("source")
        link = sopa.new_tag("a", href=fonte["src"] if fonte else "")
        link.string = "Vídeo de demonstração (MP4)"
        video.replace_with(link)
    for tag in main.find_all(["a", "img"]):
        for attr in ("href", "src"):
            if tag.get(attr):
                tag[attr] = absoluto(tag[attr], base)
    for img in main.find_all("img"):
        for attr in ("srcset", "sizes", "loading", "decoding", "width", "height"):
            img.attrs.pop(attr, None)
    # <details>: o resumo vira um subtítulo, como o visitante vê ao abrir.
    for resumo in main.find_all("summary"):
        resumo.name = "h3"
    corpo = markdownify(str(main), heading_style="ATX", bullets="-", strip=["main", "article", "section", "div", "span", "details", "header", "aside", "nav", "figure", "time", "fieldset", "label", "legend", "form"])
    corpo = re.sub(r"[ \t]+\n", "\n", corpo)
    corpo = re.sub(r"\n(!\[)", r"\n\n\1", corpo)
    corpo = re.sub(r"\n{3,}", "\n\n", corpo).strip()
    rodape = sopa.find("footer")
    assinatura = "\n\n".join(p.get_text(" ", strip=True) for p in rodape.find_all("p")) if rodape else ""
    canonico = sopa.find("link", rel="canonical")["href"]
    titulo = sopa.title.get_text(strip=True)
    md = f"Página: {canonico}\n\n{corpo}\n\n---\n\n{assinatura}\n"
    destino = Path(pasta or ".") / "index.md"
    destino.write_text(md, encoding="utf-8")
    return destino


if __name__ == "__main__":
    for p in PAGINAS:
        print("gerado:", gerar(p))
