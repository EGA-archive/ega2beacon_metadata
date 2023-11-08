#!/usr/bin/env python

"""ega2beacon.py  :  Converts EGA metadata into Beacon metadata """

__author__ = "Raul Garcia, Mauricio Moldes"
__version__ = "0.1"
__maintainer__ = "Raul Garcia, Mauricio Moldes"
__email__ = "raul.garcia@crg.es,mauricio.moldes@crg.es"
__status__ = "development"

import logging
import yaml
import psycopg2
import sys

logger = logging.getLogger('ega2beacon_logger')

""" VERIFIES THE CONNECTION TO PLSQL """


def connection_plsql(cfg):
    conn_string = "host='" + str(cfg['plsql']['host']) + "' dbname='" + str(
        cfg['plsql']['dbname']) + "' user='" + str(
        cfg['plsql']['user']) + "' password='" + str(cfg['plsql']['password']) + "' port = '" + str(
        cfg['plsql']['port']) + "'"
    conn_plsql = psycopg2.connect(conn_string)
    return conn_plsql


"""" Get metadata from PLSQL """


def get_metadata_egapro(conn_plsql):
    cursor = conn_plsql.cursor()
    sql = """select ebi_xml
        from analysis_table at
        where ega_stable_id = 'EGAZ00001450756'"""
    cursor.execute(sql)
    records = cursor.fetchall()
    return records


""" Write metadata Beacon friendly format  """


def write_metadata_beacon():
    return False


""" Convert EGA metadata into Beacon Friendly Format """


def convert_ega_beacon_metadata():
    return False

def parse_xml_analysis(xml):
    return False


def ega2beacon():
    conn_plsql = None
    try:
        conn_plsql = connection_plsql(cfg)
        if conn_plsql:
            xml = get_metadata_egapro(conn_plsql)
            parse_xml_analysis(xml)
    except Exception as e:
        print(e)




""" READ CONFIG FILE """


def read_config():
    with open("../config/config.yml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg


""" MAIN"""


def main():
    print("hello")
    try:
        # configure logging
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d]'
        logging.basicConfig(format=log_format)
        global cfg
        cfg = read_config()
        ega2beacon()

    except Exception as e:
        logger.error("Error: {}".format(e))
        sys.exit(-1)


if __name__ == '__main__':
    main()
