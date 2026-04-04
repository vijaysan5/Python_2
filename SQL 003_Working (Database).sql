create database Students_Record;
use Students_Record;
create table Records(SName varchar(30), Class varchar(5), Section varchar(2), Revision_Mark int, Internal int);
insert into Records(SName,Class,Section,Revision_Mark,Internal) values ("Aravind", 10, "B", 432, 20),("Hanviya",10,"B", 380, 19);
insert into Records(SName,Class,Section,Revision_Mark,Internal) values ("Dhivi", 10, "B", 455, 18), ("Hawitha", 10, "A", 391, 18), ("Akash", 10, "A", 495, 21),("Francis", 10, "A", 468, 19);
insert into Records(SName,Class,Section,Revision_Mark,Internal) values ("Jeni", 10, "B", 375, 18);
select * from Records;

update Records set Internal=19 where Revision_Mark<400;
update Records set Internal=20 where Revision_Mark>400;
update Records set Internal=23 where Revision_Mark>450;
update Records set Revision_Mark=435 where Revision_Mark=455;

delete from Records where SName="Jeni";

select SName,Class,Section from Records where Revision_Mark>450;
select SName,Section,Revision_Mark from Records where Revision_Mark<400;


drop table Records;