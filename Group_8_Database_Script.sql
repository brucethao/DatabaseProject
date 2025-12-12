create database if not exists zoomanagement;
use zoomanagement;

delimiter $$
create procedure zookeeper_feeding_job(in p_animal_id int)
begin
	select food_name_id, amount, animal_id, last_fed, first_name, last_name
	from Zootopia_animalfeedinglog
	join Zootopia_zookeeper
	on Zootopia_animalfeedinglog.zookeeper_id = Zootopia_zookeeper.id
	join Zootopia_user
	on Zootopia_animalfeedinglog.zookeeper_id = Zootopia_user.id;
end $$
delimiter ;

call zookeeper_feeding_job();

create view zookeeper_paycheck
as 
select id, wage, hours, (wage*hours) as paycheck
from Zootopia_zookeeper
where wage*hours > 1000;

select * from zookeeper_paycheck;

create index user_index on Zootopia_user (id, username);