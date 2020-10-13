import requests
import datetime



r = requests.get("https://api.covid19api.com/country/afghanistan")
datos_afghanistan= r.json()
confirmados_afghanistan= [ dato["Confirmed"] for dato in datos_afghanistan]
muertes_afghanistan= [ dato["Deaths"] for dato in datos_afghanistan]
fechas_afghanistan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_afghanistan]

r = requests.get("https://api.covid19api.com/country/albania")
datos_albania= r.json()
confirmados_albania= [ dato["Confirmed"] for dato in datos_albania]
muertes_albania= [ dato["Deaths"] for dato in datos_albania]
fechas_albania= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_albania]

r = requests.get("https://api.covid19api.com/country/andorra")
datos_andorra= r.json()
confirmados_andorra= [ dato["Confirmed"] for dato in datos_andorra]
muertes_andorra= [ dato["Deaths"] for dato in datos_andorra]
fechas_andorra= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_andorra]

r = requests.get("https://api.covid19api.com/country/angola")
datos_angola= r.json()
confirmados_angola= [ dato["Confirmed"] for dato in datos_angola]
muertes_angola= [ dato["Deaths"] for dato in datos_angola]
fechas_angola= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_angola]

r = requests.get("https://api.covid19api.com/country/antigua and barbuda")
datos_antigua_barbuda= r.json()
confirmados_antigua_barbuda= [ dato["Confirmed"] for dato in datos_antigua_barbuda]
muertes_antigua_barbuda= [ dato["Deaths"] for dato in datos_antigua_barbuda]
fechas_antigua_barbuda= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_antigua_barbuda]

r = requests.get("https://api.covid19api.com/country/argentina")
datos_argentina= r.json()
confirmados_argentina= [ dato["Confirmed"] for dato in datos_argentina]
muertes_argentina= [ dato["Deaths"] for dato in datos_argentina]
fechas_argentina= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_argentina]

r = requests.get("https://api.covid19api.com/country/armenia")
datos_armenia= r.json()
confirmados_armenia= [ dato["Confirmed"] for dato in datos_armenia]
muertes_armenia= [ dato["Deaths"] for dato in datos_armenia]
fechas_armenia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_armenia]

r = requests.get("https://api.covid19api.com/country/australia")
datos_australia= r.json()
confirmados_australia= [ dato["Confirmed"] for dato in datos_australia]
muertes_australia= [ dato["Deaths"] for dato in datos_australia]
fechas_australia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_australia]

r = requests.get("https://api.covid19api.com/country/austria")
datos_austria= r.json()
confirmados_austria= [ dato["Confirmed"] for dato in datos_austria]
muertes_austria= [ dato["Deaths"] for dato in datos_austria]
fechas_austria= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_austria]

r = requests.get("https://api.covid19api.com/country/azerbaijan")
datos_azerbaijan= r.json()
confirmados_azerbaijan= [ dato["Confirmed"] for dato in datos_azerbaijan]
muertes_azerbaijan= [ dato["Deaths"] for dato in datos_azerbaijan]
fechas_azerbaijan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_azerbaijan]

r = requests.get("https://api.covid19api.com/country/bahamas")
datos_bahamas= r.json()
confirmados_bahamas= [ dato["Confirmed"] for dato in datos_bahamas]
muertes_bahamas= [ dato["Deaths"] for dato in datos_bahamas]
fechas_bahamas= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_bahamas]

r = requests.get("https://api.covid19api.com/country/bahrain")
datos_bahrain= r.json()
confirmados_bahrain= [ dato["Confirmed"] for dato in datos_bahrain]
muertes_bahrain= [ dato["Deaths"] for dato in datos_bahrain]
fechas_bahrain= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_bahrain]

r = requests.get("https://api.covid19api.com/country/bangladesh")
datos_bangladesh= r.json()
confirmados_bangladesh= [ dato["Confirmed"] for dato in datos_bangladesh]
muertes_bangladesh= [ dato["Deaths"] for dato in datos_bangladesh]
fechas_bangladesh= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_bangladesh]

r = requests.get("https://api.covid19api.com/country/barbados")
datos_barbados= r.json()
confirmados_barbados= [ dato["Confirmed"] for dato in datos_barbados]
muertes_barbados= [ dato["Deaths"] for dato in datos_barbados]
fechas_barbados= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_barbados]

r = requests.get("https://api.covid19api.com/country/belarus")
datos_belarus= r.json()
confirmados_belarus= [ dato["Confirmed"] for dato in datos_belarus]
muertes_belarus= [ dato["Deaths"] for dato in datos_belarus]
fechas_belarus= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_belarus]

r = requests.get("https://api.covid19api.com/country/belgium")
datos_belgium= r.json()
confirmados_belgium= [ dato["Confirmed"] for dato in datos_belgium]
muertes_belgium= [ dato["Deaths"] for dato in datos_belgium]
fechas_belgium= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_belgium]

r = requests.get("https://api.covid19api.com/country/belize")
datos_belize= r.json()
confirmados_belize= [ dato["Confirmed"] for dato in datos_belize]
muertes_belize= [ dato["Deaths"] for dato in datos_belize]
fechas_belize= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_belize]

r = requests.get("https://api.covid19api.com/country/benin")
datos_benin= r.json()
confirmados_benin= [ dato["Confirmed"] for dato in datos_benin]
muertes_benin= [ dato["Deaths"] for dato in datos_benin]
fechas_benin= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_benin]

r = requests.get("https://api.covid19api.com/country/bhutan")
datos_bhutan= r.json()
confirmados_bhutan= [ dato["Confirmed"] for dato in datos_bhutan]
muertes_bhutan= [ dato["Deaths"] for dato in datos_bhutan]
fechas_bhutan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_bhutan]

r = requests.get("https://api.covid19api.com/country/bolivia")
datos_bolivia= r.json()
confirmados_bolivia= [ dato["Confirmed"] for dato in datos_bolivia]
muertes_bolivia= [ dato["Deaths"] for dato in datos_bolivia]
fechas_bolivia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_bolivia]



r = requests.get("https://api.covid19api.com/country/botswana")
datos_botswana= r.json()
confirmados_botswana= [ dato["Confirmed"] for dato in datos_botswana]
muertes_botswana= [ dato["Deaths"] for dato in datos_botswana]
fechas_botswana= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_botswana]

r = requests.get("https://api.covid19api.com/country/brazil")
datos_brazil= r.json()
confirmados_brazil= [ dato["Confirmed"] for dato in datos_brazil]
muertes_brazil= [ dato["Deaths"] for dato in datos_brazil]
fechas_brazil= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_brazil]

r = requests.get("https://api.covid19api.com/country/brunei darussalam")
datos_brunei_darussalam= r.json()
confirmados_brunei_darussalam= [ dato["Confirmed"] for dato in datos_brunei_darussalam]
muertes_brunei_darussalam= [ dato["Deaths"] for dato in datos_brunei_darussalam]
fechas_brunei_darussalam= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_brunei_darussalam]

r = requests.get("https://api.covid19api.com/country/bulgaria")
datos_bulgaria= r.json()
confirmados_bulgaria= [ dato["Confirmed"] for dato in datos_bulgaria]
muertes_bulgaria= [ dato["Deaths"] for dato in datos_bulgaria]
fechas_bulgaria= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_bulgaria]

r = requests.get("https://api.covid19api.com/country/burkina faso")
datos_burkina_faso= r.json()
confirmados_burkina_faso= [ dato["Confirmed"] for dato in datos_burkina_faso]
muertes_burkina_faso= [ dato["Deaths"] for dato in datos_burkina_faso]
fechas_burkina_faso= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_burkina_faso]
r = requests.get("https://api.covid19api.com/country/burundi")
datos_burundi= r.json()
confirmados_burundi= [ dato["Confirmed"] for dato in datos_burundi]
muertes_burundi= [ dato["Deaths"] for dato in datos_burundi]
fechas_burundi= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_burundi]

r = requests.get("https://api.covid19api.com/country/cambodia")
datos_cambodia= r.json()
confirmados_cambodia= [ dato["Confirmed"] for dato in datos_cambodia]
muertes_cambodia= [ dato["Deaths"] for dato in datos_cambodia]
fechas_cambodia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_cambodia]

r = requests.get("https://api.covid19api.com/country/cameroon")
datos_cameroon= r.json()
confirmados_cameroon= [ dato["Confirmed"] for dato in datos_cameroon]
muertes_cameroon= [ dato["Deaths"] for dato in datos_cameroon]
fechas_cameroon= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_cameroon]

r = requests.get("https://api.covid19api.com/country/canada")
datos_canada= r.json()
confirmados_canada= [ dato["Confirmed"] for dato in datos_canada]
muertes_canada= [ dato["Deaths"] for dato in datos_canada]
fechas_canada= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_canada]
r = requests.get("https://api.covid19api.com/country/cape verde")
datos_cape_verde= r.json()
confirmados_cape_verde= [ dato["Confirmed"] for dato in datos_cape_verde]
muertes_cape_verde= [ dato["Deaths"] for dato in datos_cape_verde]
fechas_cape_verde= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_cape_verde]

r = requests.get("https://api.covid19api.com/country/central african republic")
datos_central_african_republic= r.json()
confirmados_central_african_republic= [ dato["Confirmed"] for dato in datos_central_african_republic]
muertes_central_african_republic= [ dato["Deaths"] for dato in datos_central_african_republic]
fechas_central_african_republic= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_central_african_republic]

r = requests.get("https://api.covid19api.com/country/chad")
datos_chad= r.json()
confirmados_chad= [ dato["Confirmed"] for dato in datos_chad]
muertes_chad= [ dato["Deaths"] for dato in datos_chad]
fechas_chad= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_chad]

r = requests.get("https://api.covid19api.com/country/chile")
datos_chile= r.json()
confirmados_chile= [ dato["Confirmed"] for dato in datos_chile]
muertes_chile= [ dato["Deaths"] for dato in datos_chile]
fechas_chile= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_chile]

r = requests.get("https://api.covid19api.com/country/china")
datos_china= r.json()
confirmados_china= [ dato["Confirmed"] for dato in datos_china]
muertes_china= [ dato["Deaths"] for dato in datos_china]
fechas_china= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_china]

r = requests.get("https://api.covid19api.com/country/colombia")
datos_colombia= r.json()
confirmados_colombia= [ dato["Confirmed"] for dato in datos_colombia]
muertes_colombia= [ dato["Deaths"] for dato in datos_colombia]
fechas_colombia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_colombia]

r = requests.get("https://api.covid19api.com/country/comoros")
datos_comoros= r.json()
confirmados_comoros= [ dato["Confirmed"] for dato in datos_comoros]
muertes_comoros= [ dato["Deaths"] for dato in datos_comoros]
fechas_comoros= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_comoros]


r = requests.get("https://api.covid19api.com/country/costa rica")
datos_costa_rica= r.json()
confirmados_costa_rica= [ dato["Confirmed"] for dato in datos_costa_rica]
muertes_costa_rica= [ dato["Deaths"] for dato in datos_costa_rica]
fechas_costa_rica= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_costa_rica]

                      
r = requests.get("https://api.covid19api.com/country/croatia")
datos_croatia= r.json()
confirmados_croatia= [ dato["Confirmed"] for dato in datos_croatia]
muertes_croatia= [ dato["Deaths"] for dato in datos_croatia]
fechas_croatia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_croatia]

r = requests.get("https://api.covid19api.com/country/cuba")
datos_cuba= r.json()
confirmados_cuba= [ dato["Confirmed"] for dato in datos_cuba]
muertes_cuba= [ dato["Deaths"] for dato in datos_cuba]
fechas_cuba= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_cuba]

r = requests.get("https://api.covid19api.com/country/cyprus")
datos_cyprus= r.json()
confirmados_cyprus= [ dato["Confirmed"] for dato in datos_cyprus]
muertes_cyprus= [ dato["Deaths"] for dato in datos_cyprus]
fechas_cyprus= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_cyprus]

r = requests.get("https://api.covid19api.com/country/czech republic")
datos_czech_republic= r.json()
confirmados_czech_republic= [ dato["Confirmed"] for dato in datos_czech_republic]
muertes_czech_republic= [ dato["Deaths"] for dato in datos_czech_republic]
fechas_czech_republic= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_czech_republic]

r = requests.get("https://api.covid19api.com/country/denmark")
datos_denmark= r.json()
confirmados_denmark= [ dato["Confirmed"] for dato in datos_denmark]
muertes_denmark= [ dato["Deaths"] for dato in datos_denmark]
fechas_denmark= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_denmark]
r = requests.get("https://api.covid19api.com/country/djibouti")
datos_djibouti= r.json()
confirmados_djibouti= [ dato["Confirmed"] for dato in datos_djibouti]
muertes_djibouti= [ dato["Deaths"] for dato in datos_djibouti]
fechas_djibouti= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_djibouti]
r = requests.get("https://api.covid19api.com/country/dominica")
datos_dominica= r.json()
confirmados_dominica= [ dato["Confirmed"] for dato in datos_dominica]
muertes_dominica= [ dato["Deaths"] for dato in datos_dominica]
fechas_dominica= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_dominica]

r = requests.get("https://api.covid19api.com/country/dominican republic")
datos_dominican_republic= r.json()
confirmados_dominican_republic= [ dato["Confirmed"] for dato in datos_dominican_republic]
muertes_dominican_republic= [ dato["Deaths"] for dato in datos_dominican_republic]
fechas_dominican_republic= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_dominican_republic]

r = requests.get("https://api.covid19api.com/country/ecuador")
datos_ecuador= r.json()
confirmados_ecuador= [ dato["Confirmed"] for dato in datos_ecuador]
muertes_ecuador= [ dato["Deaths"] for dato in datos_ecuador]
fechas_ecuador= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_ecuador]
r = requests.get("https://api.covid19api.com/country/egypt")
datos_egypt= r.json()
confirmados_egypt= [ dato["Confirmed"] for dato in datos_egypt]
muertes_egypt= [ dato["Deaths"] for dato in datos_egypt]
fechas_egypt= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_egypt]

r = requests.get("https://api.covid19api.com/country/el salvador")
datos_el_salvador= r.json()
confirmados_el_salvador= [ dato["Confirmed"] for dato in datos_el_salvador]
muertes_el_salvador= [ dato["Deaths"] for dato in datos_el_salvador]
fechas_el_salvador= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_el_salvador]

r = requests.get("https://api.covid19api.com/country/equatorial guinea")
datos_equatorial_guinea= r.json()
confirmados_equatorial_guinea= [ dato["Confirmed"] for dato in datos_equatorial_guinea]
muertes_equatorial_guinea= [ dato["Deaths"] for dato in datos_equatorial_guinea]
fechas_equatorial_guinea= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_equatorial_guinea]

r = requests.get("https://api.covid19api.com/country/eritrea")
datos_eritrea= r.json()
confirmados_eritrea= [ dato["Confirmed"] for dato in datos_eritrea]
muertes_eritrea= [ dato["Deaths"] for dato in datos_eritrea]
fechas_eritrea= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_eritrea]

r = requests.get("https://api.covid19api.com/country/estonia")
datos_estonia= r.json()
confirmados_estonia= [ dato["Confirmed"] for dato in datos_estonia]
muertes_estonia= [ dato["Deaths"] for dato in datos_estonia]
fechas_estonia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_estonia]
r = requests.get("https://api.covid19api.com/country/ethiopia")
datos_ethiopia= r.json()
confirmados_ethiopia= [ dato["Confirmed"] for dato in datos_ethiopia]
muertes_ethiopia= [ dato["Deaths"] for dato in datos_ethiopia]
fechas_ethiopia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_ethiopia]
r = requests.get("https://api.covid19api.com/country/fiji")
datos_fiji= r.json()
confirmados_fiji= [ dato["Confirmed"] for dato in datos_fiji]
muertes_fiji= [ dato["Deaths"] for dato in datos_fiji]
fechas_fiji= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_fiji]
r = requests.get("https://api.covid19api.com/country/finland")
datos_finland= r.json()
confirmados_finland= [ dato["Confirmed"] for dato in datos_finland]
muertes_finland= [ dato["Deaths"] for dato in datos_finland]
fechas_finland= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_finland]
r = requests.get("https://api.covid19api.com/country/france")
datos_france= r.json()
confirmados_france= [ dato["Confirmed"] for dato in datos_france]
muertes_france= [ dato["Deaths"] for dato in datos_france]
fechas_france= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_france]
r = requests.get("https://api.covid19api.com/country/gabon")
datos_gabon= r.json()
confirmados_gabon= [ dato["Confirmed"] for dato in datos_gabon]
muertes_gabon= [ dato["Deaths"] for dato in datos_gabon]
fechas_gabon= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_gabon]
r = requests.get("https://api.covid19api.com/country/gambia")
datos_gambia= r.json()
confirmados_gambia= [ dato["Confirmed"] for dato in datos_gambia]
muertes_gambia= [ dato["Deaths"] for dato in datos_gambia]
fechas_gambia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_gambia]
r = requests.get("https://api.covid19api.com/country/georgia")
datos_georgia= r.json()
confirmados_georgia= [ dato["Confirmed"] for dato in datos_georgia]
muertes_georgia= [ dato["Deaths"] for dato in datos_georgia]
fechas_georgia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_georgia]
r = requests.get("https://api.covid19api.com/country/germany")
datos_germany= r.json()
confirmados_germany= [ dato["Confirmed"] for dato in datos_germany]
muertes_germany= [ dato["Deaths"] for dato in datos_germany]
fechas_germany= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_germany]
r = requests.get("https://api.covid19api.com/country/ghana")
datos_ghana= r.json()
confirmados_ghana= [ dato["Confirmed"] for dato in datos_ghana]
muertes_ghana= [ dato["Deaths"] for dato in datos_ghana]
fechas_ghana= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_ghana]
r = requests.get("https://api.covid19api.com/country/greece")
datos_greece= r.json()
confirmados_greece= [ dato["Confirmed"] for dato in datos_greece]
muertes_greece= [ dato["Deaths"] for dato in datos_greece]
fechas_greece= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_greece]
r = requests.get("https://api.covid19api.com/country/grenada")
datos_grenada= r.json()
confirmados_grenada= [ dato["Confirmed"] for dato in datos_grenada]
muertes_grenada= [ dato["Deaths"] for dato in datos_grenada]
fechas_grenada= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_grenada]
r = requests.get("https://api.covid19api.com/country/guatemala")
datos_guatemala= r.json()
confirmados_guatemala= [ dato["Confirmed"] for dato in datos_guatemala]
muertes_guatemala= [ dato["Deaths"] for dato in datos_guatemala]
fechas_guatemala= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_guatemala]
r = requests.get("https://api.covid19api.com/country/guinea")
datos_guinea= r.json()
confirmados_guinea= [ dato["Confirmed"] for dato in datos_guinea]
muertes_guinea= [ dato["Deaths"] for dato in datos_guinea]
fechas_guinea= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_guinea]
r = requests.get("https://api.covid19api.com/country/guinea-bissau")

datos_guinea_bissau= r.json()
confirmados_guinea_bissau= [ dato["Confirmed"] for dato in datos_guinea_bissau]
muertes_guinea_bissau= [ dato["Deaths"] for dato in datos_guinea_bissau]
fechas_guinea_bissau= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_guinea_bissau]

r = requests.get("https://api.covid19api.com/country/guyana")
datos_guyana= r.json()
confirmados_guyana= [ dato["Confirmed"] for dato in datos_guyana]
muertes_guyana= [ dato["Deaths"] for dato in datos_guyana]
fechas_guyana= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_guyana]
r = requests.get("https://api.covid19api.com/country/haiti")
datos_haiti= r.json()
confirmados_haiti= [ dato["Confirmed"] for dato in datos_haiti]
muertes_haiti= [ dato["Deaths"] for dato in datos_haiti]
fechas_haiti= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_haiti]


r = requests.get("https://api.covid19api.com/country/honduras")
datos_honduras= r.json()
confirmados_honduras= [ dato["Confirmed"] for dato in datos_honduras]
muertes_honduras= [ dato["Deaths"] for dato in datos_honduras]
fechas_honduras= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_honduras]


r = requests.get("https://api.covid19api.com/country/hungary")
datos_hungary= r.json()
confirmados_hungary= [ dato["Confirmed"] for dato in datos_hungary]
muertes_hungary= [ dato["Deaths"] for dato in datos_hungary]
fechas_hungary= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_hungary]
r = requests.get("https://api.covid19api.com/country/iceland")
datos_iceland= r.json()
confirmados_iceland= [ dato["Confirmed"] for dato in datos_iceland]
muertes_iceland= [ dato["Deaths"] for dato in datos_iceland]
fechas_iceland= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_iceland]
r = requests.get("https://api.covid19api.com/country/india")
datos_india= r.json()
confirmados_india= [ dato["Confirmed"] for dato in datos_india]
muertes_india= [ dato["Deaths"] for dato in datos_india]
fechas_india= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_india]
r = requests.get("https://api.covid19api.com/country/indonesia")
datos_indonesia= r.json()
confirmados_indonesia= [ dato["Confirmed"] for dato in datos_indonesia]
muertes_indonesia= [ dato["Deaths"] for dato in datos_indonesia]
fechas_indonesia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_indonesia]


r = requests.get("https://api.covid19api.com/country/iraq")
datos_iraq= r.json()
confirmados_iraq= [ dato["Confirmed"] for dato in datos_iraq]
muertes_iraq= [ dato["Deaths"] for dato in datos_iraq]
fechas_iraq= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_iraq]
r = requests.get("https://api.covid19api.com/country/ireland")
datos_ireland= r.json()
confirmados_ireland= [ dato["Confirmed"] for dato in datos_ireland]
muertes_ireland= [ dato["Deaths"] for dato in datos_ireland]
fechas_ireland= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_ireland]
r = requests.get("https://api.covid19api.com/country/israel")
datos_israel= r.json()
confirmados_israel= [ dato["Confirmed"] for dato in datos_israel]
muertes_israel= [ dato["Deaths"] for dato in datos_israel]
fechas_israel= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_israel]
r = requests.get("https://api.covid19api.com/country/italy")
datos_italy= r.json()
confirmados_italy= [ dato["Confirmed"] for dato in datos_italy]
muertes_italy= [ dato["Deaths"] for dato in datos_italy]
fechas_italy= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_italy]
r = requests.get("https://api.covid19api.com/country/jamaica")
datos_jamaica= r.json()
confirmados_jamaica= [ dato["Confirmed"] for dato in datos_jamaica]
muertes_jamaica= [ dato["Deaths"] for dato in datos_jamaica]
fechas_jamaica= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_jamaica]
r = requests.get("https://api.covid19api.com/country/japan")
datos_japan= r.json()
confirmados_japan= [ dato["Confirmed"] for dato in datos_japan]
muertes_japan= [ dato["Deaths"] for dato in datos_japan]
fechas_japan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_japan]
r = requests.get("https://api.covid19api.com/country/jordan")
datos_jordan= r.json()
confirmados_jordan= [ dato["Confirmed"] for dato in datos_jordan]
muertes_jordan= [ dato["Deaths"] for dato in datos_jordan]
fechas_jordan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_jordan]
r = requests.get("https://api.covid19api.com/country/kazakhstan")
datos_kazakhstan= r.json()
confirmados_kazakhstan= [ dato["Confirmed"] for dato in datos_kazakhstan]
muertes_kazakhstan= [ dato["Deaths"] for dato in datos_kazakhstan]
fechas_kazakhstan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_kazakhstan]
r = requests.get("https://api.covid19api.com/country/kenya")
datos_kenya= r.json()
confirmados_kenya= [ dato["Confirmed"] for dato in datos_kenya]
muertes_kenya= [ dato["Deaths"] for dato in datos_kenya]
fechas_kenya= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_kenya]


r = requests.get("https://api.covid19api.com/country/kuwait")
datos_kuwait= r.json()
confirmados_kuwait= [ dato["Confirmed"] for dato in datos_kuwait]
muertes_kuwait= [ dato["Deaths"] for dato in datos_kuwait]
fechas_kuwait= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_kuwait]
r = requests.get("https://api.covid19api.com/country/kyrgyzstan")
datos_kyrgyzstan= r.json()
confirmados_kyrgyzstan= [ dato["Confirmed"] for dato in datos_kyrgyzstan]
muertes_kyrgyzstan= [ dato["Deaths"] for dato in datos_kyrgyzstan]
fechas_kyrgyzstan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_kyrgyzstan]

r = requests.get("https://api.covid19api.com/country/latvia")
datos_latvia= r.json()
confirmados_latvia= [ dato["Confirmed"] for dato in datos_latvia]
muertes_latvia= [ dato["Deaths"] for dato in datos_latvia]
fechas_latvia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_latvia]
r = requests.get("https://api.covid19api.com/country/lebanon")
datos_lebanon= r.json()
confirmados_lebanon= [ dato["Confirmed"] for dato in datos_lebanon]
muertes_lebanon= [ dato["Deaths"] for dato in datos_lebanon]
fechas_lebanon= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_lebanon]
r = requests.get("https://api.covid19api.com/country/lesotho")
datos_lesotho= r.json()
confirmados_lesotho= [ dato["Confirmed"] for dato in datos_lesotho]
muertes_lesotho= [ dato["Deaths"] for dato in datos_lesotho]
fechas_lesotho= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_lesotho]
r = requests.get("https://api.covid19api.com/country/liberia")
datos_liberia= r.json()
confirmados_liberia= [ dato["Confirmed"] for dato in datos_liberia]
muertes_liberia= [ dato["Deaths"] for dato in datos_liberia]
fechas_liberia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_liberia]
r = requests.get("https://api.covid19api.com/country/libya")
datos_libya= r.json()
confirmados_libya= [ dato["Confirmed"] for dato in datos_libya]
muertes_libya= [ dato["Deaths"] for dato in datos_libya]
fechas_libya= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_libya]
r = requests.get("https://api.covid19api.com/country/liechtenstein")
datos_liechtenstein= r.json()
confirmados_liechtenstein= [ dato["Confirmed"] for dato in datos_liechtenstein]
muertes_liechtenstein= [ dato["Deaths"] for dato in datos_liechtenstein]
fechas_liechtenstein= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_liechtenstein]
r = requests.get("https://api.covid19api.com/country/lithuania")
datos_lithuania= r.json()
confirmados_lithuania= [ dato["Confirmed"] for dato in datos_lithuania]
muertes_lithuania= [ dato["Deaths"] for dato in datos_lithuania]
fechas_lithuania= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_lithuania]
r = requests.get("https://api.covid19api.com/country/luxembourg")
datos_luxembourg= r.json()
confirmados_luxembourg= [ dato["Confirmed"] for dato in datos_luxembourg]
muertes_luxembourg= [ dato["Deaths"] for dato in datos_luxembourg]
fechas_luxembourg= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_luxembourg]

r = requests.get("https://api.covid19api.com/country/macedonia, republic of")
datos_macedonia= r.json()
confirmados_macedonia= [ dato["Confirmed"] for dato in datos_macedonia]
muertes_macedonia= [ dato["Deaths"] for dato in datos_macedonia]
fechas_macedonia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_macedonia]
r = requests.get("https://api.covid19api.com/country/madagascar")
datos_madagascar= r.json()
confirmados_madagascar= [ dato["Confirmed"] for dato in datos_madagascar]
muertes_madagascar= [ dato["Deaths"] for dato in datos_madagascar]
fechas_madagascar= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_madagascar]
r = requests.get("https://api.covid19api.com/country/malawi")
datos_malawi= r.json()
confirmados_malawi= [ dato["Confirmed"] for dato in datos_malawi]
muertes_malawi= [ dato["Deaths"] for dato in datos_malawi]
fechas_malawi= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_malawi]
r = requests.get("https://api.covid19api.com/country/malaysia")
datos_malaysia= r.json()
confirmados_malaysia= [ dato["Confirmed"] for dato in datos_malaysia]
muertes_malaysia= [ dato["Deaths"] for dato in datos_malaysia]
fechas_malaysia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_malaysia]
r = requests.get("https://api.covid19api.com/country/maldives")
datos_maldives= r.json()
confirmados_maldives= [ dato["Confirmed"] for dato in datos_maldives]
muertes_maldives= [ dato["Deaths"] for dato in datos_maldives]
fechas_maldives= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_maldives]
r = requests.get("https://api.covid19api.com/country/mali")
datos_mali= r.json()
confirmados_mali= [ dato["Confirmed"] for dato in datos_mali]
muertes_mali= [ dato["Deaths"] for dato in datos_mali]
fechas_mali= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_mali]
r = requests.get("https://api.covid19api.com/country/malta")
datos_malta= r.json()
confirmados_malta= [ dato["Confirmed"] for dato in datos_malta]
muertes_malta= [ dato["Deaths"] for dato in datos_malta]
fechas_malta= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_malta]
r = requests.get("https://api.covid19api.com/country/mauritania")
datos_mauritania= r.json()
confirmados_mauritania= [ dato["Confirmed"] for dato in datos_mauritania]
muertes_mauritania= [ dato["Deaths"] for dato in datos_mauritania]
fechas_mauritania= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_mauritania]
r = requests.get("https://api.covid19api.com/country/mauritius")
datos_mauritius= r.json()
confirmados_mauritius= [ dato["Confirmed"] for dato in datos_mauritius]
muertes_mauritius= [ dato["Deaths"] for dato in datos_mauritius]
fechas_mauritius= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_mauritius]
r = requests.get("https://api.covid19api.com/country/mexico")
datos_mexico= r.json()
confirmados_mexico= [ dato["Confirmed"] for dato in datos_mexico]
muertes_mexico= [ dato["Deaths"] for dato in datos_mexico]
fechas_mexico= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_mexico]
r = requests.get("https://api.covid19api.com/country/moldova")
datos_moldova= r.json()
confirmados_moldova= [ dato["Confirmed"] for dato in datos_moldova]
muertes_moldova= [ dato["Deaths"] for dato in datos_moldova]
fechas_moldova= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_moldova]
r = requests.get("https://api.covid19api.com/country/monaco")
datos_monaco= r.json()
confirmados_monaco= [ dato["Confirmed"] for dato in datos_monaco]
muertes_monaco= [ dato["Deaths"] for dato in datos_monaco]
fechas_monaco= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_monaco]
r = requests.get("https://api.covid19api.com/country/mongolia")
datos_mongolia= r.json()
confirmados_mongolia= [ dato["Confirmed"] for dato in datos_mongolia]
muertes_mongolia= [ dato["Deaths"] for dato in datos_mongolia]
fechas_mongolia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_mongolia]
r = requests.get("https://api.covid19api.com/country/montenegro")
datos_montenegro= r.json()
confirmados_montenegro= [ dato["Confirmed"] for dato in datos_montenegro]
muertes_montenegro= [ dato["Deaths"] for dato in datos_montenegro]
fechas_montenegro= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_montenegro]
r = requests.get("https://api.covid19api.com/country/morocco")
datos_morocco= r.json()
confirmados_morocco= [ dato["Confirmed"] for dato in datos_morocco]
muertes_morocco= [ dato["Deaths"] for dato in datos_morocco]
fechas_morocco= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_morocco]
r = requests.get("https://api.covid19api.com/country/mozambique")
datos_mozambique= r.json()
confirmados_mozambique= [ dato["Confirmed"] for dato in datos_mozambique]
muertes_mozambique= [ dato["Deaths"] for dato in datos_mozambique]
fechas_mozambique= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_mozambique]
r = requests.get("https://api.covid19api.com/country/myanmar")
datos_myanmar= r.json()
confirmados_myanmar= [ dato["Confirmed"] for dato in datos_myanmar]
muertes_myanmar= [ dato["Deaths"] for dato in datos_myanmar]
fechas_myanmar= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_myanmar]
r = requests.get("https://api.covid19api.com/country/namibia")
datos_namibia= r.json()
confirmados_namibia= [ dato["Confirmed"] for dato in datos_namibia]
muertes_namibia= [ dato["Deaths"] for dato in datos_namibia]
fechas_namibia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_namibia]
r = requests.get("https://api.covid19api.com/country/nepal")
datos_nepal= r.json()
confirmados_nepal= [ dato["Confirmed"] for dato in datos_nepal]
muertes_nepal= [ dato["Deaths"] for dato in datos_nepal]
fechas_nepal= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_nepal]
r = requests.get("https://api.covid19api.com/country/netherlands")
datos_netherlands= r.json()
confirmados_netherlands= [ dato["Confirmed"] for dato in datos_netherlands]
muertes_netherlands= [ dato["Deaths"] for dato in datos_netherlands]
fechas_netherlands= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_netherlands]

r = requests.get("https://api.covid19api.com/country/new zealand")
datos_new_zealand= r.json()
confirmados_new_zealand= [ dato["Confirmed"] for dato in datos_new_zealand]
muertes_new_zealand= [ dato["Deaths"] for dato in datos_new_zealand]
fechas_new_zealand= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_new_zealand]

r = requests.get("https://api.covid19api.com/country/nicaragua")
datos_nicaragua= r.json()
confirmados_nicaragua= [ dato["Confirmed"] for dato in datos_nicaragua]
muertes_nicaragua= [ dato["Deaths"] for dato in datos_nicaragua]
fechas_nicaragua= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_nicaragua]
r = requests.get("https://api.covid19api.com/country/niger")
datos_niger= r.json()
confirmados_niger= [ dato["Confirmed"] for dato in datos_niger]
muertes_niger= [ dato["Deaths"] for dato in datos_niger]
fechas_niger= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_niger]
r = requests.get("https://api.covid19api.com/country/nigeria")
datos_nigeria= r.json()
confirmados_nigeria= [ dato["Confirmed"] for dato in datos_nigeria]
muertes_nigeria= [ dato["Deaths"] for dato in datos_nigeria]
fechas_nigeria= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_nigeria]
r = requests.get("https://api.covid19api.com/country/norway")
datos_norway= r.json()
confirmados_norway= [ dato["Confirmed"] for dato in datos_norway]
muertes_norway= [ dato["Deaths"] for dato in datos_norway]
fechas_norway= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_norway]
r = requests.get("https://api.covid19api.com/country/oman")
datos_oman= r.json()
confirmados_oman= [ dato["Confirmed"] for dato in datos_oman]
muertes_oman= [ dato["Deaths"] for dato in datos_oman]
fechas_oman= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_oman]
r = requests.get("https://api.covid19api.com/country/pakistan")
datos_pakistan= r.json()
confirmados_pakistan= [ dato["Confirmed"] for dato in datos_pakistan]
muertes_pakistan= [ dato["Deaths"] for dato in datos_pakistan]
fechas_pakistan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_pakistan]
r = requests.get("https://api.covid19api.com/country/palestinian territory")
datos_palestinian_territory= r.json()
confirmados_palestinian_territory= [ dato["Confirmed"] for dato in datos_palestinian_territory]
muertes_palestinian_territory= [ dato["Deaths"] for dato in datos_palestinian_territory]
fechas_palestinian_territory= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_palestinian_territory]
r = requests.get("https://api.covid19api.com/country/panama")
datos_panama= r.json()
confirmados_panama= [ dato["Confirmed"] for dato in datos_panama]
muertes_panama= [ dato["Deaths"] for dato in datos_panama]
fechas_panama= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_panama]
r = requests.get("https://api.covid19api.com/country/papua new guinea")
datos_papuanew_guinea= r.json()
confirmados_papuanew_guinea= [ dato["Confirmed"] for dato in datos_papuanew_guinea]
muertes_papuanew_guinea= [ dato["Deaths"] for dato in datos_papuanew_guinea]
fechas_papuanew_guinea= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_papuanew_guinea]

r = requests.get("https://api.covid19api.com/country/paraguay")
datos_paraguay= r.json()
confirmados_paraguay= [ dato["Confirmed"] for dato in datos_paraguay]
muertes_paraguay= [ dato["Deaths"] for dato in datos_paraguay]
fechas_paraguay= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_paraguay]

r = requests.get("https://api.covid19api.com/country/peru")
datos_peru= r.json()
confirmados_peru= [ dato["Confirmed"] for dato in datos_peru]
muertes_peru= [ dato["Deaths"] for dato in datos_peru]
fechas_peru= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_peru]
r = requests.get("https://api.covid19api.com/country/philippines")
datos_philippines= r.json()
confirmados_philippines= [ dato["Confirmed"] for dato in datos_philippines]
muertes_philippines= [ dato["Deaths"] for dato in datos_philippines]
fechas_philippines= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_philippines]
r = requests.get("https://api.covid19api.com/country/poland")
datos_poland= r.json()
confirmados_poland= [ dato["Confirmed"] for dato in datos_poland]
muertes_poland= [ dato["Deaths"] for dato in datos_poland]
fechas_poland= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_poland]
r = requests.get("https://api.covid19api.com/country/portugal")
datos_portugal= r.json()
confirmados_portugal= [ dato["Confirmed"] for dato in datos_portugal]
muertes_portugal= [ dato["Deaths"] for dato in datos_portugal]
fechas_portugal= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_portugal]
r = requests.get("https://api.covid19api.com/country/qatar")
datos_qatar= r.json()
confirmados_qatar= [ dato["Confirmed"] for dato in datos_qatar]
muertes_qatar= [ dato["Deaths"] for dato in datos_qatar]
fechas_qatar= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_qatar]
r = requests.get("https://api.covid19api.com/country/republic of kosovo")
datos_republic_kosovo= r.json()
confirmados_republic_kosovo= [ dato["Confirmed"] for dato in datos_republic_kosovo]
muertes_republic_kosovo= [ dato["Deaths"] for dato in datos_republic_kosovo]
fechas_republic_kosovo= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_republic_kosovo]
r = requests.get("https://api.covid19api.com/country/réunion")
datos_réunion= r.json()
confirmados_réunion= [ dato["Confirmed"] for dato in datos_réunion]
muertes_réunion= [ dato["Deaths"] for dato in datos_réunion]
fechas_réunion= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_réunion]
r = requests.get("https://api.covid19api.com/country/romania")
datos_romania= r.json()
confirmados_romania= [ dato["Confirmed"] for dato in datos_romania]
muertes_romania= [ dato["Deaths"] for dato in datos_romania]
fechas_romania= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_romania]

r = requests.get("https://api.covid19api.com/country/russian federation")
datos_russian_federation= r.json()
confirmados_russian_federation= [ dato["Confirmed"] for dato in datos_russian_federation]
muertes_russian_federation= [ dato["Deaths"] for dato in datos_russian_federation]
fechas_russian_federation= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_russian_federation]

r = requests.get("https://api.covid19api.com/country/rwanda")
datos_rwanda= r.json()
confirmados_rwanda= [ dato["Confirmed"] for dato in datos_rwanda]
muertes_rwanda= [ dato["Deaths"] for dato in datos_rwanda]
fechas_rwanda= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_rwanda]

r = requests.get("https://api.covid19api.com/country/saint kitts and nevis")
datos_saint_kitts_nevis= r.json()
confirmados_saint_kitts_nevis= [ dato["Confirmed"] for dato in datos_saint_kitts_nevis]
muertes_saint_kitts_nevis= [ dato["Deaths"] for dato in datos_saint_kitts_nevis]
fechas_saint_kitts_nevis= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_saint_kitts_nevis]

r = requests.get("https://api.covid19api.com/country/saint lucia")
datos_saint_lucia= r.json()
confirmados_saint_lucia= [ dato["Confirmed"] for dato in datos_saint_lucia]
muertes_saint_lucia= [ dato["Deaths"] for dato in datos_saint_lucia]
fechas_saint_lucia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_saint_lucia]


r = requests.get("https://api.covid19api.com/country/san marino")
datos_san_marino= r.json()
confirmados_san_marino= [ dato["Confirmed"] for dato in datos_san_marino]
muertes_san_marino= [ dato["Deaths"] for dato in datos_san_marino]
fechas_san_marino= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_san_marino]



r = requests.get("https://api.covid19api.com/country/saudi arabia")
datos_saudi_arabia= r.json()
confirmados_saudi_arabia= [ dato["Confirmed"] for dato in datos_saudi_arabia]
muertes_saudi_arabia= [ dato["Deaths"] for dato in datos_saudi_arabia]
fechas_saudi_arabia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_saudi_arabia]

r = requests.get("https://api.covid19api.com/country/senegal")
datos_senegal= r.json()
confirmados_senegal= [ dato["Confirmed"] for dato in datos_senegal]
muertes_senegal= [ dato["Deaths"] for dato in datos_senegal]
fechas_senegal= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_senegal]
r = requests.get("https://api.covid19api.com/country/serbia")
datos_serbia= r.json()
confirmados_serbia= [ dato["Confirmed"] for dato in datos_serbia]
muertes_serbia= [ dato["Deaths"] for dato in datos_serbia]
fechas_serbia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_serbia]
r = requests.get("https://api.covid19api.com/country/seychelles")
datos_seychelles= r.json()
confirmados_seychelles= [ dato["Confirmed"] for dato in datos_seychelles]
muertes_seychelles= [ dato["Deaths"] for dato in datos_seychelles]
fechas_seychelles= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_seychelles]

r = requests.get("https://api.covid19api.com/country/sierra leone")
datos_sierra_leone= r.json()
confirmados_sierra_leone= [ dato["Confirmed"] for dato in datos_sierra_leone]
muertes_sierra_leone= [ dato["Deaths"] for dato in datos_sierra_leone]
fechas_sierra_leone= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_sierra_leone]

r = requests.get("https://api.covid19api.com/country/singapore")
datos_singapore= r.json()
confirmados_singapore= [ dato["Confirmed"] for dato in datos_singapore]
muertes_singapore= [ dato["Deaths"] for dato in datos_singapore]
fechas_singapore= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_singapore]
r = requests.get("https://api.covid19api.com/country/slovakia")
datos_slovakia= r.json()
confirmados_slovakia= [ dato["Confirmed"] for dato in datos_slovakia]
muertes_slovakia= [ dato["Deaths"] for dato in datos_slovakia]
fechas_slovakia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_slovakia]
r = requests.get("https://api.covid19api.com/country/slovenia")
datos_slovenia= r.json()
confirmados_slovenia= [ dato["Confirmed"] for dato in datos_slovenia]
muertes_slovenia= [ dato["Deaths"] for dato in datos_slovenia]
fechas_slovenia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_slovenia]
r = requests.get("https://api.covid19api.com/country/somalia")
datos_somalia= r.json()
confirmados_somalia= [ dato["Confirmed"] for dato in datos_somalia]
muertes_somalia= [ dato["Deaths"] for dato in datos_somalia]
fechas_somalia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_somalia]
r = requests.get("https://api.covid19api.com/country/south africa")
datos_south_africa= r.json()
confirmados_south_africa= [ dato["Confirmed"] for dato in datos_south_africa]
muertes_south_africa= [ dato["Deaths"] for dato in datos_south_africa]
fechas_south_africa= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_south_africa]

r = requests.get("https://api.covid19api.com/country/south sudan")
datos_south_sudan= r.json()
confirmados_south_sudan= [ dato["Confirmed"] for dato in datos_south_sudan]
muertes_south_sudan= [ dato["Deaths"] for dato in datos_south_sudan]
fechas_south_sudan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_south_sudan]

r = requests.get("https://api.covid19api.com/country/spain")
datos_spain= r.json()
confirmados_spain= [ dato["Confirmed"] for dato in datos_spain]
muertes_spain= [ dato["Deaths"] for dato in datos_spain]
fechas_spain= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_spain]

r = requests.get("https://api.covid19api.com/country/sri lanka")
datos_sri_lanka= r.json()
confirmados_sri_lanka= [ dato["Confirmed"] for dato in datos_sri_lanka]
muertes_sri_lanka= [ dato["Deaths"] for dato in datos_sri_lanka]
fechas_sri_lanka= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_sri_lanka]

r = requests.get("https://api.covid19api.com/country/sudan")
datos_sudan= r.json()
confirmados_sudan= [ dato["Confirmed"] for dato in datos_sudan]
muertes_sudan= [ dato["Deaths"] for dato in datos_sudan]
fechas_sudan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_sudan]
r = requests.get("https://api.covid19api.com/country/suriname")
datos_suriname= r.json()
confirmados_suriname= [ dato["Confirmed"] for dato in datos_suriname]
muertes_suriname= [ dato["Deaths"] for dato in datos_suriname]
fechas_suriname= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_suriname]
r = requests.get("https://api.covid19api.com/country/swaziland")
datos_swaziland= r.json()
confirmados_swaziland= [ dato["Confirmed"] for dato in datos_swaziland]
muertes_swaziland= [ dato["Deaths"] for dato in datos_swaziland]
fechas_swaziland= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_swaziland]
r = requests.get("https://api.covid19api.com/country/sweden")
datos_sweden= r.json()
confirmados_sweden= [ dato["Confirmed"] for dato in datos_sweden]
muertes_sweden= [ dato["Deaths"] for dato in datos_sweden]
fechas_sweden= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_sweden]
r = requests.get("https://api.covid19api.com/country/switzerland")
datos_switzerland= r.json()
confirmados_switzerland= [ dato["Confirmed"] for dato in datos_switzerland]
muertes_switzerland= [ dato["Deaths"] for dato in datos_switzerland]
fechas_switzerland= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_switzerland]


r = requests.get("https://api.covid19api.com/country/taiwan, republic of china")
datos_taiwan= r.json()
confirmados_taiwan= [ dato["Confirmed"] for dato in datos_taiwan]
muertes_taiwan= [ dato["Deaths"] for dato in datos_taiwan]
fechas_taiwan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_taiwan]
r = requests.get("https://api.covid19api.com/country/tajikistan")
datos_tajikistan= r.json()


r = requests.get("https://api.covid19api.com/country/thailand")
datos_thailand= r.json()
confirmados_thailand= [ dato["Confirmed"] for dato in datos_thailand]
muertes_thailand= [ dato["Deaths"] for dato in datos_thailand]
fechas_thailand= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_thailand]

r = requests.get("https://api.covid19api.com/country/togo")
datos_togo= r.json()
confirmados_togo= [ dato["Confirmed"] for dato in datos_togo]
muertes_togo= [ dato["Deaths"] for dato in datos_togo]
fechas_togo= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_togo]

r = requests.get("https://api.covid19api.com/country/trinidad and tobago")
datos_trinidad_tobago= r.json()
confirmados_trinidad_tobago= [ dato["Confirmed"] for dato in datos_trinidad_tobago]
muertes_trinidad_tobago= [ dato["Deaths"] for dato in datos_trinidad_tobago]
fechas_trinidad_tobago= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_trinidad_tobago]

r = requests.get("https://api.covid19api.com/country/tunisia")
datos_tunisia= r.json()
confirmados_tunisia= [ dato["Confirmed"] for dato in datos_tunisia]
muertes_tunisia= [ dato["Deaths"] for dato in datos_tunisia]
fechas_tunisia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_tunisia]
r = requests.get("https://api.covid19api.com/country/turkey")
datos_turkey= r.json()
confirmados_turkey= [ dato["Confirmed"] for dato in datos_turkey]
muertes_turkey= [ dato["Deaths"] for dato in datos_turkey]
fechas_turkey= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_turkey]
r = requests.get("https://api.covid19api.com/country/uganda")
datos_uganda= r.json()
confirmados_uganda= [ dato["Confirmed"] for dato in datos_uganda]
muertes_uganda= [ dato["Deaths"] for dato in datos_uganda]
fechas_uganda= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_uganda]
r = requests.get("https://api.covid19api.com/country/ukraine")
datos_ukraine= r.json()
confirmados_ukraine= [ dato["Confirmed"] for dato in datos_ukraine]
muertes_ukraine= [ dato["Deaths"] for dato in datos_ukraine]
fechas_ukraine= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_ukraine]
r = requests.get("https://api.covid19api.com/country/united arab emirates")
datos_united_arab_emirates= r.json()
confirmados_united_arab_emirates= [ dato["Confirmed"] for dato in datos_united_arab_emirates]
muertes_united_arab_emirates= [ dato["Deaths"] for dato in datos_united_arab_emirates]
fechas_united_arab_emirates= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_united_arab_emirates]

r = requests.get("https://api.covid19api.com/country/united kingdom")
datos_united_kingdom= r.json()
confirmados_united_kingdom= [ dato["Confirmed"] for dato in datos_united_kingdom]
muertes_united_kingdom= [ dato["Deaths"] for dato in datos_united_kingdom]
fechas_united_kingdom= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_united_kingdom]

r = requests.get("https://api.covid19api.com/country/united states of america")
datos_USA= r.json()
confirmados_USA= [ dato["Confirmed"] for dato in datos_USA]
muertes_USA= [ dato["Deaths"] for dato in datos_USA]
fechas_USA= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_USA]

r = requests.get("https://api.covid19api.com/country/uruguay")
datos_uruguay= r.json()
confirmados_uruguay= [ dato["Confirmed"] for dato in datos_uruguay]
muertes_uruguay= [ dato["Deaths"] for dato in datos_uruguay]
fechas_uruguay= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_uruguay]
r = requests.get("https://api.covid19api.com/country/uzbekistan")
datos_uzbekistan= r.json()
confirmados_uzbekistan= [ dato["Confirmed"] for dato in datos_uzbekistan]
muertes_uzbekistan= [ dato["Deaths"] for dato in datos_uzbekistan]
fechas_uzbekistan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_uzbekistan]

r = requests.get("https://api.covid19api.com/country/venezuela")
datos_venezuela= r.json()
confirmados_venezuela= [ dato["Confirmed"] for dato in datos_venezuela]
muertes_venezuela= [ dato["Deaths"] for dato in datos_venezuela]
fechas_venezuela= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_venezuela]

r = requests.get("https://api.covid19api.com/country/viet nam")
datos_vietnam= r.json()
confirmados_vietnam= [ dato["Confirmed"] for dato in datos_vietnam]
muertes_vietnam= [ dato["Deaths"] for dato in datos_vietnam]
fechas_vietnam= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_vietnam]

r = requests.get("https://api.covid19api.com/country/western sahara")
datos_western_sahara= r.json()
confirmados_western_sahara= [ dato["Confirmed"] for dato in datos_western_sahara]
muertes_western_sahara= [ dato["Deaths"] for dato in datos_western_sahara]
fechas_western_sahara= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_western_sahara]

r = requests.get("https://api.covid19api.com/country/yemen")
datos_yemen= r.json()
confirmados_yemen= [ dato["Confirmed"] for dato in datos_yemen]
muertes_yemen= [ dato["Deaths"] for dato in datos_yemen]
fechas_yemen= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_yemen]
r = requests.get("https://api.covid19api.com/country/zambia")
datos_zambia= r.json()
confirmados_zambia= [ dato["Confirmed"] for dato in datos_zambia]
muertes_zambia= [ dato["Deaths"] for dato in datos_zambia]
fechas_zambia= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_zambia]
r = requests.get("https://api.covid19api.com/country/zimbabwe")
datos_zimbabwe= r.json()
confirmados_zimbabwe= [ dato["Confirmed"] for dato in datos_zimbabwe]
muertes_zimbabwe= [ dato["Deaths"] for dato in datos_zimbabwe]
fechas_zimbabwe= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_zimbabwe]


    

