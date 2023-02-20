import codecs
import pandas as pd
import json

from .matcher import match_landuse

GENERATED_PROJECT_ID = '01GS7K6EX6R9EM6JVB69Z00X06'
SOIL_TEXT_USER_ID =  '01GS7JD982GVQVWK2NN59MJMVK'

CREATE_SITE = 'INSERT INTO site (name, public, geom, date, author_id, project_id) VALUES '
SELECT_SITE = 'SELECT id FROM site WHERE name in ('
INSERT_SITE_PROPERTIES_VALUE = 'INSERT INTO site_property_value (site_id, property_slug, value) VALUES'

def insert_site(
    df: pd.DataFrame,
    user_id: str,
    project_id: str,
):
    site_name = df['Информация об участнике']
    coordinates_raw = df['Unnamed: 4']
    date = df['Unnamed: 2']
    i = 11
    result_query = CREATE_SITE
    while i < site_name.size:
        site_name_value = site_name.values[i]
        coordinates_string = f'ST_PointZ({coordinates_raw[i]}, \'nan\' ::float8, 4326)'
        datetime =  f'{date[i]}-01-01 00:00:00'

        create_site_query_string = ''.join(
            ( 
            '(\'', 
            site_name_value, 
            '\', ', 
            'false', 
            ', ',
            coordinates_string,
            ', \'', 
            datetime,
            '\', \'',
            user_id,
            '\', \'', 
            project_id,
            '\')' 
            )
            )

        if i == site_name.size - 1:
            i = i+1
            result_query = result_query + ' ' + create_site_query_string
            break

        i = i+1
        result_query = result_query + ' ' + create_site_query_string + ','
    return result_query

def select_new_site_ids(df: pd.DataFrame):
    site_name = df['Информация об участнике']
    i = 11
    result_query = SELECT_SITE
    while i < site_name.size:
        site_name_value = site_name.values[i]
        if i == site_name.size - 1:
            i = i+1
            result_query = result_query + '\'' + f'{site_name_value}' '\'' 
            break
            
        result_query = result_query + '\'' + f'{site_name_value}' '\',' 
        i = i+1
    result_query = result_query + ')'
    return result_query


def insert_site_properties_landuse(
    df: pd.DataFrame,
    site_ids: pd.DataFrame,
    ):
    site_id = site_ids['id']
    landuse = df['Unnamed: 5']

    result_query = INSERT_SITE_PROPERTIES_VALUE

    i = 11
    j = 1
    while i < landuse.size and j < site_ids.size:
        site_id_value = site_id.values[j]
        landuse_value = landuse[i]
        landuse_json = json.dumps(match_landuse(landuse_value))
        # result_query = result_query + '(' + '\'' + f'{site_id_value}' '\', ' + '\'landuse\', ' + f"'{landuse_json}'" + '), '
        result_query += f"('{site_id_value}', 'landuse', '{landuse_json}'), "
        i= i+1 
        j=j+1
    
    result_query = result_query + ')'
    return result_query


