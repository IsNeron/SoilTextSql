import pandas as pd

INSERT_INTO_PROJECT = 'INSERT INTO project (name, public, details, author_id, group_id) VALUES '

def insert_new_project(
    df: pd.DataFrame,
    user_id: str,
    group_id: str
):
    project_name = df['Unnamed: 3'].values[3]
    project_details = df['Unnamed: 3'].values[2]
    create_project_query_string = ''.join(
        (
        INSERT_INTO_PROJECT, 
        '(\'', 
        project_name, 
        '\', ', 
        'false', 
        ', \'',
        project_details,
        '\', \'', 
        user_id,
        '\', \'', 
        group_id,
        '\')' 
        )
    )
    return create_project_query_string

# print(create_project_query_string)
# f = codecs.open('create_project.sql', 'w', 'utf-8')
# f.write(create_project_query_string)
# f.close()