
PRAGMA foreign_keys = ON;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR
);

CREATE TABLE materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    advice VARCHAR
);

CREATE TABLE addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address VARCHAR
);

CREATE TABLE materials_addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER,
    address_id INTEGER,
    FOREIGN KEY (material_id) REFERENCES materials(id),
    FOREIGN KEY (address_id) REFERENCES addresses(id)
);

INSERT INTO materials (name, advice) VALUES ('Бумага', 'Переробці підлягають: білий папір, картон, пакувальні коробки, пакети з паперу, флаєри, листівки, газети, журнали, зошити і альбоми для малювання. Для переробки не підходять: вироби з переробленого паперу (наприклад, лотки для яєць), змішана упаковка (Tetra Pak, Pure Pak), магазинні чеки і транспортні квитки, папір з етикеткою поверхнею, також ламінована і господарська папір. На переробку візьмуть сухі і чисті паперові відходи. Пакувальний папір не повинний містити залишків їжі.');
INSERT INTO materials (name, advice) VALUES ('Скло', 'Переробці підлягають: банки, пляшки, а також бита тара і віконне скло. Переробляється: армоване скло, дзеркала, кришталь, кераміку, а також жаро- і ударостійке скло. Тару для переробки необхідно підготувати. Пляшки і банки повинні бути вимиті і висушені. Також з них необхідно зняти всі етикетки.');
INSERT INTO materials (name, advice) VALUES ('Пластик', 'Переробці підлягають: пляшки (з маркуванням PET або PETTE), пляшки і флакони (з маркуванням HDPE, PEHD, PE), а також кришки, поліетилен (у вигляді плівки), поліпропілен (у вигляді плівки, флаконів або контейнерів), полістирол, упаковки Tetra Pak, Pure Pak. На переробку не приймуть: непрозорі кольорові пляшки PET чорного, білого і жовтого кольорів, пластик без коду переробки, ПВХ, а також обгортки від цукерок, коктейльні трубочки і зубні щітки. Пластик для подальшої переробки необхідно вимити, висушити і спресувати.');
INSERT INTO materials (name, advice) VALUES ('Метал', 'Переробці підлягають: бляшані банки від консервів, чаю, кави, цукерок, алюмінієві банки від напоїв і пива, бляшані кришки, фольга і аерозольні балончики. Переробляється: небезпечні відходи (батарейки, акумулятори), фольгу з залишками їжі. Перед тим як відправити алюмінієві і бляшані банки в сміттєвий контейнер, їх необхідно вимити, висушити і по можливості зім`яти.');

INSERT INTO addresses (address) VALUES ('вул. 23 Серпня, 41 - А, ЖК "Салют"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 20, ОСББ "Лісний"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 22, ОСББ "Авангард"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 24-А, ОСББ "Машинобудівельник"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 24, ОСББ "Союз"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 18, ОСББ "Ліс"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 18, ЖК "Уют"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 14, ОСББ "ВУЗ"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 24-Б, ОСББ "Вогник"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 24-Б, ЖК "Хімік"');
INSERT INTO addresses (address) VALUES ('вул.Дерев`янко, 16-Б, ЖК "Сокіл-2"');
INSERT INTO addresses (address) VALUES ('вул.Космонавтів, 5 - А, ОСББ "ПТИМАШ"');
INSERT INTO addresses (address) VALUES ('вул.Космонавтів, 5 - А, ЖК "УЧИТЕЛЬ"');
INSERT INTO addresses (address) VALUES ('вул.Космонавтів, 7 - А, ЖК "Супутник"');
INSERT INTO addresses (address) VALUES ('вул.Космонавтів, 6, ОСББ "Зеніт"');
INSERT INTO addresses (address) VALUES ('вул.Космонавтів, 8, ОСББ "Травневе"');

INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 8);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 8);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 8);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 8);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 9);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 9);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 9);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 9);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 10);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 10);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 10);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 10);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 11);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 11);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 11);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 11);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 12);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 12);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 12);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 12);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 13);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 13);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 13);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 13);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 14);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 14);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 14);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 14);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 15);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 15);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 15);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 15);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 16);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 16);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 16);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 16);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 17);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 17);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 17);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 17);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 18);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 18);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 18);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 18);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 19);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 19);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 19);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 19);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 20);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 20);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 20);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 20);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 21);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 21);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 21);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 21);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 22);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 22);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 22);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 22);
INSERT INTO materials_addresses (material_id, address_id) VALUES (5, 23);
INSERT INTO materials_addresses (material_id, address_id) VALUES (6, 23);
INSERT INTO materials_addresses (material_id, address_id) VALUES (7, 23);
INSERT INTO materials_addresses (material_id, address_id) VALUES (8, 23);