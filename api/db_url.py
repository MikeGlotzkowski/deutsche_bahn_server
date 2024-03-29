def create_from(from_l, to_l, dd, mm, yy, hh, minmin):
    template_url = """https://reiseauskunft.bahn.de/bin/query.exe/dn?revia=yes&
existOptimizePrice=1&
country=DEU&
dbkanal_007=L01_S01_D001_KIN0014_qf-bahn-svb-kl2_lz03&
start=1&
protocol=https%3A&
S={from_destination}&
REQ0JourneyStopsSID=&
Z={to_destination}&
REQ0JourneyStopsZID=&
date={dd}.{mm}.{yy}&
time={hh}%3A{minmin}&
timesel=depart&
returnDate=&
returnTime=&
returnTimesel=depart&
optimize=0&
auskunft_travelers_number=1&
tariffTravellerType.1=E&
tariffTravellerReductionClass.1=0&
tariffClass=2&
rtMode=DB-HYBRID&
externRequest=yes&
HWAI=JS%21js%3Dyes%21ajax%3Dyes%21"""
    url = template_url.format(
        from_destination=from_l, to_destination=to_l, dd=dd, mm=mm, yy=yy, hh=hh, minmin=minmin)
    full_url = "".join(url.splitlines())
    print(full_url)
    return full_url
