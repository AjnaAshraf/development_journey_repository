create database expenses;
show databases;
use expenses;

create table expense(exp_id int primary key auto_increment,
date varchar(100) not null,
category varchar(100) not null,
amount decimal(10,2) not null,
payment_method enum('UPI', 'bank transfer', 'cash') DEFAULT 'cash'
);

desc expense;

insert into expense(date,category,amount,payment_method) values('12-8-2026', 'food', 40, 'UPI');
insert into expense(date,category,amount,payment_method) values('14-8-2026', 'transport', 120.00, 'cash');
insert into expense(date,category,amount,payment_method) values('15-8-2026', 'shopping', 850.50, 'UPI');
insert into expense(date,category,amount,payment_method) values('16-8-2026', 'groceries', 1250.00, 'bank transfer');
insert into expense(date,category,amount,payment_method) values('17-8-2026', 'food', 180.00, 'cash');
insert into expense(date,category,amount,payment_method) values('18-8-2026', 'entertainment', 500.00, 'UPI');
insert into expense(date,category,amount,payment_method) values('19-8-2026', 'electricity', 1450.75, 'bank transfer');
insert into expense(date,category,amount,payment_method) values('20-8-2026', 'transport', 300.00, 'UPI');
insert into expense(date,category,amount,payment_method) values('21-8-2026', 'medicine', 675.50, 'cash');

select * from expense where category='food';

update expense set amount = 350 where exp_id=1;

select * from expense;

