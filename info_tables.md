# Informações das tabelas no banco

### Criando o banco

Para carregar os dados, use o comando `psql -d news -f newsdata.sql`.
Eis o que faz este comando:

- `psql` — o programa de linha de comando PostgreSQL
- `-d news` — conecta ao banco de dados chamado news que foi criado para você
- `-f newsdata.sql` — executa as declarações SQL no arquivo newsdata.sql

Executar esse comando irá conectar você ao seu servidor de banco de dados instalado e executar os comandos SQL no arquivo baixado, criando tabelas e populando-as com dados.

*Explorando os dados*
Assim que tiver os dados carregados no seu banco de dados, conecte ao seu banco de dados usando `psql -d news` e explore as tabelas usando os comandos `\dt` e `\d table` e declarações `select`.

- `\dt` — display tables — lista as tabelas que estão disponíveis no banco de dados.
- `\d table` — (substitui table com o nome de uma tabela) — mostra o esquema do banco de dados para aquela tabela em particular.


### Todas as tabelas do banco.
```
 List of relations
 Schema |   Name   | Type  |  Owner  
--------+----------+-------+---------
 public | articles | table | vagrant
 public | authors  | table | vagrant
 public | log      | table | vagrant
(3 rows)
```

### Tabela articles
```
                                  Table "public.articles"
 Column |           Type           |                       Modifiers                       
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     | 
 body   | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)

```

### Tabela authors
```
                         Table "public.authors"
 Column |  Type   |                      Modifiers                       
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    | 
 id     | integer | not null default nextval('authors_id_seq'::regclass)
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)
```
### Tabela log
```
                                  Table "public.log"
 Column |           Type           |                    Modifiers                     
--------+--------------------------+--------------------------------------------------
 path   | text                     | 
 ip     | inet                     | 
 method | text                     | 
 status | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)
```