ROMdb - EmulationStation Scrapper
=================================

Introduction
------------

_**ROMdb - EmulationStation Scrapper**_ is a small console program written in Python that obtains meta-data information and screenshots for
your ROMs from [ROMdb](https://romdb.geeklogger.com) website in a format compatible with
[EmulationStation](https://github.com/RetroPie/RetroPie-Setup/wiki/EmulationStation) front-end.


Requirements
------------

Usage
-----

    python romdb_es_scrapper.py platform rom_path dat_path xml_path img_dir

  * `platform` Alias of the platform for the ROMs to be scrapped in ROMdb. The full list can be seen at
    https://romdb.geeklogger.com/documentation/platforms-aliases-and-dats. e.g. for Playstion games you would use `ps1`. 

  * `rom_path` Path of the ROMs that are going to be scrapped; wildcards are accepted. So you could use
    `/home/john/street fighter.zip` for just one ROM or `/home/john/snes/*.zip` to scan all zip files into one
    directory.

  * `dat_path` Path of the dat file used to scan the ROMs. ROMdb website uses No-Intro and Redump dats. e.g.
    `/home/john/ps1.dat`.

  * `xml_path` Path of the `gamelist.xml` file to be created that will be read by EmulationStation. e.g.
    `/home/john/.emulationstation/gamelists/ps1/gamelist.xml`.

  * `img_dir` Path of the directory to save the screenshots downloaded from ROMdb. The scrapper will automatically
    create sub-directories inside for each platform. e.g. `/home/john/screenshots/` would automatically create
    `/home/john/screenshots/ps1` directory for `ps1` games if that platform is selected.
