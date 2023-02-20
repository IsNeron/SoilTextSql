import pandas as pd

ASSIGNED_PROJECT_SITE_PROPERTY = 'INSERT INTO assigned_project_site_property (project_id, property_slug, "order") VALUES '
ASSIGNED_PROJECT_SOIL_PROPERTY = 'INSERT INTO assigned_project_soil_property (project_id, property_slug, "order") VALUES '
ASSIGNED_PROJECT_SOIL_HORIZON_PROPERTY = 'INSERT INTO assigned_project_soil_horizon_property (project_id, property_slug, "order") VALUES '

def insert_assigned_site_properties(project_id: str):
    query_site = ''.join((ASSIGNED_PROJECT_SITE_PROPERTY, 
    '(\'', project_id, '\',', ' \'landuse\', 1), ' 
    '(\'', project_id, '\',', ' \'anthropogenic_influence\', 2), '
    '(\'', project_id, '\',', ' \'vegetation_l1\', 3), ' 
    '(\'', project_id, '\',', ' \'vegetation_l2\', 4) ' ))
    return query_site

def insert_assigned_soil_properties(project_id: str):
    query_soil = ''.join((ASSIGNED_PROJECT_SOIL_PROPERTY, 
    '(\'', project_id, '\',', ' \'ussr_1977\', 1), ' 
    '(\'', project_id, '\',', ' \'russia_1977\', 2), '
    '(\'', project_id, '\',', ' \'wrb_2015\', 3)')) 
    return query_soil

# В файле ivashenko нет инфы по проперти горизонта. Пока так, будем смотреть на других файлах
# query_soil_horizon = ''.join((ASSIGNED_PROJECT_SOIL_HORIZON_PROPERTY, 
# '(\'', GENERATED_PROJECT_ID, '\',', ' \'ussr_1977\', 1), ' 
# '(\'', GENERATED_PROJECT_ID, '\',', ' \'russia_1977\', 2), '
# '(\'', GENERATED_PROJECT_ID, '\',', ' \'wrb_2015\', 3)')) 
# print(query_soil)

# f = codecs.open('assigned_properties.sql', 'w', 'utf-8')
# f.write(query_site + '\n' + ';')
# f.write(query_soil + '\n' + ';')
# f.close()