create database Detailzwork;
use Detailzwork;
create table PersonData(PersonName varchar(30), PersonAge int);
insert into PersonData(PersonName,PersonAge) values("Bhavya",21);
select * from PersonData;

create database Worker_Detailz;
use Worker_Detailz;
create table Worker_Detailz(Worker_Name varchar(30), Worker_Position varchar(20), Worker_Age int, Worker_Native_Dt varchar(50));
insert into Worker_Detailz(Worker_Name, Worker_Position, Worker_Age, Worker_Native_Dt) values ("Mownika","Buss.Member_Own",25,"Karaikal");
select * from Worker_Detailz;

