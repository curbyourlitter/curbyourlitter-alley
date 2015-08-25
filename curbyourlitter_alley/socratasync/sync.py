import traceback

from cartodb.cartodb import CartoDBAPIKey, CartoDBException
from sodapy import Socrata


def sync(connection):
    since = None
    latest = most_recent_upload(connection.cartodb_table, connection.socrata_resource)
    if latest:
        since = latest[connection.socrata_resource.unique_key]
    for batch in get_resource_data(connection.socrata_resource, since=since):
        upload_data(connection.cartodb_table, batch, adapter=connection.get_adapter())


def most_recent_upload(cartodb_table, socrata_resource):
    """Get the most recent upload by table key"""
    cl = CartoDBAPIKey(cartodb_table.apiKey, cartodb_table.domain)
    sql = 'SELECT * FROM {} ORDER BY {} DESC LIMIT 1'.format(
        cartodb_table.table,
        socrata_resource.unique_key
    )
    try:
        return cl.sql(sql)['rows'][0]
    except CartoDBException as e:
        traceback.print_exc()
        print('Exception while inserting:', e)
    except IndexError:
        return None


def get_resource_data(socrata_resource, since=None, limit=1000):
    client = Socrata(socrata_resource.domain, socrata_resource.token)
    kwargs = {
        'limit': limit,
        'where': socrata_resource.conditions,
    }
    if socrata_resource.unique_key:
        kwargs['order'] = socrata_resource.unique_key

    while True:
        if since:
            kwargs['where'] = "{} and {} > '{}'".format(
                socrata_resource.conditions,
                socrata_resource.unique_key,
                since
            )
        batch = client.get(socrata_resource.endpoint, **kwargs)
        if len(batch) > 0:
            since = batch[-1][socrata_resource.unique_key]
            yield batch
        else:
            return


def sql_str(value):
    if value is None:
        return 'NULL'
    if isinstance(value, str):
        return "'{}'".format(value)
    return value


def upload_data(cartodb_table, data, adapter=None):
    cl = CartoDBAPIKey(cartodb_table.apiKey, cartodb_table.domain)
    adapted = adapter(data)

    values = []
    for values_row in adapted['values']:
        values.append(','.join([sql_str(v) for v in values_row]))

    sql = 'INSERT INTO %s (%s) VALUES %s' % (
        cartodb_table.table,
        ','.join(adapted['column_names']),
        ','.join(['(%s)' % v for v in values]),
    )
    try:
        cl.sql(sql)
    except CartoDBException as e:
        traceback.print_exc()
        print('Exception while inserting:', e)
