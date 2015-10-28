#!/usr/bin/python
#
# A script to update can's locations to a readable intersection, where 
# possible.
#

from cartodb import CartoDBAPIKey
import click
import requests


def intersection(lat=None, lng=None, **kwargs):
    params = {
        'lat': lat,
        'lng': lng,
        'username': 'ebrelsford',
    }
    r = requests.get('http://api.geonames.org/findNearestIntersectionJSON',
                     params=params).json()
    intersection = r['intersection']
    if float(intersection['distance']) < 0.05:
        return '{} & {}'.format(intersection['street1'], intersection['street2'])
    return None


def update_location(cursor, table_name, cartodb_id=None, lat=None, lng=None):
    i = intersection(lat, lng)
    if i:
        sql = "UPDATE {} SET location = '{}' WHERE cartodb_id = {}".format(
            table_name,
            i,
            cartodb_id
        )
        cursor.sql(sql)
        print(i)
    else:
        print('No intersection found')


def get_locations(cursor, table_name):
    sql = """SELECT cartodb_id, ST_X(the_geom) AS lng, ST_Y(the_geom) AS lat
FROM {} 
WHERE location IS NULL""".format(table_name)
    return cursor.sql(sql)['rows']


@click.command()
@click.option('--api_key', help='The CartoDB API Key')
@click.option('--table_name', default='cans', help='The table to update')
@click.option('--username', default='curbyourlitter', help='The CartoDB user')
def update_locations(api_key, table_name, username):
    cursor = CartoDBAPIKey(api_key, username)
    for location in get_locations(cursor, table_name):
        update_location(cursor, table_name, **location)


if __name__ == '__main__':
    update_locations()
