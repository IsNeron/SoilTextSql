import json

landuse_dict = {
    'A': 'planting',
    'M': 'mixed',
    'H': 'livestock',
    'F': 'forestry',
    'P': 'protected',
    'S': 'settlements',
    'O': 'other'
}


def match_landuse(landuse: str):
    # if not => o -- остальные типы земплепользование
    kind = landuse[0]
    if kind in landuse_dict:
        value = landuse_dict[kind]
    else:
        return {}

    if len(landuse) > 1:
        second_kind = landuse[0:2]
    else:
        result = {
            "kind": kind
        }
        return result

    if len(landuse) > 2:
        third_kind = landuse[0:3]
        second_value = value + '_' + f'{landuse[1]}'.lower()
    else:
        result = {
            "kind": kind,
            f"{value}": f"{second_kind}",
        }
        return result

    result = {
        "kind": kind,
        f"{value}": f"{second_kind}",
        f"{second_value}": f"{third_kind}"
    }

    return result
