## Descição

Atividade 02 de Reconhecimento de Padrões, passada na aula 03 2025-05-22.

# Tarefa

Para essa atividade, vocês devem construir árvores de decisão para 3 bases diferentes, e medir a taxa de acertos de cada uma delas, que estão na nossa pasta compartilhada  

a) "diabéticos.txt"  
Para essa base de dados, vocês devem construir uma árvore de decisão com apenas um toco de decisão. Ou seja, a regra de classificação vai consistir em simplesmente perguntar se a glicemia é menor ou maior que um determinado limiar, e a partir daí a classe já será escolhida.   

b) "sinteticos1.txt"  
Para essa base de dados, vocês devem construir uma árvore de decisão com apenas dois tocos de decisão (igual a do exemplo que a gente construiu em sala). Essa é uma base sintética que eu criei, parecida com a que usei em sala como exemplo no quadro.  

c) "iris.txt"  
Para essa base de dados, vocês devem construir uma árvore de decisão com apenas dois tocos de decisão. Essa é uma base brinquedo clássica em problemas de reconhecimento de padrões. Se quiserem saber mais sobre ela, consultem esse link: [https://archive.ics.uci.edu/dataset/53/iris](https://archive.ics.uci.edu/dataset/53/iris)  


Instruções:  
- Para essa atividade, vocês devem entregar os códigos (um para cada item acima) e um documento em pdf (pode ser escrito em papel e escaneado, se preferir) com cada uma das 3 árvores, indicando claramente quais são os tocos de decisão e as folhas.  

- Para os itens b e c, vocês podem declarar um nó como uma folha sempre que a classe mais predominante possuir mais de 90% dos exemplos. Para o item a, haverá apenas um toco de decisão, então uma vez que ele for definido, as duas folhas também estão definidas.  

- Vocês não precisam construir um código que automaticamente construa toda a árvore de uma vez, testando todos os critérios de parada. Vai ser mais fácil se vocês forem construindo a árvore no papel, e usarem o código apenas para percorrer todas as perguntas possíveis em cada nó e encontrar a melhor partição para cada nó, além de verificar se ele já pode ser declarado uma folha.   

- Todas as bases de dados estão no formato txt, em que cada linha corresponde a um padrão  e a última coluna contém os rótulos. Se tiverem dificuldade em carregar os dados, me avisem. Mas saibam que, na prática, é comum que os dados venham em formatos diferentes e organizados de maneiras diferentes, então saber lidar com isso é uma habilidade importante.   

- Eu coloquei na pasta duas implementações do item A para vocês usarem como exemplo e consultarem em casos de dúvidas. Uma das implementações está em Octave ("arvore_de_decisao_octave.m") e a outra em Julia ("arvore_de_decisao_julia.jl").  

- Para o item a, o que vocês vão precisar fazer é essencialmente reproduzir os resultados que eu obtive nos códigos acima (mas por favor, não simplesmente copiem os exemplos, façam os códigos de vocês). Para os itens b e c vocês vão precisar fazer algumas extrapolações. Ao contrário do item a, os itens b e c possuem padrões multivariados (2d e 4d, respectivamente), então vocês vão precisar varrer todas as dimensões na hora de escolher a melhor partição. Para o item c, existe ainda outra extrapolação, pois a base de dados contém três classes, e não apenas duas como nos itens a e b.   

- Não se esqueçam de medir as taxas de acertos para cada árvore, podem se basear em como fiz nos dois códigos de exemplo.   

- Caso tenham dificuldades, podem discutir entre vocês, ou me consultar (no whatsapp ou pessoalmente, no grupo ou no privado). Mas não deixem de sentar e tentar fazer sozinho após isso.
