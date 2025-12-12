-- select * from `zootopia_classification`;
insert into `zootopia_classification`(type)
values
	("Mammal"),
	("Bird"),
	("Amphibian"),
	("Reptile");

-- select * from `zootopia_location`;
insert into `zootopia_location`(continent, habitat)
values
	("Asia", "tropical rainforests"),
    ("Asia", "evergreen forests"),
    ("Africa", "dry deciduous forests"),
    ("North America", "wetlands"),
    ("North America", "marshes"),
    ("South America", "rainforests"),
    ("South America", "tropical rainforests"),
    ("Europe", "woodlands"),
    ("Europe", "forest edges");

-- select * from `zootopia_animal`;
insert into `zootopia_animal`(name, age, species, weight, classification_id, animal_habitat_id)
values
	("Mort", 3, "Mouse lemur", 0.13, 
		(select id from `zootopia_classification` where type = "Mammal"), 
        (select id from `zootopia_location` where continent="Africa" and habitat ="dry deciduous forests")),
	("King Julien", 7, "King Julien", 15.5, 
		(select id from `zootopia_classification` where type = "Mammal"), 
        (select id from `zootopia_location` where continent="Africa" and habitat ="dry deciduous forests")),
    ("Leila", 13, "Jaguar", 157.8, 
		(select id from `zootopia_classification` where type = "Mammal"), 
        (select id from `zootopia_location` where continent="South America" and habitat ="tropical rainforests")),
	("Madison", 5, "Capybara", 99.3, 
		(select id from `zootopia_classification` where type = "Mammal"), 
        (select id from `zootopia_location` where continent="South America" and habitat ="rainforests")),
    ("Rich", 47, "Alligator", 620.1, 
		(select id from `zootopia_classification` where type = "Reptile"), 
        (select id from `zootopia_location` where continent="North America" and habitat ="marshes")),
	("Rick", 2, "Garter Snake", 0.24, 
		(select id from `zootopia_classification` where type = "Reptile"), 
        (select id from `zootopia_location` where continent="North America" and habitat ="wetlands")),
	("Max", 6, "European Badger", 21.4, 
		(select id from `zootopia_classification` where type = "Mammal"), 
        (select id from `zootopia_location` where continent="Europe" and habitat ="woodlands")),
	("Red", 4, "Red Fox", 9.9, 
		(select id from `zootopia_classification` where type = "Mammal"), 
        (select id from `zootopia_location` where continent="Europe" and habitat ="forest edges")),
	("Tigress", 11, "Bengal Tiger", 370.7, 
		(select id from `zootopia_classification` where type = "Mammal"), 
        (select id from `zootopia_location` where continent="Asia" and habitat ="tropical rainforests")),
	("Big Back", 49, "Asian Elephant", 7492.5, 
		(select id from `zootopia_classification` where type = "Mammal"), 
        (select id from `zootopia_location` where continent="Asia" and habitat ="evergreen forests"));
        
-- select * from `zootopia_medication`;
insert into `zootopia_medication`(medication_name)
values
	-- antibiotics
	("Florfenicol"),
    ("Tulathromycin"),
    -- antiparasitics
    ("Fenbendazole"),
    ("Fipronil"),
    -- opioids
    ("Etorphine"),
    ("Thiafentanil");
    
-- select * from `zootopia_animalmedicationlog`;
insert into `zootopia_animalmedicationlog`(date, animal_id, medication_id, medication_amount)
values
	-- Mort
	('2025-02-14 08:23:47.384756', (select id from `zootopia_animal` where name = "Mort"), (select id from `zootopia_medication` where medication_name = "Florfenicol"), 20.55),
    ('2025-03-22 15:42:19.629384', (select id from `zootopia_animal` where name = "Mort"), (select id from `zootopia_medication` where medication_name = "Fipronil"), 5.01),
    ('2025-01-09 22:17:33.847293', (select id from `zootopia_animal` where name = "Mort"), (select id from `zootopia_medication` where medication_name = "Etorphine"), 17.55),
    -- King Julien
    ('2025-05-18 11:56:08.192847', (select id from `zootopia_animal` where name = "King Julien"), (select id from `zootopia_medication` where medication_name = "Tulathromycin"), 50.54),
    ('2025-07-03 19:28:44.475629', (select id from `zootopia_animal` where name = "King Julien"), (select id from `zootopia_medication` where medication_name = "Fenbendazole"), 44.52),
    ('2025-04-11 03:09:27.738291', (select id from `zootopia_animal` where name = "King Julien"), (select id from `zootopia_medication` where medication_name = "Thiafentanil"), 84.31),
    -- Leila
    ('2025-08-29 14:33:51.926384', (select id from `zootopia_animal` where name = "Leila"), (select id from `zootopia_medication` where medication_name = "Tulathromycin"), 75.2),
    ('2025-06-07 07:44:16.584736', (select id from `zootopia_animal` where name = "Leila"), (select id from `zootopia_medication` where medication_name = "Fipronil"), 12.3),
    ('2025-09-15 20:19:02.293847', (select id from `zootopia_animal` where name = "Leila"), (select id from `zootopia_medication` where medication_name = "Thiafentanil"), 92.1),
    -- Madison
    ('2025-01-27 05:52:38.647382', (select id from `zootopia_animal` where name = "Madison"), (select id from `zootopia_medication` where medication_name = "Florfenicol"), 15.8),
    ('2025-10-22 16:08:24.829463', (select id from `zootopia_animal` where name = "Madison"), (select id from `zootopia_medication` where medication_name = "Fipronil"), 50.3),
    ('2025-03-06 09:41:59.193847', (select id from `zootopia_animal` where name = "Madison"), (select id from `zootopia_medication` where medication_name = "Etorphine"), 73.6),
    -- Rich
    ('2025-11-13 23:15:35.584920', (select id from `zootopia_animal` where name = "Rich"), (select id from `zootopia_medication` where medication_name = "Tulathromycin"), 12.6),
    ('2025-02-19 12:27:11.738291', (select id from `zootopia_animal` where name = "Rich"), (select id from `zootopia_medication` where medication_name = "Fenbendazole"), 36.5),
    ('2025-05-04 01:58:47.926475', (select id from `zootopia_animal` where name = "Rich"), (select id from `zootopia_medication` where medication_name = "Thiafentanil"), 4.58),
    -- Rick
    ('2025-07-21 18:34:23.384756', (select id from `zootopia_animal` where name = "Rick"), (select id from `zootopia_medication` where medication_name = "Florfenicol"), 73.5),
    ('2025-04-08 04:11:59.647382', (select id from `zootopia_animal` where name = "Rick"), (select id from `zootopia_medication` where medication_name = "Fipronil"), 28.53),
    ('2025-08-16 17:46:35.829463', (select id from `zootopia_animal` where name = "Rick"), (select id from `zootopia_medication` where medication_name = "Etorphine"), 12.55),
    -- Max
    ('2025-06-24 06:23:11.193847', (select id from `zootopia_animal` where name = "Max"), (select id from `zootopia_medication` where medication_name = "Tulathromycin"), 15.32),
    ('2025-10-01 19:57:47.584920', (select id from `zootopia_animal` where name = "Max"), (select id from `zootopia_medication` where medication_name = "Fenbendazole"), 54.26),
    ('2025-01-15 08:32:23.738291', (select id from `zootopia_animal` where name = "Max"), (select id from `zootopia_medication` where medication_name = "Thiafentanil"), 74.23),
    -- Red
    ('2025-09-09 21:14:59.926475', (select id from `zootopia_animal` where name = "Red"), (select id from `zootopia_medication` where medication_name = "Tulathromycin"), 87.45),
    ('2025-03-28 10:49:35.384756', (select id from `zootopia_animal` where name = "Red"), (select id from `zootopia_medication` where medication_name = "Fipronil"), 75.67),
    ('2025-11-05 23:26:11.647382', (select id from `zootopia_animal` where name = "Red"), (select id from `zootopia_medication` where medication_name = "Etorphine"), 57.76),
    -- Tigress
    ('2025-02-11 13:03:47.829463', (select id from `zootopia_animal` where name = "Tigress"), (select id from `zootopia_medication` where medication_name = "Tulathromycin"), 25.34),
    ('2025-07-30 02:38:23.193847', (select id from `zootopia_animal` where name = "Tigress"), (select id from `zootopia_medication` where medication_name = "Fenbendazole"), 23.67),
    ('2025-05-17 15:12:59.584920', (select id from `zootopia_animal` where name = "Tigress"), (select id from `zootopia_medication` where medication_name = "Thiafentanil"), 75.74),
    -- Big Back
    ('2025-12-04 05:49:35.738291', (select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_medication` where medication_name = "Tulathromycin"), 25.13),
    ('2025-04-23 18:21:11.926475', (select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_medication` where medication_name = "Fipronil"), 12.55),
    ('2025-08-11 08:56:47.384756', (select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_medication` where medication_name = "Etorphine"), 81.45);

-- select * from `zootopia_food`;
insert into `zootopia_food`(food_name)
values
	-- Meat (carcass)
	("mice"),
    ("rabbit"),
    ("squirrel"),
    ("deer"),
    ("poultry"),
    ("fish"),
    ("frog"),
    ("lizard"),
    ("cattle"),
    -- Feed
    ("primate biscuits"),
    ("carnivore chow"),
    -- Bugs
    ("beetles"),
    -- Fruits & Veggies
    ("strawberries"),
    ("blueberries"),
    ("wildberries"),
    ("pears"),
    ("apples"),
    ("figs"),
    ("lettuce"),
    ("kale"),
    ("bell peppers"),
    ("zucchini"),
    -- Other
    ("earthworms");
    
-- select * from `zootopia_diet`;
insert into `zootopia_diet`(animal_id, food_name_id)
values
	-- Mort
	((select id from `zootopia_animal` where name = "Mort"), (select id from `zootopia_food` where food_name = "beetles")),
    ((select id from `zootopia_animal` where name = "Mort"), (select id from `zootopia_food` where food_name = "blueberries")),
    ((select id from `zootopia_animal` where name = "Mort"), (select id from `zootopia_food` where food_name = "strawberries")),
    ((select id from `zootopia_animal` where name = "Mort"), (select id from `zootopia_food` where food_name = "lettuce")),
    ((select id from `zootopia_animal` where name = "Mort"), (select id from `zootopia_food` where food_name = "kale")),
    -- King Julien
    ((select id from `zootopia_animal` where name = "King Julien"), (select id from `zootopia_food` where food_name = "beetles")),
    ((select id from `zootopia_animal` where name = "King Julien"), (select id from `zootopia_food` where food_name = "figs")),
    ((select id from `zootopia_animal` where name = "King Julien"), (select id from `zootopia_food` where food_name = "pears")),
    ((select id from `zootopia_animal` where name = "King Julien"), (select id from `zootopia_food` where food_name = "lettuce")),
    ((select id from `zootopia_animal` where name = "King Julien"), (select id from `zootopia_food` where food_name = "kale")),
    -- Leila
    ((select id from `zootopia_animal` where name = "Leila"), (select id from `zootopia_food` where food_name = "rabbit")),
    ((select id from `zootopia_animal` where name = "Leila"), (select id from `zootopia_food` where food_name = "deer")),
    ((select id from `zootopia_animal` where name = "Leila"), (select id from `zootopia_food` where food_name = "poultry")),
    ((select id from `zootopia_animal` where name = "Leila"), (select id from `zootopia_food` where food_name = "fish")),
    ((select id from `zootopia_animal` where name = "Leila"), (select id from `zootopia_food` where food_name = "carnivore chow")),
    -- Madison
    ((select id from `zootopia_animal` where name = "Madison"), (select id from `zootopia_food` where food_name = "zucchini")),
    ((select id from `zootopia_animal` where name = "Madison"), (select id from `zootopia_food` where food_name = "bell peppers")),
    ((select id from `zootopia_animal` where name = "Madison"), (select id from `zootopia_food` where food_name = "kale")),
    ((select id from `zootopia_animal` where name = "Madison"), (select id from `zootopia_food` where food_name = "lettuce")),
    ((select id from `zootopia_animal` where name = "Madison"), (select id from `zootopia_food` where food_name = "primate biscuits")),
    -- Rich
    ((select id from `zootopia_animal` where name = "Rich"), (select id from `zootopia_food` where food_name = "rabbit")),
    ((select id from `zootopia_animal` where name = "Rich"), (select id from `zootopia_food` where food_name = "deer")),
    ((select id from `zootopia_animal` where name = "Rich"), (select id from `zootopia_food` where food_name = "poultry")),
    ((select id from `zootopia_animal` where name = "Rich"), (select id from `zootopia_food` where food_name = "fish")),
    ((select id from `zootopia_animal` where name = "Rich"), (select id from `zootopia_food` where food_name = "cattle")),
    -- Rick
    ((select id from `zootopia_animal` where name = "Rick"), (select id from `zootopia_food` where food_name = "mice")),
    ((select id from `zootopia_animal` where name = "Rick"), (select id from `zootopia_food` where food_name = "frog")),
    ((select id from `zootopia_animal` where name = "Rick"), (select id from `zootopia_food` where food_name = "lizard")),
    ((select id from `zootopia_animal` where name = "Rick"), (select id from `zootopia_food` where food_name = "beetles")),
    -- Max
    ((select id from `zootopia_animal` where name = "Max"), (select id from `zootopia_food` where food_name = "apples")),
    ((select id from `zootopia_animal` where name = "Max"), (select id from `zootopia_food` where food_name = "wildberries")),
    ((select id from `zootopia_animal` where name = "Max"), (select id from `zootopia_food` where food_name = "mice")),
    ((select id from `zootopia_animal` where name = "Max"), (select id from `zootopia_food` where food_name = "frog")),
    ((select id from `zootopia_animal` where name = "Max"), (select id from `zootopia_food` where food_name = "primate biscuits")),
    -- Red
    ((select id from `zootopia_animal` where name = "Red"), (select id from `zootopia_food` where food_name = "mice")),
    ((select id from `zootopia_animal` where name = "Red"), (select id from `zootopia_food` where food_name = "rabbit")),
    ((select id from `zootopia_animal` where name = "Red"), (select id from `zootopia_food` where food_name = "squirrel")),
    ((select id from `zootopia_animal` where name = "Red"), (select id from `zootopia_food` where food_name = "carnivore chow")),
    -- Tigress
    ((select id from `zootopia_animal` where name = "Tigress"), (select id from `zootopia_food` where food_name = "poultry")),
    ((select id from `zootopia_animal` where name = "Tigress"), (select id from `zootopia_food` where food_name = "deer")),
    ((select id from `zootopia_animal` where name = "Tigress"), (select id from `zootopia_food` where food_name = "rabbit")),
    ((select id from `zootopia_animal` where name = "Tigress"), (select id from `zootopia_food` where food_name = "cattle")),
    -- Big Back
    ((select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_food` where food_name = "zucchini")),
    ((select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_food` where food_name = "bell peppers")),
    ((select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_food` where food_name = "kale")),
    ((select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_food` where food_name = "lettuce")),
    ((select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_food` where food_name = "pears")),
    ((select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_food` where food_name = "apples")),
    ((select id from `zootopia_animal` where name = "Big Back"), (select id from `zootopia_food` where food_name = "primate biscuits"));

-- select * from `zootopia_animalfeedinglog`;
insert into `zootopia_animalfeedinglog`(amount, last_fed, animal_id, food_name_id, zookeeper_id)
values
-- Mort
	(0.5, '2025-08-11 08:56:47.384756', 
		(select id from `zootopia_animal` where name="Mort"), 
        (select id from `zootopia_food` where food_name="kale"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(5, '2025-08-11 08:56:47.384756', 
		(select id from `zootopia_animal` where name="Mort"), 
        (select id from `zootopia_food` where food_name="blueberries"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(3, '2025-08-11 08:56:47.384756', 
		(select id from `zootopia_animal` where name="Mort"), 
        (select id from `zootopia_food` where food_name="beetles"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
-- King Julien lemur
    (5, '2025-08-11 08:46:47.384756', 
		(select id from `zootopia_animal` where name="King Julien"), 
        (select id from `zootopia_food` where food_name="kale"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(3, '2025-08-11 08:46:47.384756', 
		(select id from `zootopia_animal` where name="King Julien"), 
        (select id from `zootopia_food` where food_name="figs"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(2, '2025-08-11 08:46:47.384756', 
		(select id from `zootopia_animal` where name="King Julien"), 
        (select id from `zootopia_food` where food_name="pears"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(8, '2025-08-11 08:36:47.384756', 
		(select id from `zootopia_animal` where name="King Julien"), 
        (select id from `zootopia_food` where food_name="beetles"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
-- Leila jaguar
    (1, '2025-08-11 08:36:47.384756', 
		(select id from `zootopia_animal` where name="Leila"), 
        (select id from `zootopia_food` where food_name="deer"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(2, '2025-08-11 08:36:47.384756', 
		(select id from `zootopia_animal` where name="Leila"), 
        (select id from `zootopia_food` where food_name="rabbit"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
-- Madison capybara
	(3, '2025-08-11 07:56:47.384756', 
		(select id from `zootopia_animal` where name="Madison"), 
        (select id from `zootopia_food` where food_name="zucchini"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
	(4, '2025-08-11 07:56:47.384756', 
		(select id from `zootopia_animal` where name="Madison"), 
        (select id from `zootopia_food` where food_name="kale"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
	(3, '2025-08-11 07:56:47.384756', 
		(select id from `zootopia_animal` where name="Madison"), 
        (select id from `zootopia_food` where food_name="lettuce"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
-- Rich alligator
	(5, '2025-08-11 07:36:47.384756', 
		(select id from `zootopia_animal` where name="Rich"), 
        (select id from `zootopia_food` where food_name="fish"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(2, '2025-08-11 07:36:47.384756', 
		(select id from `zootopia_animal` where name="Rich"), 
        (select id from `zootopia_food` where food_name="poultry"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(4, '2025-08-11 07:36:47.384756', 
		(select id from `zootopia_animal` where name="Rich"), 
        (select id from `zootopia_food` where food_name="rabbit"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
-- Rick garter snake
	(1, '2025-08-11 07:39:47.384756', 
		(select id from `zootopia_animal` where name="Rick"), 
        (select id from `zootopia_food` where food_name="mice"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
	(1, '2025-08-11 07:39:47.384756', 
		(select id from `zootopia_animal` where name="Rick"), 
        (select id from `zootopia_food` where food_name="frog"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
	(4, '2025-08-11 07:39:47.384756', 
		(select id from `zootopia_animal` where name="Rick"), 
        (select id from `zootopia_food` where food_name="beetles"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
-- Max European badger
	(2, '2025-08-11 07:29:47.384756', 
		(select id from `zootopia_animal` where name="Max"), 
        (select id from `zootopia_food` where food_name="apples"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
	(3, '2025-08-11 07:29:47.384756', 
		(select id from `zootopia_animal` where name="Max"), 
        (select id from `zootopia_food` where food_name="frog"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
	(12, '2025-08-11 07:29:47.384756', 
		(select id from `zootopia_animal` where name="Max"), 
        (select id from `zootopia_food` where food_name="wildberries"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
-- Red red fox
	(2, '2025-08-11 07:22:47.384756', 
		(select id from `zootopia_animal` where name="Red"), 
        (select id from `zootopia_food` where food_name="rabbit"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(3, '2025-08-11 07:22:47.384756', 
		(select id from `zootopia_animal` where name="Red"), 
        (select id from `zootopia_food` where food_name="squirrel"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(3, '2025-08-11 07:22:47.384756', 
		(select id from `zootopia_animal` where name="Red"), 
        (select id from `zootopia_food` where food_name="mice"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
-- Tigress Bengal tiger
	(4, '2025-08-11 07:22:47.384756', 
		(select id from `zootopia_animal` where name="Tigress"), 
        (select id from `zootopia_food` where food_name="poultry"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
	(5, '2025-08-11 07:22:47.384756', 
		(select id from `zootopia_animal` where name="Tigress"), 
        (select id from `zootopia_food` where food_name="rabbit"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "patricc" and is_zookeeper=1)),
-- Big Back Asian elephant
	(12, '2025-08-11 07:12:47.384756', 
		(select id from `zootopia_animal` where name="Big Back"), 
        (select id from `zootopia_food` where food_name="zucchini"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(15, '2025-08-11 07:12:47.384756', 
		(select id from `zootopia_animal` where name="Big Back"), 
        (select id from `zootopia_food` where food_name="lettuce"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(10, '2025-08-11 07:12:47.384756', 
		(select id from `zootopia_animal` where name="Big Back"), 
        (select id from `zootopia_food` where food_name="apples"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1)),
	(13, '2025-08-11 07:12:47.384756', 
		(select id from `zootopia_animal` where name="Big Back"), 
        (select id from `zootopia_food` where food_name="kale"), 
        (select `zootopia_zookeeper`.id from `zootopia_zookeeper` join `zootopia_user` on `zootopia_zookeeper`.user_id = `zootopia_user`.id where first_name = "spongebop" and is_zookeeper=1));
        
-- select * from `zootopia_funfact`;
insert into `zootopia_funfact`(bio, fun_facts, animal_id)
values
-- Mort mouse lemur
	("Mort is a tiny, energetic mouse lemur who was found orphaned after a storm. 
    He’s extremely curious and loves climbing anything he can get his hands on. 
    Despite his size, he has a big personality and quickly becomes a favorite of anyone who meets him.", 
    "Mouse lemur are native to Madagascar and are the smallest primates.", 
    (select id from `zootopia_animal` where name="Mort")),
-- King Julien lemur
    ("In the wild, King Julien sustained severe damage to his spine. 
    Although he had surgery, but it was unsuccessfully. 
    He can't move it move it no more.", 
    "Lemurs society is ruled and lead by females.", 
    (select id from `zootopia_animal` where name="King Julien")),
-- Leila jaguar
    ("Leila was injured in a forest fire and brought in for medical care. 
    She’s fully healed now and is known for her stealthy movements and love of swimming.", 
    "Jaguars are able to crush turtle shells.", 
    (select id from `zootopia_animal` where name="Leila")),
-- Madison capybara
    ("Madison was rescued from an illegal pet trade operation. 
    She’s extremely friendly and often acts as the “big sister” to younger animals in her enclosure.", 
    "Capybaras usually live in groups of 10 to 20.", 
    (select id from `zootopia_animal` where name="Madison")),
-- Rich alligator
    ("Rich was rescued from a backyard pond where he’d outgrown the space and couldn’t hunt properly anymore. 
    He’s surprisingly laid-back for an alligator and spends most of his day floating with just his eyes above the water", 
    "Alligators have a bite force of around 2000 pounds per square inch.", 
    (select id from `zootopia_animal` where name="Rich")),
-- Rick garter snake
    ("Rich was rescued from a backyard pond where he’d outgrown the space and couldn’t hunt properly anymore. 
    He’s surprisingly laid-back for an alligator and spends most of his day floating with just his eyes above the water", 
    "Unlike most snakes, garter snakes give live birth.", 
    (select id from `zootopia_animal` where name="Rick")),
-- Max European badger
    ("Max was rescued from a collapsed burrow site. He’s shy at first but becomes outgoing once he trusts you.", 
    "European badgers may share their burrow with other animals like rabits.", 
    (select id from `zootopia_animal` where name="Max")),
-- Red red fox
    ("Red was found with a leg injury that prevented him from hunting. 
    After recovery, he became one of the most curious and energetic animals in the refuge.", 
    "Red fox screams can sometimes be mistaken for a human scream.", 
    (select id from `zootopia_animal` where name="Red")),
-- Tigress Bengal tiger
    ("Tigress was rescued from a roadside zoo where she lived in poor conditions. 
    Now she finally has space to roam and shows off her powerful leaps.", 
    "Bengal tigers can jump up to 16 feet.", 
    (select id from `zootopia_animal` where name="Tigress")),
-- Big Back Asian elephant
    ("Big Back was injured while working in a logging camp. 
    After his rescue, he’s become known for his gentle nature and his love for splashing water on caretakers.", 
    "Asian elephants are endangered due human factors like deforestation and poaching.", 
    (select id from `zootopia_animal` where name="Big Back"));
    