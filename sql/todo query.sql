create database todo_db;
use todo_db;

create table user(
	id int auto_increment primary key,
    name varchar(100) not null,
    email varchar(200) not null
    
);
desc user;
create table todo(
	id int auto_increment primary key,
    title varchar(400) not null,
    status varchar(200) not null,
    user_id int not null
);

insert into user (name,email) values('Ajmal Ashraf','ajnaashraf005@gmail.com'),
('Rahul Menon', 'rahulmenon01@gmail.com'),
('Neha Thomas', 'nehathomas02@gmail.com'),
('Arjun Nair', 'arjunnair03@gmail.com');

insert into todo (title, status, user_id) values
(' MySQL practice', 'Completed', 1),
('Reading - silent pateint', 'Pending', 1),
(' cooking', 'In Progress', 2),
('workout', 'Completed', 2),
('Learn subqueries', 'Pending', 3);


select * from user;
select * from todo;

