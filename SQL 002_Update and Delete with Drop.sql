create database Work_Data;
use Work_Data;
create table Beautycare(W_Name varchar(30), Age int, Salary int, Care_Position varchar(30));
insert into Beautycare(W_Name, Age, Salary, Care_Position) Values("Dhivi", 21, 15000, "Program Developing");
insert into Beautycare(W_Name, Age, Salary, Care_Position) values("Anitha",25, 30000, "Prodect_Buying_Dep."), ("Vishnupriya", 19, 10000, "Program Managment"), ("Keerthi", 23, 20000, "Program Management"); 
select * from Beautycare;

insert into Beautycare(W_Name, Age, Salary, Care_Position) values("Bhavithra",20, 10000, "Mackup Artist"), ("Sanjana",23, 10000, "Mackup Artist");

select * from Beautycare where Age<20;
select W_Name from Beautycare where Salary<20000;
select W_Name,Salary from Beautycare where Salary>25000;

delete from Beautycare where Age<20;
update Beautycare set Salary=23000 where Care_Position="Program Managment";
update Beautycare set Salary=12000 where Care_Position="Mackup Artist";
SET SQL_SAFE_UPDATES = 0;

drop table Beautycare;