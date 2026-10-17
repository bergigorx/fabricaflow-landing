/* ============================================================
   CONFIGURAÇÃO: troque aqui e só aqui.
   ENDPOINT_FORMULARIO: URL do webhook do Zapier (gatilho "Catch Hook").
   Enquanto estiver com o valor de exemplo, o formulário não envia nada
   e mostra ao visitante o link direto do WhatsApp.
   ============================================================ */
const ENDPOINT_FORMULARIO = "https://hooks.zapier.com/hooks/catch/29163368/41k9r9z/";
const WHATSAPP_NUMERO = "5511978746889";
const WHATSAPP_EXIBICAO = "(11) 97874-6889";
const TEMPO_LIMITE_MS = 15000;

/* Proteção contra robôs e envios em massa (a URL do webhook é pública, como em qualquer site estático).
   ORIGEM_FORMULARIO não é segredo: serve para o filtro do Zap descartar chamadas que não vieram deste formulário. */
const ORIGEM_FORMULARIO = "landing-fabricaflow-v1";
const TEMPO_MINIMO_MS = 3000;            // ninguém preenche o formulário em menos de 3 segundos
const INTERVALO_ENTRE_ENVIOS_MS = 60000; // um envio por minuto por navegador
const paginaAbertaEm = Date.now();
let ultimoEnvioEm = 0;

const endpointConfigurado = !/EXEMPLO|0000000/.test(ENDPOINT_FORMULARIO);

/* ---------- Calculadora "Quanto custa esperar" ---------- */
const reais = new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL", maximumFractionDigits: 0 });
const SEMANAS_POR_MES = 4.33;
let custoMensalEstimado = null;

function numero(id) {
  const valor = parseFloat(String(document.getElementById(id).value).replace(",", "."));
  return Number.isFinite(valor) && valor >= 0 ? valor : null;
}

function atualizarCalculadora() {
  const linhas = [
    { a: "calc-pedidos", b: "calc-ticket", fator: 1, saida: "calc-r1", texto: "de faturamento que não entrou" },
    { a: "calc-horas-maquina", b: "calc-custo-maquina", fator: 1, saida: "calc-r2", texto: "de prejuízo direto" },
    { a: "calc-horas-equipe", b: "calc-custo-equipe", fator: SEMANAS_POR_MES, saida: "calc-r3", texto: "por mês em gente fora do trabalho que importa" },
  ];
  const textosVazios = ["= faturamento que não entrou", "= prejuízo direto", "= gente fora do trabalho que importa"];
  let total = 0;
  let algum = false;
  linhas.forEach((linha, i) => {
    const a = numero(linha.a);
    const b = numero(linha.b);
    const saida = document.getElementById(linha.saida);
    if (a === null || b === null) {
      saida.textContent = textosVazios[i];
      return;
    }
    const valor = a * b * linha.fator;
    total += valor;
    algum = true;
    saida.innerHTML = `= <strong>${reais.format(valor)}</strong> ${linha.texto}`;
  });
  custoMensalEstimado = algum ? Math.round(total) : null;
  document.getElementById("calc-total").textContent = algum ? `${reais.format(total)} por mês` : "Preencha os campos acima";
}

const calculadora = document.getElementById("calculadora");
calculadora.addEventListener("input", atualizarCalculadora);
calculadora.addEventListener("submit", (e) => e.preventDefault());

/* ---------- Galeria de telas ---------- */
const abas = Array.from(document.querySelectorAll('.galeria-abas [role="tab"]'));
const telaImg = document.getElementById("tela-img");
const telaLink = document.getElementById("tela-link");
const telaLegenda = document.getElementById("tela-legenda");
const telaTitulo = document.getElementById("tela-titulo");
const painel = document.getElementById("painel-telas");

function selecionarAba(aba, focar) {
  abas.forEach((outra) => {
    const ativa = outra === aba;
    outra.setAttribute("aria-selected", String(ativa));
    outra.tabIndex = ativa ? 0 : -1;
  });
  const tela = aba.dataset.tela;
  telaImg.src = `img/${tela}.webp`;
  telaImg.srcset = `img/${tela}-800.webp 800w, img/${tela}.webp 1440w`;
  telaImg.alt = aba.dataset.alt;
  telaLink.href = `img/${tela}.webp`;
  telaLegenda.textContent = aba.dataset.legenda;
  telaTitulo.textContent = `fabricaflow · ${aba.textContent}`;
  painel.setAttribute("aria-labelledby", aba.id);
  if (focar) aba.focus();
  aba.scrollIntoView({ block: "nearest", inline: "nearest", behavior: "smooth" });
}

abas.forEach((aba, i) => {
  aba.addEventListener("click", () => selecionarAba(aba, false));
  aba.addEventListener("keydown", (e) => {
    const teclas = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 };
    if (e.key in teclas) {
      e.preventDefault();
      selecionarAba(abas[(i + teclas[e.key] + abas.length) % abas.length], true);
    } else if (e.key === "Home" || e.key === "End") {
      e.preventDefault();
      selecionarAba(e.key === "Home" ? abas[0] : abas[abas.length - 1], true);
    }
  });
});

// Pré-carrega as outras telas depois que a página terminar de carregar.
window.addEventListener("load", () => {
  const largura = window.innerWidth <= 960 ? "-800" : "";
  abas.slice(1).forEach((aba) => { new Image().src = `img/${aba.dataset.tela}${largura}.webp`; });
});

/* ---------- Botão fixo no celular: aparece depois do topo e some quando o formulário aparece ---------- */
const ctaFixo = document.getElementById("cta-fixo");
if ("IntersectionObserver" in window) {
  const visivel = { topo: true, contato: false };
  const alvos = new Map([[document.querySelector(".hero-acoes"), "topo"], [document.getElementById("contato"), "contato"]]);
  const observador = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => { visivel[alvos.get(entrada.target)] = entrada.isIntersecting; });
    ctaFixo.classList.toggle("escondido", visivel.topo || visivel.contato);
  }, { rootMargin: "0px 0px -15% 0px" });
  alvos.forEach((_, alvo) => observador.observe(alvo));
} else {
  ctaFixo.classList.remove("escondido");
}

/* ---------- Formulário ---------- */
const form = document.getElementById("formulario");
const aviso = document.getElementById("f-aviso");
const botaoEnviar = document.getElementById("f-enviar");

const regras = {
  "f-nome": (v) => (v.trim().length >= 2 ? "" : "Informe seu nome."),
  "f-empresa": (v) => (v.trim().length >= 2 ? "" : "Informe o nome da empresa."),
  "f-email": (v) => (/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) ? "" : "Informe um e-mail válido, como nome@empresa.com.br."),
  "f-whatsapp": (v) => {
    const digitos = v.replace(/\D/g, "");
    return digitos.length >= 10 && digitos.length <= 13 ? "" : "Informe o WhatsApp com DDD, como (11) 90000-0000.";
  },
  "f-segmento": (v) => (v ? "" : "Escolha o segmento da sua fábrica."),
};

function validarCampo(id) {
  const campo = document.getElementById(id);
  const mensagem = id === "f-consentimento"
    ? (campo.checked ? "" : "Marque a autorização para podermos entrar em contato.")
    : regras[id](campo.value);
  const erro = document.getElementById(`${id}-erro`);
  erro.textContent = mensagem;
  if (mensagem) {
    campo.setAttribute("aria-invalid", "true");
    campo.setAttribute("aria-describedby", erro.id);
  } else {
    campo.removeAttribute("aria-invalid");
    campo.removeAttribute("aria-describedby");
  }
  return !mensagem;
}

const camposValidados = [...Object.keys(regras), "f-consentimento"];
camposValidados.forEach((id) => {
  const campo = document.getElementById(id);
  const evento = campo.type === "checkbox" || campo.tagName === "SELECT" ? "change" : "blur";
  campo.addEventListener(evento, () => validarCampo(id));
  campo.addEventListener("input", () => { if (campo.getAttribute("aria-invalid")) validarCampo(id); });
});

// Máscara leve para o WhatsApp: (11) 90000-0000
document.getElementById("f-whatsapp").addEventListener("input", (e) => {
  const d = e.target.value.replace(/\D/g, "").slice(0, 11);
  if (d.length > 6) e.target.value = `(${d.slice(0, 2)}) ${d.slice(2, d.length - 4)}-${d.slice(-4)}`;
  else if (d.length > 2) e.target.value = `(${d.slice(0, 2)}) ${d.slice(2)}`;
  else e.target.value = d;
});

// Remove caracteres de controle, limita o tamanho e neutraliza fórmulas de planilha (=, +, -, @)
// para que um texto malicioso não vire fórmula no Google Sheets ou no Excel.
function limpar(texto, maximo = 1000) {
  let t = String(texto).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, "").trim().slice(0, maximo);
  if (/^[=+\-@\t\r]/.test(t)) t = `'${t}`;
  return t;
}

function coletarDados() {
  const valor = (id) => limpar(document.getElementById(id).value);
  const dores = Array.from(form.querySelectorAll('input[name="dor"]:checked')).map((c) => c.value);
  const params = new URLSearchParams(window.location.search);
  return {
    nome: valor("f-nome"),
    empresa: valor("f-empresa"),
    cargo: valor("f-cargo"),
    email: valor("f-email"),
    whatsapp: valor("f-whatsapp"),
    cidade: valor("f-cidade"),
    segmento: valor("f-segmento"),
    funcionarios: valor("f-funcionarios"),
    principal_dor: dores.join(", "),
    mensagem: valor("f-mensagem"),
    consentimento_lgpd: "sim",
    custo_mensal_estimado: custoMensalEstimado === null ? "" : String(custoMensalEstimado),
    utm_source: limpar(params.get("utm_source") || "", 100),
    utm_medium: limpar(params.get("utm_medium") || "", 100),
    utm_campaign: limpar(params.get("utm_campaign") || "", 100),
    pagina: limpar(window.location.origin + window.location.pathname, 200),
    origem: ORIGEM_FORMULARIO,
    tempo_preenchimento_s: String(Math.round((Date.now() - paginaAbertaEm) / 1000)),
    enviado_em: new Date().toISOString(),
  };
}

function linkWhatsApp(dados) {
  const texto = dados
    ? `Olá, Igor! Quero agendar a demonstração do FábricaFlow. Sou ${dados.nome}, da ${dados.empresa}` +
      `${dados.cidade ? ` (${dados.cidade})` : ""}, segmento ${dados.segmento}.`
    : "Olá, Igor! Quero agendar a demonstração do FábricaFlow.";
  return `https://wa.me/${WHATSAPP_NUMERO}?text=${encodeURIComponent(texto)}`;
}

function mostrarAviso(tipo, html) {
  aviso.className = `aviso aviso-${tipo}`;
  aviso.innerHTML = html;
  aviso.hidden = false;
  aviso.scrollIntoView({ block: "nearest", behavior: "smooth" });
}

function escapar(texto) {
  return texto.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

async function enviar(dados) {
  if (!endpointConfigurado) throw new Error("Endpoint do formulário ainda não configurado.");
  const controle = new AbortController();
  const timer = setTimeout(() => controle.abort(), TEMPO_LIMITE_MS);
  try {
    // Envio como formulário (application/x-www-form-urlencoded): é uma requisição "simples",
    // sem pré-verificação CORS, e o Zapier recebe cada campo separado.
    const resposta = await fetch(ENDPOINT_FORMULARIO, {
      method: "POST",
      body: new URLSearchParams(dados),
      signal: controle.signal,
    });
    if (!resposta.ok) throw new Error(`Resposta ${resposta.status}`);
  } finally {
    clearTimeout(timer);
  }
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  aviso.hidden = true;

  const invalidos = camposValidados.filter((id) => !validarCampo(id));
  if (invalidos.length) {
    document.getElementById(invalidos[0]).focus();
    return;
  }

  // Robôs costumam preencher o campo escondido ou enviar rápido demais: finge sucesso e não envia.
  if (document.getElementById("f-site").value || Date.now() - paginaAbertaEm < TEMPO_MINIMO_MS) {
    form.reset();
    mostrarAviso("ok", "<strong>Pedido recebido.</strong>");
    return;
  }

  const dados = coletarDados();
  try { ultimoEnvioEm = Math.max(ultimoEnvioEm, Number(localStorage.getItem("ff_ultimo_envio")) || 0); } catch (_) { /* sem armazenamento */ }
  if (Date.now() - ultimoEnvioEm < INTERVALO_ENTRE_ENVIOS_MS) {
    mostrarAviso("ok",
      `<strong>Já recebemos seu pedido.</strong>` +
      `<span>Para mudar alguma informação, chame no WhatsApp <a href="${linkWhatsApp(dados)}" target="_blank" rel="noopener">${WHATSAPP_EXIBICAO}</a>.</span>`);
    return;
  }
  botaoEnviar.disabled = true;
  botaoEnviar.textContent = "Enviando…";
  try {
    await enviar(dados);
    ultimoEnvioEm = Date.now();
    try { localStorage.setItem("ff_ultimo_envio", String(ultimoEnvioEm)); } catch (_) { /* sem armazenamento */ }
    form.reset();
    mostrarAviso("ok",
      `<strong>Pedido recebido, ${escapar(dados.nome.split(" ")[0])}!</strong>` +
      `<span>O Igor vai falar com você pelo WhatsApp ou e-mail para combinar o melhor horário da demonstração.</span>` +
      `<span>Se preferir adiantar, chame agora no WhatsApp <a href="${linkWhatsApp(dados)}" target="_blank" rel="noopener">${WHATSAPP_EXIBICAO}</a>.</span>`);
  } catch (erro) {
    console.warn("Falha no envio do formulário:", erro);
    mostrarAviso("erro",
      `<strong>Não conseguimos registrar seu pedido agora.</strong>` +
      `<span>Seus dados continuam preenchidos. Fale direto com o Igor pelo WhatsApp ${WHATSAPP_EXIBICAO}: a mensagem já vai pronta.</span>` +
      `<a class="botao" href="${linkWhatsApp(dados)}" target="_blank" rel="noopener">Chamar no WhatsApp</a>`);
  } finally {
    botaoEnviar.disabled = false;
    botaoEnviar.textContent = "Agendar minha demonstração";
  }
});
