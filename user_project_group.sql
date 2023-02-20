insert into "user" (id, email, password_hash, role, verified, confirmed, name)
values ('00000000000101001101010100', 'soiltext@esoil.ru', '$2b$12$qIA6yewrMaGG3fEdr76n5eA9D1WttdVTjbZa34SZXCessrmkAq7gW', 'AUTHOR', true, true, 'SoilText');

insert into project_group (id, name, public, details, author_id) VALUES ('00000000000101001101010100', 'SoilText', false, 'SoilTextDetails', '00000000000101001101010100');