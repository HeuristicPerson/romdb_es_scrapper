"""
Small script to query ROMdb for information about a ROMSET providing the platform for it and a compressed file as
parameters. By now, the program is compatible with 7z, and zip format and only recognizes ROMs without headers (so, for
example, NES ROMs are incompatible yet).
"""

import argparse
import json
import os
import sys
import urllib


from libs import compressed_files
from libs import cons
from libs import romdb_data


# Classes
#=======================================================================================================================
# Helper functions
#=======================================================================================================================
def _get_args():
    """
    Function to obtain and validate the command line arguments.
    :return:
    """
    o_parser = argparse.ArgumentParser()
    o_parser.add_argument('platform', action='store', help='Platform alias')
    o_parser.add_argument('file', action='store', help='File to query in ROMdb')
    o_parser.add_argument('-format', action='store', help='Parent games and sagas format. s=short, m=medium, f=full')

    o_arguments = o_parser.parse_args()

    # Arguments validation
    #---------------------
    u_file = o_arguments.file
    if not os.path.isfile(u_file):
        print 'ERROR: Can\'t open file "%s"' % u_file
        sys.exit()

    u_platform = o_arguments.platform

    return {'u_file': u_file, 'u_platform': u_platform}


def _get_file_romset(pu_file):
    """
    Function to get information from a ROM file.
    :return:
    """
    u_ext = pu_file.rpartition(u'.')[2]

    if u_ext == u'7z':
        o_romset = compressed_files.scan_7z_file(pu_file)
    elif u_ext == u'zip':
        o_romset = compressed_files.scan_zip_file(pu_file)
    else:
        print 'ERROR: Invalid ROM file extension "%s"' % u_ext
        sys.exit()

    return o_romset


def query_game_by_nid(pi_nid):
    """
    Function to query ROMdb about a game by its nid.
    :param pi_nid: The nid of the game. e.g. 23
    :type pi_nid: int

    :return: The game object.
    :rtype libs.romdb_dava.Game
    """
    u_url = u'%s/api/game/%s' % (cons.u_URL, pi_nid)

    # [1/?] Querying ROMdb about the romset
    # --------------------------------------
    o_response = urllib.urlopen(u_url)
    dx_json = json.loads(o_response.read())

    # [2/?] Parsing the json output
    #------------------------------
    o_romdb_game = romdb_data.Game()
    o_romdb_game.from_json(dx_json)
    print o_romdb_game.nice_text(ps_format='medium')

    return o_romdb_game


def query_romset_by_crc32(pu_platform, pu_crc32):
    """
    Function to query a ROMSet by its (clean) crc32.

    :param pu_flatform: Alias of the platform in ROMdb. e.g. u'ps1', 'snt-crt'...
    :type pu_crc32: unicode

    :param pu_crc32: (clean) CRC32 of the ROMset. Two notes here: 1) It's a composed CRC32, by adding the CRC32 of all
                     the files that belong to the ROMset, 2) "clean" means that some files are not taken into account
                     (e.g. ".cue" files), and the header of some ROMs is removed (e.g. NES ROMs).
    :type pu_crc32: unicode

    :return: A romdb version object.
    :rtype libs.romdb_data.Version
    """
    u_url = u'%s/api/version/%s/%s' % (cons.u_URL, pu_platform, pu_crc32)

    # [1/?] Querying ROMdb about the romset
    #--------------------------------------
    o_response = urllib.urlopen(u_url)

    try:
        dx_json = json.loads(o_response.read())

        # [2/?] Parsing the json and building a full Version object with all the information
        #-----------------------------------------------------------------------------------
        # Parsing the json data
        o_romdb_version = romdb_data.Version()
        o_romdb_version.from_json(dx_json)
    except ValueError:
        o_romdb_version = None

    return o_romdb_version


def query_romset_by_name(pu_platform, pu_file):
    """
    Function to query ROMdb about a version given a file. The file will be scanned in order to obtain the CRC32 and then
    that CRC32 will be used to query ROMdb.

    :param po_romset:
    :return:
    """

    # [1/?] Creating a romset-file object by reading the file
    #--------------------------------------------------------
    # TODO: When the platform is NES (for example), remove the header and compute the CRC32
    o_romset = _get_file_romset(pu_file)
    o_romset.u_platform = pu_platform

    return query_romset_by_crc32(pu_platform, o_romset.u_ccrc32)

    #u_url = u'%s/api/version/%s/%s' % (cons.u_URL, pu_platform, o_romset.u_ccrc32)

    #print u_url

    # [2/?] Querying ROMdb about the romset
    #--------------------------------------
    #o_response = urllib.urlopen(u_url)
    #dx_json = json.loads(o_response.read())

    # [3/?] Parsing the json and building a full Version object with all the information
    #-----------------------------------------------------------------------------------
    # Parsing the json data
    #o_romdb_version = romdb_data.Version()
    #o_romdb_version.from_json(dx_json)

    #return o_romdb_version


# Main code
#=======================================================================================================================
if __name__ == '__main__':
    #print 'ROMDB file info v1.0 - 2018-10-27'
    #print '================================='
    #dx_args = _get_args()

    #o_version = query_romset_by_name(dx_args['u_platform'], dx_args['u_file'])

    #print dx_romdb_json
    #print o_version.nice_text(ps_format='medium')

    # --- TEST CODE ---
    query_game_by_nid(14591)
    # ------ end ------