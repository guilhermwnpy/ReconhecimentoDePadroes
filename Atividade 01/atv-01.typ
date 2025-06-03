#import "lib.typ"

#show: lib.template.with(
  "Reconhecimento de Padrões", 
  "Atividade 01"
)

= Padrões

== Definição de "Padrão"

Um padrão, é de forma genérica um conjunto de características mensuráveis que definem um objeto. A partir dessas informações é possível analisar diferentes objetos com características semalhantes ou não, a fim de determinar uma relação entre eles, essa relação é dada pela classe que os objetos podem ser associados.

De uma forma mais científica, um padrão é um vetor contendo as *características* de um objeto. Tendo acesso as características relevantes de uma base de objetos é possível associar esses objetos a rótulos que os classificam.

== Exemplos de Padrões

=== Moedas

Tendo em vista que um padrão é um conjunto de características que definem um objeto, é possível tomar como exemplo moedas, onde há diversos tipos sendo atualmente fabricadas no Brasil.

Cada moeda diferente é um objeto que com suas características representam um padrão, onde as mais relevantes podem ser:

+ Diâmetro
+ Cor
+ Peso
+ Material

Cada moeda terá características únicas, mas haverá conjuntos de moedas com características que se assemelham umas as outras, a partir dessa semelhança de características ou diferença de características, é possível classificar o tipo de moeda entre moedas de R\$0,50, R\$0,25, R\$0,10, R\$0,05.

#align(center)[
  #table(
    columns: 5,
    align: center,
    [*Moeda*], [*Diâmetro (mm)*], [*Cor*], [*Peso (g)*], [*Material*],
    [R\$0,50], [23], [Cinza], [7,81], [Aço],
    [R\$0,25], [25], [Marrom], [7,55], [Aço + Bronze],
    [R\$0,10], [20], [Marrom], [4,8], [Aço + Bronze],
    [R\$0,5], [22], [Marrom], [4,10], [Aço + Cobre],
  )
]

== Base de dados

Acesso: https://tinyurl.com/guilherme-dataset-recpad

A base de dados é entitulada de "Mental Health" e disponibiliza um conjunto de dados realistas gerados a partir de uma simulação sintética de uma pesquisa de saúde mental global realizada com 10.000 indivíduos.

A base de dados de saúde mental tem 14 características e 10.000 objetos. As características são: age, gender, employment_status, work_environment, mental_health_history, seeks_treatment, stress_level, sleep_hours, physical_activity_days, depression_score, anxiety_score, social_support_score, productivity_score, mental_health_risk.

A partir de uma base de dados como essa é possível aplicar classificação, por exemplo, para prever "mental_health_risk" que é um atributo discretizado, onde pode ser facilmente rotulado. Assim como regressão para estimar por exemplo, o "stress_level" a partir dos valores em "sleep_hours", "physical_activity_days" e "social_support_score".