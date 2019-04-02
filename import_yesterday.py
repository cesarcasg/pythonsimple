# runs importing notes from yesterday - el universal
#import os

from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
print yesterday.strftime('%Y%m%d')

#os.system("/usr/bin/php -f /desarrollo/apieluniversal/internal/importa_notas_eluniversal_2019.php produccion secciones todo ")
import subprocess

# if the script don't need output.
#subprocess.call("/usr/bin/php -f /desarrollo/apieluniversal/internal/importa_notas_eluniversal_2019.php produccion secciones todo")

# if you want output
proc = subprocess.Popen("/usr/bin/php -f /desarrollo/apieluniversal/internal/importa_notas_eluniversal_2019.php produccion secciones todo "+yesterday.strftime('%Y%m%d'), shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()
