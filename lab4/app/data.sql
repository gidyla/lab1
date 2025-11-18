USE lab4;

INSERT INTO device_type (name) VALUES
('Laptop'), 
('Desktop'), 
('Printer'), 
('Smartphone'), 
('Tablet'),
('Monitor'),
('Scanner'),
('Camera'),
('Keyboard');

INSERT INTO give_service (describtion, service_time, device_condition, device_type_id) VALUES 
('New laptop provided', '2024-01-10', 'New', 1), 
('Desktop allocated', '2024-01-15', 'Used', 2), 
('Printer installed', '2024-02-01', 'New', 3), 
('Smartphone assigned', '2024-02-05', 'New', 4), 
('Tablet issued', '2024-02-10', 'Used', 5),
('Monitor set up', '2024-02-15', 'New', 6),
('Scanner configured', '2024-02-20', 'Used', 7),
('Camera mounted', '2024-02-25', 'New', 8),
('Keyboard connected', '2024-03-01', 'Used', 9);

INSERT INTO room_location (room, desk) VALUES 
('101', 'A1'), 
('102', 'B2'), 
('103', 'C3'), 
('104', 'D4'), 
('105', 'E5'),
('106', 'F6'),
('107', 'G7'),
('108', 'H8'),
('109', 'I9');


INSERT INTO office_location (office_adress, room_location_id) VALUES 
('Main Office', 1), 
('Branch A', 2), 
('Branch B', 3), 
('Data Center', 4), 
('Remote Site', 5),
('Headquarters', 6),
('Branch C', 7),
('Warehouse', 8),
('Support Office', 9);

INSERT INTO employee (name, surname) VALUES 
('John', 'Doe'), 
('Alice', 'Smith'), 
('Bob', 'Johnson'), 
('Charlie', 'Brown'), 
('David', 'White'),
('Emma', 'Davis'),
('Liam', 'Taylor'),
('Sophia', 'Martinez'),
('James', 'Hernandez');

INSERT INTO workplace (employee_id, office_location_id) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9);

INSERT INTO repair_service (describtion, service_time, device_condition, device_type_id) VALUES 
('Laptop screen replaced', '2024-03-10', 'Repaired', 1), 
('Desktop power supply fixed', '2024-03-15', 'Repaired', 2), 
('Printer roller changed', '2024-03-20', 'Repaired', 3), 
('Smartphone battery replaced', '2024-03-25', 'Repaired', 4), 
('Tablet touchscreen fixed', '2024-03-30', 'Repaired', 5),
('Monitor replaced', '2024-04-01', 'Repaired', 6),
('Scanner serviced', '2024-04-05', 'Repaired', 7),
('Camera lens replaced', '2024-04-10', 'Repaired', 8),
('Keyboard fixed', '2024-04-15', 'Repaired', 9);

INSERT INTO exchange_service (describtion, service_time, device_condition, device_type_id) VALUES 
('Laptop exchanged for newer model', '2024-04-01', 'New', 1), 
('Desktop swapped for upgraded version', '2024-04-05', 'New', 2), 
('Printer replaced with better model', '2024-04-10', 'New', 3), 
('Smartphone exchanged for latest version', '2024-04-15', 'New', 4), 
('Tablet upgraded to newest model', '2024-04-20', 'New', 5),
('Monitor exchanged for high-definition version', '2024-04-25', 'New', 6),
('Scanner replaced with latest model', '2024-04-30', 'New', 7),
('Camera swapped for upgraded version', '2024-05-05', 'New', 8),
('Keyboard replaced with ergonomic version', '2024-05-10', 'New', 9);

INSERT INTO update_service (describtion, service_time, device_condition, device_type_id) VALUES 
('Laptop OS updated', '2024-05-01', 'Updated', 1), 
('Desktop software patched', '2024-05-05', 'Updated', 2), 
('Printer firmware upgraded', '2024-05-10', 'Updated', 3), 
('Smartphone software updated', '2024-05-15', 'Updated', 4), 
('Tablet OS refreshed', '2024-05-20', 'Updated', 5),
('Monitor drivers updated', '2024-05-25', 'Updated', 6),
('Scanner software enhanced', '2024-06-01', 'Updated', 7),
('Camera firmware upgraded', '2024-06-05', 'Updated', 8),
('Keyboard configuration updated', '2024-06-10', 'Updated', 9);

INSERT INTO bugfix_service (describtion, service_time, device_condition, device_type_id) VALUES 
('Fixed laptop boot issue', '2024-06-01', 'Fixed', 1), 
('Resolved desktop crashing problem', '2024-06-05', 'Fixed', 2), 
('Printer connectivity bug fixed', '2024-06-10', 'Fixed', 3), 
('Smartphone app crash resolved', '2024-06-15', 'Fixed', 4), 
('Tablet screen lag issue fixed', '2024-06-20', 'Fixed', 5),
('Monitor display issue fixed', '2024-06-25', 'Fixed', 6),
('Scanner scanning error resolved', '2024-06-30', 'Fixed', 7),
('Camera autofocus bug fixed', '2024-07-05', 'Fixed', 8),
('Keyboard key not working issue fixed', '2024-07-10', 'Fixed', 9);

INSERT INTO workplace_give (give_service_id, workplace_id) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9);

INSERT INTO workplace_update (update_service_id, workplace_id) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9);

INSERT INTO workplace_exchange (exchange_service_id, workplace_id) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9);

INSERT INTO workplace_repair (repair_service_id, workplace_id) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9);

INSERT INTO workplace_bugfix(bugfix_service_id, workplace_id) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9);


drop procedure if exists get_exchange_by_device_type;
drop procedure if exists get_office_by_room;
drop procedure if exists get_employee_by_office;
drop procedure if exists get_office_by_employee;


delimiter //

create procedure get_exchange_by_device_type(device_type_id int)
begin
	select d.id, e.*
	from exchange_service e
	join device_type d on d.id = e.device_type_id
	where e.device_type_id = device_type_id;
end //

create procedure get_office_by_room(room_location_id int)
begin
	select r.id, o.*
	from office_location o
	join room_location r on r.id = o.room_location_id
	where o.room_location_id = room_location_id;
end //

create procedure get_employee_by_office(office_location_id int)
begin
	select w.*, e.*
	from employee e
	join workplace w on w.employee_id = e.id
	where w.office_location_id = office_location_id;
end //

create procedure get_office_by_employee(employee_id int)
begin
	select w.*, o.*
	from office_location o
	join workplace w on w.office_location_id = o.id
	where w.employee_id = employee_id;
end //

delimiter ;