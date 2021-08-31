import datetime
import re
import json

# titles = {"MRS","MR","MS","MSTR","DR"}

def decode(bcbp):
    result = {}

    leg = bcbp[1]

    try:
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
    except:
        return '{"error":"unable to parse string - incorrect format"}'

def encode(firstname, lastname, pnr, origin, destination, operator, flight_number, date, cabin_class, seat_number, checkin_sequence, softerror=False):
    fullname_pre = (lastname + "/" + firstname).upper().replace(" ","").replace("-","")
    if len(fullname_pre) < 20:
        fullname = fullname_pre + (" " * (20 - int(len(fullname_pre))))
    else:
        if softerror == True:
            return "Error: Set softerror to False to see full error."
        else:
            raise ValueError('BCBP Encode Error','Fullname > 20 Chars')
    
    pnr = pnr.upper()
    if len(pnr) <= 7:
        pnr = pnr + (" " * (7 - int(len(pnr))))
    else:
        if softerror == True:
            return "Error: Set softerror to False to see full error."
        else:
            raise ValueError('BCBP Encode Error','PNR > 7 Chars')


    odo_info = (origin + destination + operator).replace(" ","").upper()
    if len(odo_info) <= 8:
        odo = odo_info + (" " * (8 - int(len(odo_info))))
    else:
        if softerror == True:
            return "Error: Set softerror to False to see full error."
        else:
            raise ValueError('BCBP Encode Error','Origin and destination must be 3 characters long. Operator must be 2 characters long.')
    
    flight_no = (flight_number).replace(" ","").upper()
    if len(flight_no) <= 4:
        flight_no = flight_no + (" " * (4 - int(len(flight_no))))
    else:
        if softerror == True:
            return "Error: Set softerror to False to see full error."
        else:
            raise ValueError('BCBP Encode Error','Flight Number > 4 Chars')

    julian_date = (date.strftime('%j')).replace(" ","").upper()
    if len(str(julian_date)) <= 3:
        julian_date = julian_date + (" " * (3 - int(len(julian_date))))
    else:
        if softerror == True:
            return "Error: Set softerror to False to see full error."
        else:
            raise ValueError('BCBP Encode Error','Date > 3 Chars')

    cabin = (cabin_class).replace(" ","").upper()
    if len(cabin) <= 1:
        cabin = cabin + (" " * (1 - int(len(cabin))))
    else:
        if softerror == True:
            return "Error: Set softerror to False to see full error."
        else:
            raise ValueError('BCBP Encode Error','Cabin Class > 1 Chars')

    seat = (seat_number).replace(" ","").upper()
    if len(seat) <= 4:
        seat = seat + (" " * (4 - int(len(seat))))
    else:
        if softerror == True:
            return "Error: Set softerror to False to see full error."
        else:
            raise ValueError('BCBP Encode Error','Seat Number > 4 Chars')
    
    checkin = (checkin_sequence).replace(" ","").upper()
    if len(checkin) <= 4:
        checkin = checkin + (" " * (4 - int(len(checkin))))
    else:
        if softerror == True:
            return "Error: Set softerror to False to see full error."
        else:
            raise ValueError('BCBP Encode Error','Check-In Sequence > 4 Chars')

    bcbp = "M1{}{} {} {} {}{}{}{}".format(fullname, pnr, odo, flight_no, julian_date, cabin, seat, checkin).upper()

    return bcbp