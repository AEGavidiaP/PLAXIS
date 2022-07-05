#copiar carpetas "plxscripting" y  "Crypto", ademas del archivo "encryption"
import subprocess
import os
from plxscripting.easy import *

inputport = 10000
ouputport = 10001

plaxispw= r'BDfW!<vsMNg3LuHR'  #Cambiar segun usuario de PLAXIS

plaxis_path = r'C:\Program Files\Bentley\Geotechnical\PLAXIS 2D CONNECT Edition V21'
plaxis_input = 'Plaxis2DXInput.exe'

# first launch PLAXIS
args = [os.path.join(plaxis_path, plaxis_input),
        "--AppServerPort={}".format(inputport),
        "--AppServerPassWord={}".format(plaxispw)]
inputprocess = subprocess.Popen(args)

s_i, g_i = new_server('localhost', inputport, password=plaxispw, timeout=10.0)

s_i.new()

s_o, g_o = new_server('localhost', ouputport, password=s_i.connection._password)

#.......CODE.......#

#Close Plaxis 

s_i.close()
inputprocess.terminate()