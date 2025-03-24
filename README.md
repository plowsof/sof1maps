# Note to repo admins
Upload map .zip files without a root folder and with lowercase map names, where the name.zip matches the name.bsp exactly.

eg. \
**example123.zip** \
maps/ \
&nbsp;&nbsp;&nbsp;dm/ \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;example123.bsp

# Why?
This repo is intended to be used to serve maps to both windows and linux versions of SoF.  Both use the fopen api from stdio.  The filesystem on windows is case-insensitive, and linux case-sensitive. Windows does a case sensitive matching when searching inside a .PAK file as exception.  Git and URL are case sensitive.  The mapname originates in server console, it checks if the file exists on disk (here is OS difference), sends the mapname to the client via configstrings CS_MODELS+1 which is maps/CS_NAME, the client calls CM_LoadMap, the same check if the file exists on disk (here is OS difference) occurs on client now.

Which ever way you look at it, the filename.bsp that is download has to match case sensitive to the string supplied by the sof server on linux systems. So since we want to provide for linux + windows versions of sof, the name of the .zip has to match the name of the .bsp exactly/case-sensitive, because it is matching the string sent from the SoF Server in SV_SpawnServer (from console map dm/bLaBlA)

Best practise to have every map named lowercase so no need to remember exact case pattern.

So in the repo: the rule should be lowercase for every map. .zip and .bsp.

On linux this will make maps with caps in them that live withtin a .PAK or an out-sourced zip no longer be used. But that is fine.
