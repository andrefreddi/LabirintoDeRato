

## Labirinto do rato em busca profunda
---
#### Equipe: André F. Willian C.

---
### Funcionamento

Ao iniciar o código executando arquivo Main.py, podemos ver uma tela para o usuário inserir as informações

![image](https://user-images.githubusercontent.com/52337680/167725879-38a480e0-40e0-497d-81d2-2174be8c4ffc.png)

Onde podemos carregar o labirinto presente no repositório, inserir as posições do rato e saída e mostrar o caminho do rato.

---
#### Carregar Labirinto

Nesta tela podemos carregar o labirinto utilizado no programa, lembrando que caso queira pode ser alterado o labirinto.

![image](https://user-images.githubusercontent.com/52337680/167726260-e5f5e588-f7b6-4efa-8722-8d793bc2e128.png)

---
#### Inserir Posições do rato e da saída

Nesta tela podemos definir as posições do rato e da saída, podendo ser diferente da sugerida para o exercício, caso ocorra de um valor invalido, ira gerar um erro.

![image](https://user-images.githubusercontent.com/52337680/167726642-c7fcde21-0efc-428f-bfb6-56775c6bc70b.png)

Como o exercício pede, vamos colocar os valores 2 e 7 para o rato e 34 e 1 para a saída.

![image](https://user-images.githubusercontent.com/52337680/167726771-d766ae53-75a0-4801-b15f-cc906df0dd3b.png)

![image](https://user-images.githubusercontent.com/52337680/167726872-57390eff-0ccf-4e1f-b17a-1bdff2a3a7a1.png)
---
#### Mostrar caminho

Ao clicar em mostrar caminho o programa ira nos mostrar quantos passos o rato deu até chegar na saída.

![image](https://user-images.githubusercontent.com/52337680/167726984-a6b0796a-27ab-4d6d-908b-874554f81ba2.png)

OBS: Caso o rato não consiga chegar até o caminho de saída, ira retornar um erro.

Logo após ira nos mostrar o caminho do rato

![20220510_184900](https://user-images.githubusercontent.com/52337680/167727642-f54b7a4d-a676-4c00-acc4-6eb653632c12.gif)

---
#### Erro de não conseguir chegar a saída

Bom caso ele não consiga chegar a saída ele ira nos retornar um erro

Para isso vamos usar outro labirinto, menor porem o suficiente para esse teste.

Primeiro vamos ver como é o labirinto

Posições utilizadas:

![image](https://user-images.githubusercontent.com/52337680/167729762-61a7bc4e-827b-42e5-abd8-3d371dae6222.png)

Saída valida

![20220510_190642](https://user-images.githubusercontent.com/52337680/167729668-69e0b822-13de-47f8-bc89-9d85982f71d1.gif)

----
#### E agora vamos gerar nosso erro.

Posições utilizadas:

![image](https://user-images.githubusercontent.com/52337680/167729957-5cdad169-186a-45d9-97ed-f30117a0cd34.png)

E o retorno ao tentar exibir o caminho:

![image](https://user-images.githubusercontent.com/52337680/167729927-96b0698b-4679-4ec5-8d64-d1c1316532cc.png)


----

## Código

#### Arquivo Main

Apenas vamos chamar as demais funções

![image](https://user-images.githubusercontent.com/52337680/167730343-36103931-fa86-4617-808e-9a721ac74875.png) 

#### Arquivo App

Onde definimos os valores para nosso labirinto

Aqui definimos o nosso menu inicial:
![image](https://user-images.githubusercontent.com/52337680/167730452-83d76711-a5b2-470f-8d3d-db970d8b2b72.png)
Carregamos o arquivo do labirinto em formato .csv utilizando o filedialog junto ao askopenfilename
Foi a maneira mais simples que encontrei para essa solução, e ainda deixando disponível para testes.

![image](https://user-images.githubusercontent.com/52337680/167730543-56ee4986-eca7-4937-ad40-f2d2dc8a4b22.png)

Logo após ele converte o arquivo recebido em matriz, no arquivo Grafo.py

![image](https://user-images.githubusercontent.com/52337680/167731118-1f132c9c-0b01-4164-bf93-a4e7d6a47ed5.png)

Gerando a posições de cada elemento, usando os caminhos de inicio e destino que seta a busca em largura

![image](https://user-images.githubusercontent.com/52337680/167731251-5cc2f122-7413-48a6-baf9-3cc36d58b144.png)

Com o labirinto em matriz ele faz a conversão em Grafo

Utilizando da conversão em matriz. gera o grafo nos retornando as vértices e adicionando as arestas.

![image](https://user-images.githubusercontent.com/52337680/167731364-35f672a6-efff-4d01-98b4-d102b5d4ae3d.png)

E ainda no arquivo Grafo.py temos as definições das vértices para cor, pai e distancia

![image](https://user-images.githubusercontent.com/52337680/167731959-6e1bff7e-3c08-4dbd-bfa6-bdafcf6a97a3.png)

Onde retornamos o caminho que o rato percorreu no grafico

![image](https://user-images.githubusercontent.com/52337680/167732044-51cf2cf8-7340-49af-a96a-b5c11e7b7f2c.png)

Voltando ao App.py

Temos a janela onde definimos as posições

![image](https://user-images.githubusercontent.com/52337680/167732164-45096d07-ae0b-4897-9f96-9655b5a89312.png)

Onde faz a verificação, que nos pode gerar erro caso invalida

![image](https://user-images.githubusercontent.com/52337680/167732221-4f2304aa-fa1f-43a4-b777-8cc1fdf21768.png)

E a demonstração do caminho do rato

Função que verifica se o rato quem como chegar ate a saída
![image](https://user-images.githubusercontent.com/52337680/167732302-d5cf21f2-b591-48a4-8a7a-3f573cf5c5df.png)

O inicio da construção gráfica do caminho do rato e seu trajeto

![image](https://user-images.githubusercontent.com/52337680/167732458-9b3095a4-3428-403e-80ef-65f9b9a237d7.png)


E o While que faz sua construção gráfica e seu caminho ate a saída, fazendo com ela a animação 
Utilizei a biblioteca do pygame 
Primeira vez utilizando e tive bastante dificuldade <> https://www.pygame.org/news
![image](https://user-images.githubusercontent.com/52337680/167732563-e3d8f0bf-ca33-4cdf-97be-434c93d4ace5.png)

E por fim do App temos o atualiza informações que serve para validar os valores inseridos na primeira etapa

![image](https://user-images.githubusercontent.com/52337680/167732738-d617e252-bce8-4258-8353-4c02feb35466.png)


By

![20220510_184900](https://user-images.githubusercontent.com/52337680/167727642-f54b7a4d-a676-4c00-acc4-6eb653632c12.gif)




