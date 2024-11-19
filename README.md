### Criar um serializer que transforme dados de uma entidade Book (Livro) em um formato JSON específico, incluindo alguns campos calculados.
**Descrição do Exercício:**
1. Crie um modelo Book com os seguintes campos: 
  - title: Título do livro
  - author: Nome do autor
  - published_date: Data de publicação
  - price: Preço do livro (DecimalField)
  - pages: Quantidade de páginas (IntegerField)
2. Crie um serializer BookSerializer que: 
  - Exponha os campos title, author e published_date diretamente.
  - Inclua um campo price_in_dollars que converte o valor do campo price de reais para dólares. (Você pode usar uma  taxa de conversão fictícia de 5.0 reais por dólar para simplificação).
  - O serializer deve validar o campo pages, garantindo que o número de páginas seja positivo.
3. Crie uma view que utilize esse serializer para listar todos os livros em formato JSON.
