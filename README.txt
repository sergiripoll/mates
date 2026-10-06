PUBLICAR AMB GITHUB PAGES (sense instal·lar res)
1. Crea un repositori PÚBLIC a github.com (p. ex. "mates").
2. Add file > Upload files: arrossega el CONTINGUT d'aquesta carpeta (no la carpeta), incloent .github. Commit.
   Si .github no es puja: Add file > Create new file, nom ".github/workflows/publica.yml" i enganxa'n el contingut.
3. Settings > Pages > Source: "GitHub Actions".
4. Pestanya Actions: espera el check verd. La web queda a https://USUARI.github.io/mates/

AFEGIR MATERIAL: al repositori, entra a content/2n-cientific/<tema>/ (o 2n-social), Add file > Upload files,
deixa-hi el .md i Commit. En ~1 minut es publica i l'índex s'actualitza sol.
Capçalera: title, curs (2n), modalitat (cientific/social/tots), tema, tipus (teoria/exercicis/solucions)
Fórmules en LaTeX: $...$ i $$...$$. Solucions amagades: <details><summary>..</summary>..</details>
