
Este projeto de Django será construido junto ao Curso Udemy Python.
O objetivo final das aulas é a criação de uma Agenda.

Informações importantes:
1. Pasta migrations do App - Registra e aplica configurações do models (BD);

Comandos importantes Locais:
1. runserver - Inicia o servidor;
2. createsuperuser - Cria o Super Usuário;
3. makemigrations - Atualiza as modificações nos models;
4. migrate - Aplica novas Atualizações;

Comandos importantes Servidor:
1. sudo add-apt-repository ppa:deadsnakes/ppa
> Adiciona o repositorio do Python
2. sudo apt install pythonX.XX pythonX.XX-venv
3. git init --bare
> Repositorio bare, para onde os desenvolvedores fazem commit, parecido com: git push origin main
>> O 'origin' faz referência ao GitHub.
>> Esse repositório é destinado apenas a push e pull, sem área de trabalho ou árvore de mudanças.
> Já no bare, usa-se git push "repositorio-próprio" main
4. git remote add agendarepo ~/agendarepo/
> Com este comando o repositório '--bare' funcionara como um ponto central de sincronização.
>> Funciona parecido como o GitHub.

Comandos importantes Postgre:
1. sudo -U postgres psql

Comandos importantes gerais:
1. python3 -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"

Ferramentas:
1. Adicionar/Editar/Apagar Contatos;
2. Criar perfil de Usuário;
3. Validação de usuário e senha;
4. Validação de senha forte;
