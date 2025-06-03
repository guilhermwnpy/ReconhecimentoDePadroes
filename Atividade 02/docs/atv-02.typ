#import "lib.typ"

#show: lib.template.with(
  "Reconhecimento de Padrões", 
  "Atividade 02"
)

= Árvores de Decisão

== Árvore 1 - Diabéticos

Essa árvore de decisão contém apenas um toco de decisão. Foi criado um vetor contendo todos os dados da coluna de glicemia de todos os padrões, e a partir da Teoria de Informação de Shannon e redução de impureza, foi possível determinar um limiar para separação de classes.

Limiar: 127

#align(center)[
  #pad(20pt)[
    #image("img/atv-02-diabeticos.png", width: 30em)
    ]
]

== Árvore 2 - Sintéticos

A base de dados `sintéticos` tem duas colunas de atributos e uma coluna que define qual a classe do padrão. A partir da Teoria de Informação de Shannon e redução de impurezas, para ambos os dois limiares dos dois tocos de decisão, foi encontrado que a melhor redução de impurezas foi encontrada nos atributos $X_2$.

1º Limiar: -1.55 \
2º Limiar: 5.36

#align(center)[
  #pad(20pt)[
     #image("img/atv-02-sinteticos.png", width: 30em)
    ]
]

#pagebreak()
== Árvore 3 - Íris

A base de dados `íris` tem 4 colunas de atributos, e a 5º coluna determina a classe dos padrões. 

1º Limiar: 0.8\
2º Limiar: 1.7

#align(center)[
  #pad(20pt)[
    #image("img/atv-02-iris.png", width: 30em)
    ]
]

