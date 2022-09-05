# Scraper
O scraper é um bot de coleta de dados de páginas web, ele realiza a coleta em uma página por meio de uma spider e para cada página nova é necessário criar uma nova spider.

##### Primeiro é necessário baixar as dependências:<br>
* **scrapy**:`pip install scrapy`

O scraper está dividido cinco arquivos em uma pasta, os arquivos são:<br>
* settings.py para a configuração do bot de coleta de dados;
* pipelines.py que define oprações de formatação para os dados coletados; 
* middlewares.py configura a operação das spiders;
* items.py permite customisar como os dados do site serão formatados; 
* pasta spiders é onde ficam os arquivos com as spiders;

#### Contribuindo:
Para ajudar a com o projeto é possivel adicionar novas spiders para abranger uma gama maior de críticas de jogos.
**Adicionado Spider:**
* É preciso criar um novo arquivo .py, para isso pode ser executado o comando `scrapy genspider [nome do arquivo] [URL do site alvo]`. Note: que o nome do arquivo de preferencia tem ser igual a nome do site escolhido.
* Preencher o metodo parse da classe criada com o a estrutura que vai ser armazenada e de onde vem cada informação
![exemplo](https://raw.githubusercontent.com/keiyanishio/Projeto3-TechWeb/main/imagens/exemplo_parse.png)
* Adicionar pipelines de limpiza para os dados caso necessário

**Testando:**
Para testar se o elemento css escolhido está dando a resposta esperada é possivel abrir o shell do scrapy com `scrapy shell` executar o comando `fetch('URL')` e depois executar `response.css(classe).get`.

**Para aprender mais sobre a biblioteca:**
https://docs.scrapy.org/en/latest/index.html