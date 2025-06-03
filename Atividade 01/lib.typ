#import "@preview/marginalia:0.1.3" as marginalia: note, wideblock

#let template(
  title,
  description,
  body
) = {

  set text(size: 11pt, font: "TeX Gyre Pagella")
  set par(justify: true)
  set heading(numbering: "1.")

  set par(
    justify: true
  )

  align(center+horizon)[
    #text(title, size: 20pt)

    #text(description, size: 17pt)

    #text("Guilherme Freire Franco", size: 14pt)

    #datetime.today().display()
  ]

  pagebreak()

  // Configuração de página
  set page(
    margin: (x: 2cm),
    footer: {
        set text(8pt)
        v(1fr)
        line(stroke: 0.5pt, length: 17cm)
        v(5pt)
        title
        h(1fr)
        context {
          counter(page).display(
            "1 / 1",
            both: true,
          )
        }
        v(0.75cm)
      },
  )
  
  body
}