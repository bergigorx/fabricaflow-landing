/* Menu lateral do celular: abre pelo botão ☰, fecha no X, no fundo escuro, no Esc ou ao escolher um link. */
(function () {
  const botao = document.querySelector(".menu-botao");
  const menu = document.getElementById("menu-lateral");
  const fundo = document.querySelector(".menu-fundo");
  if (!botao || !menu || !fundo) return;
  const fechar = menu.querySelector(".menu-fechar");

  // Marca a página atual.
  const atual = window.location.pathname;
  menu.querySelectorAll(".menu-links a[href]").forEach((a) => {
    const url = new URL(a.href, window.location.href);
    if (!url.hash && url.pathname === atual) a.setAttribute("aria-current", "page");
  });

  function abrir() {
    document.body.classList.add("menu-aberto");
    menu.removeAttribute("inert");
    botao.setAttribute("aria-expanded", "true");
    fechar.focus();
  }
  function fecharMenu(devolverFoco) {
    document.body.classList.remove("menu-aberto");
    menu.setAttribute("inert", "");
    botao.setAttribute("aria-expanded", "false");
    if (devolverFoco) botao.focus();
  }

  menu.setAttribute("inert", "");
  botao.addEventListener("click", abrir);
  fechar.addEventListener("click", () => fecharMenu(true));
  fundo.addEventListener("click", () => fecharMenu(true));
  menu.addEventListener("click", (e) => { if (e.target.closest("a")) fecharMenu(false); });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && document.body.classList.contains("menu-aberto")) fecharMenu(true);
  });
  // Ao voltar para a tela larga com o menu aberto, fecha.
  window.matchMedia("(min-width: 961px)").addEventListener("change", (m) => { if (m.matches) fecharMenu(false); });
})();
