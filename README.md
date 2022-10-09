# Excel -> Python -> SQL

 Simples projeto de conversão de dados xlsx para SQL usando python e pandas

## Banco de dados
O banco de dados utilizado nesse projeto foi o PostreSQL, sendo necessário o driver de conectividade psycopg2-bynary!

## Intruções para uso!

Após clonar o repositório, execute os seguintes comandos:
``` 
pip install -r requirements.txt
```
Após isso, precisará criar um arquivo ".env" com os seguintes conteudos dentro dele:
```
DB_HOST=
DB_NAME=
DB_USER=
DB_PASS=
```
Para utilizar exatamente como está nesse código precisara criar uma tabela da seguiunta forma em seu banco de dados:
```
create table testes(
	id serial primary key,
	category varchar(15) not null,
	name varchar(25) not null,
	price numeric not null,
	desc_price numeric not null,
	sku varchar not null,
	route varchar(255) not null,
	img_main text not null,
	img_front text not null,
	img_right text not null,
	img_left text not null,
	img_back text not null,
	highlights boolean default 'FALSE' not null,
	is_available boolean default 'TRUE' not null
)

```
E agora é só utilizar 
