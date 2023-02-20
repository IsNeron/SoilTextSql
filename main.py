import codecs
import pandas as pd

from services.create_project import insert_new_project
from services.assigned_properties import insert_assigned_site_properties, insert_assigned_soil_properties
from services.site_properties import insert_site, select_new_site_ids, insert_site_properties_landuse
from services.matcher import match_landuse

#В две переменные ниже нужно записать id, полученные в результате работы скрипта user_project_group.sql
SOIL_TEXT_USER_ID =  '00000000000101001101010100'
SOIL_TEXT_GROUP_ID = '00000000000101001101010100'

GENERATED_PROJECT_ID = '01GSQ58Q7VWN9TPYS7AB0W5B3Z'

soil_text_data = pd.read_excel(r'C:\Users\KT\Desktop\ivashchenko.xlsx')
site_ids = pd.read_excel(r'C:\Users\KT\Desktop\ivashenko_ids.xlsx')

# project = insert_new_project(soil_text_data, SOIL_TEXT_USER_ID, SOIL_TEXT_GROUP_ID)
# print(project)
# assigned = insert_assigned_site_properties(GENERATED_PROJECT_ID)
# print(assigned + ';')
# print(insert_assigned_soil_properties(GENERATED_PROJECT_ID)  + ';')
# print(insert_site(soil_text_data,  SOIL_TEXT_USER_ID, GENERATED_PROJECT_ID)  + ';') 
# print(select_new_site_ids(soil_text_data))

# print(soil_text_data['Unnamed: 5'])

a = insert_site_properties_landuse(soil_text_data, site_ids)
print(a)