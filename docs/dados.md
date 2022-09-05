# Análise de Dados

##### Primeiro é necessário baixar as dependências:<br>
* **pandas**:`pip install pandas`
* **matplotlib**: `pip install matplolib`
* **numpy**: `pip install numpy`

O WebScraper, além de coletar as notas dos jogos, obteve outros parâmetros para fazer uma análise.<br>
Os parâmetros coletados no projeto foram título, nota, publisher, desenvolvedora e lançamento, apresentado no arquivo json.

![json](https://raw.githubusercontent.com/keiyanishio/Projeto3-TechWeb/main/imagens/arquivo_json.png)

Após a coleta e o arquivo GameInformer.json criado a ánalise pode ser feita. Assim, no arquivo Análise dos dados.ipynb está a análise do projeto. Duas análises foram apresentadas, a primeira foi a distribuição das notas dos jogos. E a segunda foi as notas dos jogos das seguintes distribuidoras: Nintendo, Sony Interactive Entertainment (Playstation) e Xbox Game Studios, para saber qual das empresas tem as melhores notas.

Distribuição das notas dos jogos:

![distribuicao](https://raw.githubusercontent.com/keiyanishio/Projeto3-TechWeb/main/imagens/distribuicao_de_notas.png)

Nintendo x Playstation x Xbox:

![distribuidora](https://raw.githubusercontent.com/keiyanishio/Projeto3-TechWeb/main/imagens/distribuidoras.png)

Como mencionado anteriormente, houve uma coleta de outros parâmetros pelo WebScraper, podendo futuramente fazer outros tipos de análises envolvendo esses dados. 