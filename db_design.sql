
create table restaurant (
	id serial primary key
	name varchar(80) not null,
);


create table menu_item (
 	id serial primary key,
 	name varchar(80),
 	course varchar(250),
 	description varchar(250),
 	price varchar(8),
 	restaurant_id references restaurant (id)
);
