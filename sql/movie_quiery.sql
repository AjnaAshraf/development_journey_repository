create database movie_db;
show databases;
use movie_db;

create table movie( 
id int primary key auto_increment, 
title varchar(200) not null,
year varchar(10) not null,
run_time int,
rating decimal(2,1) not null,
genre enum("action","comedy","thriller","drama","horror") default "action"
);

desc movie;

insert into movie(title,year,run_time,rating,genre) values('abcd',2002,120,8.5,'action');
insert into movie(title,year,run_time,rating,genre) values('kgf',2008,150,9.5,'action');
insert into movie(title,year,run_time,rating,genre) values('balan',2026,160,8.5,'drama');
insert into movie(title,year,run_time,rating,genre) values('spiderman',2026,130,8.5,'action');
insert into movie(title,year,run_time,rating,genre) values('khalifa',2026,160,9.5,'action');

select * from movie;
update movie set title = "athiradi" , year = 2025,run_time = 200,rating = 8.7,genre = "comedy" where id = 1;
select * from movie where id=1;