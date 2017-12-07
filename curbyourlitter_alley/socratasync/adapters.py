def threeoneone(data):
    mapping = {
        'unique_key': 'unique_key',
        'created_date': 'created_date',
        'closed_date': 'closed_date',
        'agency': 'agency',
        'agency_name': 'agency_name',
        'complaint_type': 'complaint_type',
        'descriptor': 'descriptor',
        'location_type': 'location_type',
        'incident_zip': 'incident_zip',
        'incident_address': 'incident_address',
        'street_name': 'street_name',
        'cross_street_1': 'cross_street1',
        'cross_street_2': 'cross_street2',
        'intersection_street_1': 'intersection_street1',
        'intersection_street_2': 'intersection_street2',
        'address_type': 'address_type',
        'city': 'city',
        'facility type': 'facility_type',
        'status': 'status',
        'due_date': 'due_date',
    }
    src_columns = sorted(list(mapping.keys()))
    dst_columns = [mapping[c] for c in src_columns] + ['the_geom',]

    values = []
    for row in data:
        row_values = list(map(lambda column: row.get(column, None), src_columns))
        row_values.append(geom(row))
        values.append(row_values)

    # TODO filter based on the_geom, just in case we grabbed something without
    # a zip code that we don't want anymore
    return {
        'column_names': dst_columns,
        'values': values,
    }


def geom(row):
    try:
        longitude = row['longitude']
        latitude = row['latitude']
    except KeyError:
        print('no latlng', row.get('x_coordinate_state_plane', None),
              row.get('y_coordinate_state_plane', None))
        return None
        # TODO reproject -> WGS84
        #x = row['x_coordinate_state_plane_']
        #y = row['y_coordinate_state_plane_']
    return 'SRID=4326;POINT ({:s} {:s})'.format(longitude, latitude)
