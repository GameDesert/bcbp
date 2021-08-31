import datetime
import re
import json

# titles = {"MRS","MR","MS","MSTR","DR"}

def decode(bcbp):
    result = {}

    leg = bcbp[1]

    name_bcbp = bcbp[2:22].replace(" ", "")
    fullname = name_bcbp.split("/")
    result["firstname"] = str(re.sub('(MRS|MR|MS|MSTR|DR)$','',fullname[1]).replace(" ", ""))
    result["lastname"] = str(fullname[0].replace(" ", ""))

    result["pnr"] = str(bcbp[22:30].replace(" ", ""))
    result["origin"] = str(bcbp[30:33].replace(" ", ""))
    result["destination"] = str(bcbp[33:36].replace(" ", ""))
    result["operator"] = str(bcbp[36:38].replace(" ", ""))
    result["flight_number"] = str(bcbp[39:43].replace(" ", ""))
    result["date"] = str(datetime.datetime.strptime(bcbp[44:47], '%j').strftime('%d/%b'))
    result["cabin_class"] = str(bcbp[47].replace(" ", ""))
    result["seat_number"] = str(bcbp[48:52].replace(" ", ""))
    result["checkin_sequence"] = str(bcbp[52:56].replace(" ", ""))

    output = json.dumps(result)

    return output