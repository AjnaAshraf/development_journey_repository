create database course_db;
use course_db;

create table course(
			id int auto_increment primary key,
            title varchar(200) not null,
            fee decimal(8,2) not null,
            duration varchar(200) not null
);

create table batch(
			id int auto_increment primary key,
            title varchar(200) unique not null,
            head_count int not null,
            course_id int not null
);

insert into course (title,fee,duration) values('MERN STACK',75000,'6.5 MONTHS');
insert into course (title,fee,duration) values('DJANGO',64000,'6 MONTHS');
insert into course (title,fee,duration) values('SOFTWARE TESTING',75000,'5 MONTHS');
insert into course (title,fee,duration) values('DATA SCIENCE',85000,'7.5 MONTHS');

select * from course;

insert into batch (title,head_count,course_id) values('pydjango june',40,2);
insert into batch (title,head_count,course_id) values('pydjango july',50,2);
insert into batch (title,head_count,course_id) values('DS june',40,4);
insert into batch (title,head_count,course_id) values('mern june',45,1);
insert into batch (title,head_count,course_id) values('pydjango Aug',35,2);
insert into batch (title,head_count,course_id) values('st aug',25,6);

select * from batch;
select * from course;

select course.title,course.fee,batch.title,batch.head_count from course left join batch on course.id = batch.course_id;
select course.title,course.fee,batch.title,batch.head_count from course inner join batch on course.id = batch.course_id;
select course.title,course.fee,batch.title,batch.head_count from course right join batch on course.id = batch.course_id;