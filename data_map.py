import json
import folium
from collections import defaultdict
import numpy as np
import pandas as pd
from pyproj import Proj, transform

data = {
   "data": [
        {
            "id": "2122",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/dordrecht-zero-emission-zone-logistics",
            "introtext": "Dordrecht will implement ZEZ logistic 1 January 2026",
            "cityname": "Dordrecht - Zero Emission Zone Logistics",
            "city_latitude": "51.81",
            "city_longitude": "4.69",
            "scheme_color": "5"
        },
        {
            "id": "2332",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/venlo-zero-emission-zone-logistics",
            "introtext": "Venlo will implement ZEZ logistic 1 January 2027",
            "cityname": "Venlo - Zero Emission Zone Logistics",
            "city_latitude": "51.22",
            "city_longitude": "6.10",
            "scheme_color": "5"
        },
        {
            "id": "2215",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/amsterdam-zero-emission-zone",
            "introtext": "Amsterdam will have a zero emission zone in place from 2025.",
            "cityname": "Amsterdam - Zero Emission Zone",
            "city_latitude": "52.37",
            "city_longitude": "4.89",
            "scheme_color": "5"
        },
        {
            "id": "2119",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/alphen-aan-den-rijn-zero-emission-zone-logistics",
            "introtext": "Alphen aan den Rijn will implement ZEZ logistic 1 July 2026",
            "cityname": "Alphen aan den Rijn - Zero Emission Zone Logistics",
            "city_latitude": "52.12",
            "city_longitude": "4.65",
            "scheme_color": "5"
        },
        {
            "id": "2049",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/amersfoort-zero-emission-zone-logistics",
            "introtext": "Amersfoort will implement ZEZ logistic 1 January 2025",
            "cityname": "Amersfoort - Zero Emission Zone Logistics",
            "city_latitude": "52.02",
            "city_longitude": "4.36",
            "scheme_color": "5"
        },
        {
            "id": "1682",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/rotterdam-s-gravendijkwal-lorry-zez",
            "introtext": "There is a lorry ban on the `s-Gravendijkwal road to reduce cut-through traffic and pollution",
            "cityname": "Rotterdam s-Gravendijkwal - lorry Zero Emission Zone",
            "city_latitude": "51.92",
            "city_longitude": "4.47",
            "scheme_color": "5"
        },
        {
            "id": "1535",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/london-zez-islington-and-hackney",
            "introtext": "UK-LO",
            "cityname": "London Zero Emission Zone - Islington and Hackney",
            "city_latitude": "51.55",
            "city_longitude": "-0.06",
            "scheme_color": "5"
        },
        {
            "id": "1934",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/oxford-zez",
            "introtext": "",
            "cityname": "Oxford - Zero Emission Zone",
            "city_latitude": "51.75",
            "city_longitude": "-1.25",
            "scheme_color": "5"
        },
        {
            "id": "2124",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/ede-zero-emission-zone-logistics",
            "introtext": "Ede will implement ZEZ logistic 1 January 2030",
            "cityname": "Ede - Zero Emission Zone Logistics",
            "city_latitude": "52.04",
            "city_longitude": "5.66",
            "scheme_color": "5"
        },
        {
            "id": "2128",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/helmond-zez",
            "introtext": "",
            "cityname": "Helmond - Zero Emission Zone",
            "city_latitude": "51.48",
            "city_longitude": "5.66",
            "scheme_color": "5"
        },
        {
            "id": "2048",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/arnhem-zero-emission-zone-logistics",
            "introtext": "Arnhem will implement ZEZ logistic 1 June 2026",
            "cityname": "Arnhem - Zero Emission Zone Logistics",
            "city_latitude": "51.98",
            "city_longitude": "5.91",
            "scheme_color": "5"
        },
        {
            "id": "2050",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/amsterdam-zero-emission-zone-logistics",
            "introtext": "Amsterdam will implement ZEZ logistic 1 January 2025",
            "cityname": "Amsterdam - Zero Emission Zone Logistics",
            "city_latitude": "52.37",
            "city_longitude": "4.89",
            "scheme_color": "5"
        },
        {
            "id": "2045",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/1576-paris-zero-emission-zone",
            "introtext": "There is also an <a title=\"Access Regulation\"  href=\"/countries-mainmenu-147/france/paris-ar\">Access Regulation</a> in place in Paris<br>\r\nParis started a monthly <b>carfree</b> day on the 18th May 2016. The second carfree day will take place 22th September 2017.\r\n",
            "cityname": "Paris - Zero Emission Zone",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "5"
        },
        {
            "id": "2046",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-paris-zero-emission-zone",
            "introtext": "There is also an <a title=\"Access Regulation\"  href=\"/countries-mainmenu-147/france/paris-ar\">Access Regulation</a> in place in Paris<br>\r\nParis started a monthly <b>carfree</b> day on the 18th May 2016. The second carfree day will take place 22th September 2017.\r\n",
            "cityname": "Greater Paris - Zero Emission Zone",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "5"
        },
        {
            "id": "2051",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/assen-zero-emission-zone-logistics",
            "introtext": "Assen will implement ZEZ logistic 1 January 2025",
            "cityname": "Assen - Zero Emission Zone Logistics",
            "city_latitude": "52.99",
            "city_longitude": "6.56",
            "scheme_color": "5"
        },
        {
            "id": "2052",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/delft-zero-emission-zone-logistics",
            "introtext": "Delft will implement ZEZ logistic 1 January 2025",
            "cityname": "Delft - Zero Emission Zone Logistics",
            "city_latitude": "52.01",
            "city_longitude": "4.35",
            "scheme_color": "5"
        },
        {
            "id": "2053",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/den-haag-zero-emission-zone-logistics",
            "introtext": "Den Haag will implement ZEZ logistic 1 January 2025",
            "cityname": "Den Haag - Zero Emission Zone Logistics",
            "city_latitude": "52.07",
            "city_longitude": "4.30",
            "scheme_color": "5"
        },
        {
            "id": "2054",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/eindhoven-zero-emission-zone-logistics",
            "introtext": "Eindhoven will implement ZEZ logistic 1 January 2025",
            "cityname": "Eindhoven - Zero Emission Zone Logistics",
            "city_latitude": "51.44",
            "city_longitude": "5.46",
            "scheme_color": "5"
        },
        {
            "id": "2055",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/enschede-zero-emission-zone-logistics",
            "introtext": "Enschede will implement ZEZ logistic 1 July 2025",
            "cityname": "Enschede - Zero Emission Zone Logistics",
            "city_latitude": "52.22",
            "city_longitude": "6.89",
            "scheme_color": "5"
        },
        {
            "id": "2056",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/gouda-zero-emission-zone-logistics",
            "introtext": "Gouda will implement ZEZ logistic 1 January 2025",
            "cityname": "Gouda - Zero Emission Zone Logistics",
            "city_latitude": "52.01",
            "city_longitude": "4.71",
            "scheme_color": "5"
        },
        {
            "id": "2057",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/groningen-zero-emission-zone-logistics",
            "introtext": "Groningen will implement ZEZ logistic 1 April 2025",
            "cityname": "Groningen - Zero Emission Zone Logistics",
            "city_latitude": "53.21",
            "city_longitude": "6.56",
            "scheme_color": "5"
        },
        {
            "id": "2058",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/haarlem-zero-emission-zone-logistics",
            "introtext": "Haarlem will implement ZEZ logistic 1 June 2025",
            "cityname": "Haarlem - Zero Emission Zone Logistics",
            "city_latitude": "52.38",
            "city_longitude": "4.64",
            "scheme_color": "5"
        },
        {
            "id": "2060",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/leiden-zero-emission-zone-logistics",
            "introtext": "Leiden will implement ZEZ logistic 1 January 2025",
            "cityname": "Leiden - Zero Emission Zone Logistics",
            "city_latitude": "52.16",
            "city_longitude": "4.49",
            "scheme_color": "5"
        },
        {
            "id": "2061",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/maastricht-zero-emission-zone-logistics",
            "introtext": "Maastricht will implement ZEZ logistic 1 January 2025",
            "cityname": "Maastricht - Zero Emission Zone Logistics",
            "city_latitude": "50.85",
            "city_longitude": "5.69",
            "scheme_color": "5"
        },
        {
            "id": "2062",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/nijmegen-zero-emission-zone-logistics",
            "introtext": "Nijmegen will implement ZEZ logistic 1 January 2025",
            "cityname": "Nijmegen - Zero Emission Zone Logistics",
            "city_latitude": "51.81",
            "city_longitude": "5.83",
            "scheme_color": "5"
        },
        {
            "id": "2063",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/rotterdam-zero-emission-zone-logistics",
            "introtext": "Rotterdam will implement ZEZ logistic 1 January 2025",
            "cityname": "Rotterdam - Zero Emission Zone Logistics",
            "city_latitude": "51.92",
            "city_longitude": "4.47",
            "scheme_color": "5"
        },
        {
            "id": "2065",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/s-hertogenbosch-den-bosch-zero-emission-zone-logistics",
            "introtext": "s-Hertogenbosch will implement ZEZ logistic 1 March 2025",
            "cityname": "s-Hertogenbosch (Den Bosch) - Zero Emission Zone Logistics",
            "city_latitude": "51.70",
            "city_longitude": "5.30",
            "scheme_color": "5"
        },
        {
            "id": "2066",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/tilburg-zero-emission-zone-logistics",
            "introtext": "Tilburg will implement ZEZ logistic 1 January 2025",
            "cityname": "Tilburg - Zero Emission Zone Logistics",
            "city_latitude": "51.56",
            "city_longitude": "5.09",
            "scheme_color": "5"
        },
        {
            "id": "2067",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/utrecht-zero-emission-zone-logistics",
            "introtext": "Utrecht will implement ZEZ logistic 1 January 2025",
            "cityname": "Utrecht - Zero Emission Zone Logistics",
            "city_latitude": "52.09",
            "city_longitude": "5.12",
            "scheme_color": "5"
        },
        {
            "id": "2323",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/bruxelles-brussels-zero-emission-zone",
            "introtext": "",
            "cityname": "Bruxelles - Brussel (Brussels) - Zero Emission Zone",
            "city_latitude": "50.85",
            "city_longitude": "4.35",
            "scheme_color": "5"
        },
        {
            "id": "2068",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/zaanstad-zero-emission-zone-logistics",
            "introtext": "Zaanstad will implement ZEZ logistic 1 January 2030",
            "cityname": "Zaanstad - Zero Emission Zone Logistics",
            "city_latitude": "52.45",
            "city_longitude": "4.75",
            "scheme_color": "5"
        },
        {
            "id": "2070",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/zwolle-zero-emission-zone-logistics",
            "introtext": "Zwolle will implement ZEZ logistic 1 January 2025",
            "cityname": "Zwolle - Zero Emission Zone Logistics",
            "city_latitude": "52.51",
            "city_longitude": "6.08",
            "scheme_color": "5"
        },
        {
            "id": "2072",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/oslo-zero-emission-zone",
            "introtext": "",
            "cityname": "Oslo - Zero Emission Zone",
            "city_latitude": "59.91",
            "city_longitude": "10.75",
            "scheme_color": "5"
        },
        {
            "id": "2121",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/deventer-zero-emission-zone-logistics",
            "introtext": "Deventer will implement ZEZ logistic 1 January 2028",
            "cityname": "Deventer - Zero Emission Zone Logistics",
            "city_latitude": "52.26",
            "city_longitude": "6.15",
            "scheme_color": "5"
        },
        {
            "id": "2127",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/schiphol-zero-emission-zone-logistics",
            "introtext": "Schipol will implement ZEZ logistic 1 January 2026",
            "cityname": "Schiphol - Zero Emission Zone Logistics",
            "city_latitude": "52.31",
            "city_longitude": "4.74",
            "scheme_color": "5"
        },
        {
            "id": "2120",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/apeldoorn-zero-emission-zone-logistics",
            "introtext": "Apeldoorn will implement ZEZ logistic 1 January 2030",
            "cityname": "Apeldoorn - Zero Emission Zone Logistics",
            "city_latitude": "52.21",
            "city_longitude": "5.96",
            "scheme_color": "5"
        },
        {
            "id": "2219",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/almere-zero-emission-zone-logistics",
            "introtext": "Almere will implement ZEZ logistic 1 January 2028.",
            "cityname": "Almere - Zero Emission Zone Logistics",
            "city_latitude": "52.37",
            "city_longitude": "5.22",
            "scheme_color": "5"
        },
        {
            "id": "2270",
            "citypath": "/countries-mainmenu-147/denmark-mainmenu-221/copenhagen-kobenhavn-frederiksberg-zero-emission-zone",
            "introtext": "",
            "cityname": "Copenhagen (København) & Frederiksberg - Zero Emission Zone",
            "city_latitude": "55.67",
            "city_longitude": "12.56",
            "scheme_color": "5"
        },
        {
            "id": "2300",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/hilversum-zero-emission-zone-logistics",
            "introtext": "Hilversum  will implement ZEZ logistic at a date not decided yet.",
            "cityname": "Hilversum - Zero Emission Zone Logistics",
            "city_latitude": "52.22",
            "city_longitude": "5.16",
            "scheme_color": "5"
        },
        {
            "id": "2327",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-zero-emission-zone",
            "introtext": "<p>\r\n\tStockholm also has various schmes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/sweden-mainmenu-248/stockholm\">low emission zone</a></li>\r\n\t<li>\r\n\t\ta <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-charging-scheme\" title=\"Charging Scheme\">charging scheme</a></li>\r\n\t<li>\r\n\t\tand <a href=\"/countries-mainmenu-147/sweden-mainmenu-248/stockholm-lorry-regulations\">lorry regulations</a>&nbsp;</li>\r\n</ul><br>\r\nAnd from 31.12.2024 also a zero emission zone.\r\n",
            "cityname": "Stockholm - Zero Emission Zone",
            "city_latitude": "59.33",
            "city_longitude": "18.06",
            "scheme_color": "5"
        },
        {
            "id": "2441",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/breda-zero-emission-zone-logistics",
            "introtext": "Breda will implement ZEZ logistic 1 January 2029",
            "cityname": "Breda - Zero Emission Zone Logistics",
            "city_latitude": "51.57",
            "city_longitude": "4.76",
            "scheme_color": "5"
        },
        {
            "id": "499",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/palermo",
            "introtext": "The combined low emission zone, road charge, congestion charge and ZTL scheme has been in operation since 10 October 2016.\r\n",
            "cityname": "Palermo",
            "city_latitude": "38.11",
            "city_longitude": "13.36",
            "scheme_color": "2"
        },
        {
            "id": "490",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/milan-area-c-charging-scheme",
            "introtext": "<p>\r\n\tThere are several schemes in Milan:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\t<strong>NEW!</strong>&nbsp;<a href=\"/countries-mainmenu-147/italy-mainmenu-81/milano-lez-area-b\">Area B</a> is a Low Emission Zone that will be activated the <strong>25 February 2019</strong>. It will cover the entire city of Milan.</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milan-area-c-charging-scheme\" title=\"Milan C\">Milan C</a>&nbsp;is a combined Low Emission Zone and urban road charging scheme</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milano-ar\" title=\"Milan - AR\">Milan - AR</a>, an Access Regulation</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/como\" title=\"Milan province\">Milan province</a>, the Low Emission Zones of the four provinces of Milan, Como, Varese and Lecco merge to give a &#39;paw print&#39; shaped LEZ (see <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/milano\" title=\"Milan Province\">Milan Province</a>).</li>\r\n\t<li>\r\n\t\tshort term restrictions are possible, particularly in the winter <a href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/como\" title=\"See the Milan LEZ page\">See the Milan LEZ page</a>. To find out if scheme is operational go <a href=\"https://inlinea.cittametropolitana.mi.it/dati_ambientali/pm10/\" target=\"_blank\" title=\"Milan website about PM10 air pollution\">here</a>.</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milan-area-c-charging-scheme\" title=\"Milan C\">Milan C</a> now substitutes the <a class=\"new-window nturl\" href=\"/ecopass\" title=\"Milan ecopass\">Milan ecopass</a> that is no longer in operation.</li>\r\n</ul>\r\n\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a&nbsp;<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"><b>winter emergency scheme</b></a> in place from 1 October - 31 March.</p>\r\n\r\n<p>\r\n\t&nbsp;</p>\r\n",
            "cityname": "Milano Area C LEZ & CS",
            "city_latitude": "45.47",
            "city_longitude": "9.19",
            "scheme_color": "2"
        },
        {
            "id": "2438",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/harstad-charging-scheme",
            "introtext": "",
            "cityname": "Harstad - Road Toll",
            "city_latitude": "67.28",
            "city_longitude": "14.40",
            "scheme_color": "2"
        },
        {
            "id": "2434",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/bodo-charging-scheme",
            "introtext": "Bodo has a combined low emission zone and road tolling scheme if they are more polluting.",
            "cityname": "Bodo - Road Toll",
            "city_latitude": "67.28",
            "city_longitude": "14.40",
            "scheme_color": "2"
        },
        {
            "id": "1469",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/mersey-river-crossings-tunnel-toll",
            "introtext": "<p>\r\n\tThere are different options to cross the river Mersey in Liverpool:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\tvia Mersey Gateway (bridge)</li>\r\n\t<li>\r\n\t\tvia Silver Jubilee Bridge&nbsp;(is closed for refurbishment until end of 2018)</li>\r\n\t<li>\r\n\t\tthrough the Mersey Tunnels (Kingsway: Liverpool to Wallasey, Queensway: Liverpool to Birkenhead)</li>\r\n</ul>\r\n\r\n<p>\r\n\t&nbsp;</p>\r\n\r\n<p>\r\n\t&nbsp;</p>\r\n",
            "cityname": "Mersey River - Crossings Toll",
            "city_latitude": "53.40",
            "city_longitude": "-2.99",
            "scheme_color": "2"
        },
        {
            "id": "2435",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/alesund-charging-scheme",
            "introtext": "Alesund has a combined low emission zone and road tolling scheme if they are more polluting.",
            "cityname": "Alesund - Road Toll",
            "city_latitude": "62.47",
            "city_longitude": "6.14",
            "scheme_color": "2"
        },
        {
            "id": "812",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/london-charging-scheme",
            "introtext": "UK-LO",
            "cityname": "London - CS",
            "city_latitude": "51.51",
            "city_longitude": "-0.13",
            "scheme_color": "2"
        },
        {
            "id": "813",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/trondheim-charging-scheme",
            "introtext": "In addition, a seperate 'Low Emission Zone' is being considered for <a title=\"LEZ\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/trondheim\">Trondheim</a>.\r\n",
            "cityname": "Trondheim - CS",
            "city_latitude": "63.44",
            "city_longitude": "10.39",
            "scheme_color": "2"
        },
        {
            "id": "815",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/oslo-charging-scheme",
            "introtext": "<p>\r\n\tSince the end of 2016 the implementation of low emission zones is legally possible in Norway.</p>\r\n\r\n<p>\r\n\tA low emission zone has been implemented through the already existing congestion charging scheme 1st October 2017.</p>\r\n\r\n<p>\r\n\tThe congestion charge differentiates by environmental standard (Euro standard), fuel type, time, distance and if you have an AutoPASS.</p>\r\n\r\n<p>\r\n\tOslo also has&nbsp;an&nbsp;<a href=\"/countries-mainmenu-147/norway-mainmenu-197/oslo-emergency-scheme\" title=\"Oslo emergency scheme\">emergency scheme</a>&nbsp;&nbsp;in cases of high pollution.</p>\r\n\r\n<p>\r\n\t<br />\r\n\tOslo is also implementing measures to remove cars from the city centre by 2019 and improve the quality of the city centre. This is being done by removing parking spaces and making more space for cycling and public spaces, and has already started.</p>\r\n",
            "cityname": "Oslo - LEZ - CS",
            "city_latitude": "59.91",
            "city_longitude": "10.75",
            "scheme_color": "2"
        },
        {
            "id": "817",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/bergen-charging-scheme",
            "introtext": "Bergen has a combined low emission zone and road tolling scheme, where vehicles are charged more during rush hour, or if they are more polluting.</p>\n\n<p>\n\tThere is also an <a href=\"/countries-mainmenu-147/norway-mainmenu-197/bergen-odd-even-scheme\" title=\"Charging Scheme\">emergency scheme</a> that is in operation during high pollution events.",
            "cityname": "Bergen - CS",
            "city_latitude": "60.39",
            "city_longitude": "5.32",
            "scheme_color": "2"
        },
        {
            "id": "818",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/durham-charging-scheme",
            "introtext": "Durham has an access regulation scheme.",
            "cityname": "Durham - CS",
            "city_latitude": "54.78",
            "city_longitude": "-1.58",
            "scheme_color": "2"
        },
        {
            "id": "822",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/malta/valetta-charging-scheme",
            "introtext": "The road charging scheme is cordon based. The vehicle is charged when crossing into the area, enforced with cameras at the entrance of the scheme.",
            "cityname": "Valletta - CS",
            "city_latitude": "35.9",
            "city_longitude": "14.5",
            "scheme_color": "2"
        },
        {
            "id": "826",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/goeteborg-charging-scheme",
            "introtext": "Göteborg also has a <a title=\"LEZ\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/goteborg\">Low Emission Zone</a> in place.",
            "cityname": "Göteborg (Gothenburg) - CS",
            "city_latitude": "57.71",
            "city_longitude": "11.97",
            "scheme_color": "2"
        },
        {
            "id": "827",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-charging-scheme",
            "introtext": "<p>\r\n\tStockholm also has various schmes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/sweden-mainmenu-248/stockholm\">low emission zone</a></li>\r\n\t<li>\r\n\t\ta <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-charging-scheme\" title=\"Charging Scheme\">charging scheme</a></li>\r\n\t<li>\r\n\t\tand <a href=\"/countries-mainmenu-147/sweden-mainmenu-248/stockholm-lorry-regulations\">lorry regulations</a>&nbsp;</li>\r\n</ul>\r\n",
            "cityname": "Stockholm - CS",
            "city_latitude": "59.33",
            "city_longitude": "18.06",
            "scheme_color": "2"
        },
        {
            "id": "871",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/kristiansand-charging-scheme",
            "introtext": "NO-CS",
            "cityname": "Kristiansand - CS",
            "city_latitude": "58.15",
            "city_longitude": "8.00",
            "scheme_color": "2"
        },
        {
            "id": "872",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/stavanger-charging-scheme",
            "introtext": "NO-CS",
            "cityname": "Stavanger - CS",
            "city_latitude": "58.97",
            "city_longitude": "5.73",
            "scheme_color": "2"
        },
        {
            "id": "876",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/haugesund-charging-scheme",
            "introtext": "In Norway is a charging scheme in place.",
            "cityname": "Haugesund - CS",
            "city_latitude": "59.41",
            "city_longitude": "8.00",
            "scheme_color": "2"
        },
        {
            "id": "2353",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/lithuania/kaunas-charging-scheme",
            "introtext": "",
            "cityname": "Kaunas - CS",
            "city_latitude": "54.89",
            "city_longitude": "23.90",
            "scheme_color": "2"
        },
        {
            "id": "1683",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/latvia/jurmala-cs",
            "introtext": "Jurmala has a charging scheme in place.",
            "cityname": "Jurmala - CS",
            "city_latitude": "56.95",
            "city_longitude": "23.62",
            "scheme_color": "2"
        },
        {
            "id": "1514",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/dartford-charging-scheme",
            "introtext": "UK-LO\r\n",
            "cityname": "Dartford - Tunnel Toll",
            "city_latitude": "51.46",
            "city_longitude": "0.25",
            "scheme_color": "2"
        },
        {
            "id": "2436",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/lower glomma-charging-scheme",
            "introtext": "",
            "cityname": "Lower Glomma - Road Toll",
            "city_latitude": "59.28",
            "city_longitude": "11.10",
            "scheme_color": "2"
        },
        {
            "id": "2433",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/tromso-charging-scheme",
            "introtext": "Tromso has a combined low emission zone and road tolling scheme, where vehicles are charged more during rush hour, or if they are more polluting.",
            "cityname": "Tromso - CS",
            "city_latitude": "69.64",
            "city_longitude": "18.95",
            "scheme_color": "2"
        },
        {
            "id": "2113",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-nancy",
            "introtext": "france",
            "cityname": "Greater Nancy",
            "city_latitude": "48.69",
            "city_longitude": "6.18",
            "scheme_color": "1"
        },
        {
            "id": "68",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/london",
            "introtext": "UK-LO",
            "cityname": "London",
            "city_latitude": "51.51",
            "city_longitude": "-0.13",
            "scheme_color": "1"
        },
        {
            "id": "2294",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/distrito-centro",
            "introtext": "<p>\r\n\tMadrid has various schemes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid\" title=\"low emission zone\">low emission parking scheme</a>&nbsp;that favours less polluting vehicles</li>\r\n\t<li>\r\n\t\ta <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">low emission traffic limited zone</a>&nbsp;vehicles have to be owned by residents or zero emission</li>\r\n\t<li>\r\n\t\tan <a href=\"/countries-mainmenu-147/spain/madrid-odd-and-even-numberplates\">emergency scheme</a>&nbsp;</li>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid-weight\" title=\"weight restriction\">weight regulation</a></li>\r\n</ul>\r\n\r\n<p>\r\n\t<strong>NEW! From&nbsp;30 November 2018&nbsp;<a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">Central Madrid</a>&nbsp;</strong>is in place. The&nbsp;existing APRs (&Aacute;reas de Prioridad Residencial &nbsp;= areas where residents have priority) be extended and united into one big APR that is called Madrid Central.</p>\r\n\r\n<p>\r\n\tIt will be of informative character for the first two months and will be fully enforced from <strong>February 2019 on</strong>. The APR Central Madrid will cover practically the entire downtown area of Madrid.&nbsp;</p>\r\n\r\n<p>\r\n\tThe standards in the Central Madrid low emission zone are gradually tightened until a zero emission zone is reached in 2025.</p>\r\n\r\n<p>\r\n\tThe Grand Via is planned to be car-free by summer 2019.<br />\r\n\tMadrid is one of 4 cities that have stated they wish to remove diesel vehicles from the city. As part of this, the city plans to increase the numbers of access restrictions for private cars.</p>\r\n",
            "cityname": "Madrid - Distrito Centro",
            "city_latitude": "40.42",
            "city_longitude": "-3.70",
            "scheme_color": "1"
        },
        {
            "id": "123",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/a12-motorway-tirol",
            "introtext": "<b>On the A12</b> there are several schemes, please select the one you want information on, and then the details will show below",
            "cityname": "A12 Motorway (Tirol)",
            "city_latitude": "47.26",
            "city_longitude": "11.45",
            "scheme_color": "1"
        },
        {
            "id": "142",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/breda",
            "introtext": "Breda has had a Low Emission Zone in place since the 5th October 2007. ",
            "cityname": "Breda",
            "city_latitude": "52.38",
            "city_longitude": "4.64",
            "scheme_color": "1"
        },
        {
            "id": "145",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/eindhoven",
            "introtext": "Eindhoven has had a Low Emission Zone in place since the 1st July 2007.",
            "cityname": "Eindhoven",
            "city_latitude": "51.44",
            "city_longitude": "5.47",
            "scheme_color": "1"
        },
        {
            "id": "146",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/den-bosch-s-hertogenbosch",
            "introtext": "S'-Hertogenbosch has had a Low Emission Zone in place since the 1st September 2007. ",
            "cityname": "s-Hertogenbosch",
            "city_latitude": "51.70",
            "city_longitude": "5.30",
            "scheme_color": "1"
        },
        {
            "id": "148",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/maastricht",
            "introtext": "Maastricht town centre has been a Low Emission Zone from 1st March 2010. This LEZ affects only lorries.<br>\r\nThe low emission zone in Maastricht is expected to include cars and vans from 2020.\r\nThe municipality investigated the possibility to enforce this low\r\nemission zone by stickers, but is likely to use cameras.",
            "cityname": "Maastricht",
            "city_latitude": "50.85",
            "city_longitude": "5.71",
            "scheme_color": "1"
        },
        {
            "id": "149",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/rotterdam",
            "introtext": "Rotterdam has a LEZ in place.<br>\r\nRotterdam also has an access regulation in place called <a title=\"Rotterdam - AR\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/netherlands-mainmenu-88/rotterdam-ar\">Rotterdam - AR</a>.",
            "cityname": "Rotterdam",
            "city_latitude": "51.92",
            "city_longitude": "4.47",
            "scheme_color": "1"
        },
        {
            "id": "158",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/tilburg",
            "introtext": "Tilburg has had a Low Emission Zone in place since the 1st September 2007. ",
            "cityname": "Tilburg",
            "city_latitude": "51.56",
            "city_longitude": "5.08",
            "scheme_color": "1"
        },
        {
            "id": "159",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/utrecht",
            "introtext": "Utrecht has had a Low Emission Zone in place since the 1st July 2007.<br>\nThere is also a lorry ban on the street \"`s-Gravendijkwal\" in the city center for lorries > 3.5T.",
            "cityname": "Utrecht",
            "city_latitude": "52.09",
            "city_longitude": "5.12",
            "scheme_color": "1"
        },
        {
            "id": "164",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/berlin",
            "introtext": "",
            "cityname": "Berlin",
            "city_latitude": "52.52",
            "city_longitude": "13.41",
            "scheme_color": "1"
        },
        {
            "id": "174",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/koln-cologne",
            "introtext": "Köln (Cologne) has a Low Emission Zone in operation since 1st January 2008. ",
            "cityname": "Köln (Cologne)",
            "city_latitude": "50.94",
            "city_longitude": "6.96",
            "scheme_color": "1"
        },
        {
            "id": "143",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/delft",
            "introtext": "Delft has had a Low Emission Zone in place since 1st January 2010.",
            "cityname": "Delft",
            "city_latitude": "52.02",
            "city_longitude": "4.36",
            "scheme_color": "1"
        },
        {
            "id": "147",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/leiden",
            "introtext": "Leiden has had a Low Emission Zone since 1st January 2010. <br>\nFrom July 1, 2013, only trucks with diesel engines Euro Class IV or higher and trucks that drive on gas have access to the environmental zone.",
            "cityname": "Leiden",
            "city_latitude": "52.17",
            "city_longitude": "4.47",
            "scheme_color": "1"
        },
        {
            "id": "144",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/den-haag",
            "introtext": "Den Haag (The Hague) has had a Low Emission Zone in place since the 16th April 2008. <br>\nA further zone is being investigated for Rijswijk, a suburb to the east of Den Haag.<br><br> ",
            "cityname": "Den Haag (The Hague)",
            "city_latitude": "52.0",
            "city_longitude": "4.28",
            "scheme_color": "1"
        },
        {
            "id": "141",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/amsterdam",
            "introtext": "<p>\r\n\tAmsterdam has three different low emission zones in place.</p>\r\n\r\n<p>\r\n\tThese are:</p>\r\n\r\n<ol>\r\n\t<li>\r\n\t\tlorries &gt; 3.5t since <strong>9 October 2008</strong></li>\r\n\t<li>\r\n\t\tdiesel delivery vans since <strong>1 January</strong> <strong>2017</strong> &ndash; diesel delivery vans built before 1 January 2000 are no longer allowed to enter the low emission zone</li>\r\n\t<li>\r\n\t\tmoped, diesel taxis and diesel buses since <strong>1 January </strong>2018 &ndash; diesel taxis built before 2009 and diesel busses built before 2005, mopeds built before 2011 are no longer allowed to enter the low emission zone</li>\r\n</ol>\r\n\r\n<p>\r\n\tAmsterdam wants to tighten the standard for lorries &gt;3.5t in <strong>2020</strong>.</p>\r\n\r\n<p>\r\n\tAmsterdam&rsquo;s goas for the future is to be as much emission-free as possible by 2025. Hence electric vehicles are promoted in Amsterdam.</p>\r\n\r\n<p>\r\n\tFor <strong>2026</strong> Amsterdam wants its <strong>public bus transport</strong> to be <strong>emission free</strong>.</p>\r\n",
            "cityname": "Amsterdam",
            "city_latitude": "52.37",
            "city_longitude": "4.89",
            "scheme_color": "1"
        },
        {
            "id": "258",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/dortmund",
            "introtext": "",
            "cityname": "Dortmund",
            "city_latitude": "51.5",
            "city_longitude": "7.47",
            "scheme_color": "1"
        },
        {
            "id": "260",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/duisburg",
            "introtext": "",
            "cityname": "Duisburg",
            "city_latitude": "51.43",
            "city_longitude": "6.75",
            "scheme_color": "1"
        },
        {
            "id": "262",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/dusseldorf",
            "introtext": "",
            "cityname": "Düsseldorf",
            "city_latitude": "51.22",
            "city_longitude": "6.78",
            "scheme_color": "1"
        },
        {
            "id": "256",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/bottrop",
            "introtext": "",
            "cityname": "Bottrop",
            "city_latitude": "51.52",
            "city_longitude": "6.97",
            "scheme_color": "1"
        },
        {
            "id": "254",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/bonn",
            "introtext": "",
            "cityname": "Bonn",
            "city_latitude": "50.73",
            "city_longitude": "7.10",
            "scheme_color": "1"
        },
        {
            "id": "252",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/bochum",
            "introtext": "",
            "cityname": "Bochum",
            "city_latitude": "51.47",
            "city_longitude": "7.22",
            "scheme_color": "1"
        },
        {
            "id": "182",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/osnabruck",
            "introtext": "Osnabrück has a Low Emission Zone in place.",
            "cityname": "Osnabrück",
            "city_latitude": "52.27",
            "city_longitude": "8.05",
            "scheme_color": "1"
        },
        {
            "id": "178",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/munchen",
            "introtext": "München also has a <a title=\"lorry transit ban\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/muenchen-munich-ar\">lorry transit ban</a> in place.",
            "cityname": "München (Munich)",
            "city_latitude": "48.14",
            "city_longitude": "11.57",
            "scheme_color": "1"
        },
        {
            "id": "176",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/leipzig",
            "introtext": "Leipzig also has a <a title=\"lorry transit ban\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/leipzig-ar\">lorry transit ban</a> in place.",
            "cityname": "Leipzig",
            "city_latitude": "51.33",
            "city_longitude": "12.37",
            "scheme_color": "1"
        },
        {
            "id": "162",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/augsburg",
            "introtext": "",
            "cityname": "Augsburg",
            "city_latitude": "48.37",
            "city_longitude": "10.9",
            "scheme_color": "1"
        },
        {
            "id": "166",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/bremen",
            "introtext": "",
            "cityname": "Bremen",
            "city_latitude": "53.07",
            "city_longitude": "8.78",
            "scheme_color": "1"
        },
        {
            "id": "170",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/frankfurt",
            "introtext": "Frankfurt has a low emission zone in place.",
            "cityname": "Frankfurt",
            "city_latitude": "50.12",
            "city_longitude": "8.68",
            "scheme_color": "1"
        },
        {
            "id": "773",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/ingersheim",
            "introtext": "Ingersheim is now part of the regional Low Emission Zone called\r\n<strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a>, Hemmingen and Region\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).\r\n",
            "cityname": "Ingersheim",
            "city_latitude": "48.96",
            "city_longitude": "9.18",
            "scheme_color": "1"
        },
        {
            "id": "1823",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/bergamo",
            "introtext": "",
            "cityname": "Bergamo Province",
            "city_latitude": "45.70",
            "city_longitude": "9.67",
            "scheme_color": "1"
        },
        {
            "id": "1824",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/brescia",
            "introtext": "",
            "cityname": "Brescia Province",
            "city_latitude": "45.70",
            "city_longitude": "9.67",
            "scheme_color": "1"
        },
        {
            "id": "1825",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/como",
            "introtext": "",
            "cityname": "Como Province",
            "city_latitude": "45.80",
            "city_longitude": "9.08",
            "scheme_color": "1"
        },
        {
            "id": "1826",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/cremona",
            "introtext": "",
            "cityname": "Cremona Province",
            "city_latitude": "45.13",
            "city_longitude": "10.03",
            "scheme_color": "1"
        },
        {
            "id": "1827",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lecco",
            "introtext": "",
            "cityname": "Lecco Province",
            "city_latitude": "45.85",
            "city_longitude": "9.39",
            "scheme_color": "1"
        },
        {
            "id": "1828",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lodi",
            "introtext": "",
            "cityname": "Lodi Province",
            "city_latitude": "45.31",
            "city_longitude": "9.50",
            "scheme_color": "1"
        },
        {
            "id": "1829",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/mantova",
            "introtext": "",
            "cityname": "Mantova Province",
            "city_latitude": "45.16",
            "city_longitude": "10.80",
            "scheme_color": "1"
        },
        {
            "id": "1830",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/monza-and-brianza-province",
            "introtext": "",
            "cityname": "Monza and Brianza Province",
            "city_latitude": "45.58",
            "city_longitude": "9.27",
            "scheme_color": "1"
        },
        {
            "id": "1831",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/pavia",
            "introtext": "",
            "cityname": "Pavia Province",
            "city_latitude": "45.19",
            "city_longitude": "9.16",
            "scheme_color": "1"
        },
        {
            "id": "1832",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/varese",
            "introtext": "",
            "cityname": "Varese Province",
            "city_latitude": "45.80",
            "city_longitude": "8.83",
            "scheme_color": "1"
        },
        {
            "id": "1833",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/milano",
            "introtext": "",
            "cityname": "Milano Province",
            "city_latitude": "45.47",
            "city_longitude": "9.19",
            "scheme_color": "1"
        },
        {
            "id": "994",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/paris",
            "introtext": "france",
            "cityname": "Paris",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "1"
        },
        {
            "id": "1498",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/grenoble",
            "introtext": "france",
            "cityname": "Greater Grenoble",
            "city_latitude": "45.18",
            "city_longitude": "5.72",
            "scheme_color": "1"
        },
        {
            "id": "2317",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/cordoba",
            "introtext": "Cordoba has implemented a ZBE that covers the same area as the Acire zone.",
            "cityname": "Cordoba",
            "city_latitude": "31.42",
            "city_longitude": "-64.18",
            "scheme_color": "1"
        },
        {
            "id": "1478",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/limburg",
            "introtext": "Limburg has implemented a Low Emission Zone 31 January 2018.",
            "cityname": "Limburg",
            "city_latitude": "50.39",
            "city_longitude": "8.07",
            "scheme_color": "1"
        },
        {
            "id": "833",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/brighton",
            "introtext": "There is one street in Brighton that is formally an LEZ now. Only public buses are affected by this LEZ.",
            "cityname": "Brighton",
            "city_latitude": "50.82",
            "city_longitude": "-0.15",
            "scheme_color": "1"
        },
        {
            "id": "416",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/bolzano-province/bressanone-brixen",
            "introtext": "The city of Bressanone (Brixen) has a low emission zone in place. For further details see  below.",
            "cityname": "Bressanone (Brixen)",
            "city_latitude": "46.72",
            "city_longitude": "11.65",
            "scheme_color": "1"
        },
        {
            "id": "414",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/bolzano-province/bolzano-bozen7",
            "introtext": "There is also an access regulation called <a title=\"Bolzano - AR\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/bolzano-province/bolzano-ar\">Bolzano - AR</a> in place.",
            "cityname": "Bolzano (Bozen)",
            "city_latitude": "46.50",
            "city_longitude": "11.35",
            "scheme_color": "1"
        },
        {
            "id": "823",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/wien-vienna",
            "introtext": "Wien has a low emission zone in place.",
            "cityname": "Wien (Vienna)",
            "city_latitude": "48.2081743",
            "city_longitude": "16.3738189",
            "scheme_color": "1"
        },
        {
            "id": "824",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/burgenland",
            "introtext": "Burgenland has a low emission zone.",
            "cityname": "Burgenland",
            "city_latitude": "47.50",
            "city_longitude": "16.62",
            "scheme_color": "1"
        },
        {
            "id": "825",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/niederoesterreich",
            "introtext": "Niederösterreich has a low emission zone in place.",
            "cityname": "Niederosterreich",
            "city_latitude": "48.41",
            "city_longitude": "15.61",
            "scheme_color": "1"
        },
        {
            "id": "330",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm",
            "introtext": "<p>\r\n\tStockholm also has various schmes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/sweden-mainmenu-248/stockholm\">low emission zone</a></li>\r\n\t<li>\r\n\t\ta <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-charging-scheme\" title=\"Charging Scheme\">charging scheme</a></li>\r\n\t<li>\r\n\t\tand <a href=\"/countries-mainmenu-147/sweden-mainmenu-248/stockholm-lorry-regulations\">lorry regulations</a>&nbsp;</li>\r\n</ul>\r\n",
            "cityname": "Stockholm",
            "city_latitude": "59.33",
            "city_longitude": "18.06",
            "scheme_color": "1"
        },
        {
            "id": "2117",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/sant-cugat",
            "introtext": "Sant Cugat del Valles has implemented a ZBE, low emission  1 May 2021. zone ",
            "cityname": "Sant Cugat del Valles",
            "city_latitude": "41.46",
            "city_longitude": "2.08",
            "scheme_color": "1"
        },
        {
            "id": "326",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/lund",
            "introtext": "",
            "cityname": "Lund",
            "city_latitude": "55.7",
            "city_longitude": "13.19",
            "scheme_color": "1"
        },
        {
            "id": "328",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/malmo",
            "introtext": "",
            "cityname": "Malmö",
            "city_latitude": "55.61",
            "city_longitude": "13.00",
            "scheme_color": "1"
        },
        {
            "id": "324",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/helsingborg",
            "introtext": "",
            "cityname": "Helsingborg",
            "city_latitude": "56.05",
            "city_longitude": "12.68",
            "scheme_color": "1"
        },
        {
            "id": "322",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/goteborg",
            "introtext": "Göteborg also has a <a title=”Charging Scheme\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/goeteborg-charging-scheme\">Charging Scheme</a> in place.",
            "cityname": "Göteborg (Gothenburg)",
            "city_latitude": "57.71",
            "city_longitude": "11.97",
            "scheme_color": "1"
        },
        {
            "id": "308",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/denmark-mainmenu-221/odense",
            "introtext": "Odense has a low emission zone in place since the 1 July 2010.",
            "cityname": "Odense",
            "city_latitude": "55.39",
            "city_longitude": "10.39",
            "scheme_color": "1"
        },
        {
            "id": "100",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/czech-republic-mainmenu-448/praha",
            "introtext": "Prague is considering a Low Emission Zone, the start date is unknown. The earliest Czech law allows is 2019.<br>\n\nPlease note that there is also a <a title=\"Praha (Prague permit scheme)\" class=\"nturl\" href=\"/countries-mainmenu-147/czech-republic-mainmenu-448/praha-prague-permit\">traffic regulation / permit scheme</a> in Praha (Prague) that requires your vehicle to meet certain emission standards. <br>\n\nAnd an access regulation for <a title=\"coaches\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/czech-republic-mainmenu-448/praha-prague-coaches\">tourist buses</a> in Prague.\n\n\n",
            "cityname": "Praha (Prague)",
            "city_latitude": "50.09",
            "city_longitude": "14.42",
            "scheme_color": "1"
        },
        {
            "id": "219",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/markgroningen",
            "introtext": "Markgröningen is now part of the regional Low Emission Zone called\r\n<strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a>, Hemmingen and Region\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).<br>\r\nThere is also a <a title=\"lorry transit ban\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroeningen-ar\">lorry transit ban</a> in place in Markgröningen.\r\n",
            "cityname": "Markgröningen",
            "city_latitude": "48.90",
            "city_longitude": "9.08",
            "scheme_color": "1"
        },
        {
            "id": "304",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/denmark-mainmenu-221/arhus",
            "introtext": "Århus has a low emission zone in place.",
            "cityname": "Aarhus",
            "city_latitude": "56.16",
            "city_longitude": "10.21",
            "scheme_color": "1"
        },
        {
            "id": "302",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/denmark-mainmenu-221/aalborg",
            "introtext": "The LEZ has been in place since 1st February 2009.",
            "cityname": "Aalborg",
            "city_latitude": "57.05",
            "city_longitude": "9.92",
            "scheme_color": "1"
        },
        {
            "id": "264",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/essen",
            "introtext": "",
            "cityname": "Essen",
            "city_latitude": "51.47",
            "city_longitude": "7.03",
            "scheme_color": "1"
        },
        {
            "id": "266",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/gelsenkirchen",
            "introtext": "",
            "cityname": "Gelsenkirchen",
            "city_latitude": "51.53",
            "city_longitude": "7.1",
            "scheme_color": "1"
        },
        {
            "id": "268",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/muelheim",
            "introtext": "",
            "cityname": "Mülheim",
            "city_latitude": "50.12",
            "city_longitude": "8.83",
            "scheme_color": "1"
        },
        {
            "id": "1512",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/a12-sectoral-driving-ban",
            "introtext": "<b>On the A12</b> there are several schemes, please select the one you want information on, and then the details will show below",
            "cityname": "A12 Sectoral driving ban ",
            "city_latitude": "47.26",
            "city_longitude": "11.45",
            "scheme_color": "1"
        },
        {
            "id": "2201",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/london-construction",
            "introtext": "UK-LO",
            "cityname": "London Construction",
            "city_latitude": "51.51",
            "city_longitude": "-0.13",
            "scheme_color": "1"
        },
        {
            "id": "270",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/munster",
            "introtext": "",
            "cityname": "Münster",
            "city_latitude": "51.96",
            "city_longitude": "7.67",
            "scheme_color": "1"
        },
        {
            "id": "272",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/neuss",
            "introtext": "",
            "cityname": "Neuss",
            "city_latitude": "51.2",
            "city_longitude": "6.66",
            "scheme_color": "1"
        },
        {
            "id": "274",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/oberhausen",
            "introtext": "",
            "cityname": "Oberhausen",
            "city_latitude": "51.48",
            "city_longitude": "6.85",
            "scheme_color": "1"
        },
        {
            "id": "276",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/recklinghausen",
            "introtext": "",
            "cityname": "Recklinghausen",
            "city_latitude": "51.58",
            "city_longitude": "7.2",
            "scheme_color": "1"
        },
        {
            "id": "278",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/wuppertal",
            "introtext": "",
            "cityname": "Wuppertal",
            "city_latitude": "51.25",
            "city_longitude": "7.15",
            "scheme_color": "1"
        },
        {
            "id": "202",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/freiburg",
            "introtext": "Due to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).",
            "cityname": "Freiburg",
            "city_latitude": "47.98",
            "city_longitude": "7.85",
            "scheme_color": "1"
        },
        {
            "id": "2333",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/parla",
            "introtext": "Parla will implement a low emission zone in 2025",
            "cityname": "Parla",
            "city_latitude": "40.23",
            "city_longitude": "-3.76",
            "scheme_color": "1"
        },
        {
            "id": "216",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg",
            "introtext": "Ludwigsburg is now part of the regional Low Emission Zone called\r\n<strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim&Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a>, Hemmingen and Region\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).\r\n",
            "cityname": "Ludwigsburg",
            "city_latitude": "48.88",
            "city_longitude": "9.18",
            "scheme_color": "1"
        },
        {
            "id": "218",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/mannheim",
            "introtext": "Mannheim has a Low Emission Zone in place.",
            "cityname": "Mannheim",
            "city_latitude": "49.48",
            "city_longitude": "8.48",
            "scheme_color": "1"
        },
        {
            "id": "220",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/muhlacker",
            "introtext": "Mühlacker has a Low Emission Zone in place.",
            "cityname": "Mühlacker",
            "city_latitude": "48.95",
            "city_longitude": "8.84",
            "scheme_color": "1"
        },
        {
            "id": "224",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/pforzheim",
            "introtext": "Pforzheim has a Low Emission Zone in place.",
            "cityname": "Pforzheim",
            "city_latitude": "48.87",
            "city_longitude": "8.68",
            "scheme_color": "1"
        },
        {
            "id": "226",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim",
            "introtext": "Pleidelsheim is now part of the regional Low Emission Zone called\r\n<strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a>, Hemmingen and Region\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).\r\n<br>There is also an access restriction in place in Pleidelsheim called <a title=\"Pleidelsheim - AR\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim-ar\">Pleidelsheim - AR</a>.",
            "cityname": "Pleidelsheim",
            "city_latitude": "48.96",
            "city_longitude": "9.2",
            "scheme_color": "1"
        },
        {
            "id": "232",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/stuttgart",
            "introtext": "Stuttgart also has a <a title=\"lorry transit ban\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/stuttgart-ar\">lorry transit ban</a> in place.<br>\nIn the case of high pollution events, there is also an alarm scheme. See below for further details.",
            "cityname": "Stuttgart",
            "city_latitude": "48.78",
            "city_longitude": "9.18",
            "scheme_color": "1"
        },
        {
            "id": "1675",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/remseck",
            "introtext": "The three regional Low Emission Zones of Stuttgart, Ludwigsburg and Leonberg\r\nnow all join up, to make, in practice, a combined Low Emission Zone.<br><br> \r\n\r\nThe Ludwigsburg and area regional LEZ includes <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> and covers also <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim, Patonville & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen \">Bietigheim-Bissingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>.<br><br>\r\n\r\n\r\nThe regional LEZ for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a> includes the towns of Ditzingen, Gerlingen, Hemmingen,\r\nKorntal-Münchingen and Schwieberdingen<br><br>\r\n\r\n \r\n\r\nThe Stuttgart LEZ borders both the LEZs above. <br><br>\r\n\r\n \r\n\r\nDue to potential confusion, please note that there are LEZs in\r\nBaden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar \">Freiberg am Neckar</a> (note the U or E in the spelling, too).<br>\r\n",
            "cityname": "Remseck",
            "city_latitude": "48.87",
            "city_longitude": "9.26",
            "scheme_color": "1"
        },
        {
            "id": "1014",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/offenbach",
            "introtext": "Offenbach has a Low Emission Zone in place.",
            "cityname": "Offenbach",
            "city_latitude": "50.12",
            "city_longitude": "8.68",
            "scheme_color": "1"
        },
        {
            "id": "502",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/acqui-terme",
            "introtext": "Acqui Terme in Piemont Italy has a low emission zone in place.",
            "cityname": "Acqui Terme",
            "city_latitude": "44.67",
            "city_longitude": "8.47",
            "scheme_color": "1"
        },
        {
            "id": "504",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alessandria",
            "introtext": "Alessandria has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Alessandria",
            "city_latitude": "44.55",
            "city_longitude": "8.37",
            "scheme_color": "1"
        },
        {
            "id": "506",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/casale-monferrato",
            "introtext": "There is also an access regulation in place called <a title=\"Casala Monferrato - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/casale-monferrato-access-regulation\">Casale Monferrato - AR</a>.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Casale Monferrato",
            "city_latitude": "45.13",
            "city_longitude": "8.44",
            "scheme_color": "1"
        },
        {
            "id": "508",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novi-ligure",
            "introtext": "There is also an access regulation in place called <a title=\"Novi Ligure - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novi-ligure-ar\">Novi Ligure - AR</a>.",
            "cityname": "Novi Ligure",
            "city_latitude": "44.77",
            "city_longitude": "8.78",
            "scheme_color": "1"
        },
        {
            "id": "510",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/tortona",
            "introtext": "Tortona has a low emission zone in place, also called ZTL in Italian. ",
            "cityname": "Tortona",
            "city_latitude": "44.86",
            "city_longitude": "8.83",
            "scheme_color": "1"
        },
        {
            "id": "512",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/valenza",
            "introtext": "Valenza has a low emission zone in place, also called ZTL in Italian. ",
            "cityname": "Valenza",
            "city_latitude": "45.02",
            "city_longitude": "8.65",
            "scheme_color": "1"
        },
        {
            "id": "514",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/asti",
            "introtext": "Asti in Piemont Italy has a low emission zone in place.",
            "cityname": "Asti",
            "city_latitude": "44.90",
            "city_longitude": "8.21",
            "scheme_color": "1"
        },
        {
            "id": "516",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/biella",
            "introtext": "There is also an access regulation in place called <a title=\"Biella - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/biella-access-regulation\">Biella - AR</a>.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Biella",
            "city_latitude": "45.57",
            "city_longitude": "8.05",
            "scheme_color": "1"
        },
        {
            "id": "518",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alba",
            "introtext": "Alba has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Alba",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "520",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/bra",
            "introtext": "The city of Bra has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Bra",
            "city_latitude": "44.7",
            "city_longitude": "7.85",
            "scheme_color": "1"
        },
        {
            "id": "522",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cuneo",
            "introtext": "<p> \tCuneo has an access regulation in place <a href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cuneo-ar\">Cuneo - AR</a>&nbsp;and a low emission zone in place, also called ZTL in Italian.&nbsp;</p><br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>\r\n",
            "cityname": "Cuneo",
            "city_latitude": "44.38",
            "city_longitude": "7.54",
            "scheme_color": "1"
        },
        {
            "id": "524",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/fossano",
            "introtext": "Fossano has a low emission zone in place, also called ZTL in Italian. ",
            "cityname": "Fossano",
            "city_latitude": "44.55",
            "city_longitude": "7.72",
            "scheme_color": "1"
        },
        {
            "id": "526",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/mondovi",
            "introtext": "Mondovi' has a low emission zone in place, also called ZTL in Italian. ",
            "cityname": "Mondovi",
            "city_latitude": "44.39",
            "city_longitude": "7.82",
            "scheme_color": "1"
        },
        {
            "id": "2249",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cossato",
            "introtext": "Cossato has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Cossato",
            "city_latitude": "45.56",
            "city_longitude": "8.17",
            "scheme_color": "1"
        },
        {
            "id": "528",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/savigliano",
            "introtext": "Savigliano has a low emission zone in place, also called ZTL in Italian. ",
            "cityname": "Savigliano",
            "city_latitude": "44.65",
            "city_longitude": "7.63",
            "scheme_color": "1"
        },
        {
            "id": "530",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgomanero",
            "introtext": "Borgomanero has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Borgomanero",
            "city_latitude": "45.7",
            "city_longitude": "8.47",
            "scheme_color": "1"
        },
        {
            "id": "532",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novara",
            "introtext": "There is also an access regulation in place called <a title=\"Novara - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novara-ar\">Novara - AR</a>.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Novara",
            "city_latitude": "45.44",
            "city_longitude": "8.62",
            "scheme_color": "1"
        },
        {
            "id": "534",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/beinasco",
            "introtext": "Beinasco has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Beinasco",
            "city_latitude": "45.02",
            "city_longitude": "7.58",
            "scheme_color": "1"
        },
        {
            "id": "536",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgaro-torinese",
            "introtext": "Borgaro Torinese has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Borgaro Torinese",
            "city_latitude": "45.15",
            "city_longitude": "7.65",
            "scheme_color": "1"
        },
        {
            "id": "538",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/carmagnola",
            "introtext": "Carmagnola has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Carmagnola",
            "city_latitude": "44.84",
            "city_longitude": "7.72",
            "scheme_color": "1"
        },
        {
            "id": "540",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chieri",
            "introtext": "There is also an access regulation in place called <a title=\"Chieri - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chieri-access-regulation\">Chieri - AR</a>.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Chieri",
            "city_latitude": "45.01",
            "city_longitude": "7.82",
            "scheme_color": "1"
        },
        {
            "id": "542",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chivasso",
            "introtext": "There is also an access regulation in place called <a title=\"Chivasso - AR\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chivasso-access-regulation\">Chivasso - AR</a>.",
            "cityname": "Chivasso",
            "city_latitude": "45.19",
            "city_longitude": "7.89",
            "scheme_color": "1"
        },
        {
            "id": "544",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/collegno",
            "introtext": "Collegno has a low emission zone in place, also called ZTL in Italian. \r\n<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Collegno",
            "city_latitude": "45.08",
            "city_longitude": "7.58",
            "scheme_color": "1"
        },
        {
            "id": "546",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/grugliasco",
            "introtext": "Grugliasco has a low emission zone in place, also called ZTL in Italian. \r\n<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Grugliasco",
            "city_latitude": "45.07",
            "city_longitude": "7.58",
            "scheme_color": "1"
        },
        {
            "id": "548",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/ivrea",
            "introtext": "There is also an access regulation in place called <a title=\"Ivrea - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/Ivrea-ar\">Ivrea - AR</a>.",
            "cityname": "Ivrea",
            "city_latitude": "45.47",
            "city_longitude": "7.88",
            "scheme_color": "1"
        },
        {
            "id": "550",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/moncalieri",
            "introtext": "Moncalieri has a low emission zone in place, also called ZTL in Italian. \r\n<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Moncalieri",
            "city_latitude": "45.0",
            "city_longitude": "7.68",
            "scheme_color": "1"
        },
        {
            "id": "552",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/nichelino",
            "introtext": "Nichelino has a low emission zone in place, also called ZTL in Italian. \r\n<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Nichelino",
            "city_latitude": "45.0",
            "city_longitude": "7.65",
            "scheme_color": "1"
        },
        {
            "id": "554",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/orbassano",
            "introtext": "Orbassano has a low emission zone in place, also called ZTL in Italian. ",
            "cityname": "Orbassano",
            "city_latitude": "45.0",
            "city_longitude": "7.53",
            "scheme_color": "1"
        },
        {
            "id": "556",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pinerolo",
            "introtext": "There is also an access regulation in place called <a title=\"Pinerolo - AR\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pinerolo-ar\">Pinerolo - AR</a><br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Pinerolo",
            "city_latitude": "44.88",
            "city_longitude": "7.35",
            "scheme_color": "1"
        },
        {
            "id": "558",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/rivoli",
            "introtext": "Rivoli has a low emission zone in place, also called ZTL in Italian. <br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Rivoli",
            "city_latitude": "45.05",
            "city_longitude": "7.52",
            "scheme_color": "1"
        },
        {
            "id": "560",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/san-mauro-torinese",
            "introtext": "San Mauro Torinese has a low emission zone in place, also called ZTL in Italian. ",
            "cityname": "San Mauro Torinese",
            "city_latitude": "45.1",
            "city_longitude": "7.77",
            "scheme_color": "1"
        },
        {
            "id": "562",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/settimo-torinese",
            "introtext": "Settimo Torinese has a low emission zone in place, also called ZTL in Italian. <br><br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Settimo Torinese",
            "city_latitude": "45.13",
            "city_longitude": "7.77",
            "scheme_color": "1"
        },
        {
            "id": "564",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/torino",
            "introtext": "There is also an access regulation in place called <a title=\"Torino - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/torino-ar\">Torino - AR</a> and a possible <b>emergency scheme</b> (see below) in high air pollution events. <br>\r\nThe first Sunday of the month is 'ecological Sunday'. <br> <p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Torino",
            "city_latitude": "45.08",
            "city_longitude": "7.66",
            "scheme_color": "1"
        },
        {
            "id": "566",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/venaria-reale",
            "introtext": "Venaria Reale has a low emission zone in place, also called ZTL in Italian. <p>\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Venaria Reale",
            "city_latitude": "45.12",
            "city_longitude": "7.63",
            "scheme_color": "1"
        },
        {
            "id": "568",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vercelli",
            "introtext": "There is also an access regulation in place called <a title=\"Vercelli - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vercelli-ar\">Vercelli - AR</a>.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Vercelli",
            "city_latitude": "45.32",
            "city_longitude": "8.42",
            "scheme_color": "1"
        },
        {
            "id": "754",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/rijswijk",
            "introtext": "Rijswijk, east of Den Haag will implement a Low Emission Zone on 1st November 2010.",
            "cityname": "Rijswijk",
            "city_latitude": "52.03",
            "city_longitude": "4.32",
            "scheme_color": "1"
        },
        {
            "id": "572",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/trento",
            "introtext": "There is also an <a title=\"Access Regulation\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/trento-access-regulation\">Access Regulation</a> in Trento.",
            "cityname": "Trento",
            "city_latitude": "46.07",
            "city_longitude": "11.13",
            "scheme_color": "1"
        },
        {
            "id": "600",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/rome",
            "introtext": "<p>\r\n\tThere are <strong>3&nbsp;Low Emission Zones</strong>&nbsp;in Rome:</p>\r\n\r\n<p>\r\n\t1)&nbsp;<em><strong>Green zone</strong></em></p>\r\n\r\n<p>\r\n\t2)&nbsp;<em><strong>Railway ring</strong></em></p>\r\n\r\n<p>\r\n\t3)&nbsp;<em><strong>City centre</strong>&nbsp;</em>with delivery regulations covering a slightly larger area than the main centre of Rome</p>\r\n\r\n<p>\r\n\tThere are also <strong>access regulations </strong>in place, see&nbsp;<a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/rome-ar-2\" title=\"Rome - AR\">Rome - AR</a>&nbsp;and&nbsp;<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/rome-coaches-2\" title=\"Roma - Coaches\">Roma - Coaches</a>.<br />\r\n\tThere is also the possibility of&nbsp;<strong>emergency measures</strong>&nbsp;on days with extreme pollution, particularly in the winter. Options include banning alternating number plates, or a ban all vehicles. Notification is by the local press.</p>\r\n\r\n<p>\r\n\t<strong>Ecological Sundays</strong>: the mayor has banned vehicles from driving through the Italian capital on Sundays in a bid to tackle severe smog. Police have been advised to fine anyone who flouts the tough traffic restrictions.</p>\r\n\r\n<p>\r\n\tOn&nbsp;<strong>ecological Sundays</strong> all vehicles are banned from 07:30 &ndash; 12:30 und 16:30 &ndash; 20:30.</p>\r\n\r\n<p>\r\n\tAnd in the entire capital of Rome vehicles including motorcycles and motorbikes without an annual inspection are not allowed to circulate.</p>\r\n\r\n<p>\r\n\t&nbsp;</p>\r\n",
            "cityname": "Roma (Rome)",
            "city_latitude": "41.90",
            "city_longitude": "12.50",
            "scheme_color": "1"
        },
        {
            "id": "70",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/norwich",
            "introtext": "There is a low emission zone in place in Norwich.",
            "cityname": "Norwich",
            "city_latitude": "52.63",
            "city_longitude": "1.3",
            "scheme_color": "1"
        },
        {
            "id": "72",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/oxford",
            "introtext": "There is a low emission zone in Oxford.",
            "cityname": "Oxford",
            "city_latitude": "51.75",
            "city_longitude": "-1.25",
            "scheme_color": "1"
        },
        {
            "id": "323",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/moelndal",
            "introtext": "Low Emission Zone in operations since 1st July 2010",
            "cityname": "Mölndal",
            "city_latitude": "57.66",
            "city_longitude": "12.01",
            "scheme_color": "1"
        },
        {
            "id": "702",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/viareggio",
            "introtext": "Viareggio has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Viareggio ",
            "city_latitude": "43.87",
            "city_longitude": "10.23",
            "scheme_color": "1"
        },
        {
            "id": "704",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence",
            "introtext": "There is also an access regulation called <a title=\"Firenze - AR\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence-ar\">Firenze - AR</a>",
            "cityname": "Firenze (Florence)",
            "city_latitude": "43.78",
            "city_longitude": "11.25",
            "scheme_color": "1"
        },
        {
            "id": "757",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/scandicci",
            "introtext": "Scandicci has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Scandicci ",
            "city_latitude": "43.75",
            "city_longitude": "11.19",
            "scheme_color": "1"
        },
        {
            "id": "712",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/sesto-fiorentino",
            "introtext": "There is also an access regulation in place called <a title=\"Sesto Fiorentino - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/sesto-fiorentino-ar\">Sesto Fiorentino - AR</a>.",
            "cityname": "Sesto Fiorentino",
            "city_latitude": "43.83",
            "city_longitude": "11.20",
            "scheme_color": "1"
        },
        {
            "id": "714",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/prato",
            "introtext": "<p>\r\n\tPrato has a low emission zone in place. There is also an access regulation in Prato, see <a href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/prato-ar\">Prato - AR</a>.</p>\r\n",
            "cityname": "Prato",
            "city_latitude": "43.88",
            "city_longitude": "11.10",
            "scheme_color": "1"
        },
        {
            "id": "718",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/pisa",
            "introtext": "There is also an access regulation in place called <a title=\"Pisa - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/pisa-ar\">Pisa - AR</a>.",
            "cityname": "Pisa",
            "city_latitude": "43.72",
            "city_longitude": "10.40",
            "scheme_color": "1"
        },
        {
            "id": "720",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/lucca",
            "introtext": "There is also an access regulation in place called <a title=\"Lucca - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/lucca-ar\">Lucca - AR</a>.",
            "cityname": "Lucca",
            "city_latitude": "43.84",
            "city_longitude": "10.50",
            "scheme_color": "1"
        },
        {
            "id": "722",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/calenzano",
            "introtext": "Calenzano has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Calenzano",
            "city_latitude": "43.87",
            "city_longitude": "11.17",
            "scheme_color": "1"
        },
        {
            "id": "724",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/campi-bisenzio",
            "introtext": "Campi Bisenzio has a low emission zone in place, also called ZTL in Italian.<br>There is also an emergency ZTL in place in Campi Bisenzio.",
            "cityname": "Campi Bisenzio",
            "city_latitude": "43.82",
            "city_longitude": "11.13",
            "scheme_color": "1"
        },
        {
            "id": "726",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/empoli",
            "introtext": "There is also an access regulation in place, see <a title=\"Empoli - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/empoli-ar\">Empoli - AR</a>.",
            "cityname": "Empoli",
            "city_latitude": "43.72",
            "city_longitude": "10.95",
            "scheme_color": "1"
        },
        {
            "id": "610",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/napoli",
            "introtext": "There is also an access regulation in place called <a title=\"Napoli - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/campania-region/napoli-ar\">Napoli - AR</a>.\n",
            "cityname": "Napoli",
            "city_latitude": "40.83",
            "city_longitude": "14.25",
            "scheme_color": "1"
        },
        {
            "id": "772",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar",
            "introtext": "Freiberg am Neckar is now part of the regional LEZ called <strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/möglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a>, Hemmingen and Region\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).\r\n",
            "cityname": "Freiberg am Neckar",
            "city_latitude": "48.93",
            "city_longitude": "9.20",
            "scheme_color": "1"
        },
        {
            "id": "750",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/krefeld-nrw",
            "introtext": "",
            "cityname": "Krefeld",
            "city_latitude": "51.33",
            "city_longitude": "6.57",
            "scheme_color": "1"
        },
        {
            "id": "745",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/aosta-valle-d/mont-blanc-tunnel",
            "introtext": "",
            "cityname": "Mont Blanc tunnel",
            "city_latitude": "45.82",
            "city_longitude": "6.95",
            "scheme_color": "1"
        },
        {
            "id": "2411",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/castellon",
            "introtext": "Castellon has implemented a ZBE >b> 1 January 2025</b>.",
            "cityname": "Castellon",
            "city_latitude": "39.97",
            "city_longitude": "-0.05",
            "scheme_color": "1"
        },
        {
            "id": "747",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/verona",
            "introtext": "Verona has a low emission zone in place. This zone covers the entire municipality of Verona. It keeps certain vehicles not meeting the required Euro standard from entering the municipality at certain times.<br><br>\r\nThere is also an access regulation in place called <a title=\"Verona - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/veneto/verona-ar\">Verona - AR</a>.<br/><br>\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Verona",
            "city_latitude": "45.44",
            "city_longitude": "10.99",
            "scheme_color": "1"
        },
        {
            "id": "792",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/steiermark",
            "introtext": "<p>\r\n\tThe Low Emission Zone in Steiermark covers a large part of the Steiermark area.<br />\r\n\tSome of the larger towns included are: Bruck an der Mur, Deutschlandsberg, Feldbach, F&uuml;rstenfeld, Graz, Hartberg, Leibnitz, Leoben, Murtal, M&uuml;rzzuschlag, Radkersburg, Voitsberg and Weiz, but many more areas around are also included.</p>\r\n\r\n<p>\r\n\tA map and a full list of towns is given on the right.</p>\r\n\r\n<p>\r\n\t<br />\r\n\tBased on the IG-L &ndash; Austrian Emission Class Ordinance every driver can label his vehicle with an exhaust class sticker. The sticker provides information about the exhaust gas class according to the pollutant emissions of a motor vehicle.<br />\r\n\tAn official Austrian sticker must be purchased and put on the windshield of the vehicle. For more information about those stickers see <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78\" target=\"_blank\" title=\"Information Austrian stickers\">here</a>.</p>\r\n",
            "cityname": "Steiermark",
            "city_latitude": "47.25",
            "city_longitude": "15.17",
            "scheme_color": "1"
        },
        {
            "id": "749",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/carrara",
            "introtext": "There is also an access regulation in place called <a title=\"Carrara - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/carrara-ar\">Carrara - AR</a>.",
            "cityname": "Carrara",
            "city_latitude": "44.08",
            "city_longitude": "10.1",
            "scheme_color": "1"
        },
        {
            "id": "752",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/magdeburg",
            "introtext": "Magdeburg has a Low Emission Zone in place since 1st September 2011.",
            "cityname": "Magdeburg",
            "city_latitude": "52.13",
            "city_longitude": "11.62",
            "scheme_color": "1"
        },
        {
            "id": "760",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/dinslaken",
            "introtext": "",
            "cityname": "Dinslaken",
            "city_latitude": "51.57",
            "city_longitude": "6.73",
            "scheme_color": "1"
        },
        {
            "id": "766",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/castrop-rauxel",
            "introtext": "",
            "cityname": "Castrop-Rauxel",
            "city_latitude": "51.56",
            "city_longitude": "7.31",
            "scheme_color": "1"
        },
        {
            "id": "758",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/comune-di-signa",
            "introtext": "Comune di Signa has an emergency smog scheme in place.",
            "cityname": "Comune di Signa",
            "city_latitude": "45.81",
            "city_longitude": "9.05",
            "scheme_color": "1"
        },
        {
            "id": "763",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/hagen",
            "introtext": "",
            "cityname": "Hagen",
            "city_latitude": "51.36",
            "city_longitude": "7.47",
            "scheme_color": "1"
        },
        {
            "id": "767",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/gladbeck",
            "introtext": "",
            "cityname": "Gladbeck",
            "city_latitude": "51.57",
            "city_longitude": "6.98",
            "scheme_color": "1"
        },
        {
            "id": "768",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/herne",
            "introtext": "",
            "cityname": "Herne",
            "city_latitude": "51.53",
            "city_longitude": "7.20",
            "scheme_color": "1"
        },
        {
            "id": "769",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/herten",
            "introtext": "",
            "cityname": "Herten",
            "city_latitude": "51.60",
            "city_longitude": "7.13",
            "scheme_color": "1"
        },
        {
            "id": "775",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/arnhem",
            "introtext": "Arnhem has started a Low Emission Zone for lorries >3.5t on the 1st July 2014.<br>\r\nFrom 1-1-2019 diesel passenger cars will be affected, too.",
            "cityname": "Arnhem",
            "city_latitude": "51.98",
            "city_longitude": "5.91",
            "scheme_color": "1"
        },
        {
            "id": "2424",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/tres-cantos",
            "introtext": "Tres Cantos has implemented a ZBE 1 January 2025.",
            "cityname": "Tres Cantos",
            "city_latitude": "40.60",
            "city_longitude": "-3.70",
            "scheme_color": "1"
        },
        {
            "id": "782",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/wiesbaden",
            "introtext": "Wiesbaden has a Low Emission Zone LEZ with <a title=\"Mainz\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/mainz\">Mainz</a>.",
            "cityname": "Wiesbaden",
            "city_latitude": "50.08",
            "city_longitude": "8.24",
            "scheme_color": "1"
        },
        {
            "id": "784",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/graz",
            "introtext": "Graz itself has no Low Emission Zone after the Austrian LEZ framework, however the Styria-based LEZ operates in Graz.",
            "cityname": "Graz",
            "city_latitude": "47.07",
            "city_longitude": "15.42",
            "scheme_color": "1"
        },
        {
            "id": "785",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/mainz",
            "introtext": "Mainz has a joint Low Emission Zone with <a title=\"Wiesbaden\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/wiesbaden\">Wiesbaden</a>.<br>There is a diesel ban expected for Mainz from 1 September 2019.",
            "cityname": "Mainz",
            "city_latitude": "50",
            "city_longitude": "8.27",
            "scheme_color": "1"
        },
        {
            "id": "787",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/remscheid",
            "introtext": "Remscheid has a Low Emission Zone in place.",
            "cityname": "Remscheid",
            "city_latitude": "51.18",
            "city_longitude": "7.19",
            "scheme_color": "1"
        },
        {
            "id": "788",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/galluzzo",
            "introtext": "Galluzzo is on the outskirts of Florence (Firenze), and so its LEZ is linked to that of Florence.",
            "cityname": "Galluzzo",
            "city_latitude": "43.78",
            "city_longitude": "11.25",
            "scheme_color": "1"
        },
        {
            "id": "789",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/genova",
            "introtext": "There is also an access regulation in place called <a title=\"Genova - AR\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/genova-ar\">Genova - AR</a>.",
            "cityname": "Genova",
            "city_latitude": "44.41",
            "city_longitude": "8.93",
            "scheme_color": "1"
        },
        {
            "id": "790",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/citta-di-arona",
            "introtext": "Citta di Arona has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Arona",
            "city_latitude": "43.47",
            "city_longitude": "12.23",
            "scheme_color": "1"
        },
        {
            "id": "793",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/uppsala",
            "introtext": "",
            "cityname": "Uppsala",
            "city_latitude": "59.85",
            "city_longitude": "17.63",
            "scheme_color": "1"
        },
        {
            "id": "796",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/tamm",
            "introtext": "Tamm is now part of the regional Low Emission Zone called\r\n<strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a>, Hemmingen and Region\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).\r\n",
            "cityname": "Tamm",
            "city_latitude": "48.92",
            "city_longitude": "9.12",
            "scheme_color": "1"
        },
        {
            "id": "797",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/kornwestheim",
            "introtext": "The three regional Low Emission Zones of Stuttgart, Ludwigsburg and Leonberg\r\nnow all join up, to make, in practice, a combined Low Emission Zone.<br><br> \r\n\r\nThe Ludwigsburg and area regional LEZ includes <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> and covers also <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim, Patonville & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen \">Bietigheim-Bissingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>.<br><br>\r\n\r\n\r\nThe regional LEZ for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a> includes the towns of Ditzingen, Gerlingen, Hemmingen,\r\nKorntal-Münchingen and Schwieberdingen<br><br>\r\n\r\n \r\n\r\nThe Stuttgart LEZ borders both the LEZs above. <br><br>\r\n\r\n \r\n\r\nDue to potential confusion, please note that there are LEZs in\r\nBaden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar \">Freiberg am Neckar</a> (note the U or E in the spelling, too).<br>\r\n",
            "cityname": "Kornwestheim",
            "city_latitude": "48.86",
            "city_longitude": "9.19",
            "scheme_color": "1"
        },
        {
            "id": "798",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/asperg",
            "introtext": "Asperg is now part of the regional LEZ called\r\n<strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg, Hemmingen and Region</a>\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).\r\n",
            "cityname": "Asperg",
            "city_latitude": "48.91",
            "city_longitude": "9.14",
            "scheme_color": "1"
        },
        {
            "id": "799",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/moeglingen",
            "introtext": "Möglingen is now part of the regional Low Emission Zone called\r\n<strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a>, Hemmingen and Region\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).\r\n",
            "cityname": "Möglingen",
            "city_latitude": "48.89",
            "city_longitude": "9.13",
            "scheme_color": "1"
        },
        {
            "id": "800",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen",
            "introtext": "\r\nBietigheim-Bissingen is now part of the regional LEZ called\r\n<strong>Ludwigsburg and area</strong>.<br>\r\n\r\nThe Low Emission Zone for <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ludwigsburg\">Ludwigsburg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/ingersheim\">Ingersheim</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> also covers <a href=\"/countries-mainmenu-147/germany-mainmenu-61/kornwestheim\">Kornwestheim & Remseck</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/asperg\">Asperg</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/moeglingen\">Möglingen</a>, <a href=\"/countries-mainmenu-147/germany-mainmenu-61/tamm\">Tamm</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/bietigheim-bissingen\">Bietigheim-Bissingen</a> since 1st January 2013.<br>\r\nThe towns of Ditzingen, Gerlingen, Hemmingen, Korntal-Münchingen and Schwieberdingen have been included in the new regional LEZ for \"<a href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Leonberg</a>, Hemmingen and Region\" since 2nd December 2013.<br>\r\nDue to potential confusion, please note that there are LEZs in Baden-Württemberg in both <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiburg\">Freiburg</a> and <a href=\"/countries-mainmenu-147/germany-mainmenu-61/freiberg-am-neckar\">Freiberg am Neckar</a> (note the U or E in the spelling too).\r\n",
            "cityname": "Bietigheim-Bissingen",
            "city_latitude": "48.94",
            "city_longitude": "9.12",
            "scheme_color": "1"
        },
        {
            "id": "801",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/antwerp",
            "introtext": "flem",
            "cityname": "Antwerpen (Antwerp)",
            "city_latitude": "51.22",
            "city_longitude": "4.40",
            "scheme_color": "1"
        },
        {
            "id": "2036",
            "citypath": "http://urbanaccessregulations.eu//countries-mainmenu-147/united-kingdom-mainmenu-205/portsmouth",
            "introtext": "",
            "cityname": "Portsmouth",
            "city_latitude": "50.80",
            "city_longitude": "-1.08",
            "scheme_color": "1"
        },
        {
            "id": "802",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/umea",
            "introtext": "Umeå has had a Low Emission Zone since the 1st April 2014 according to the Swedish LEZ framework.",
            "cityname": "Umea",
            "city_latitude": "63.8",
            "city_longitude": "20.2",
            "scheme_color": "1"
        },
        {
            "id": "803",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/langenfeld",
            "introtext": "",
            "cityname": "Langenfeld",
            "city_latitude": "51.11",
            "city_longitude": "6.95",
            "scheme_color": "1"
        },
        {
            "id": "804",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/monchengladbach",
            "introtext": "",
            "cityname": "Mönchengladbach",
            "city_latitude": "51.19",
            "city_longitude": "6.44",
            "scheme_color": "1"
        },
        {
            "id": "806",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/greece/athens",
            "introtext": "Athens has a low emission zone in place.",
            "cityname": "Athens",
            "city_latitude": "37.98",
            "city_longitude": "23.72",
            "scheme_color": "1"
        },
        {
            "id": "1390",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/aachen",
            "introtext": "",
            "cityname": "Aachen",
            "city_latitude": "50.78",
            "city_longitude": "6.08",
            "scheme_color": "1"
        },
        {
            "id": "1850",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/lugo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Lugo - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "11.90",
            "scheme_color": "1"
        },
        {
            "id": "830",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/denmark-mainmenu-221/kobenhavn-frederiksberg",
            "introtext": "The LEZ has been in place since 1st September 2008.",
            "cityname": "Copenhagen (København) & Frederiksberg",
            "city_latitude": "55.67",
            "city_longitude": "12.56",
            "scheme_color": "1"
        },
        {
            "id": "842",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/ferentino-lazio",
            "introtext": "Ferentino has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Ferentino",
            "city_latitude": "41.69",
            "city_longitude": "13.25",
            "scheme_color": "1"
        },
        {
            "id": "1681",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/76-europe/united-kingdom-low-emission-zones/1087-london-clean-bus-zones-2",
            "introtext": "",
            "cityname": "London Clean Bus Zones",
            "city_latitude": "51.51",
            "city_longitude": "-0.13",
            "scheme_color": "1"
        },
        {
            "id": "843",
            "citypath": "http://urbanaccessregulations.eu//countries-mainmenu-147/united-kingdom-mainmenu-205/nottingham",
            "introtext": "A CAZ low emission zone was considered for Nottingham, but it is not needed as Nottingham keeps the limits.<br><br> SQPS is short for Statutory Quality Partnership Scheme and is a legally binding partnership between Nottingham City Council and local bus operators. ",
            "cityname": "Nottingham",
            "city_latitude": "52.95",
            "city_longitude": "-1.15",
            "scheme_color": "1"
        },
        {
            "id": "2295",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/plaza-eliptica",
            "introtext": "<p>\r\n\tMadrid has various schemes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid\" title=\"low emission zone\">low emission parking scheme</a>&nbsp;that favours less polluting vehicles</li>\r\n\t<li>\r\n\t\ta <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">low emission traffic limited zone</a>&nbsp;vehicles have to be owned by residents or zero emission</li>\r\n\t<li>\r\n\t\tan <a href=\"/countries-mainmenu-147/spain/madrid-odd-and-even-numberplates\">emergency scheme</a>&nbsp;</li>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid-weight\" title=\"weight restriction\">weight regulation</a></li>\r\n</ul>\r\n\r\n<p>\r\n\t<strong>NEW! From&nbsp;30 November 2018&nbsp;<a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">Central Madrid</a>&nbsp;</strong>is in place. The&nbsp;existing APRs (&Aacute;reas de Prioridad Residencial &nbsp;= areas where residents have priority) be extended and united into one big APR that is called Madrid Central.</p>\r\n\r\n<p>\r\n\tIt will be of informative character for the first two months and will be fully enforced from <strong>February 2019 on</strong>. The APR Central Madrid will cover practically the entire downtown area of Madrid.&nbsp;</p>\r\n\r\n<p>\r\n\tThe standards in the Central Madrid low emission zone are gradually tightened until a zero emission zone is reached in 2025.</p>\r\n\r\n<p>\r\n\tThe Grand Via is planned to be car-free by summer 2019.<br />\r\n\tMadrid is one of 4 cities that have stated they wish to remove diesel vehicles from the city. As part of this, the city plans to increase the numbers of access restrictions for private cars.</p>\r\n",
            "cityname": "Madrid - Plaza Eliptica",
            "city_latitude": "40.42",
            "city_longitude": "-3.70",
            "scheme_color": "1"
        },
        {
            "id": "882",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/finland/helsinki",
            "introtext": "Currently there are two schemes in place in Helsinki:<br>\nan Environmental Zone for buses and garbage trucks (dustbin lorries) and an Access Restriction scheme called <a title=\"Helsinki - AR\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/finland/helsinki-ar\">Helsinki - AR</a> for lorries longer than 12 meters.",
            "cityname": "Helsinki",
            "city_latitude": "60.17",
            "city_longitude": "24.94",
            "scheme_color": "1"
        },
        {
            "id": "885",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/rotterdam-ar",
            "introtext": "From 01.10.2014 regulations apply for lorries with a diesel engine entering the Rotterdam industrial zone of <b>Maasvlakte 1 and 2</b>.<br>\r\nThere is also a lorry ban in Rotterdam on <b>`s-Gravendijkwal</b> for lorries > 3.5 tonnes.<br>\r\nRotterdam also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/netherlands-mainmenu-88/rotterdam\">Low Emission Zone</a> in place.",
            "cityname": "Rotterdam Dock - AR/LEZ",
            "city_latitude": "51.92",
            "city_longitude": "4.47",
            "scheme_color": "1"
        },
        {
            "id": "2335",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/wroclaw",
            "introtext": "<p>\r\n\tAccess regulations for vehicles >9 tonnes have been in place in Wroclaw since 1st January 2012.</p>There will be a low emission zone in Wroclaw from 2025.\r\n\r\n<p>\r\n\tThere has been a recent Polish Law that allows cities to implement &quot;<strong>clean transport areas</strong>&quot;. These are areas where only electric, hydrogen-powered, CNG and LNG vehicles would be allowed in. So far no city has decided to&nbsp;implement one. Check this page regularly for updates.\r\n",
            "cityname": "Wroclaw",
            "city_latitude": "51.1",
            "city_longitude": "17.03",
            "scheme_color": "1"
        },
        {
            "id": "923",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/siegen-lez",
            "introtext": "",
            "cityname": "Siegen",
            "city_latitude": "50.88",
            "city_longitude": "8.02",
            "scheme_color": "1"
        },
        {
            "id": "1153",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/oberoesterreich",
            "introtext": "Oberösterreich has a low emission zone for HGV in place.",
            "cityname": "Oberösterreich",
            "city_latitude": "48.41",
            "city_longitude": "15.61",
            "scheme_color": "1"
        },
        {
            "id": "1196",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/regensburg",
            "introtext": "Regensburg has implemented a Low Emission Zone 14 January 2018.",
            "cityname": "Regensburg",
            "city_latitude": "49.03",
            "city_longitude": "12.11",
            "scheme_color": "1"
        },
        {
            "id": "2308",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/warsawa-lez",
            "introtext": "",
            "cityname": "Warsawa",
            "city_latitude": "52.2",
            "city_longitude": "21.01",
            "scheme_color": "1"
        },
        {
            "id": "1510",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/a12-night-driving-ban",
            "introtext": "<b>On the A12</b> there are several schemes, please select the one you want information on, and then the details will show below",
            "cityname": "A12 Night driving ban ",
            "city_latitude": "47.26",
            "city_longitude": "11.45",
            "scheme_color": "1"
        },
        {
            "id": "2218",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/parma",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Parma",
            "city_latitude": "44.80",
            "city_longitude": "10.33",
            "scheme_color": "1"
        },
        {
            "id": "1199",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/darmstadt",
            "introtext": "",
            "cityname": "Darmstadt",
            "city_latitude": "50.08",
            "city_longitude": "8.24",
            "scheme_color": "1"
        },
        {
            "id": "1242",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/halle-saale",
            "introtext": "",
            "cityname": "Halle (Saale)",
            "city_latitude": "51.50",
            "city_longitude": "11.97",
            "scheme_color": "1"
        },
        {
            "id": "1219",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/granarolo-dell-emilia",
            "introtext": "There is a winter driving restriction/access regulation (ZTL) in Castenaso. Region: Emilia Romagna; province: Bologna.<p>\n\t<br />\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2018 - 31 March 2019.</p>\n",
            "cityname": "Granarolo dell Emilia",
            "city_latitude": "44.05",
            "city_longitude": "12.57",
            "scheme_color": "1"
        },
        {
            "id": "2018",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/bradford",
            "introtext": "Bradford Council’s Executive is meeting (18 February 2020) to consider ambitious plans to improve air quality and the health of people in the district - particularly the city centre, Shipley and Saltaire where pollution is highest.",
            "cityname": "Bradford",
            "city_latitude": "53.79",
            "city_longitude": "-1.75",
            "scheme_color": "1"
        },
        {
            "id": "2021",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/york",
            "introtext": "",
            "cityname": "York",
            "city_latitude": "53.95",
            "city_longitude": "-1.08",
            "scheme_color": "1"
        },
        {
            "id": "2020",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/newcastle",
            "introtext": "Newcastle proposed a Clean Air Zone. The feedback they received was used to help shape the final plans. These plans were agreed by Newcastle, Gateshead and North Tyneside councils and submitted to government in early 2020.<br>\r\n\r\nIn response to the global coronavirus pandemic, they are currently in discussion with government regarding timescales for the implementation of the plans. ",
            "cityname": "Newcastle",
            "city_latitude": "54.96",
            "city_longitude": "-1.60",
            "scheme_color": "1"
        },
        {
            "id": "1413",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/marburg",
            "introtext": "Marburg has a Low Emission Zone in place.",
            "cityname": "Marburg",
            "city_latitude": "50.80",
            "city_longitude": "8.77",
            "scheme_color": "1"
        },
        {
            "id": "1457",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/bruxelles-brussel-brussels",
            "introtext": "",
            "cityname": "Bruxelles - Brussel (Brussels)",
            "city_latitude": "50.85",
            "city_longitude": "4.35",
            "scheme_color": "1"
        },
        {
            "id": "1468",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/eschweiler",
            "introtext": "",
            "cityname": "Eschweiler",
            "city_latitude": "50.81",
            "city_longitude": "6.26",
            "scheme_color": "1"
        },
        {
            "id": "1476",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/barcelona",
            "introtext": "<p>\r\n\tBarcelona also has an <a href=\"/countries-mainmenu-147/spain/barcelona-access-regulation\" title=\"access regulation\">access regulation</a> in place.<br />\r\n\tFrom December 2017 Barcelona city has an <strong>emergency scheme</strong>&nbsp;in place that is only active during episodes of high pollution.</p>\r\n\r\n<p>\r\n\tAnd Greater Barcelona will have a permanent scheme from 1 December 2019 (see dates and details below).</p>\r\n\r\n<p>\r\n\tThen the circulation of the most polluting vehicles is progressively restricted in Barcelona city and Greater Barcelona.<br />\r\n\t&nbsp;</p>\r\n",
            "cityname": "Barcelona",
            "city_latitude": "41.39",
            "city_longitude": "2.16",
            "scheme_color": "1"
        },
        {
            "id": "2381",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/bilbao ",
            "introtext": "",
            "cityname": "Bilbao",
            "city_latitude": "43.26",
            "city_longitude": "-2.93",
            "scheme_color": "1"
        },
        {
            "id": "2280",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/montebelluna-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Montebelluna - Winter Low Emission Zone",
            "city_latitude": "45.77",
            "city_longitude": "12.04",
            "scheme_color": "1"
        },
        {
            "id": "2282",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/mira -winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mira - Winter Low Emission Zone",
            "city_latitude": "45.43",
            "city_longitude": "12.13",
            "scheme_color": "1"
        },
        {
            "id": "2283",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/altopascio",
            "introtext": "Altopascio has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Altopascio",
            "city_latitude": "43.81",
            "city_longitude": "10.67",
            "scheme_color": "1"
        },
        {
            "id": "2284",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/capannori",
            "introtext": "Capannori has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Capannori",
            "city_latitude": "43.84",
            "city_longitude": "10.56",
            "scheme_color": "1"
        },
        {
            "id": "2285",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/livorno",
            "introtext": "Livorno has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Livorno",
            "city_latitude": "43.32",
            "city_longitude": "10.31",
            "scheme_color": "1"
        },
        {
            "id": "1484",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/belgium/gent-ghent",
            "introtext": "flem",
            "cityname": "Gent (Ghent)",
            "city_latitude": "51.05",
            "city_longitude": "3.72",
            "scheme_color": "1"
        },
        {
            "id": "1494",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/friuli-venezia-giulia-region/pordenone",
            "introtext": "<p>\r\n\tPordenone has a low emission zone&nbsp;in place and an access regulation <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/friuli-venezia-giulia-region/pordenone-access-regulation\" target=\"_blank\" title=\"Pordenone - AR\">Pordenone - AR</a>.</p>\r\n",
            "cityname": "Pordenone",
            "city_latitude": "45.96",
            "city_longitude": "12.66",
            "scheme_color": "1"
        },
        {
            "id": "1513",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/glasgow",
            "introtext": "Glasgow has a low emission zone (LEZ) in place since 31 December 2018.<br>\r\nGlasgow's LEZ is being phased in and will in the beginning only apply to local service buses.",
            "cityname": "Glasgow",
            "city_latitude": "55.86",
            "city_longitude": "-4.25",
            "scheme_color": "1"
        },
        {
            "id": "1500",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/lille",
            "introtext": "france",
            "cityname": "Lille",
            "city_latitude": "50.63",
            "city_longitude": "3.06",
            "scheme_color": "1"
        },
        {
            "id": "1504",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/overath",
            "introtext": "Overath has a Low Emission Zone (LEZ) in place since 1 October 2017.",
            "cityname": "Overath",
            "city_latitude": "50.93",
            "city_longitude": "7.28",
            "scheme_color": "1"
        },
        {
            "id": "1515",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/edinburgh",
            "introtext": "The Scottish Government has committed to working with the Edinburgh Local Authority to establish a low emission zone in 2020.",
            "cityname": "Edinburgh",
            "city_latitude": "55.95",
            "city_longitude": "-3.19",
            "scheme_color": "1"
        },
        {
            "id": "1516",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/aberdeen",
            "introtext": "The Scottish Government has committed to working with the Aberdeen Local Authority to establish a low emission zone in 2020. The Scottish Government committed to the introduction of LEZs in Scotland’s four biggest cities (Aberdeen, Dundee, Edinburgh and Glasgow). ",
            "cityname": "Aberdeen",
            "city_latitude": "57.15",
            "city_longitude": "-2.09",
            "scheme_color": "1"
        },
        {
            "id": "1517",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/dundee",
            "introtext": "The Scottish Government has committed to working with the Dundee Local Authority to establish a low emission zone in 2020.<p>Check <a href=\"https://www.lowemissionzones.scot/get-ready/vehicle-registration-checker\" target=\"_blank\" rel=\"noopener noreferrer\">here </a>if your vehicle is affected.</p>",
            "cityname": "Dundee",
            "city_latitude": "56.46",
            "city_longitude": "-2.97",
            "scheme_color": "1"
        },
        {
            "id": "1523",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/bordeaux",
            "introtext": "france",
            "cityname": "Bordeaux",
            "city_latitude": "44.84",
            "city_longitude": "-0.58",
            "scheme_color": "1"
        },
        {
            "id": "1550",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/strasbourg-delivery",
            "introtext": "france",
            "cityname": "Strasbourg - Delivery",
            "city_latitude": "48.57",
            "city_longitude": "7.75",
            "scheme_color": "1"
        },
        {
            "id": "1693",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/strasbourg",
            "introtext": "france",
            "cityname": "Strasbourg",
            "city_latitude": "48.57",
            "city_longitude": "7.75",
            "scheme_color": "1"
        },
        {
            "id": "1554",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/birmingham",
            "introtext": "Birmingham has decided for a clean air zone (CAZ) as detailed below, and has currently submitted this to the national government for permission and funding. The final legal order to start implementation is expected in April 2019.<br>Birmingham plans to implement the Clean Air Zone (CAZ) by 1 January 2020.<p> </p>\r\n<p>The <a href=\"https://vehiclecheck.drive-clean-air-zone.service.gov.uk/vehicle_checkers/enter_details\" target=\"_blank\" rel=\"noopener noreferrer\">GOV.UK vehicle checker</a> service will tell you whether you will have to pay a daily charge to drive your vehicle in any clean air zone in England. </p>",
            "cityname": "Birmingham",
            "city_latitude": "52.48",
            "city_longitude": "-1.89",
            "scheme_color": "1"
        },
        {
            "id": "2022",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/lisbon",
            "introtext": "There is currently one Low Emission Zone in Portugal",
            "cityname": "Lisbon",
            "city_latitude": "38.72",
            "city_longitude": "-9.13",
            "scheme_color": "1"
        },
        {
            "id": "2222",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/israel/jerusalem",
            "introtext": "Jerusalem has a low emission zone in place.",
            "cityname": "Jerusalem",
            "city_latitude": "31.77",
            "city_longitude": "35.21",
            "scheme_color": "1"
        },
        {
            "id": "2223",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/israel/haifa",
            "introtext": "Haifa has a low emission zone in place.",
            "cityname": "Haifa",
            "city_latitude": "32.79",
            "city_longitude": "34.98",
            "scheme_color": "1"
        },
        {
            "id": "1572",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/clermont-ferrand",
            "introtext": "france",
            "cityname": "Clermont-Auvergne-Métropole",
            "city_latitude": "45.77",
            "city_longitude": "3.08",
            "scheme_color": "1"
        },
        {
            "id": "1573",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-lyon",
            "introtext": "france",
            "cityname": "Greater Lyon",
            "city_latitude": "45.74",
            "city_longitude": "4.84",
            "scheme_color": "1"
        },
        {
            "id": "1574",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/montpellier",
            "introtext": "france",
            "cityname": "Montpellier-Mediterranee-Metropole",
            "city_latitude": "43.61",
            "city_longitude": "3.87",
            "scheme_color": "1"
        },
        {
            "id": "1575",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-paris",
            "introtext": "france",
            "cityname": "Greater Paris",
            "city_latitude": "48.87",
            "city_longitude": "2.34",
            "scheme_color": "1"
        },
        {
            "id": "1579",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/milano-lez-area-b",
            "introtext": "<p>\r\n\tThere are several schemes in Milan:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\t<a href=\"/countries-mainmenu-147/italy-mainmenu-81/milano-lez-area-b\">Area B</a> is a Low Emission Zone operating from<strong>25 February 2019</strong>. It covers the entire city of Milan.</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milan-area-c-charging-scheme\" title=\"Milan C\">Milan C</a>&nbsp;is a combined Low Emission Zone and urban road charging scheme</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milano-ar\" title=\"Milan - AR\">Milan - AR</a>, an Access Regulation</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/como\" title=\"Milan province\">Milan province</a>, the Low Emission Zones of the four provinces of Milan, Como, Varese and Lecco merge to give a &#39;paw print&#39; shaped LEZ (see <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/milano\" title=\"Milan Province\">Milan Province</a>).</li>\r\n\t<li>\r\n\t\tshort term restrictions are possible, particularly in the winter <a href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/como\" title=\"See the Milan LEZ page\">See the Milan LEZ page</a>. To find out if scheme is operational go <a href=\"https://inlinea.cittametropolitana.mi.it/dati_ambientali/pm10/\" target=\"_blank\" title=\"Milan website about PM10 air pollution\">here</a>.</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milan-area-c-charging-scheme\" title=\"Milan C\">Milan C</a> now substitutes the <a class=\"new-window nturl\" href=\"/ecopass\" title=\"Milan ecopass\">Milan ecopass</a> that is no longer in operation.</li>\r\n</ul>\r\n\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a&nbsp;<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"><b>winter emergency scheme</b></a> in place from 1 October - 31 March.</p>\r\n\r\n<p>\r\n\t&nbsp;</p>\r\n",
            "cityname": "Milano Area B",
            "city_latitude": "45.47",
            "city_longitude": "9.19",
            "scheme_color": "1"
        },
        {
            "id": "1580",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/terni",
            "introtext": "Terni has a low emission zone in place, also called ZTL in Italian.",
            "cityname": "Terni - Emergency Scheme",
            "city_latitude": "42.56",
            "city_longitude": "12.64",
            "scheme_color": "1"
        },
        {
            "id": "2298",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/badalona",
            "introtext": "",
            "cityname": "Badalona",
            "city_latitude": "41.44",
            "city_longitude": "2.24",
            "scheme_color": "1"
        },
        {
            "id": "1678",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/bath",
            "introtext": "A class C clean air zone (CAZ) will see charges for all higher emission vehicles, except cars, driving in the centre of Bath from March 2021",
            "cityname": "Bath",
            "city_latitude": "51.37",
            "city_longitude": "-2.35",
            "scheme_color": "1"
        },
        {
            "id": "1698",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/bristol",
            "introtext": "",
            "cityname": "Bristol",
            "city_latitude": "51.45",
            "city_longitude": "-2.58",
            "scheme_color": "1"
        },
        {
            "id": "1849",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/imola-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Imola - Winter Low Emission Zone",
            "city_latitude": "44.35",
            "city_longitude": "11.72",
            "scheme_color": "1"
        },
        {
            "id": "1848",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/granarolo-dell-emilia-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Granarolo dell Emilia - Winter Low Emission Zone",
            "city_latitude": "44.05",
            "city_longitude": "12.57",
            "scheme_color": "1"
        },
        {
            "id": "1922",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/emilia-romagna-cities-with-winter-lez/bologna-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Bologna - Winter Low Emission Zone",
            "city_latitude": "44.49",
            "city_longitude": "11.32",
            "scheme_color": "1"
        },
        {
            "id": "2389",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/mollet-del-valles",
            "introtext": "Mollet del Valles has implemented a low emission zone (ZBE = zona de bajas emisiones)",
            "cityname": "Mollet del Valles",
            "city_latitude": "41.54",
            "city_longitude": "2.21",
            "scheme_color": "1"
        },
        {
            "id": "2331",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/torremolinos",
            "introtext": "Torremolinos has implemented a low emission zone (ZBE = zona de bajas emisiones) end of 2024.",
            "cityname": "Torremolinos",
            "city_latitude": "36.62",
            "city_longitude": "-4.49",
            "scheme_color": "1"
        },
        {
            "id": "2276",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/vitoria-gasteiz",
            "introtext": "",
            "cityname": "Vitoria Gasteiz",
            "city_latitude": "42.85",
            "city_longitude": "-2.67",
            "scheme_color": "1"
        },
        {
            "id": "2451",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-annemasse",
            "introtext": "france",
            "cityname": "Greater Annemasse",
            "city_latitude": "49.18",
            "city_longitude": "6.23",
            "scheme_color": "1"
        },
        {
            "id": "1834",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/argelato-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Argelato - Winter Low Emission Zone",
            "city_latitude": "44.39",
            "city_longitude": "11.21",
            "scheme_color": "1"
        },
        {
            "id": "1835",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/calderara-di-reno-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Calderara di Reno - Winter Low Emission Zone",
            "city_latitude": "44.34",
            "city_longitude": "11.16",
            "scheme_color": "1"
        },
        {
            "id": "1836",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/carpi-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Carpi - Winter Low Emission Zone",
            "city_latitude": "44.47",
            "city_longitude": "10.53",
            "scheme_color": "1"
        },
        {
            "id": "1837",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/casalecchio-di-reno-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Casalecchio di Reno - Winter Low Emission Zone",
            "city_latitude": "44.47",
            "city_longitude": "11.27",
            "scheme_color": "1"
        },
        {
            "id": "2305",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/bulgaria/sofia",
            "introtext": "Sofia has a low emission zone in place and a lorry ban.",
            "cityname": "Sofia",
            "city_latitude": "42.69",
            "city_longitude": "23.32",
            "scheme_color": "1"
        },
        {
            "id": "1838",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/castel-maggiore-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Castel Maggiore - Winter Low Emission Zone",
            "city_latitude": "44.57",
            "city_longitude": "11.36",
            "scheme_color": "1"
        },
        {
            "id": "1839",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/castelfranco-emilia-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Castelfranco Emilia - Winter Low Emission Zone",
            "city_latitude": "44.59",
            "city_longitude": "11.04",
            "scheme_color": "1"
        },
        {
            "id": "1840",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/castenaso-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Castenaso - Winter Low Emission Zone",
            "city_latitude": "44.51",
            "city_longitude": "11.46",
            "scheme_color": "1"
        },
        {
            "id": "1841",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/cento-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cento - Winter Low Emission Zone",
            "city_latitude": "44.73",
            "city_longitude": "11.28",
            "scheme_color": "1"
        },
        {
            "id": "1842",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/cesena-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cesena - Winter Low Emission Zone",
            "city_latitude": "44.13",
            "city_longitude": "12.23",
            "scheme_color": "1"
        },
        {
            "id": "1843",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/faenza-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Faenza - Winter Low Emission Zone",
            "city_latitude": "44.28",
            "city_longitude": "11.88",
            "scheme_color": "1"
        },
        {
            "id": "1844",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ferrara-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ferrara - Winter Low Emission Zone",
            "city_latitude": "44.50",
            "city_longitude": "11.37",
            "scheme_color": "1"
        },
        {
            "id": "1845",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/fiorano-modenese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Fiorano Modenese - Winter Low Emission Zone",
            "city_latitude": "44.53",
            "city_longitude": "10.82",
            "scheme_color": "1"
        },
        {
            "id": "1846",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/forli-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Forlì - Winter Low Emission Zone",
            "city_latitude": "44.23",
            "city_longitude": "12.05",
            "scheme_color": "1"
        },
        {
            "id": "1847",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/formigine-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Formigine - Winter Low Emission Zone",
            "city_latitude": "44.57",
            "city_longitude": "10.84",
            "scheme_color": "1"
        },
        {
            "id": "1851",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/maranello-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Maranello - Winter Low Emission Zone",
            "city_latitude": "44.52",
            "city_longitude": "10.86",
            "scheme_color": "1"
        },
        {
            "id": "1852",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/modena-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Modena - Winter Low Emission Zone",
            "city_latitude": "44.64",
            "city_longitude": "10.92",
            "scheme_color": "1"
        },
        {
            "id": "1853",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ozzano-dell-emilia-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ozzano dell Emilia - Winter Low Emission Zone",
            "city_latitude": "44.44",
            "city_longitude": "11.47",
            "scheme_color": "1"
        },
        {
            "id": "1854",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/parma-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Parma - Winter Low Emission Zone",
            "city_latitude": "44.80",
            "city_longitude": "10.33",
            "scheme_color": "1"
        },
        {
            "id": "1855",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/piacenza-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Piacenza - Winter Low Emission Zone",
            "city_latitude": "45.04",
            "city_longitude": "9.70",
            "scheme_color": "1"
        },
        {
            "id": "1856",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ravenna-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ravenna - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "12.20",
            "scheme_color": "1"
        },
        {
            "id": "1857",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/reggio-nell-emilia-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Reggio nell Emilia - Winter Low Emission Zone",
            "city_latitude": "44.70",
            "city_longitude": "10.63",
            "scheme_color": "1"
        },
        {
            "id": "1858",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/riccione-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Riccione - Winter Low Emission Zone",
            "city_latitude": "44.0",
            "city_longitude": "12.39",
            "scheme_color": "1"
        },
        {
            "id": "1859",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/rimini-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rimini - Winter Low Emission Zone",
            "city_latitude": "44.05",
            "city_longitude": "12.57",
            "scheme_color": "1"
        },
        {
            "id": "1860",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/rubiera-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rubiera - Winter Low Emission Zone",
            "city_latitude": "44.39",
            "city_longitude": "10.47",
            "scheme_color": "1"
        },
        {
            "id": "1861",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/san-lazzaro-di-savena-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Lazzaro di Savena - Winter Low Emission Zone",
            "city_latitude": "44.28",
            "city_longitude": "11.24",
            "scheme_color": "1"
        },
        {
            "id": "1862",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/sassuolo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Sassuolo - Winter Low Emission Zone",
            "city_latitude": "44.55",
            "city_longitude": "10.78",
            "scheme_color": "1"
        },
        {
            "id": "1863",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/zola-predosa-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Zola Predosa - Winter Low Emission Zone",
            "city_latitude": "44.29",
            "city_longitude": "11.13",
            "scheme_color": "1"
        },
        {
            "id": "1866",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alba-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Alba - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "1867",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/adria-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Adria - Winter Low Emission Zone",
            "city_latitude": "45.30",
            "city_longitude": "12.30",
            "scheme_color": "1"
        },
        {
            "id": "1868",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alessandria-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Alessandria - Winter Low Emission Zone",
            "city_latitude": "44.55",
            "city_longitude": "8.37",
            "scheme_color": "1"
        },
        {
            "id": "1869",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/asti-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Asti - Winter Low Emission Zone",
            "city_latitude": "44.90",
            "city_longitude": "8.21",
            "scheme_color": "1"
        },
        {
            "id": "1870",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/beinasco-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Beinasco - Winter Low Emission Zone",
            "city_latitude": "45.02",
            "city_longitude": "7.58",
            "scheme_color": "1"
        },
        {
            "id": "1871",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/biella-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Biella - Winter Low Emission Zone",
            "city_latitude": "45.57",
            "city_longitude": "8.05",
            "scheme_color": "1"
        },
        {
            "id": "1872",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgaro-torinese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Borgaro Torinese - Winter Low Emission Zone",
            "city_latitude": "45.15",
            "city_longitude": "7.65",
            "scheme_color": "1"
        },
        {
            "id": "1873",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/bra-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Bra - Winter Low Emission Zone",
            "city_latitude": "44.7",
            "city_longitude": "7.85",
            "scheme_color": "1"
        },
        {
            "id": "1874",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/carmagnola-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Carmagnola - Winter Low Emission Zone",
            "city_latitude": "44.84",
            "city_longitude": "7.72",
            "scheme_color": "1"
        },
        {
            "id": "1875",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/casale-monferrato-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Casale Monferrato - Winter Low Emission Zone",
            "city_latitude": "45.13",
            "city_longitude": "8.44",
            "scheme_color": "1"
        },
        {
            "id": "1876",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chieri-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Chieri - Winter Low Emission Zone",
            "city_latitude": "45.01",
            "city_longitude": "7.82",
            "scheme_color": "1"
        },
        {
            "id": "1877",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chivasso-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Chivasso - Winter Low Emission Zone",
            "city_latitude": "45.19",
            "city_longitude": "7.89",
            "scheme_color": "1"
        },
        {
            "id": "1878",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/collegno-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Collegno - Winter Low Emission Zone",
            "city_latitude": "45.08",
            "city_longitude": "7.58",
            "scheme_color": "1"
        },
        {
            "id": "1879",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/grugliasco-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Grugliasco - Winter Low Emission Zone",
            "city_latitude": "45.07",
            "city_longitude": "7.58",
            "scheme_color": "1"
        },
        {
            "id": "1880",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/ivrea-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ivrea - Winter Low Emission Zone",
            "city_latitude": "45.47",
            "city_longitude": "7.88",
            "scheme_color": "1"
        },
        {
            "id": "1881",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/leini-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Leini - Winter Low Emission Zone",
            "city_latitude": "45.11",
            "city_longitude": "7.43",
            "scheme_color": "1"
        },
        {
            "id": "1882",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/mappano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mappano - Winter Low Emission Zone",
            "city_latitude": "45.9",
            "city_longitude": "7.42",
            "scheme_color": "1"
        },
        {
            "id": "1883",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/moncalieri-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Moncalieri - Winter Low Emission Zone",
            "city_latitude": "45.0",
            "city_longitude": "7.68",
            "scheme_color": "1"
        },
        {
            "id": "1884",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/nichelino-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Nichelino - Winter Low Emission Zone",
            "city_latitude": "45.0",
            "city_longitude": "7.65",
            "scheme_color": "1"
        },
        {
            "id": "1885",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novara-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Novara - Winter Low Emission Zone",
            "city_latitude": "45.44",
            "city_longitude": "8.62",
            "scheme_color": "1"
        },
        {
            "id": "1886",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/orbassano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Orbassano - Winter Low Emission Zone",
            "city_latitude": "45.0",
            "city_longitude": "7.53",
            "scheme_color": "1"
        },
        {
            "id": "1887",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pianezza-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Pianezza - Winter Low Emission Zone",
            "city_latitude": "45.6",
            "city_longitude": "7.33",
            "scheme_color": "1"
        },
        {
            "id": "1888",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/rivalta-di-torino-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rivalta di Torino - Winter Low Emission Zone",
            "city_latitude": "45.2",
            "city_longitude": "7.32",
            "scheme_color": "1"
        },
        {
            "id": "2109",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/rennes",
            "introtext": "france",
            "cityname": "Rennes",
            "city_latitude": "48.11",
            "city_longitude": "-1.67",
            "scheme_color": "1"
        },
        {
            "id": "2013",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/aix-marseille-provence",
            "introtext": "france",
            "cityname": "Aix-Marseille-Provence",
            "city_latitude": "43.29",
            "city_longitude": "5.36",
            "scheme_color": "1"
        },
        {
            "id": "1890",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/san-mauro-torinese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Mauro Torinese - Winter Low Emission Zone",
            "city_latitude": "45.1",
            "city_longitude": "7.77",
            "scheme_color": "1"
        },
        {
            "id": "1891",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/settimo-torinese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Settimo Torinese - Winter Low Emission Zone",
            "city_latitude": "45.13",
            "city_longitude": "7.77",
            "scheme_color": "1"
        },
        {
            "id": "1892",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/torino-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Torino - Winter Low Emission Zone",
            "city_latitude": "45.08",
            "city_longitude": "7.66",
            "scheme_color": "1"
        },
        {
            "id": "1893",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/tortona-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Tortona - Winter Low Emission Zone",
            "city_latitude": "44.86",
            "city_longitude": "8.83",
            "scheme_color": "1"
        },
        {
            "id": "1894",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/trecate-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Trecate - Winter Low Emission Zone",
            "city_latitude": "45.26",
            "city_longitude": "8.44",
            "scheme_color": "1"
        },
        {
            "id": "1895",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/venaria-reale-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Venaria Reale - Winter Low Emission Zone",
            "city_latitude": "45.12",
            "city_longitude": "7.63",
            "scheme_color": "1"
        },
        {
            "id": "1896",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vercelli-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Vercelli - Winter Low Emission Zone",
            "city_latitude": "45.32",
            "city_longitude": "8.42",
            "scheme_color": "1"
        },
        {
            "id": "1897",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vinovo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Vinovo - Winter Low Emission Zone",
            "city_latitude": "44.57",
            "city_longitude": "7.38",
            "scheme_color": "1"
        },
        {
            "id": "1898",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/volpiano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Volpiano - Winter Low Emission Zone",
            "city_latitude": "45.12",
            "city_longitude": "7.47",
            "scheme_color": "1"
        },
        {
            "id": "1899",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/badia-polesine-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Badia Polesine - Winter Low Emission Zone",
            "city_latitude": "45.60",
            "city_longitude": "11.30",
            "scheme_color": "1"
        },
        {
            "id": "1900",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/bassano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Bassano del Grappa - Winter Low Emission Zone",
            "city_latitude": "45.77",
            "city_longitude": "11.73",
            "scheme_color": "1"
        },
        {
            "id": "1901",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/belluno-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Belluno - Winter Low Emission Zone",
            "city_latitude": "46.15",
            "city_longitude": "12.21",
            "scheme_color": "1"
        },
        {
            "id": "1902",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/castelfranco-veneto-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Castelfranco Veneto - Winter Low Emission Zone",
            "city_latitude": "45.40",
            "city_longitude": "11.56",
            "scheme_color": "1"
        },
        {
            "id": "1903",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/chioggia-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Chioggia - Winter Low Emission Zone",
            "city_latitude": "45.13",
            "city_longitude": "12.17",
            "scheme_color": "1"
        },
        {
            "id": "1904",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/cinto-euganeo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cinto Euganeo - Winter Low Emission Zone",
            "city_latitude": "45.17",
            "city_longitude": "11.40",
            "scheme_color": "1"
        },
        {
            "id": "1905",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/citadella-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Citadella - Winter Low Emission Zone",
            "city_latitude": "45.39",
            "city_longitude": "11.47",
            "scheme_color": "1"
        },
        {
            "id": "1906",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/conegliano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Conegliano - Winter Low Emission Zone",
            "city_latitude": "45.89",
            "city_longitude": "12.30",
            "scheme_color": "1"
        },
        {
            "id": "1907",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/este-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Este - Winter Low Emission Zone",
            "city_latitude": "45.22",
            "city_longitude": "11.66",
            "scheme_color": "1"
        },
        {
            "id": "1908",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/feltre-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Feltre - Winter Low Emission Zone",
            "city_latitude": "46.10",
            "city_longitude": "11.54",
            "scheme_color": "1"
        },
        {
            "id": "1909",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/legnago-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Legnago - Winter Low Emission Zone",
            "city_latitude": "45.12",
            "city_longitude": "11.18",
            "scheme_color": "1"
        },
        {
            "id": "1910",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/mansue-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mansue - Winter Low Emission Zone",
            "city_latitude": "45.49",
            "city_longitude": "12.32",
            "scheme_color": "1"
        },
        {
            "id": "1911",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/mirano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mirano - Winter Low Emission Zone",
            "city_latitude": "45.49",
            "city_longitude": "12.11",
            "scheme_color": "1"
        },
        {
            "id": "1912",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/monselice-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Monselice - Winter Low Emission Zone",
            "city_latitude": "45.23",
            "city_longitude": "11.75",
            "scheme_color": "1"
        },
        {
            "id": "1913",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/padova-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Padova - Winter Low Emission Zone",
            "city_latitude": "45.41",
            "city_longitude": "11.88",
            "scheme_color": "1"
        },
        {
            "id": "1914",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/piove-di-sacco-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Piove di Sacco - Winter Low Emission Zone",
            "city_latitude": "45.30",
            "city_longitude": "12.03",
            "scheme_color": "1"
        },
        {
            "id": "1915",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/rovigo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rovigo - Winter Low Emission Zone",
            "city_latitude": "45.07",
            "city_longitude": "11.79",
            "scheme_color": "1"
        },
        {
            "id": "1916",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/san-bonifacio-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Bonifacio - Winter Low Emission Zone",
            "city_latitude": "45.24",
            "city_longitude": "11.17",
            "scheme_color": "1"
        },
        {
            "id": "1917",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/san-dona-di-piave-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Dona di Piave - Winter Low Emission Zone",
            "city_latitude": "45.38",
            "city_longitude": "12.34",
            "scheme_color": "1"
        },
        {
            "id": "1918",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/schio-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Schio - Winter Low Emission Zone",
            "city_latitude": "45.43",
            "city_longitude": "11.21",
            "scheme_color": "1"
        },
        {
            "id": "1919",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/treviso-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Treviso - Winter Low Emission Zone",
            "city_latitude": "45.66",
            "city_longitude": "12.25",
            "scheme_color": "1"
        },
        {
            "id": "1920",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/verona-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Verona - Winter Low Emission Zone",
            "city_latitude": "45.44",
            "city_longitude": "10.99",
            "scheme_color": "1"
        },
        {
            "id": "1921",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/vicenza-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Vicenza - Winter Low Emission Zone",
            "city_latitude": "45.55",
            "city_longitude": "11.55",
            "scheme_color": "1"
        },
        {
            "id": "2336",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/granada",
            "introtext": "Granada will implement a ZBE 1 April  2025.",
            "cityname": "Granada",
            "city_latitude": "37.17",
            "city_longitude": "-3.59",
            "scheme_color": "1"
        },
        {
            "id": "2005",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cambiano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cambiano - Winter Low Emission Zone",
            "city_latitude": "44.97",
            "city_longitude": "7.76",
            "scheme_color": "1"
        },
        {
            "id": "2006",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/caselle-torinese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Caselle Torinese - Winter Low Emission Zone",
            "city_latitude": "45.18",
            "city_longitude": "7.65",
            "scheme_color": "1"
        },
        {
            "id": "2007",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/la-loggia-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "La Loggia - Winter Low Emission Zone",
            "city_latitude": "44.95",
            "city_longitude": "7.66",
            "scheme_color": "1"
        },
        {
            "id": "2008",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/rivoli-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rivoli - Winter Low Emission Zone",
            "city_latitude": "45.06",
            "city_longitude": "7.52",
            "scheme_color": "1"
        },
        {
            "id": "2009",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/santena-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Santena - Winter Low Emission Zone",
            "city_latitude": "44.95",
            "city_longitude": "7.77",
            "scheme_color": "1"
        },
        {
            "id": "2010",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/trofarello-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Trofarello - Winter Low Emission Zone",
            "city_latitude": "44.92",
            "city_longitude": "7.74",
            "scheme_color": "1"
        },
        {
            "id": "2014",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/toulouse",
            "introtext": "france",
            "cityname": "Toulouse",
            "city_latitude": "43.60",
            "city_longitude": "1.44",
            "scheme_color": "1"
        },
        {
            "id": "2017",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/belgium/wallonia-region",
            "introtext": "",
            "cityname": "Wallonia Region",
            "city_latitude": "50.46",
            "city_longitude": "4.86",
            "scheme_color": "1"
        },
        {
            "id": "2417",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/vigo",
            "introtext": "Vigo has a limited traffic zone in place and will implement a low emission zone.",
            "cityname": "Vigo",
            "city_latitude": "42.24",
            "city_longitude": "-8.72",
            "scheme_color": "1"
        },
        {
            "id": "2026",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/rouen",
            "introtext": "france",
            "cityname": "Rouen",
            "city_latitude": "49.44",
            "city_longitude": "1.10",
            "scheme_color": "1"
        },
        {
            "id": "2027",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/nice",
            "introtext": "france",
            "cityname": "Nice Cote d Azur Metropolis",
            "city_latitude": "43.71",
            "city_longitude": "7.26",
            "scheme_color": "1"
        },
        {
            "id": "2129",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-emissions-based-parking",
            "introtext": "<p>\r\n\tMadrid has various schemes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid\" title=\"low emission zone\">low emission parking scheme</a>&nbsp;that favours less polluting vehicles</li>\r\n\t<li>\r\n\t\ta <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">low emission traffic limited zone</a>&nbsp;vehicles have to be owned by residents or zero emission</li>\r\n\t<li>\r\n\t\tan <a href=\"/countries-mainmenu-147/spain/madrid-odd-and-even-numberplates\">emergency scheme</a>&nbsp;</li>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid-weight\" title=\"weight restriction\">weight regulation</a></li>\r\n</ul>\r\n\r\n<p>\r\n\t<strong>NEW! From&nbsp;30 November 2018&nbsp;<a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">Central Madrid</a>&nbsp;</strong>is in place. The&nbsp;existing APRs (&Aacute;reas de Prioridad Residencial &nbsp;= areas where residents have priority) be extended and united into one big APR that is called Madrid Central.</p>\r\n\r\n<p>\r\n\tIt will be of informative character for the first two months and will be fully enforced from <strong>February 2019 on</strong>. The APR Central Madrid will cover practically the entire downtown area of Madrid.&nbsp;</p>\r\n\r\n<p>\r\n\tThe standards in the Central Madrid low emission zone are gradually tightened until a zero emission zone is reached in 2025.</p>\r\n\r\n<p>\r\n\tThe Grand Via is planned to be car-free by summer 2019.<br />\r\n\tMadrid is one of 4 cities that have stated they wish to remove diesel vehicles from the city. As part of this, the city plans to increase the numbers of access restrictions for private cars.</p>\r\n",
            "cityname": "Madrid - emissions-based parking",
            "city_latitude": "40.42",
            "city_longitude": "-3.70",
            "scheme_color": "1"
        },
        {
            "id": "2043",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/reims",
            "introtext": "france",
            "cityname": "Reims",
            "city_latitude": "49.25",
            "city_longitude": "4.03",
            "scheme_color": "1"
        },
        {
            "id": "2110",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-saint-etienne",
            "introtext": "france",
            "cityname": "Greater Saint-Etienne",
            "city_latitude": "45.43",
            "city_longitude": "4.38",
            "scheme_color": "1"
        },
        {
            "id": "2137",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-lez",
            "introtext": "<p>\r\n\tMadrid has various schemes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid\" title=\"low emission zone\">low emission parking scheme</a>&nbsp;that favours less polluting vehicles</li>\r\n\t<li>\r\n\t\ta <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">low emission traffic limited zone</a>&nbsp;vehicles have to be owned by residents or zero emission</li>\r\n\t<li>\r\n\t\tan <a href=\"/countries-mainmenu-147/spain/madrid-odd-and-even-numberplates\">emergency scheme</a>&nbsp;</li>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid-weight\" title=\"weight restriction\">weight regulation</a></li>\r\n</ul>\r\n\r\n<p>\r\n\t<strong>NEW! From&nbsp;30 November 2018&nbsp;<a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">Central Madrid</a>&nbsp;</strong>is in place. The&nbsp;existing APRs (&Aacute;reas de Prioridad Residencial &nbsp;= areas where residents have priority) be extended and united into one big APR that is called Madrid Central.</p>\r\n\r\n<p>\r\n\tIt will be of informative character for the first two months and will be fully enforced from <strong>February 2019 on</strong>. The APR Central Madrid will cover practically the entire downtown area of Madrid.&nbsp;</p>\r\n\r\n<p>\r\n\tThe standards in the Central Madrid low emission zone are gradually tightened until a zero emission zone is reached in 2025.</p>\r\n\r\n<p>\r\n\tThe Grand Via is planned to be car-free by summer 2019.<br />\r\n\tMadrid is one of 4 cities that have stated they wish to remove diesel vehicles from the city. As part of this, the city plans to increase the numbers of access restrictions for private cars.</p>\r\n",
            "cityname": "Madrid",
            "city_latitude": "40.42",
            "city_longitude": "-3.70",
            "scheme_color": "1"
        },
        {
            "id": "2158",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/acqui-terme-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Acqui Terme - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2159",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alpignano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Alpignano - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2160",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/arona-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Arona - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2161",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/avigliana-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Avigliana - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2162",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/baldissero-torinese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Baldissero Torinese - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2163",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgo-san-dalmazzo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Borgo San Dalmazzo - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2164",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgomanero-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Borgomanero - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2166",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cameri-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cameri - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2140",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/sheffield",
            "introtext": "",
            "cityname": "Sheffield",
            "city_latitude": "53.38",
            "city_longitude": "-1.46",
            "scheme_color": "1"
        },
        {
            "id": "2167",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/candiolo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Candiolo - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2168",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/canelli-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Canelli - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2169",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/carignano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Carignano - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2170",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cirie-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cirie - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2171",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cossato-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cossato - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2172",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/druento-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Druento - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2173",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/fossano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Fossano - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2174",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/galliate-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Galliate - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2175",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/giaveno-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Giaveno - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2176",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/mondovi-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mondovi - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2177",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/nizza-monferrato-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Nizza Monferrato - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2178",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novi-ligure-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Novi Ligure - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2179",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/oleggio-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Oleggio - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2180",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/omegna-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Omegna - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2181",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/ovada- Winter Low Emission Zone-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ovada - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2182",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pecetto-torinese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Pecetto Torinese - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2183",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pinerolo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Pinerolo - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2184",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pino-torinese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Pino Torinese - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2185",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/piobesi-torinese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Piobesi Torinese - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2186",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/piossasco -winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Piossasco - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2187",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/poirino-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Poirino - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2189",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/rivarolo-canavese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rivarolo Canavese - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2197",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cuneo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cuneo - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2191",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/saluzzo-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Saluzzo - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2192",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/san-maurizio-canavese-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Maurizio Canavese - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2193",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/savigliano-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Savigliano - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2194",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/valdilana-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Valdilana - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2195",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/valenza-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Valenza - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2196",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/verbania-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Verbania - Winter Low Emission Zone",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "1"
        },
        {
            "id": "2198",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/haarlem",
            "introtext": "Haarlem has had a Low Emission Zone in place since the 1 January 2022.",
            "cityname": "Haarlem",
            "city_latitude": "51.59",
            "city_longitude": "4.77",
            "scheme_color": "1"
        },
        {
            "id": "2316",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/zaragoza",
            "introtext": "Zaragoza has implemented a provisional low emission zone January 2023.",
            "cityname": "Zaragoza",
            "city_latitude": "41.64",
            "city_longitude": "-0.88",
            "scheme_color": "1"
        },
        {
            "id": "2225",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/krakow-cracow",
            "introtext": "",
            "cityname": "Krakow",
            "city_latitude": "50.06",
            "city_longitude": "19.94",
            "scheme_color": "1"
        },
        {
            "id": "2226",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alpignano",
            "introtext": "Alpignano has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Alpignano",
            "city_latitude": "45.09",
            "city_longitude": "7.52",
            "scheme_color": "1"
        },
        {
            "id": "2227",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/baldissero-torinese",
            "introtext": "Baldissero Torinese has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Baldissero Torinese",
            "city_latitude": "45.06",
            "city_longitude": "7.81",
            "scheme_color": "1"
        },
        {
            "id": "2221",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/greece/thessaloniki",
            "introtext": "Thessaloniki has a low emission zone in place.",
            "cityname": "Thessaloniki",
            "city_latitude": "40.62",
            "city_longitude": "22.94",
            "scheme_color": "1"
        },
        {
            "id": "2228",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cambiano",
            "introtext": "Cambiano has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Cambiano",
            "city_latitude": "44.97",
            "city_longitude": "7.76",
            "scheme_color": "1"
        },
        {
            "id": "2229",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/candiolo",
            "introtext": "Candiolo has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Candiolo",
            "city_latitude": "44.95",
            "city_longitude": "7.60",
            "scheme_color": "1"
        },
        {
            "id": "2230",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/carignano",
            "introtext": "Carignano has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Carignano",
            "city_latitude": "45.90",
            "city_longitude": "7.66",
            "scheme_color": "1"
        },
        {
            "id": "2231",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/caselle-torinese",
            "introtext": "Caselle Torinese  has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Caselle Torinese",
            "city_latitude": "45.16",
            "city_longitude": "7.64",
            "scheme_color": "1"
        },
        {
            "id": "2232",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/druento",
            "introtext": "Druento has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Druento",
            "city_latitude": "46.13",
            "city_longitude": "8.42",
            "scheme_color": "1"
        },
        {
            "id": "2233",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/la-loggia",
            "introtext": "La Loggia has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "La Loggia",
            "city_latitude": "44.95",
            "city_longitude": "7.66",
            "scheme_color": "1"
        },
        {
            "id": "2234",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/leini",
            "introtext": "Leinì has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Leini",
            "city_latitude": "45.17",
            "city_longitude": "7.71",
            "scheme_color": "1"
        },
        {
            "id": "2235",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/mappano",
            "introtext": "Mappano has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Mappano",
            "city_latitude": "45.14",
            "city_longitude": "7.70",
            "scheme_color": "1"
        },
        {
            "id": "2236",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pecetto-torinese",
            "introtext": "Pecetto Torinese has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Pecetto Torinese",
            "city_latitude": "45.01",
            "city_longitude": "7.75",
            "scheme_color": "1"
        },
        {
            "id": "2237",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pianezza",
            "introtext": "Pianezza has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Pianezza",
            "city_latitude": "45.11",
            "city_longitude": "7.55",
            "scheme_color": "1"
        },
        {
            "id": "2238",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pino-torinese",
            "introtext": "Pino Torinese has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Pino Torinese",
            "city_latitude": "45.04",
            "city_longitude": "7.77",
            "scheme_color": "1"
        },
        {
            "id": "2239",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/piobesi-torinese",
            "introtext": "Piobesi Torinese has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Piobesi Torinese",
            "city_latitude": "46.13",
            "city_longitude": "8.42",
            "scheme_color": "1"
        },
        {
            "id": "2240",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/piossasco",
            "introtext": "Piossasco has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Piossasco",
            "city_latitude": "44.98",
            "city_longitude": "7.46",
            "scheme_color": "1"
        },
        {
            "id": "2241",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/rivalta-di-torino",
            "introtext": "Rivalta di Torino has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Rivalta di Torino",
            "city_latitude": "45.01",
            "city_longitude": "7.51",
            "scheme_color": "1"
        },
        {
            "id": "2242",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/santena",
            "introtext": "Santena has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Santena",
            "city_latitude": "44.95",
            "city_longitude": "7.77",
            "scheme_color": "1"
        },
        {
            "id": "2243",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/trofarello",
            "introtext": "Trofarello has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Trofarello",
            "city_latitude": "44.97",
            "city_longitude": "7.74",
            "scheme_color": "1"
        },
        {
            "id": "2244",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vinovo",
            "introtext": "Vinovo has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Vinovo",
            "city_latitude": "44.95",
            "city_longitude": "7.63",
            "scheme_color": "1"
        },
        {
            "id": "2245",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/volpiano",
            "introtext": "Volpiano has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Volpiano",
            "city_latitude": "45.20",
            "city_longitude": "7.77",
            "scheme_color": "1"
        },
        {
            "id": "2246",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/ovada",
            "introtext": "Ovada has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Ovada",
            "city_latitude": "44.63",
            "city_longitude": "8.63",
            "scheme_color": "1"
        },
        {
            "id": "2247",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/canelli",
            "introtext": "Canelli has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Canelli",
            "city_latitude": "44.72",
            "city_longitude": "8.28",
            "scheme_color": "1"
        },
        {
            "id": "2248",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/nizza-monferrato",
            "introtext": "Nizza Monferrato has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Nizza Monferrato",
            "city_latitude": "44.75",
            "city_longitude": "8.36",
            "scheme_color": "1"
        },
        {
            "id": "2250",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/valdilana",
            "introtext": "Valdilana has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Valdilana",
            "city_latitude": "45.66",
            "city_longitude": "8.12",
            "scheme_color": "1"
        },
        {
            "id": "2251",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgo-san-dalmazzo",
            "introtext": "Borgo San Dalmazzo has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Borgo San Dalmazzo",
            "city_latitude": "44.32",
            "city_longitude": "7.48",
            "scheme_color": "1"
        },
        {
            "id": "2252",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/busca",
            "introtext": "Busca has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Busca",
            "city_latitude": "44.32",
            "city_longitude": "7.48",
            "scheme_color": "1"
        },
        {
            "id": "2253",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/saluzzo",
            "introtext": "Saluzzo has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Saluzzo",
            "city_latitude": "44.64",
            "city_longitude": "7.49",
            "scheme_color": "1"
        },
        {
            "id": "2254",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cameri",
            "introtext": "Cameri has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Cameri",
            "city_latitude": "45.49",
            "city_longitude": "8.66",
            "scheme_color": "1"
        },
        {
            "id": "2255",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/galliate",
            "introtext": "Galliate has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Galliate",
            "city_latitude": "45.48",
            "city_longitude": "8.71",
            "scheme_color": "1"
        },
        {
            "id": "2256",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/oleggio",
            "introtext": "Oleggio has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Oleggio",
            "city_latitude": "45.59",
            "city_longitude": "8.63",
            "scheme_color": "1"
        },
        {
            "id": "2257",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/trecate",
            "introtext": "Trecate has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Trecate",
            "city_latitude": "45.43",
            "city_longitude": "8.73",
            "scheme_color": "1"
        },
        {
            "id": "2258",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/avigliana",
            "introtext": "Avigliana has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Avigliana",
            "city_latitude": "45.07",
            "city_longitude": "7.40",
            "scheme_color": "1"
        },
        {
            "id": "2259",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cirie",
            "introtext": "Cirie has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Cirie",
            "city_latitude": "45.23",
            "city_longitude": "7.60",
            "scheme_color": "1"
        },
        {
            "id": "2260",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/giaveno",
            "introtext": "Giaveno has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Giaveno",
            "city_latitude": "45.04",
            "city_longitude": "7.35",
            "scheme_color": "1"
        },
        {
            "id": "2261",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/poirino",
            "introtext": "Poirino has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Poirino",
            "city_latitude": "44.91",
            "city_longitude": "7.84",
            "scheme_color": "1"
        },
        {
            "id": "2262",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/rivarolo-canavese",
            "introtext": "Rivarolo Canavese has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Rivarolo Canavese",
            "city_latitude": "45.33",
            "city_longitude": "7.72",
            "scheme_color": "1"
        },
        {
            "id": "2263",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/san-maurizio-canavese",
            "introtext": "San Maurizio Canavese has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "San Maurizio Canavese",
            "city_latitude": "45.20",
            "city_longitude": "7.64",
            "scheme_color": "1"
        },
        {
            "id": "2264",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgosesia",
            "introtext": "Borgosesia has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Borgosesia",
            "city_latitude": "45.72",
            "city_longitude": "8.25",
            "scheme_color": "1"
        },
        {
            "id": "2265",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/omegna",
            "introtext": "Omegna has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Omegna",
            "city_latitude": "45.87",
            "city_longitude": "8.40",
            "scheme_color": "1"
        },
        {
            "id": "2266",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgosesia-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Borgosesia - Winter Low Emission Zone",
            "city_latitude": "45.72",
            "city_longitude": "8.25",
            "scheme_color": "1"
        },
        {
            "id": "2267",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/verbania",
            "introtext": "Verbania has a low emission zone in place, also called ZTL in Italian.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Verbania",
            "city_latitude": "45.92",
            "city_longitude": "8.55",
            "scheme_color": "1"
        },
        {
            "id": "2387",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/busca-winter-low-emission-zone",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Busca - Winter Low Emission Zone",
            "city_latitude": "44.3",
            "city_longitude": "7.28",
            "scheme_color": "1"
        },
        {
            "id": "2272",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/sant-joan-despi",
            "introtext": "Sant Joan Despi has implemented a ZBE, low emission  1 January 2022. zone ",
            "cityname": "Sant Joan Despi",
            "city_latitude": "41.36",
            "city_longitude": "2.06",
            "scheme_color": "1"
        },
        {
            "id": "2297",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/sevilla",
            "introtext": "Sevilla has a low emission zone in the city centre. \n",
            "cityname": "Sevilla",
            "city_latitude": "37.38",
            "city_longitude": "-5.98",
            "scheme_color": "1"
        },
        {
            "id": "2321",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/roma-rome-winter-low-emission-zone",
            "introtext": "Rome has winter low emission zone in place.",
            "cityname": "Roma (Rome) - Winter Low Emission Zone",
            "city_latitude": "41.90",
            "city_longitude": "12.50",
            "scheme_color": "1"
        },
        {
            "id": "2351",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/valladolid",
            "introtext": "Valladolid has implemented a low emission zone (ZBE = zona de bajas emisiones) in 1 January 2025.",
            "cityname": "Valladolid",
            "city_latitude": "41.65",
            "city_longitude": "-4.72",
            "scheme_color": "1"
        },
        {
            "id": "2368",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/estepona",
            "introtext": "Estepona has implemented a ZBE in 2023.",
            "cityname": "Estepona",
            "city_latitude": "36.42",
            "city_longitude": "-5.15",
            "scheme_color": "1"
        },
        {
            "id": "2355",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/san-sebastian",
            "introtext": "San Sebastian has implemented a ZBE end of 2024. ",
            "cityname": "San Sebastian",
            "city_latitude": "43.32",
            "city_longitude": "-1.98",
            "scheme_color": "1"
        },
        {
            "id": "2356",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/avila",
            "introtext": "Avila has implemented a ZBE 1 January 2025.",
            "cityname": "Avila",
            "city_latitude": "40.65",
            "city_longitude": "-4.69",
            "scheme_color": "1"
        },
        {
            "id": "2358",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/sabadell",
            "introtext": "Sabadell has implemented a low emission zone (ZBE = zona de bajas emisiones) 1 January 2025.",
            "cityname": "Sabadell",
            "city_latitude": "41.54",
            "city_longitude": "2.10",
            "scheme_color": "1"
        },
        {
            "id": "2359",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/terrassa",
            "introtext": "Terrassa has implemented a low emission zone (ZBE = zona de bajas emisiones)",
            "cityname": "Terrassa",
            "city_latitude": "41.56",
            "city_longitude": "2.01",
            "scheme_color": "1"
        },
        {
            "id": "2361",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/almeria",
            "introtext": "Almeria has implemented a ZBE 1 January 2024.",
            "cityname": "Almeria",
            "city_latitude": "36.83",
            "city_longitude": "-2.45",
            "scheme_color": "1"
        },
        {
            "id": "2423",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/elche",
            "introtext": "Elche has implemented a ZBE >b> 1 January 2025</b>.",
            "cityname": "Elche",
            "city_latitude": "39.97",
            "city_longitude": "-0.05",
            "scheme_color": "1"
        },
        {
            "id": "2363",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/malaga",
            "introtext": "Malaga has implemented a ZBE end of 2024.",
            "cityname": "Malaga",
            "city_latitude": "36.72",
            "city_longitude": "-4.42",
            "scheme_color": "1"
        },
        {
            "id": "2362",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/guadalajara",
            "introtext": "Guadalajara has implemented a ZBE in March 2024. ",
            "cityname": "Guadalajara",
            "city_latitude": "40.63",
            "city_longitude": "-3.16",
            "scheme_color": "1"
        },
        {
            "id": "2365",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/cornella-de-llobregat",
            "introtext": "Cornella de Llobregat has implemented a ZBE 1 January 2020.",
            "cityname": "Cornella de Llobregat",
            "city_latitude": "41.46",
            "city_longitude": "2.07",
            "scheme_color": "1"
        },
        {
            "id": "2366",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/espluges-de-llobregat",
            "introtext": "Espluges de Llobregat has implemented a ZBE in 1 May 2021.",
            "cityname": "Espluges de Llobregat",
            "city_latitude": "41.37",
            "city_longitude": "2.08",
            "scheme_color": "1"
        },
        {
            "id": "2367",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/sant-adria-de-besos",
            "introtext": "Sant Adria de Besos has implemented a low emission zone 7 November 2019.",
            "cityname": "Sant Adria de Besos",
            "city_latitude": "41.43",
            "city_longitude": "2.21",
            "scheme_color": "1"
        },
        {
            "id": "2370",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/torrejon-de-ardoz",
            "introtext": "Torrejon de Ardoz has implemented a ZBE 1 January 2023.",
            "cityname": "Torrejon de Ardoz",
            "city_latitude": "40.45",
            "city_longitude": "-3.47",
            "scheme_color": "1"
        },
        {
            "id": "2371",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/fuenlabrada",
            "introtext": "Fuenlabrada has implemented a low emission zone in 15 July 2024.",
            "cityname": "Fuenlabrada",
            "city_latitude": "40.29",
            "city_longitude": "-3.80",
            "scheme_color": "1"
        },
        {
            "id": "2452",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-annecy",
            "introtext": "france",
            "cityname": "Greater Annecy",
            "city_latitude": "45.91",
            "city_longitude": "6.11",
            "scheme_color": "1"
        },
        {
            "id": "2382",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/burgos",
            "introtext": "Burgos has implemented a ZBE 31 December 2024. ",
            "cityname": "Burgos",
            "city_latitude": "42.35",
            "city_longitude": "-3.68",
            "scheme_color": "1"
        },
        {
            "id": "2383",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/dos-hermanas",
            "introtext": "Dos Hermanas has implemented a ZBE 1 January 2025.",
            "cityname": "Dos Hermanas",
            "city_latitude": "37.28",
            "city_longitude": "-5.92",
            "scheme_color": "1"
        },
        {
            "id": "2418",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/el-ejido",
            "introtext": "El Ejido has implemented a ZBE 1 January 2025.",
            "cityname": "El Ejido",
            "city_latitude": "41.32",
            "city_longitude": "2.09",
            "scheme_color": "1"
        },
        {
            "id": "2388",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/paris-emissions-based-parking",
            "introtext": "",
            "cityname": "Paris - emissions-based parking",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "1"
        },
        {
            "id": "2391",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/marbella",
            "introtext": "Marbella has implemented a ZBE beginning of 2024.",
            "cityname": "Marbella",
            "city_latitude": "36.51",
            "city_longitude": "-4.88",
            "scheme_color": "1"
        },
        {
            "id": "2392",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/viladecans",
            "introtext": "Viladecans has implemented a ZBE 1 July 2024.",
            "cityname": "Viladecans",
            "city_latitude": "41.44",
            "city_longitude": "2.24",
            "scheme_color": "1"
        },
        {
            "id": "2431",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/molina-de-segura",
            "introtext": "Molina de Segura has implemented a ZBE 23 December 2024.",
            "cityname": "Molina de Segura",
            "city_latitude": "38.05",
            "city_longitude": "-1.21",
            "scheme_color": "1"
        },
        {
            "id": "2393",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/sant-boi-de-llobregat",
            "introtext": "Sant Boi de Llobregat has implemented a ZBE 1 July 2024.",
            "cityname": "Sant Boi de Llobregat",
            "city_latitude": "41.34",
            "city_longitude": "2.03",
            "scheme_color": "1"
        },
        {
            "id": "2394",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/el-prat-de-llobregat",
            "introtext": "El Prat de Llobregat has implemented a ZBE 1 July 2024.",
            "cityname": "El Prat de Llobregat",
            "city_latitude": "41.32",
            "city_longitude": "2.09",
            "scheme_color": "1"
        },
        {
            "id": "2395",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/gava",
            "introtext": "Gava has implemented a ZBE 1 July 2024.",
            "cityname": "Gava",
            "city_latitude": "41.30",
            "city_longitude": "2.00",
            "scheme_color": "1"
        },
        {
            "id": "2410",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/majadahonda",
            "introtext": "Majadahonda has implemented a low emission zone in 1 January 2025.",
            "cityname": "Majadahonda",
            "city_latitude": "40.47",
            "city_longitude": "-3.86",
            "scheme_color": "1"
        },
        {
            "id": "2397",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/cerdanyola-del-valles",
            "introtext": "Cerdanyola del Valles has implemented a ZBE 1 July 2024.",
            "cityname": "Cerdanyola del Valles",
            "city_latitude": "41.49",
            "city_longitude": "2.13",
            "scheme_color": "1"
        },
        {
            "id": "2398",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/getafe",
            "introtext": "Getafe has implemented a ZBE 1 January 2024.",
            "cityname": "Getafe",
            "city_latitude": "40.30",
            "city_longitude": "-3.72",
            "scheme_color": "1"
        },
        {
            "id": "2399",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/salamanca",
            "introtext": "Salamanca has implemented a ZBE 1 June 2024.",
            "cityname": "Salamanca",
            "city_latitude": "40.96",
            "city_longitude": "-5.66",
            "scheme_color": "1"
        },
        {
            "id": "2400",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/segovia",
            "introtext": "Segovia has implemented a 1 January 2025.",
            "cityname": "Segovia",
            "city_latitude": "40.94",
            "city_longitude": "-4.10",
            "scheme_color": "1"
        },
        {
            "id": "2401",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/mostoles",
            "introtext": "Mostoles has implemented a ZBE 1 January 2025.",
            "cityname": "Mostoles",
            "city_latitude": "40.32",
            "city_longitude": "-3.86",
            "scheme_color": "1"
        },
        {
            "id": "2402",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/torrelavega",
            "introtext": "Torrelavega has implemented a ZBE 9 August 2024.",
            "cityname": "Torrelavega",
            "city_latitude": "43.35",
            "city_longitude": "-4.04",
            "scheme_color": "1"
        },
        {
            "id": "2415",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/siero",
            "introtext": "The city council of Siero has agreed to implement a low emission zone 29 August 2024.",
            "cityname": "Siero",
            "city_latitude": "43.39",
            "city_longitude": "-5.66",
            "scheme_color": "1"
        },
        {
            "id": "2404",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/boadilla-del-monte",
            "introtext": "Boadilla del Monte has implemented a ZBE 1 January 2025.",
            "cityname": "Boadilla del Monte",
            "city_latitude": "40.43",
            "city_longitude": "-3.89",
            "scheme_color": "1"
        },
        {
            "id": "2413",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/lyon-emissions-based-parking",
            "introtext": "france",
            "cityname": "Lyon - emissions-based parking",
            "city_latitude": "45.74",
            "city_longitude": "4.84",
            "scheme_color": "1"
        },
        {
            "id": "2416",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/valencia",
            "introtext": "Valencia has an emergency scheme that comes into place in cases of high pollution events, a limited traffic zone and a low emission zone in place.",
            "cityname": "Valencia",
            "city_latitude": "39.47",
            "city_longitude": "-0.38",
            "scheme_color": "1"
        },
        {
            "id": "2425",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/linares",
            "introtext": "Linares has implemented a ZBE 1 January 2025.",
            "cityname": "Linares",
            "city_latitude": "38.09",
            "city_longitude": "-3.63",
            "scheme_color": "1"
        },
        {
            "id": "2429",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/benidorm",
            "introtext": "Benidorm has implemented a low emission zone (ZBE = Zona de Bajas Emisiones) 1 January 2025.",
            "cityname": "Benidorm",
            "city_latitude": "38.54",
            "city_longitude": "-0.12",
            "scheme_color": "1"
        },
        {
            "id": "2422",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/palma-de-mallorca",
            "introtext": "",
            "cityname": "Palma de Mallorca",
            "city_latitude": "39.57",
            "city_longitude": "2.65",
            "scheme_color": "1"
        },
        {
            "id": "2426",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/lleida",
            "introtext": "Lleida has implemented a ZBE 1 January 2025.",
            "cityname": "Lleida",
            "city_latitude": "41.61",
            "city_longitude": "0.62",
            "scheme_color": "1"
        },
        {
            "id": "2447",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/alcala-de-guadaira ",
            "introtext": "",
            "cityname": "Alcala de Guadaira",
            "city_latitude": "37.33",
            "city_longitude": "-5.84",
            "scheme_color": "1"
        },
        {
            "id": "2445",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/alcobendas ",
            "introtext": "",
            "cityname": "Alcobendas",
            "city_latitude": "40.32",
            "city_longitude": "-3.38",
            "scheme_color": "1"
        },
        {
            "id": "2449",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/la-linea-de-la-concepcion",
            "introtext": "La Linea de la Concepcion will implement a ZBE in spring 2025.",
            "cityname": "La Linea de la Concepcion",
            "city_latitude": "36.16",
            "city_longitude": "-5.34",
            "scheme_color": "1"
        },
        {
            "id": "2450",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/caen",
            "introtext": "france",
            "cityname": "Caen",
            "city_latitude": "49.18",
            "city_longitude": "-0.37",
            "scheme_color": "1"
        },
        {
            "id": "2453",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/nantes",
            "introtext": "france",
            "cityname": "Nantes",
            "city_latitude": "47.21",
            "city_longitude": "-1.55",
            "scheme_color": "1"
        },
        {
            "id": "2454",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/le-havre",
            "introtext": "france",
            "cityname": "Le Havre",
            "city_latitude": "49.49",
            "city_longitude": "0.10",
            "scheme_color": "1"
        },
        {
            "id": "2455",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/dijon",
            "introtext": "france",
            "cityname": "Dijon",
            "city_latitude": "47.33",
            "city_longitude": "5.04",
            "scheme_color": "1"
        },
        {
            "id": "2456",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/chiclana-de-la-frontera",
            "introtext": "Chiclana de la Frontera will implement a ZBE in 2025.",
            "cityname": "Chiclana de la Frontera",
            "city_latitude": "36.41",
            "city_longitude": "-6.14",
            "scheme_color": "1"
        },
        {
            "id": "2098",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/ponferrada-emergency-scheme",
            "introtext": "",
            "cityname": "Ponferrada - Emergency Scheme",
            "city_latitude": "42.55",
            "city_longitude": "-6.59",
            "scheme_color": "4"
        },
        {
            "id": "1680",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/bruxelles-brussel-brussels",
            "introtext": "",
            "cityname": "Bruxelles - Brussel (Brussels) - Emergency Scheme",
            "city_latitude": "50.83",
            "city_longitude": "4.36",
            "scheme_color": "4"
        },
        {
            "id": "2324",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence-emergency-scheme",
            "introtext": "There is also an access regulation called <a title=\"Firenze - AR\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence-ar\">Firenze - AR</a>",
            "cityname": "Firenze (Florence) - Emergency Scheme",
            "city_latitude": "43.78",
            "city_longitude": "11.25",
            "scheme_color": "4"
        },
        {
            "id": "2325",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/santa-croce-sull-arno-emergency-scheme",
            "introtext": "There is an emergency scheme in Santa Croce sull'Arno that is activated when the air quality levels are exceeded.",
            "cityname": "Santa Croce sull Arno - Emergency Scheme",
            "city_latitude": "43.43",
            "city_longitude": "10.46",
            "scheme_color": "4"
        },
        {
            "id": "2042",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/rouen-emergency-scheme\n\n\n",
            "introtext": "france",
            "cityname": "Rouen - Emergency Scheme",
            "city_latitude": "49.43",
            "city_longitude": "1.10",
            "scheme_color": "4"
        },
        {
            "id": "1684",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/hungary/budapest-emergency-scheme",
            "introtext": "",
            "cityname": "Budapest - Emergency Scheme",
            "city_latitude": "47.50",
            "city_longitude": "19.04",
            "scheme_color": "4"
        },
        {
            "id": "1524",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/marseille-emergency-scheme\n\n\n",
            "introtext": "france",
            "cityname": "Marseille - Emergency Scheme",
            "city_latitude": "43.29",
            "city_longitude": "5.37",
            "scheme_color": "4"
        },
        {
            "id": "1697",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/geneve-geneva-genf-emergency-scheme",
            "introtext": "",
            "cityname": "Geneve (Geneva, Genf) - Emergency Scheme",
            "city_latitude": "46.20",
            "city_longitude": "6.14",
            "scheme_color": "4"
        },
        {
            "id": "2320",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/roma-rome-emergency-scheme",
            "introtext": "Roma has an emergency scheme in place that is activated if certain air pollution limits are exceeded.",
            "cityname": "Roma (Rome) - Emergency Scheme",
            "city_latitude": "41.90",
            "city_longitude": "12.50",
            "scheme_color": "4"
        },
        {
            "id": "1727",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/cremona-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cremona Province - Emergency Scheme",
            "city_latitude": "45.13",
            "city_longitude": "10.03",
            "scheme_color": "4"
        },
        {
            "id": "1728",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lecco-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Lecco Province - Emergency Scheme",
            "city_latitude": "45.85",
            "city_longitude": "9.39",
            "scheme_color": "4"
        },
        {
            "id": "1729",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lodi-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Lodi Province - Emergency Scheme",
            "city_latitude": "45.31",
            "city_longitude": "9.50",
            "scheme_color": "4"
        },
        {
            "id": "1730",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/mantova-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mantova Province - Emergency Scheme",
            "city_latitude": "45.16",
            "city_longitude": "10.80",
            "scheme_color": "4"
        },
        {
            "id": "1745",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chivasso-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Chivasso - Emergency Scheme",
            "city_latitude": "45.19",
            "city_longitude": "7.89",
            "scheme_color": "4"
        },
        {
            "id": "1746",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/collegno-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Collegno - Emergency Scheme",
            "city_latitude": "45.08",
            "city_longitude": "7.58",
            "scheme_color": "4"
        },
        {
            "id": "1394",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/bergen-odd-even-scheme",
            "introtext": "There is an emergency scheme during high pollution events.<br>\r\nFirst time the scheme came into action was 06.01.- 08.01.2016.\r\n\r\n<br>There is also a <a title=\"Charging Scheme\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/bergen-charging-scheme\">Charging Scheme </a> is in place in Bergen.\r\n<br>A <a title=\"Low Emission Zone\" href=\"/countries-mainmenu-147/norway-mainmenu-197/bergen\">Low Emission Zone</a> being also planned for Bergen, as soon as it gets government approval.\r\n\r\n\r\n\r\n",
            "cityname": "Bergen - Emergency Scheme",
            "city_latitude": "60.39",
            "city_longitude": "5.32",
            "scheme_color": "4"
        },
        {
            "id": "1747",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/grugliasco-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Grugliasco - Emergency Scheme",
            "city_latitude": "45.07",
            "city_longitude": "7.58",
            "scheme_color": "4"
        },
        {
            "id": "1950",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/belgium/vlaanderen-region-emergency-scheme",
            "introtext": "",
            "cityname": "Vlaanderen Region - Emergency Scheme",
            "city_latitude": "51.20",
            "city_longitude": "3.22",
            "scheme_color": "4"
        },
        {
            "id": "1547",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/sevilla-emergency-restriction",
            "introtext": "Sevilla has an emergency restriction in the city centre. \r\n",
            "cityname": "Sevilla - Emergency Scheme",
            "city_latitude": "37.38",
            "city_longitude": "-5.98",
            "scheme_color": "4"
        },
        {
            "id": "1193",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/paris-odd-even-scheme",
            "introtext": "There are a number of schemes in Paris.",
            "cityname": "Paris - Emergency Scheme",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "4"
        },
        {
            "id": "1412",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-odd-and-even-numberplates",
            "introtext": "Madrid has various schemes in place:</p>\n\n<ul>\n\t<li>\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid\" title=\"low emission zone\">low emission parking scheme</a>&nbsp;that favours less polluting vehicles</li>\n\t<li>\n\t\ta <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">low emission traffic limited zone</a>&nbsp;vehicles have to be owned by residents or zero emission</li>\n\t<li>\n\t\tan <a href=\"/countries-mainmenu-147/spain/madrid-odd-and-even-numberplates\">emergency scheme</a>&nbsp;</li>\n\t<li>\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid-weight\" title=\"weight restriction\">weight regulation</a></li>\n</ul>\n\n<p>\n\t<strong>NEW! From&nbsp;30 November 2018&nbsp;<a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">Central Madrid</a>&nbsp;</strong>is in place. The&nbsp;existing APRs (&Aacute;reas de Prioridad Residencial &nbsp;= areas where residents have priority) be extended and united into one big APR that is called Madrid Central.</p>\n\n<p>\n\tIt will be of informative character for the first two months and will be fully enforced from <strong>February 2019 on</strong>. The APR Central Madrid will cover practically the entire downtown area of Madrid.&nbsp;</p>\n\n<p>\n\tThe standards in the Central Madrid low emission zone are gradually tightened until a zero emission zone is reached in 2025.</p>\n\n<p>\n\tThe Grand Via is planned to be car-free by summer 2019.<br />\n\tMadrid is one of 4 cities that have stated they wish to remove diesel vehicles from the city. As part of this, the city plans to increase the numbers of access restrictions for private cars.</p>\n",
            "cityname": "Madrid - Emergency Scheme",
            "city_latitude": "40.42",
            "city_longitude": "-3.70",
            "scheme_color": "4"
        },
        {
            "id": "1423",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/oslo-emergency-scheme",
            "introtext": "<p>\r\n\tDuring high pollution events Oslo can implement a diesel ban.</p>\r\n\r\n<p>\r\n\tThe municipality informs with an APP called &#39;Bil i Oslo&#39;&nbsp;24 hours before a possible emergency measure.<br />\r\n\tThere is a <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/oslo-charging-scheme\" title=\"Charging Scheme\">Charging Scheme</a> in place in Oslo, as well as a <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/oslo\" title=\"Low Emission Zone\">Low Emission Zone</a> being planned.<br />\r\n\tThe city authorities in Oslo are also considering making the centre of the city car-free in 2019. We will include more information when it is confirmed.</p>\r\n",
            "cityname": "Oslo - Emergency measure",
            "city_latitude": "59.91",
            "city_longitude": "10.75",
            "scheme_color": "4"
        },
        {
            "id": "1936",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/auvergne-rhone-alpes-emergency-scheme",
            "introtext": "",
            "cityname": "Auvergne-Rhône-Alpes - Emergency Scheme",
            "city_latitude": "45.76",
            "city_longitude": "4.83",
            "scheme_color": "4"
        },
        {
            "id": "1937",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/bourgogne-france-comte-emergency-scheme-3",
            "introtext": "",
            "cityname": "Bourgogne-Franche-Comté - Emergency Scheme",
            "city_latitude": "47.31",
            "city_longitude": "5.01",
            "scheme_color": "4"
        },
        {
            "id": "1470",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/grenoble-emergency-scheme",
            "introtext": "france",
            "cityname": "Grenoble - Emergency Scheme",
            "city_latitude": "45.18",
            "city_longitude": "5.72",
            "scheme_color": "4"
        },
        {
            "id": "1502",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/strasbourg-emergency-scheme\n",
            "introtext": "france",
            "cityname": "Strasbourg - Emergency Scheme",
            "city_latitude": "48.57",
            "city_longitude": "7.75",
            "scheme_color": "4"
        },
        {
            "id": "1702",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/annecy-haute-savoie-emergency-scheme",
            "introtext": "france",
            "cityname": "Annecy / Haute-Savoie - Emergency Scheme",
            "city_latitude": "45.91",
            "city_longitude": "6.13",
            "scheme_color": "4"
        },
        {
            "id": "2279",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/montebelluna-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Montebelluna - Emergency Scheme",
            "city_latitude": "45.77",
            "city_longitude": "12.04",
            "scheme_color": "4"
        },
        {
            "id": "2281",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/mira -emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mira - Emergency Scheme",
            "city_latitude": "45.43",
            "city_longitude": "12.13",
            "scheme_color": "4"
        },
        {
            "id": "1474",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/lyon-emergency-scheme",
            "introtext": "france\n",
            "cityname": "Lyon - Villeurbanne - Emergency Scheme",
            "city_latitude": "45.74",
            "city_longitude": "4.84",
            "scheme_color": "4"
        },
        {
            "id": "1731",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/milano-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Milano Province - Emergency Scheme",
            "city_latitude": "45.47",
            "city_longitude": "9.19",
            "scheme_color": "4"
        },
        {
            "id": "1732",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/monza-and-brianza-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Monza and Brianza Province - Emergency Scheme",
            "city_latitude": "45.58",
            "city_longitude": "9.27",
            "scheme_color": "4"
        },
        {
            "id": "1733",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/pavia-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Pavia Province - Emergency Scheme",
            "city_latitude": "45.19",
            "city_longitude": "9.16",
            "scheme_color": "4"
        },
        {
            "id": "1734",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/varese-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Varese Province - Emergency Scheme",
            "city_latitude": "45.80",
            "city_longitude": "8.83",
            "scheme_color": "4"
        },
        {
            "id": "1735",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alba-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Alba - Emergency Scheme",
            "city_latitude": "44.42",
            "city_longitude": "8.2",
            "scheme_color": "4"
        },
        {
            "id": "1497",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/lille-emergency-scheme\n\n\n",
            "introtext": "france",
            "cityname": "Lille - Emergency Scheme",
            "city_latitude": "50.63",
            "city_longitude": "3.06",
            "scheme_color": "4"
        },
        {
            "id": "1521",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/city-toulouse-emergency-scheme",
            "introtext": "france",
            "cityname": "Toulouse - Emergency Scheme",
            "city_latitude": "43.60",
            "city_longitude": "1.44",
            "scheme_color": "4"
        },
        {
            "id": "1551",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/rennes-emergency-scheme",
            "introtext": "Rennes has an emergency scheme in place during high pollution episodes.",
            "cityname": "Rennes - Emergency Scheme",
            "city_latitude": "48.11",
            "city_longitude": "-1.67",
            "scheme_color": "4"
        },
        {
            "id": "1541",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/chambery-emergency-scheme",
            "introtext": "france",
            "cityname": "Chambery / Savoie - Emergency Scheme",
            "city_latitude": "45.56",
            "city_longitude": "5.92",
            "scheme_color": "4"
        },
        {
            "id": "1544",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/valencia-emergency-restriction",
            "introtext": "Valencia has an emergency scheme that comes into place in cases of high pollution events.",
            "cityname": "Valencia - Emergency Scheme",
            "city_latitude": "39.47",
            "city_longitude": "-0.38",
            "scheme_color": "4"
        },
        {
            "id": "1545",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/valladolid-emergency-restriction",
            "introtext": "Valldolid has an emergency scheme that comes into place in cases of high pollution events.",
            "cityname": "Valladolid - Emergency Scheme",
            "city_latitude": "41.65",
            "city_longitude": "-4.72",
            "scheme_color": "4"
        },
        {
            "id": "2038",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/steiermark-emnergency-scheme",
            "introtext": "",
            "cityname": "Steiermark - Emergency Scheme",
            "city_latitude": "47.25",
            "city_longitude": "15.17",
            "scheme_color": "4"
        },
        {
            "id": "1701",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/barcelona-emergency-scheme",
            "introtext": "Barcelona has an emergency scheme in place that is activated in case of high pollution episodes.",
            "cityname": "Barcelona - Emergency Scheme",
            "city_latitude": "41.39",
            "city_longitude": "2.16",
            "scheme_color": "4"
        },
        {
            "id": "1726",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/como-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Como Province - Emergency Scheme",
            "city_latitude": "45.80",
            "city_longitude": "9.08",
            "scheme_color": "4"
        },
        {
            "id": "1736",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alessandria-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Alessandria - Emergency Scheme",
            "city_latitude": "44.55",
            "city_longitude": "8.37",
            "scheme_color": "4"
        },
        {
            "id": "1737",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/asti-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Asti - Emergency Scheme",
            "city_latitude": "44.90",
            "city_longitude": "8.21",
            "scheme_color": "4"
        },
        {
            "id": "1738",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/beinasco-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Beinasco - Emergency Scheme",
            "city_latitude": "45.02",
            "city_longitude": "7.58",
            "scheme_color": "4"
        },
        {
            "id": "1739",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/biella-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Biella - Emergency Scheme",
            "city_latitude": "45.57",
            "city_longitude": "8.05",
            "scheme_color": "4"
        },
        {
            "id": "1740",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/borgaro-torinese-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Borgaro Torinese - Emergency Scheme",
            "city_latitude": "45.15",
            "city_longitude": "7.65",
            "scheme_color": "4"
        },
        {
            "id": "1741",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/bra-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Bra - Emergency Scheme",
            "city_latitude": "44.7",
            "city_longitude": "7.85",
            "scheme_color": "4"
        },
        {
            "id": "1742",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/carmagnola-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Carmagnola - Emergency Scheme",
            "city_latitude": "44.84",
            "city_longitude": "7.72",
            "scheme_color": "4"
        },
        {
            "id": "1743",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/casale-monferrato-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Casale Monferrato - Emergency Scheme",
            "city_latitude": "45.13",
            "city_longitude": "8.44",
            "scheme_color": "4"
        },
        {
            "id": "1744",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chieri-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Chieri - Emergency Scheme",
            "city_latitude": "45.01",
            "city_longitude": "7.82",
            "scheme_color": "4"
        },
        {
            "id": "1725",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/brescia-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Brescia Province - Emergency Scheme",
            "city_latitude": "45.70",
            "city_longitude": "9.67",
            "scheme_color": "4"
        },
        {
            "id": "1724",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/bergamo-province-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Bergamo Province - Emergency Scheme",
            "city_latitude": "45.70",
            "city_longitude": "9.67",
            "scheme_color": "4"
        },
        {
            "id": "1748",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/ivrea-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ivrea - Emergency Scheme",
            "city_latitude": "45.47",
            "city_longitude": "7.88",
            "scheme_color": "4"
        },
        {
            "id": "1749",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/leini-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Leini - Emergency Scheme",
            "city_latitude": "45.11",
            "city_longitude": "7.43",
            "scheme_color": "4"
        },
        {
            "id": "1750",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/mappano-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mappano - Emergency Scheme",
            "city_latitude": "45.9",
            "city_longitude": "7.42",
            "scheme_color": "4"
        },
        {
            "id": "1751",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/moncalieri-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Moncalieri - Emergency Scheme",
            "city_latitude": "45.0",
            "city_longitude": "7.68",
            "scheme_color": "4"
        },
        {
            "id": "1752",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/nichelino-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Nichelino - Emergency Scheme",
            "city_latitude": "45.0",
            "city_longitude": "7.65",
            "scheme_color": "4"
        },
        {
            "id": "1753",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novara-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Novara - Emergency Scheme",
            "city_latitude": "45.44",
            "city_longitude": "8.62",
            "scheme_color": "4"
        },
        {
            "id": "1754",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/orbassano-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Orbassano - Emergency Scheme",
            "city_latitude": "45.0",
            "city_longitude": "7.53",
            "scheme_color": "4"
        },
        {
            "id": "1755",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pianezza-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Pianezza - Emergency Scheme",
            "city_latitude": "45.6",
            "city_longitude": "7.33",
            "scheme_color": "4"
        },
        {
            "id": "1756",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/rivalta-di-torino-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rivalta di Torino - Emergency Scheme",
            "city_latitude": "45.2",
            "city_longitude": "7.32",
            "scheme_color": "4"
        },
        {
            "id": "1757",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/rivoli-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rivoli - Emergency Scheme",
            "city_latitude": "45.05",
            "city_longitude": "7.52",
            "scheme_color": "4"
        },
        {
            "id": "1758",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/san-mauro-torinese-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Mauro Torinese - Emergency Scheme",
            "city_latitude": "45.1",
            "city_longitude": "7.77",
            "scheme_color": "4"
        },
        {
            "id": "1759",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/settimo-torinese-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Settimo Torinese - Emergency Scheme",
            "city_latitude": "45.13",
            "city_longitude": "7.77",
            "scheme_color": "4"
        },
        {
            "id": "1760",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/torino-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Torino - Emergency Scheme",
            "city_latitude": "45.08",
            "city_longitude": "7.66",
            "scheme_color": "4"
        },
        {
            "id": "1761",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/tortona-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Tortona - Emergency Scheme",
            "city_latitude": "44.86",
            "city_longitude": "8.83",
            "scheme_color": "4"
        },
        {
            "id": "1762",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/trecate-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Trecate - Emergency Scheme",
            "city_latitude": "45.26",
            "city_longitude": "8.44",
            "scheme_color": "4"
        },
        {
            "id": "1763",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/venaria-reale-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Venaria Reale - Emergency Scheme",
            "city_latitude": "45.12",
            "city_longitude": "7.63",
            "scheme_color": "4"
        },
        {
            "id": "1764",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vercelli-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Vercelli - Emergency Scheme",
            "city_latitude": "45.32",
            "city_longitude": "8.42",
            "scheme_color": "4"
        },
        {
            "id": "1765",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vinovo-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Vinovo - Emergency Scheme",
            "city_latitude": "44.57",
            "city_longitude": "7.38",
            "scheme_color": "4"
        },
        {
            "id": "1766",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/volpiano-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Volpiano - Emergency Scheme",
            "city_latitude": "45.12",
            "city_longitude": "7.47",
            "scheme_color": "4"
        },
        {
            "id": "1767",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/treviso-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Treviso - Emergency Scheme",
            "city_latitude": "45.66",
            "city_longitude": "12.25",
            "scheme_color": "4"
        },
        {
            "id": "1768",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/padova-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Padova - Emergency Scheme",
            "city_latitude": "45.41",
            "city_longitude": "11.88",
            "scheme_color": "4"
        },
        {
            "id": "1769",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/vicenza-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Vicenza - Emergency Scheme",
            "city_latitude": "45.55",
            "city_longitude": "11.55",
            "scheme_color": "4"
        },
        {
            "id": "1770",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/verona-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Verona - Emergency Scheme",
            "city_latitude": "45.44",
            "city_longitude": "10.99",
            "scheme_color": "4"
        },
        {
            "id": "1771",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/bassano-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Belluno - Emergency Scheme",
            "city_latitude": "46.15",
            "city_longitude": "12.21",
            "scheme_color": "4"
        },
        {
            "id": "1772",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/feltre-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Feltre - Emergency Scheme",
            "city_latitude": "46.10",
            "city_longitude": "11.54",
            "scheme_color": "4"
        },
        {
            "id": "1773",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/castelfranco-veneto-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Castelfranco Veneto - Emergency Scheme",
            "city_latitude": "45.40",
            "city_longitude": "11.56",
            "scheme_color": "4"
        },
        {
            "id": "1774",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/conegliano-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Conegliano - Emergency Scheme",
            "city_latitude": "45.89",
            "city_longitude": "12.30",
            "scheme_color": "4"
        },
        {
            "id": "1775",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/mansue-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mansue - Emergency Scheme",
            "city_latitude": "45.49",
            "city_longitude": "12.32",
            "scheme_color": "4"
        },
        {
            "id": "1776",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/mirano-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Mirano - Emergency Scheme",
            "city_latitude": "45.49",
            "city_longitude": "12.11",
            "scheme_color": "4"
        },
        {
            "id": "1777",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/san-dona-di-piave-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Dona di Piave - Emergency Scheme",
            "city_latitude": "45.38",
            "city_longitude": "12.34",
            "scheme_color": "4"
        },
        {
            "id": "1778",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/chioggia-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Chioggia - Emergency Scheme",
            "city_latitude": "45.13",
            "city_longitude": "12.17",
            "scheme_color": "4"
        },
        {
            "id": "1779",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/adria-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Adria - Emergency Scheme",
            "city_latitude": "45.30",
            "city_longitude": "12.30",
            "scheme_color": "4"
        },
        {
            "id": "1780",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/rovigo-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rovigo - Emergency Scheme",
            "city_latitude": "45.07",
            "city_longitude": "11.79",
            "scheme_color": "4"
        },
        {
            "id": "1781",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/badia-polesine-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Badia Polesine - Emergency Scheme",
            "city_latitude": "45.60",
            "city_longitude": "11.30",
            "scheme_color": "4"
        },
        {
            "id": "1782",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/este-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Este - Emergency Scheme",
            "city_latitude": "45.14",
            "city_longitude": "11.40",
            "scheme_color": "4"
        },
        {
            "id": "1783",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/cinto-euganeo-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cinto Euganeo - Emergency Scheme",
            "city_latitude": "45.17",
            "city_longitude": "11.40",
            "scheme_color": "4"
        },
        {
            "id": "1784",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/monselice-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Monselice - Emergency Scheme",
            "city_latitude": "45.23",
            "city_longitude": "11.75",
            "scheme_color": "4"
        },
        {
            "id": "1785",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/piove-di-sacco-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Piove di Sacco - Emergency Scheme",
            "city_latitude": "45.30",
            "city_longitude": "12.03",
            "scheme_color": "4"
        },
        {
            "id": "1786",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/citadella-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Citadella - Emergency Scheme",
            "city_latitude": "45.39",
            "city_longitude": "11.47",
            "scheme_color": "4"
        },
        {
            "id": "1787",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/bassano-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Bassano del Grappa - Emergency Scheme",
            "city_latitude": "45.77",
            "city_longitude": "11.73",
            "scheme_color": "4"
        },
        {
            "id": "1788",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/schio-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Schio - Emergency Scheme",
            "city_latitude": "45.43",
            "city_longitude": "11.21",
            "scheme_color": "4"
        },
        {
            "id": "1789",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/legnago-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Legnago - Emergency Scheme",
            "city_latitude": "45.12",
            "city_longitude": "11.18",
            "scheme_color": "4"
        },
        {
            "id": "1790",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/san-bonifacio-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Bonifacio - Emergency Scheme",
            "city_latitude": "45.24",
            "city_longitude": "11.17",
            "scheme_color": "4"
        },
        {
            "id": "1791",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/fiorano-modenese-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Fiorano Modenese - Emergency Scheme",
            "city_latitude": "44.53",
            "city_longitude": "10.82",
            "scheme_color": "4"
        },
        {
            "id": "1792",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/maranello-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Maranello - Emergency Scheme",
            "city_latitude": "44.52",
            "city_longitude": "10.86",
            "scheme_color": "4"
        },
        {
            "id": "1793",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/rubiera-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rubiera - Emergency Scheme",
            "city_latitude": "44.39",
            "city_longitude": "10.47",
            "scheme_color": "4"
        },
        {
            "id": "1794",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/argelato-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Argelato - Emergency Scheme",
            "city_latitude": "44.39",
            "city_longitude": "11.21",
            "scheme_color": "4"
        },
        {
            "id": "1795",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/bologna-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Bologna - Emergency Scheme",
            "city_latitude": "44.49",
            "city_longitude": "11.32",
            "scheme_color": "4"
        },
        {
            "id": "1796",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/calderara-di-reno-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Calderara di Reno - Emergency Scheme",
            "city_latitude": "44.34",
            "city_longitude": "11.16",
            "scheme_color": "4"
        },
        {
            "id": "1797",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/176-europe/emergency-pollution-schemes/emilia-romagna-emergency-schemes/1180-carpi-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Carpi - Emergency Scheme",
            "city_latitude": "44.47",
            "city_longitude": "10.53",
            "scheme_color": "4"
        },
        {
            "id": "1798",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/casalecchio-di-reno-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Casalecchio di Reno - Emergency Scheme",
            "city_latitude": "44.47",
            "city_longitude": "11.27",
            "scheme_color": "4"
        },
        {
            "id": "1799",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/castel-maggiore-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Castel Maggiore - Emergency Scheme",
            "city_latitude": "44.57",
            "city_longitude": "11.36",
            "scheme_color": "4"
        },
        {
            "id": "1800",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/castelfranco-emilia-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Castelfranco Emilia - Emergency Scheme",
            "city_latitude": "44.59",
            "city_longitude": "11.04",
            "scheme_color": "4"
        },
        {
            "id": "1801",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/castenaso-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Castenaso - Emergency Scheme",
            "city_latitude": "44.51",
            "city_longitude": "11.46",
            "scheme_color": "4"
        },
        {
            "id": "1802",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/cento-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cento - Emergency Scheme",
            "city_latitude": "44.73",
            "city_longitude": "11.28",
            "scheme_color": "4"
        },
        {
            "id": "1803",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/cesena-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Cesena - Emergency Scheme",
            "city_latitude": "44.13",
            "city_longitude": "12.23",
            "scheme_color": "4"
        },
        {
            "id": "1804",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/faenza-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Faenza - Emergency Scheme",
            "city_latitude": "44.28",
            "city_longitude": "11.88",
            "scheme_color": "4"
        },
        {
            "id": "1805",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ferrara-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ferrara - Emergency Scheme",
            "city_latitude": "44.50",
            "city_longitude": "11.37",
            "scheme_color": "4"
        },
        {
            "id": "1806",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/forli-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Forlì - Emergency Scheme",
            "city_latitude": "44.23",
            "city_longitude": "12.05",
            "scheme_color": "4"
        },
        {
            "id": "1807",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/formigine-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Formigine - Emergency Scheme",
            "city_latitude": "44.57",
            "city_longitude": "10.84",
            "scheme_color": "4"
        },
        {
            "id": "1808",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/granarolo-dell-emilia-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Granarolo dell Emilia - Emergency Scheme",
            "city_latitude": "44.05",
            "city_longitude": "12.57",
            "scheme_color": "4"
        },
        {
            "id": "1809",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/imola-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Imola - Emergency Scheme",
            "city_latitude": "44.35",
            "city_longitude": "11.72",
            "scheme_color": "4"
        },
        {
            "id": "1810",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/lugo-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Lugo - Emergency Scheme",
            "city_latitude": "44.42",
            "city_longitude": "11.90",
            "scheme_color": "4"
        },
        {
            "id": "1811",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/modena-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Modena - Emergency Scheme",
            "city_latitude": "44.64",
            "city_longitude": "10.92",
            "scheme_color": "4"
        },
        {
            "id": "1812",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ozzano-dell-emilia-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ozzano dell Emilia - Emergency Scheme",
            "city_latitude": "44.44",
            "city_longitude": "11.47",
            "scheme_color": "4"
        },
        {
            "id": "1813",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/parma-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Parma - Emergency Scheme",
            "city_latitude": "44.80",
            "city_longitude": "10.33",
            "scheme_color": "4"
        },
        {
            "id": "1814",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/piacenza-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Piacenza - Emergency Scheme",
            "city_latitude": "45.04",
            "city_longitude": "9.70",
            "scheme_color": "4"
        },
        {
            "id": "1815",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ravenna-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Ravenna - Emergency Scheme",
            "city_latitude": "44.42",
            "city_longitude": "12.20",
            "scheme_color": "4"
        },
        {
            "id": "1816",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/reggio-nell-emilia-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Reggio nell Emilia - Emergency Scheme",
            "city_latitude": "44.70",
            "city_longitude": "10.63",
            "scheme_color": "4"
        },
        {
            "id": "1817",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/riccione-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Riccione - Emergency Scheme",
            "city_latitude": "44.0",
            "city_longitude": "12.39",
            "scheme_color": "4"
        },
        {
            "id": "1818",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/rimini-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Rimini - Emergency Scheme",
            "city_latitude": "44.05",
            "city_longitude": "12.57",
            "scheme_color": "4"
        },
        {
            "id": "1819",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/san-lazzaro-di-savena-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "San Lazzaro di Savena - Emergency Scheme",
            "city_latitude": "44.28",
            "city_longitude": "11.24",
            "scheme_color": "4"
        },
        {
            "id": "1820",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/sassuolo-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Sassuolo - Emergency Scheme",
            "city_latitude": "44.55",
            "city_longitude": "10.78",
            "scheme_color": "4"
        },
        {
            "id": "1821",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/zola-predosa-emergency-scheme",
            "introtext": "The four regions of the Po Valley, Emilia Romagna, Lombardia, Piemonte and Veneto have agreed on an emergency scheme when the Pm10 levels are exceeded for several consecutive days.",
            "cityname": "Zola Predosa - Emergency Scheme",
            "city_latitude": "44.29",
            "city_longitude": "11.13",
            "scheme_color": "4"
        },
        {
            "id": "1925",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-nancy-emergency-scheme",
            "introtext": "france",
            "cityname": "Greater Nancy - Emergency Scheme",
            "city_latitude": "48.69",
            "city_longitude": "6.18",
            "scheme_color": "4"
        },
        {
            "id": "1940",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/corse-emergency-scheme",
            "introtext": "",
            "cityname": "Corse - Emergency Scheme",
            "city_latitude": "41.92",
            "city_longitude": "8.73",
            "scheme_color": "4"
        },
        {
            "id": "1938",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/bretagne-emergency-scheme",
            "introtext": "",
            "cityname": "Bretagne - Emergency Scheme",
            "city_latitude": "48.11",
            "city_longitude": "-1.67",
            "scheme_color": "4"
        },
        {
            "id": "1939",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/centre-val-de-loire-emergency-scheme",
            "introtext": "",
            "cityname": "Centre-Val de Loire - Emergency Scheme",
            "city_latitude": "47.90",
            "city_longitude": "1.91",
            "scheme_color": "4"
        },
        {
            "id": "1942",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/hauts-de-france-emergency-scheme",
            "introtext": "",
            "cityname": "Hauts-de-France - Emergency Scheme",
            "city_latitude": "50.62",
            "city_longitude": "3.05",
            "scheme_color": "4"
        },
        {
            "id": "1941",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/grand-est-emergency-scheme",
            "introtext": "",
            "cityname": "Grand Est - Emergency Scheme",
            "city_latitude": "48.58",
            "city_longitude": "7.75",
            "scheme_color": "4"
        },
        {
            "id": "1943",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/ile-de-france-emergency-scheme",
            "introtext": "",
            "cityname": "Île-de-France - Emergency Scheme",
            "city_latitude": "48.86",
            "city_longitude": "2.34",
            "scheme_color": "4"
        },
        {
            "id": "1944",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/normandie-emergency-scheme",
            "introtext": "",
            "cityname": "Normandie - Emergency Scheme",
            "city_latitude": "49.43",
            "city_longitude": "1.10",
            "scheme_color": "4"
        },
        {
            "id": "1945",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/nouvelle-aquitaine-emergency-scheme",
            "introtext": "",
            "cityname": "Nouvelle-Aquitaine - Emergency Scheme",
            "city_latitude": "44.83",
            "city_longitude": "-0.58",
            "scheme_color": "4"
        },
        {
            "id": "1946",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/occitane-emergency-scheme",
            "introtext": "",
            "cityname": "Occitane - Emergency Scheme",
            "city_latitude": "43.60",
            "city_longitude": "1.44",
            "scheme_color": "4"
        },
        {
            "id": "1947",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/pays-de-la-loire-emergency-scheme",
            "introtext": "",
            "cityname": "Pays de la Loire - Emergency Scheme",
            "city_latitude": "47.21",
            "city_longitude": "-1.55",
            "scheme_color": "4"
        },
        {
            "id": "1948",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/provence-alpes-cote-d-azur-emergency-scheme",
            "introtext": "",
            "cityname": "Provence-Alpes-Côte d’Azur - Emergency Scheme",
            "city_latitude": "43.29",
            "city_longitude": "5.37",
            "scheme_color": "4"
        },
        {
            "id": "1951",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/belgium/wallonia-region-emergency-scheme",
            "introtext": "",
            "cityname": "Wallonia Region - Emergency Scheme",
            "city_latitude": "50.46",
            "city_longitude": "4.86",
            "scheme_color": "4"
        },
        {
            "id": "1952",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/wien-vienna-emergency-scheme",
            "introtext": "",
            "cityname": "Wien (Vienna) - Emergency Scheme",
            "city_latitude": "48.20",
            "city_longitude": "16.37",
            "scheme_color": "4"
        },
        {
            "id": "2039",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/kaernten-emergency-scheme",
            "introtext": "",
            "cityname": "Kärnten - Emergency Scheme",
            "city_latitude": "47.72",
            "city_longitude": "14.18",
            "scheme_color": "4"
        },
        {
            "id": "2040",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/oberosterreich-emergency-scheme",
            "introtext": "",
            "cityname": "Oberösterreich - Emergency Scheme",
            "city_latitude": "48.02",
            "city_longitude": "13.97",
            "scheme_color": "4"
        },
        {
            "id": "2041",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/salzburg-emergency-scheme",
            "introtext": "",
            "cityname": "Salzburg - Emergency Scheme",
            "city_latitude": "47.80",
            "city_longitude": "13.05",
            "scheme_color": "4"
        },
        {
            "id": "2428",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/departement-var-emergency-scheme",
            "introtext": "",
            "cityname": "Var - Emergency Scheme",
            "city_latitude": "43.12",
            "city_longitude": "6.01",
            "scheme_color": "4"
        },
        {
            "id": "2326",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/greece/athens-emergency-scheme",
            "introtext": "Athens has an emergency low emission zone implemented.",
            "cityname": "Athens - Emergency Scheme",
            "city_latitude": "37.98",
            "city_longitude": "23.72",
            "scheme_color": "4"
        },
        {
            "id": "2360",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/alcala-de-henares-emergency-scheme",
            "introtext": "Alcala de Henares has implemented a low emission zone 1 January 2023.",
            "cityname": "Alcala de Henares - Emergency Scheme",
            "city_latitude": "40.48",
            "city_longitude": "-3.35",
            "scheme_color": "4"
        },
        {
            "id": "2396",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/granollers-emergency-scheme",
            "introtext": "Granollers has implemented ZBE January 2025.",
            "cityname": "Granollers - Emergency Scheme",
            "city_latitude": "41.60",
            "city_longitude": "2.28",
            "scheme_color": "4"
        },
        {
            "id": "2409",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/bordeaux-emergency-scheme\n\n\n",
            "introtext": "france",
            "cityname": "Bordeaux - Emergency Scheme",
            "city_latitude": "44.84",
            "city_longitude": "-0.58",
            "scheme_color": "4"
        },
        {
            "id": "2444",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/las-rozas-de-madrid-emergency-scheme",
            "introtext": "",
            "cityname": "Las Rozas de Madrid - Emergency Scheme",
            "city_latitude": "40.49",
            "city_longitude": "-3.88",
            "scheme_color": "4"
        },
        {
            "id": "2086",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/logrono-ar",
            "introtext": "",
            "cityname": "Logrono - Limited Traffic Zone",
            "city_latitude": "42.46",
            "city_longitude": "-2.44",
            "scheme_color": "3"
        },
        {
            "id": "2087",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/toledo-ar",
            "introtext": "",
            "cityname": "Toledo - Limited Traffic Zone",
            "city_latitude": "39.85",
            "city_longitude": "-4.02",
            "scheme_color": "3"
        },
        {
            "id": "2088",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/malaga-ar",
            "introtext": "",
            "cityname": "Malaga - Limited Traffic Zone",
            "city_latitude": "36.72",
            "city_longitude": "-4.42",
            "scheme_color": "3"
        },
        {
            "id": "2089",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/cordoba-ar",
            "introtext": "",
            "cityname": "Cordoba - Limited Traffic Zone",
            "city_latitude": "37.88",
            "city_longitude": "-4.77",
            "scheme_color": "3"
        },
        {
            "id": "2090",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/sevilla-ar",
            "introtext": "",
            "cityname": "Sevilla - Limited Traffic Zone",
            "city_latitude": "37.38",
            "city_longitude": "-5.98",
            "scheme_color": "3"
        },
        {
            "id": "2091",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/alicante-ar",
            "introtext": "Alicante has an access regulation in its city centre.",
            "cityname": "Alacant - Limited Traffic Zone",
            "city_latitude": "38.34",
            "city_longitude": "-0.49",
            "scheme_color": "3"
        },
        {
            "id": "2092",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/cuenca-ar",
            "introtext": "",
            "cityname": "Cuenca - Limited Traffic Zone",
            "city_latitude": "40.07",
            "city_longitude": "-2.13",
            "scheme_color": "3"
        },
        {
            "id": "2093",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/santiago-de-compostela-ar",
            "introtext": "",
            "cityname": "Santiago de Compostela - Limited Traffic Zone",
            "city_latitude": "42.87",
            "city_longitude": "-8.54",
            "scheme_color": "3"
        },
        {
            "id": "2094",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/tarifa-ar",
            "introtext": "",
            "cityname": "Tarifa - Limited Traffic Zone",
            "city_latitude": "36.01",
            "city_longitude": "-5.60",
            "scheme_color": "3"
        },
        {
            "id": "2099",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/caceres-ar",
            "introtext": "",
            "cityname": "Caceres - Limited Traffic Zone",
            "city_latitude": "39.47",
            "city_longitude": "-6.37",
            "scheme_color": "3"
        },
        {
            "id": "2095",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/leon-ar",
            "introtext": "",
            "cityname": "Leon - Limited Traffic Zone",
            "city_latitude": "42.59",
            "city_longitude": "-5.56",
            "scheme_color": "3"
        },
        {
            "id": "2096",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/san-sebastian-ar",
            "introtext": "",
            "cityname": "San Sebastian - Limited Traffic Zone",
            "city_latitude": "43.32",
            "city_longitude": "-1.98",
            "scheme_color": "3"
        },
        {
            "id": "2085",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/vigo-ar",
            "introtext": "",
            "cityname": "Vigo - Limited Traffic Zone",
            "city_latitude": "42.24",
            "city_longitude": "-8.72",
            "scheme_color": "3"
        },
        {
            "id": "1694",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/belluno-ar",
            "introtext": "The Access Regulation (ZTL) of Belluno covers part of the historic center.\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 2019.</p>\r\n",
            "cityname": "Belluno - Limited Traffic Zone",
            "city_latitude": "46.15",
            "city_longitude": "12.21",
            "scheme_color": "3"
        },
        {
            "id": "2031",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/pontevedra-ar",
            "introtext": "\r\n",
            "cityname": "Pontevedra - pedestrian",
            "city_latitude": "42.42",
            "city_longitude": "-8.64",
            "scheme_color": "3"
        },
        {
            "id": "1687",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/tirol-summer-through-traffic-bans",
            "introtext": "In the summer, May to mid October, there are though traffic bans on secondary roads in Tirol. Exceptions are for destination and originating traffic and residents only.",
            "cityname": "Tirol Summer Through Traffic Bans",
            "city_latitude": "47.26",
            "city_longitude": "11.45",
            "scheme_color": "3"
        },
        {
            "id": "1118",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/spoleto-ar",
            "introtext": "The Access Regulation (ZTL) of Spoleto covers part of the historic center.",
            "cityname": "Spoleto - Limited Traffic Zone",
            "city_latitude": "42.74",
            "city_longitude": "12.74",
            "scheme_color": "3"
        },
        {
            "id": "1673",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/zermatt-carfree",
            "introtext": "CH",
            "cityname": "Zermatt - car-free",
            "city_latitude": "46.02",
            "city_longitude": "7.74",
            "scheme_color": "3"
        },
        {
            "id": "1508",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/a12-air-quality-based-speed-limit",
            "introtext": "<b>On the A12</b> there are several schemes, please select the one you want information on, and then the details will show below",
            "cityname": "A12 Air quality-based speed limit",
            "city_latitude": "47.26",
            "city_longitude": "11.45",
            "scheme_color": "3"
        },
        {
            "id": "1671",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/stoos-carfree",
            "introtext": "CH",
            "cityname": "Stoos - car-free",
            "city_latitude": "47",
            "city_longitude": "8.69",
            "scheme_color": "3"
        },
        {
            "id": "1672",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/wengen-carfree",
            "introtext": "CH",
            "cityname": "Wengen - car-free",
            "city_latitude": "46.6",
            "city_longitude": "7.91",
            "scheme_color": "3"
        },
        {
            "id": "2037",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/bruxelles-brussel-brussels-ar",
            "introtext": "",
            "cityname": "Bruxelles - Brussel (Brussels) - LTZ",
            "city_latitude": "50.85",
            "city_longitude": "4.35",
            "scheme_color": "3"
        },
        {
            "id": "1707",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/crema-ar",
            "introtext": "",
            "cityname": "Crema - Limited Traffic Zone",
            "city_latitude": "45.21",
            "city_longitude": "9.40",
            "scheme_color": "3"
        },
        {
            "id": "2312",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/heidelberg-carfree",
            "introtext": "Heidelberg has a carfree area.",
            "cityname": "Heidelberg - car-free",
            "city_latitude": "49.40",
            "city_longitude": "8.66",
            "scheme_color": "3"
        },
        {
            "id": "949",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/piacenza-ar",
            "introtext": "The Access Regulation (ZTL) of Piacenza is divided in four parts: A, B, C and D.<br>\r\nZTL D allows all vehicles, even without a permit, to transit in direction of Via Roma and Via Sclabrini.\r\n\r\n<br><br>There is also an access regulation in place called <a title=\"Piacenza\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/piacenza\">Piacenza</a>.<br><br>\r\n\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Piacenza - Limited Traffic Zone",
            "city_latitude": "45.04",
            "city_longitude": "9.70",
            "scheme_color": "3"
        },
        {
            "id": "2439",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/fuengirola-limited-traffic-zone",
            "introtext": "",
            "cityname": "Fuengirola - Limited Traffic Zone",
            "city_latitude": "37.28",
            "city_longitude": "-5.92",
            "scheme_color": "3"
        },
        {
            "id": "1467",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/palma-ar",
            "introtext": "Palma de Mallorca / Spain has progressively transformed parts of the historic centre into an access regulated area called ACIRE.<br>\nThe restricted traffic zones (ACIRE) are special areas where only the traffic of authorized vehicles and other specific vehicles with a permit are allowed to enter.\n\n",
            "cityname": "Palma de Mallorca - Limited Traffic Zone",
            "city_latitude": "39.56",
            "city_longitude": "2.65",
            "scheme_color": "3"
        },
        {
            "id": "1226",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/abruzzo-region/lanciano-ar",
            "introtext": "The Access Regulation (ZTL) of Lanciano covers part of the historic center and is divided in five parts: <br>\r\n- Quartiere Civitanova Sacca<br>\r\n- Quartiere Lancianovecchia<br>\r\n- Quartiere Borgo<br>\r\n- Piazza Plebiscito<br>\r\n- Via Monte Maiella<br>\r\n- Corso Trento e Trieste.",
            "cityname": "Lanciano - Limited Traffic Zone",
            "city_latitude": "42.23",
            "city_longitude": "14.39",
            "scheme_color": "3"
        },
        {
            "id": "1227",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/abruzzo-region/pescara-ar",
            "introtext": "The Access Regulation (ZTL) of Pescara covers part of the historic center.",
            "cityname": "Pescara - Limited Traffic Zone",
            "city_latitude": "46.06",
            "city_longitude": "11.24",
            "scheme_color": "3"
        },
        {
            "id": "1022",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/rho-ar",
            "introtext": "The Access Regulation (ZTL) of Rho covers part of the historic center. \r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Rho - Limited Traffic Zone",
            "city_latitude": "45.53",
            "city_longitude": "9.04",
            "scheme_color": "3"
        },
        {
            "id": "869",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/barcelona-superblocks",
            "introtext": "Barcelona also has an <a title=\"emergency scheme\"  href=\"/countries-mainmenu-147/spain/barcelona\">emergency scheme</a> and will have a <a title=\"low emission zone\"  href=\"/countries-mainmenu-147/spain/barcelona\">low emission zone </a> in place.<br>\nBarcelona has progressively transformed the historic centre (\"Ciutat Vella\") into a pedestrian zone during certain times of the day. The access is regulated with pylons and by a central control unit.<br><br>\n\nBarcelona has also established a concept called <b>superblocks/supermanzanas</b>. This concept keeps transit traffic out of the superblocks. These are defined through a set of basic roads which form a polygon or inner area, and contain within them a public space geared toward the citizen.<br><br>\n\nIn these parts of Barcelona the superblock concept has already been established: <br>\n- Gracia<br>\n- Santa Maria del Mar<br>\n- El Born<br><br>\n\nFor these parts the concept will be established in the near future:<br>\n- Viladecans<br>\n- El Prat (Cataluña)<br>\n- A Coruña<br>\n- Ferrol (Galicia)<br>\n- 22@<br>\t\n\n\n\n",
            "cityname": "Barcelona - superblocks",
            "city_latitude": "41.39",
            "city_longitude": "2.16",
            "scheme_color": "3"
        },
        {
            "id": "1667",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/muerren-carfree",
            "introtext": "CH",
            "cityname": "Mürren - car-free",
            "city_latitude": "46.55",
            "city_longitude": "7.89",
            "scheme_color": "3"
        },
        {
            "id": "1511",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/a12-night-time-speed-limit",
            "introtext": "<b>On the A12</b> there are several schemes, please select the one you want information on, and then the details will show below",
            "cityname": "A12 Night time speed limit",
            "city_latitude": "47.26",
            "city_longitude": "11.45",
            "scheme_color": "3"
        },
        {
            "id": "1668",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/riederalp-carfree",
            "introtext": "CH",
            "cityname": "Riederalp - car-free",
            "city_latitude": "46.37",
            "city_longitude": "8.02",
            "scheme_color": "3"
        },
        {
            "id": "2427",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/poland/weight-restrictions-in-poland",
            "introtext": "",
            "cityname": "Weight restrictions in Poland",
            "city_latitude": "52.00",
            "city_longitude": "20.00",
            "scheme_color": "3"
        },
        {
            "id": "753",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/rovereto-ar",
            "introtext": "There is an access regulation in the historic part of Rovereto.",
            "cityname": "Rovereto - Limited Traffic Zone",
            "city_latitude": "45.88",
            "city_longitude": "11.03",
            "scheme_color": "3"
        },
        {
            "id": "2157",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/wien-vienna-kurzparkzone",
            "introtext": "",
            "cityname": "Wien (Vienna) - Kurzparkzone",
            "city_latitude": "47.07",
            "city_longitude": "15.42",
            "scheme_color": "3"
        },
        {
            "id": "1045",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/galliate-ar",
            "introtext": "The Access Regulation (ZTL) of Galliate covers part of the historic center.",
            "cityname": "Galliate - Limited Traffic Zone",
            "city_latitude": "45.48",
            "city_longitude": "8.69",
            "scheme_color": "3"
        },
        {
            "id": "1046",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/ivrea-ar",
            "introtext": "The Access Regulation (ZTL) of Ivrea covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Ivrea\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/ivrea\">Ivrea</a>.",
            "cityname": "Ivrea - Limited Traffic Zone",
            "city_latitude": "45.47",
            "city_longitude": "7.88",
            "scheme_color": "3"
        },
        {
            "id": "2328",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/dordrecht-car-free",
            "introtext": "",
            "cityname": "Dordrecht - car-free",
            "city_latitude": "52.99",
            "city_longitude": "6.56",
            "scheme_color": "3"
        },
        {
            "id": "2337",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/breda-car-free",
            "introtext": "",
            "cityname": "Breda - car-free",
            "city_latitude": "51.57",
            "city_longitude": "4.76",
            "scheme_color": "3"
        },
        {
            "id": "765",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/pergine-valsugana-ar",
            "introtext": "There is also a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/trentino-province/pergine-valsugana\">Low Emission Zone</a> in Pergine Valsugana.",
            "cityname": "Pergine Valsugana - Limited Traffic Zone",
            "city_latitude": "46.06",
            "city_longitude": "11.24",
            "scheme_color": "3"
        },
        {
            "id": "1949",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/krefeld-nrw",
            "introtext": "Krefeld also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/krefeld\">Low Emission Zone</a> in place.",
            "cityname": "Krefeld - Transit Ban",
            "city_latitude": "51.33",
            "city_longitude": "6.58",
            "scheme_color": "3"
        },
        {
            "id": "779",
            "citypath": "http://urbanaccessregulations.eu//countries-mainmenu-147/hungary/budapest",
            "introtext": "",
            "cityname": "Budapest - lorry LTZ",
            "city_latitude": "47.50",
            "city_longitude": "19.04",
            "scheme_color": "3"
        },
        {
            "id": "1531",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/poggiponsi-ar",
            "introtext": "The Access Regulation (ZTL) of Poggibonsi covers part of the historic center.",
            "cityname": "Poggibonsi - Limited Traffic Zone",
            "city_latitude": "43.47",
            "city_longitude": "11.15",
            "scheme_color": "3"
        },
        {
            "id": "2080",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/graz-pedestrian",
            "introtext": "",
            "cityname": "Graz - pedestrian",
            "city_latitude": "47.07",
            "city_longitude": "15.42",
            "scheme_color": "3"
        },
        {
            "id": "2081",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/bruxelles-brussel-brussels-pedestrian-zone",
            "introtext": "",
            "cityname": "Bruxelles - Brussel (Brussels) - pedestrian zone",
            "city_latitude": "50.85",
            "city_longitude": "4.35",
            "scheme_color": "3"
        },
        {
            "id": "881",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/finland/helsinki-ar",
            "introtext": "Currently there are two schemes in place in Helsinki:<br>\nan Access Restriction scheme for lorries longer than 12 meters and an <a title=\"Environmental Zone\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/finland/helsinki\">Environmental Zone</a> for buses and refuse vehicles.\n",
            "cityname": "Helsinki - lorry LTZ",
            "city_latitude": "60.17",
            "city_longitude": "24.94",
            "scheme_color": "3"
        },
        {
            "id": "1015",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/slovenia/ljubljana-ar",
            "introtext": "There is an access regulation in place in the historic centre of Ljubljana.",
            "cityname": "Ljubljana - pedestrian",
            "city_latitude": "50.12",
            "city_longitude": "8.68",
            "scheme_color": "3"
        },
        {
            "id": "925",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/abruzzo-region/teramo-ar",
            "introtext": "The Access Regulation (ZTL) of Teramo covers an important part of the historic center.",
            "cityname": "Teramo - Limited Traffic Zone",
            "city_latitude": "42.66",
            "city_longitude": "13.70",
            "scheme_color": "3"
        },
        {
            "id": "846",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/london-lorry-control",
            "introtext": "The London Lorry Control Scheme is often mistakenly referred to as the Lorry Ban. Restrictions are in place on the use of heavy goods vehicles to help minimise noise pollution in residential areas during unsocial hours through restricted use of these roads. The Lorry Control Scheme takes the form of controls on the movement of any heavy goods vehicles over 18 tonnes maximum gross weight at night and weekends within the red boundary on the site map.</p>\r\n\r\n",
            "cityname": "London Lorry Control",
            "city_latitude": "51.51",
            "city_longitude": "-0.13",
            "scheme_color": "3"
        },
        {
            "id": "855",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/czech-republic-mainmenu-448/brno-ar",
            "introtext": "",
            "cityname": "Brno - pedestrian",
            "city_latitude": "49.19",
            "city_longitude": "16.60",
            "scheme_color": "3"
        },
        {
            "id": "856",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/ireland/dublin-ar",
            "introtext": "There has been an access restriction for heavy goods vehicles with 5+ axels in a cordon area of Dublin since February 2007.",
            "cityname": "Dublin - lorry LTZ",
            "city_latitude": "53.33",
            "city_longitude": "-6.25",
            "scheme_color": "3"
        },
        {
            "id": "847",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/rome-ar",
            "introtext": "<p>\r\n\tThe mayor has banned vehicles from driving through the Italian capital on Sundays in a bid to tackle severe smog. Police have been advised to fine anyone who flouts the tough traffic restrictions.<br />\r\n\t<br />\r\n\t<b>In August the ZTL is always suspended at <i>night</i> in City Centre, Monti, Testaccio, Trastevere and San Lorenzo because of the summer holidays.</b><br />\r\n\t<br />\r\n\tThere are 6 different schemes in operation in Rome:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\tZTL City Centre (night and day), covering the main centre of Rome</li>\r\n\t<li>\r\n\t\tthe Access Regulation (ZTL) of Trastevere (night and day)</li>\r\n\t<li>\r\n\t\tSan Lorenzo (night),</li>\r\n\t<li>\r\n\t\tTestaccio (night)</li>\r\n\t<li>\r\n\t\tTridente (day and night)</li>\r\n\t<li>\r\n\t\tMonti (night)</li>\r\n</ul>\r\n\r\n<p>\r\n\tThere is also a Low Emission Zone in <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/rome\" title=\"Rome\">Rome</a> and <a class=\"new-window nturl\" href=\"countries-mainmenu-147/italy-mainmenu-81/lazio-region/rome-coaches\" title=\"Roma - Coaches\">Rome - Coaches</a>, an access regulation for tourist buses.<br />\r\n\tThere is also the possibility of emergency measures on days with extreme pollution, particularly in the winter. Options include banning alternating number plates, or a ban all vehicles. Notification is by the local press.</p>\r\n",
            "cityname": "Roma (Rome) - Limited Traffic Zone",
            "city_latitude": "41.90",
            "city_longitude": "12.50",
            "scheme_color": "3"
        },
        {
            "id": "849",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/napoli-ar",
            "introtext": "<p>\r\n\tThe ZTL of Napoli consists of 6 parts:</p>\r\n\r\n<p>\r\n\tZTL Tarsia-Pignasecca-Dante<br />\r\n\tZTL Belledonne, Martiri, Poerio<br />\r\n\tZTL Centro Antico<br />\r\n\tZTL Morelli, Filangieri, Mille<br />\r\n\tZTL di Chiaia<br />\r\n\tZTL Marechiaro</p>\r\n\r\n<p>\r\n\t<br />\r\n\tThere is also an LEZ in place in <a href=\"/countries-mainmenu-147/italy-mainmenu-81/napoli\" title=\"Napoli\">Napoli</a>.</p>\r\n",
            "cityname": "Napoli - Limited Traffic Zone",
            "city_latitude": "40.83",
            "city_longitude": "14.25",
            "scheme_color": "3"
        },
        {
            "id": "1151",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/salerno-ar",
            "introtext": "The Access Regulation (ZTL) of Salerno covers part of the historical center.",
            "cityname": "Salerno - Limited Traffic Zone",
            "city_latitude": "40.68",
            "city_longitude": "14.76",
            "scheme_color": "3"
        },
        {
            "id": "850",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/genova-ar",
            "introtext": "The following 8 Access Regulations (ZTL) are in place in Genova:<br>\r\n- Centro Storico<br>\r\n- Boccadasse<br>\r\n- Bolzaneto<br>\r\n- Castelletto<br>\r\n- Molo<br>\r\n- Nervi<br>\r\n- Rivarolo<br>\r\n- Vernazzola\r\n\r\n<br><br>There is also an LEZ in place in <a title=\"Genova\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/genova\">Genova</a>.",
            "cityname": "Genova - Limited Traffic Zone",
            "city_latitude": "44.41",
            "city_longitude": "8.93",
            "scheme_color": "3"
        },
        {
            "id": "851",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/torino-ar",
            "introtext": "<p>\r\n\tThe access regulation <strong>ZTL Centrale</strong> concerns an important part of the <strong>historic centre</strong>:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\t<strong>ZTL Romana</strong></li>\r\n\t<li>\r\n\t\t<strong>ZTL Public transport</strong></li>\r\n\t<li>\r\n\t\t<strong>ZTL Pedestrian&nbsp;</strong></li>\r\n</ul>\r\n\r\n<p>\r\n\t<strong>Outside</strong> of ZTL Centrale is <strong>ZTL Valentino</strong>.<br />\r\n\tThere is also an LEZ in place in <a href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/torino\" title=\"Torino\">Torino</a>.</p> \r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Torino - Limited Traffic Zone",
            "city_latitude": "45.08",
            "city_longitude": "7.66",
            "scheme_color": "3"
        },
        {
            "id": "854",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/czech-republic-mainmenu-448/praha",
            "introtext": "There are three different schemes in place in Praha.<br>\r\nAn LEZ (Low Emission Zone) in <a title=\"Praha\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/czech-republic-mainmenu-448/praha\">Praha</a>, a Permit Scheme for <a title=\"lorries\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/czech-republic-mainmenu-448/praha-prague-permit\">lorries</a> and an ARS (Access Control Scheme) for coaches/tour buses.",
            "cityname": "Praha (Prague) Coaches",
            "city_latitude": "50.09",
            "city_longitude": "14.42",
            "scheme_color": "3"
        },
        {
            "id": "852",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/milano-ar",
            "introtext": "<p>\r\n\tThere are several schemes in Milan:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\t<strong>NEW!</strong>&nbsp;<a href=\"/countries-mainmenu-147/italy-mainmenu-81/milano-lez-area-b\">Area B</a> is a Low Emission Zone that will be activated the <strong>25 February 2019</strong>. It will cover the entire city of Milan.</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milan-area-c-charging-scheme\" title=\"Milan C\">Milan C</a>&nbsp;is a combined Low Emission Zone and urban road charging scheme</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milano-ar\" title=\"Milan - AR\">Milan - AR</a>, an Access Regulation</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/como\" title=\"Milan province\">Milan province</a>, the Low Emission Zones of the four provinces of Milan, Como, Varese and Lecco merge to give a &#39;paw print&#39; shaped LEZ (see <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/milano\" title=\"Milan Province\">Milan Province</a>).</li>\r\n\t<li>\r\n\t\tshort term restrictions are possible, particularly in the winter <a href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/como\" title=\"See the Milan LEZ page\">See the Milan LEZ page</a>. To find out if scheme is operational go <a href=\"https://inlinea.cittametropolitana.mi.it/dati_ambientali/pm10/\" target=\"_blank\" title=\"Milan website about PM10 air pollution\">here</a>.</li>\r\n\t<li>\r\n\t\t<a class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/milan-area-c-charging-scheme\" title=\"Milan C\">Milan C</a> now substitutes the <a class=\"new-window nturl\" href=\"/ecopass\" title=\"Milan ecopass\">Milan ecopass</a> that is no longer in operation.</li>\r\n</ul>\r\n\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a&nbsp;<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"><b>winter emergency scheme</b></a> in place from 1 October - 31 March.</p>\r\n\r\n<p>\r\n\t&nbsp;</p>\r\n",
            "cityname": "Milano - Limited Traffic Zone",
            "city_latitude": "45.47",
            "city_longitude": "9.19",
            "scheme_color": "3"
        },
        {
            "id": "853",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/czech-republic-mainmenu-448/praha",
            "introtext": "There are three different schemes in place in Praha. The other two schemes are:<br>\r\nA <a title=\"Prague low emission zone\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/czech-republic-mainmenu-448/praha\">low emission zone</a>.<br>\r\nAnd an access regulation for <a title=\"coaches\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/czech-republic-mainmenu-448/praha-prague-coaches\">tourist buses</a>.",
            "cityname": "Praha (Prague) - Access Regulation - Lorry LEZ",
            "city_latitude": "50.09",
            "city_longitude": "14.42",
            "scheme_color": "3"
        },
        {
            "id": "857",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/reading-ar",
            "introtext": "This ARS (Access Regulation Scheme) denies certain vehicles access to the city centre at certain times.",
            "cityname": "Reading - car-free",
            "city_latitude": "51.45",
            "city_longitude": "-0.97",
            "scheme_color": "3"
        },
        {
            "id": "858",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/krakow-ar",
            "introtext": "",
            "cityname": "Krakow - AR",
            "city_latitude": "50.06",
            "city_longitude": "19.94",
            "scheme_color": "3"
        },
        {
            "id": "859",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/warsawa",
            "introtext": "<p> \tWarsaw has an access regulation in place.</p>  <p> \tThere has been a recent Polish Law that allows cities to implement &quot;<strong>clean transport areas</strong>&quot;. These are areas where only electric, hydrogen-powered, CNG and LNG vehicles would be allowed in. So far no city has decided to&nbsp;implement one. Check this page regularly for updates.",
            "cityname": "Warsawa (Warsaw) - lorry LTZ",
            "city_latitude": "52.2",
            "city_longitude": "21.01",
            "scheme_color": "3"
        },
        {
            "id": "860",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/wroclaw-ar",
            "introtext": "<p>\n\tAccess regulations for vehicles >9 tonnes have been in place in Wroclaw since 1st January 2012.</p>\n\n<p>\n\tThere has been a recent Polish Law that allows cities to implement &quot;<strong>clean transport areas</strong>&quot;. These are areas where only electric, hydrogen-powered, CNG and LNG vehicles would be allowed in. So far no city has decided to&nbsp;implement one. Check this page regularly for updates.\n",
            "cityname": "Wroclaw - lorry LTZ",
            "city_latitude": "51.1",
            "city_longitude": "17.03",
            "scheme_color": "3"
        },
        {
            "id": "865",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-weight",
            "introtext": "<p>\r\n\tMadrid has various schemes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid\" title=\"low emission zone\">low emission parking scheme</a>&nbsp;that favours less polluting vehicles</li>\r\n\t<li>\r\n\t\ta <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">low emission traffic limited zone</a>&nbsp;vehicles have to be owned by residents or zero emission</li>\r\n\t<li>\r\n\t\tan <a href=\"/countries-mainmenu-147/spain/madrid-odd-and-even-numberplates\">emergency scheme</a>&nbsp;</li>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid-weight\" title=\"weight restriction\">weight regulation</a></li>\r\n</ul>\r\n\r\n<p>\r\n\t<strong>NEW! From&nbsp;30 November 2018&nbsp;<a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">Central Madrid</a>&nbsp;</strong>is in place. The&nbsp;existing APRs (&Aacute;reas de Prioridad Residencial &nbsp;= areas where residents have priority) be extended and united into one big APR that is called Madrid Central.</p>\r\n\r\n<p>\r\n\tIt will be of informative character for the first two months and will be fully enforced from <strong>February 2019 on</strong>. The APR Central Madrid will cover practically the entire downtown area of Madrid.&nbsp;</p>\r\n\r\n<p>\r\n\tThe standards in the Central Madrid low emission zone are gradually tightened until a zero emission zone is reached in 2025.</p>\r\n\r\n<p>\r\n\tThe Grand Via is planned to be car-free by summer 2019.<br />\r\n\tMadrid is one of 4 cities that have stated they wish to remove diesel vehicles from the city. As part of this, the city plans to increase the numbers of access restrictions for private cars.</p>\r\n",
            "cityname": "Madrid - Weight Restriction",
            "city_latitude": "40.42",
            "city_longitude": "-3.70",
            "scheme_color": "3"
        },
        {
            "id": "866",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/poznan-poznan",
            "introtext": "<p>\r\n\tThere is an access regulation for lorries over 3.5 tonnes, 10 tonnes and 16 tonnes to enter city centre of Poznan.</p>\r\n\r\n<p>\r\n\tThere has been a recent Polish Law that allows cities to implement &quot;<strong>clean transport areas</strong>&quot;. These are areas where only electric, hydrogen-powered, CNG and LNG vehicles would be allowed in. So far no city has decided to&nbsp;implement one. Check this page regularly for updates.",
            "cityname": "Poznan (Poznan) - lorry LTZ",
            "city_latitude": "52.40",
            "city_longitude": "16.92",
            "scheme_color": "3"
        },
        {
            "id": "867",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/lodz",
            "introtext": "<p>\r\n\tThere is a permit &quot;scheme&quot; on the touristic Piotrkowska street. A few selected vehicles can apply for permits to enter an otherwise pedestrian length of road.</p>\r\n\r\n<p>\r\n\tThere has been a recent Polish Law that allows cities to implement &quot;<strong>clean transport areas</strong>&quot;. These are areas where only electric, hydrogen-powered, CNG and LNG vehicles would be allowed in. So far no city has decided to&nbsp;implement one. Check this page regularly for updates.",
            "cityname": "Lodz (Lodz) - pedestrian",
            "city_latitude": "51.75",
            "city_longitude": "19.45",
            "scheme_color": "3"
        },
        {
            "id": "868",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/romania/bucuresti-bucharest",
            "introtext": "Vehicles >5 tonnes can only enter the centre region of Bucharest at a certain time and only with a permit. There is zone A and zone B. The cost of the permit depends on the zone and the weight of the vehicle.",
            "cityname": "Bucuresti (Bucharest) - lorry ban",
            "city_latitude": "44.43",
            "city_longitude": "26.10",
            "scheme_color": "3"
        },
        {
            "id": "875",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/latvia/riga-wr",
            "introtext": "There is also a <a title=\"vehicle free area in the Old Town of Riga\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/latvia/riga\">vehicle free area in the Old Town of Riga</a>.",
            "cityname": "Riga - Weight R",
            "city_latitude": "56.95",
            "city_longitude": "24.11",
            "scheme_color": "3"
        },
        {
            "id": "888",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/dresden-ar",
            "introtext": "Dresden has an access regulation in place.",
            "cityname": "Dresden - Transit Ban",
            "city_latitude": "51.05",
            "city_longitude": "13.74",
            "scheme_color": "3"
        },
        {
            "id": "877",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/latvia/riga",
            "introtext": "From 2010 January there was an update in the traffic regulation in the Old Town of Riga.<br>\nThere is also a <a title=\"Traffic Department of Riga City\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/latvia/riga-wr\">weight-based access regulation in Riga</a> for freight vehicles over 5 tonnes on specified streets and periods.",
            "cityname": "Riga - pedestrian",
            "city_latitude": "56.96",
            "city_longitude": "24.11",
            "scheme_color": "3"
        },
        {
            "id": "878",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/gent-ar",
            "introtext": "<div class=\"divContent\" id=\"introtext_show\">\r\n\t<p>\r\n\t\t<em><strong>Warning!</strong></em></p>\r\n\r\n\t<p>\r\n\t\t<em><strong>There are no stickers in Belgium. Only use official&nbsp;websites to register for LEZs or other schemes. From the city, registration&nbsp;is free, and day pases are much cheaper than they are from other websites.</strong></em></p>\r\n\r\n\t<p>\r\n\t\tGent has an access regulation in place and <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/gent-ghent\">a low emission zone</a> will be implemented in 2020.</p>\r\n</div>\r\n",
            "cityname": "Gent - Limited Traffic Zone",
            "city_latitude": "51.05",
            "city_longitude": "3.72",
            "scheme_color": "3"
        },
        {
            "id": "879",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/paris-lorry-ban",
            "introtext": "There is an access regulation in place in Paris concerning HGV (heavy goods vehicles) over 7.5 tonnes.<br>\r\nThere is also an <a title=\"LEZ\"  href=\"/countries-mainmenu-147/france/paris\">LEZ</a> in place in Paris and <a title=\"Emergency Air Quality Scheme\" href=\"/countries-mainmenu-147/france/paris-odd-even-scheme\">Emergency Scheme</a> in operation at times of very high air pollution.",
            "cityname": "Paris - Lorry Ban",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "3"
        },
        {
            "id": "880",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/london-coaches-ar",
            "introtext": "UK-LO",
            "cityname": "London Coaches - AR",
            "city_latitude": "51.51",
            "city_longitude": "-0.13",
            "scheme_color": "3"
        },
        {
            "id": "887",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/bonn-ar",
            "introtext": "Bonn also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/bonn\">Low Emission Zone</a> in place.",
            "cityname": "Bonn - Transit Ban",
            "city_latitude": "50.73",
            "city_longitude": "7.10",
            "scheme_color": "3"
        },
        {
            "id": "884",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/bulgaria/sofia-ar",
            "introtext": "At certain times vehicles >4 tonnes and >15 tonnes are not allowed to enter the city centre of Sofia.",
            "cityname": "Sofia - Lorry Ban",
            "city_latitude": "42.69",
            "city_longitude": "23.32",
            "scheme_color": "3"
        },
        {
            "id": "886",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/bologna",
            "introtext": "The Access Regulation (ZTL) of the Historical Center, is a wide area within the historic center of Bologna. The Access Regulation includes the ZTL T AREA and Universita which have more restrictive times.<br><br>\r\n\r\nThere is also an LEZ in place in <a title=\"Bologna\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/bologna\">Bologna</a>.",
            "cityname": "Bologna - ZTL / LEZ",
            "city_latitude": "44.49",
            "city_longitude": "11.32",
            "scheme_color": "3"
        },
        {
            "id": "890",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/hannover-ar",
            "introtext": "Hannover also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/hannover\">Low Emission Zone</a> in place.",
            "cityname": "Hannover - Transit Ban",
            "city_latitude": "52.37",
            "city_longitude": "9.73",
            "scheme_color": "3"
        },
        {
            "id": "891",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/leipzig-ar",
            "introtext": "Leipzig also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/leipzig\">Low Emission Zone</a> in place.",
            "cityname": "Leipzig - Transit Ban",
            "city_latitude": "51.33",
            "city_longitude": "12.37",
            "scheme_color": "3"
        },
        {
            "id": "892",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/leonberg-ditzingen-ar",
            "introtext": "Leonberg-Ditzingen also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/leonberg\">Low Emission Zone</a> in place.",
            "cityname": "Leonberg-Ditzingen - Transit Ban",
            "city_latitude": "48.79",
            "city_longitude": "9.00",
            "scheme_color": "3"
        },
        {
            "id": "893",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim-ar",
            "introtext": "Pleidelsheim also has an LEZ in place in <a title=\"Pleidelsheim\"  href=\"/countries-mainmenu-147/germany-mainmenu-61/pleidelsheim\">Pleidelsheim</a>.",
            "cityname": "Pleidelsheim - Transit Ban",
            "city_latitude": "48.96",
            "city_longitude": "9.2",
            "scheme_color": "3"
        },
        {
            "id": "894",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/muenchen-munich-ar",
            "introtext": "München also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/munchen\">Low Emission Zone</a> in place.",
            "cityname": "München (Munich) - Transit Ban",
            "city_latitude": "48.14",
            "city_longitude": "11.57",
            "scheme_color": "3"
        },
        {
            "id": "896",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/markgröningen-ar",
            "introtext": "There is also an Low Emission Zone in place in <a title=\"Markgröningen\"  href=\"/countries-mainmenu-147/germany-mainmenu-61/markgroningen\">Markgröningen</a>.\r\n",
            "cityname": "Markgröningen - Transit Ban",
            "city_latitude": "48.90",
            "city_longitude": "9.08",
            "scheme_color": "3"
        },
        {
            "id": "897",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/stuttgart-ar",
            "introtext": "<p>Stuttgart has a transit ban for lorries &gt;3.5 tonnes in place.</p>\n\n<p>Stuttgart also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/stuttgart\">Low Emission Zone</a> in place.</p>\n",
            "cityname": "Stuttgart - Transit Ban",
            "city_latitude": "48.78",
            "city_longitude": "9.18",
            "scheme_color": "3"
        },
        {
            "id": "898",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/ulm-ar",
            "introtext": "Ulm also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/ulm\">Low Emission Zone</a> in place.",
            "cityname": "Ulm - Transit Ban",
            "city_latitude": "48.40",
            "city_longitude": "9.99",
            "scheme_color": "3"
        },
        {
            "id": "1191",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/imola-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Imola covers part of the historic center.<br>There is also a Low Emission Zone in <a title=\"Imola\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/imola\">Imola</a>.\r\n<br><br>\r\n<p>\r\n\tEmilia - Romagna, Lomardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Imola - Limited Traffic Zone",
            "city_latitude": "44.35",
            "city_longitude": "11.72",
            "scheme_color": "3"
        },
        {
            "id": "926",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/abruzzo-region/chieti-ar",
            "introtext": "There are 7 Access Regulations (ZTL) in place in Chieti:<br>\n-\tZTL A (Santa Maria) <br>\n-\tZTL B1 (St. Justin): <br>\n-\tZTL B2 (Piazza Malta) <br>\n-\tZTL B3 (Corso Marruccino) <br>\n-\tZTLB4 (S. Gaetano) <br>\n-\tZTL C (S. Maddalena) <br>\n-\tZTL D (Civitella)\n",
            "cityname": "Chieti - Limited Traffic Zone",
            "city_latitude": "42.35",
            "city_longitude": "14.17",
            "scheme_color": "3"
        },
        {
            "id": "927",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/abruzzo-region/sulmona-ar",
            "introtext": "There are 3 Access Regulations (ZTL) in place in Sulmona:<br>\n- Zone 1: the area between Porta Napoli and Piazza del Carmine; <br>\n- Zona 2: the area between Piazza del Carmine and Via De Nino<br>\n- Zona 3: the area between Piazza SS. Annunziata and Piazza Carlo Tresca\n\n",
            "cityname": "Sulmona - Limited Traffic Zone",
            "city_latitude": "42.05",
            "city_longitude": "13.93",
            "scheme_color": "3"
        },
        {
            "id": "928",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/basilicata-region/potenza-access-regulation",
            "introtext": "The Access Regulation (ZTL) in Potenza covers a big part of the historic center. The boundary in the South is via del Popolo and in the North is via Giuseppe Mazzin.\n",
            "cityname": "Potenza - Limited Traffic Zone",
            "city_latitude": "40.64",
            "city_longitude": "15.80",
            "scheme_color": "3"
        },
        {
            "id": "929",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/basilicata-region/melfi-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Melfi covers part of the historic center. The boundaries are the following streets. Via Gianbattista Ronca, vicolo dell'Armonia, corso Garibaldi, strada Vittorio Emanuele.",
            "cityname": "Melfi - Limited Traffic Zone",
            "city_latitude": "41.00",
            "city_longitude": "15.66",
            "scheme_color": "3"
        },
        {
            "id": "930",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/basilicata-region/matera-access-regulation",
            "introtext": "Three Access Regulations (ZTL) are covering the historic center of Mantera:<br>\n\nZona Verde (green zone) – Historic center<br>\nZona Azurra (blue zone) - Area Duomo / Via San Biagio<br>\nZona Gialla (yellow zone) - Area Sassi \n",
            "cityname": "Matera - Limited Traffic Zone",
            "city_latitude": "40.67",
            "city_longitude": "16.60",
            "scheme_color": "3"
        },
        {
            "id": "931",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/calabria-region/cariati-ar",
            "introtext": "The Access Regulation (ZTL) of Cariati covers the entire area of the historic center.\n",
            "cityname": "Cariati - Limited Traffic Zone",
            "city_latitude": "39.49",
            "city_longitude": "16.96",
            "scheme_color": "3"
        },
        {
            "id": "932",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/calabria-region/tropea-ar",
            "introtext": "The Access Regulation (ZTL) of Tropea covers part of the historic center.<br>\nSince 2013 a summer ZTL exists.",
            "cityname": "Tropea - Limited Traffic Zone",
            "city_latitude": "38.68",
            "city_longitude": "15.89",
            "scheme_color": "3"
        },
        {
            "id": "987",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/mantova-ar",
            "introtext": "The Access Regulation (ZTL) of Mantova covers a large part of the historic center. The ZTL is divided in ZTL A, B, N, U, Libertà and Trieste-Garibaldi.<br>\r\nThere is also a Low Emission Zone in <a title=\"Mantova\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/mantova\">Mantova</a>.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Mantova - Limited Traffic Zone",
            "city_latitude": "45.16",
            "city_longitude": "10.80",
            "scheme_color": "3"
        },
        {
            "id": "944",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/cesena-ar",
            "introtext": "<p>\r\n\tThe city centre of Cesena has XX different access regulations (ZTLs):</p>\r\n\r\n<p>\r\n\tZTL A, B and C.</p>\r\n\r\n<p>\r\n\tThere is also an LEZ in <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/cesena\" title=\"Cesena\">Cesena</a>.</p>\r\n",
            "cityname": "Cesena - Limited Traffic Zone",
            "city_latitude": "44.13",
            "city_longitude": "12.23",
            "scheme_color": "3"
        },
        {
            "id": "943",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/cervia-ar",
            "introtext": "There are three Access Regulations (ZTL) in Cervia:<br>\n- ZTL Centro<br>\n- ZTL Porto Canale<br>\n- ZTL Milano Marittima",
            "cityname": "Cervia - Limited Traffic Zone",
            "city_latitude": "44.26",
            "city_longitude": "12.35",
            "scheme_color": "3"
        },
        {
            "id": "946",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ferrara-ar",
            "introtext": "There are four Access Regulations (ZTL) in Ferrara:<br>\r\n- ZTL Duomo<br>\r\n- ZTL Garibaldi<br>\r\n- ZTL Medioevale<br>\r\n- ZTL conte Ercole I d'Este<br><br>There is also an LEZ in place in <a title=\"Ferrara\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ferrara\">Ferrara</a>.\r\n<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Ferrara - Limited Traffic Zone",
            "city_latitude": "44.50",
            "city_longitude": "11.37",
            "scheme_color": "3"
        },
        {
            "id": "947",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/modena-ar",
            "introtext": "The Access Regulation (ZTL) of Modena covers part of the historic center.\r\n\r\n<br>There is also an access regulation in place called <a title=\"Modena\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/modena\">Modena</a>.\r\nEmilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>\r\n",
            "cityname": "Modena - Limited Traffic Zone",
            "city_latitude": "44.64",
            "city_longitude": "10.92",
            "scheme_color": "3"
        },
        {
            "id": "948",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/parma-ar",
            "introtext": "The Access Regulation (ZTL) of Parma covers a large part of the historic center.\r\n<br>There is also an access regulation in place called <a title=\"Parma\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/parma\">Parma</a>.Emilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>\r\n",
            "cityname": "Parma - Limited Traffic Zone",
            "city_latitude": "44.80",
            "city_longitude": "10.33",
            "scheme_color": "3"
        },
        {
            "id": "950",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ravenna-ar",
            "introtext": "The Access Regulation (ZTL) of Ravenna covers a large area of the historic center.<br>There is also a low emission zone in place called <a title=\"Ravenna\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/ravenna\">Ravenna</a>.<br>Emilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>\r\n",
            "cityname": "Ravenna - Limited Traffic Zone",
            "city_latitude": "44.42",
            "city_longitude": "12.20",
            "scheme_color": "3"
        },
        {
            "id": "951",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/reggio-emilia-ar",
            "introtext": "The Access Regulation (ZTL) of Reggio Emilia covers a large area of the historic center.<br>\r\nThe LTZ Reggio Emilia is traversable in the direction west - south using Via Garibaldi and Via Ariosto.<br>\r\nThere is also a low emission zone in place called <a title=\"Reggio Emilia\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/reggio-emilia \">Reggio Emilia</a>.<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Reggio Emilia - Limited Traffic Zone",
            "city_latitude": "44.70",
            "city_longitude": "10.63",
            "scheme_color": "3"
        },
        {
            "id": "952",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/rimini-ar",
            "introtext": "The Access Regulation (ZTL) of Rimini is divided in two areas: <br>\r\n- Centro Storico<br>\r\n- Borgo San Giuliano<br><br>There is also a Low Emission Zone in <a title=\"Rimini\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/rimini\">Rimini</a>.<br>Emilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Rimini - Limited Traffic Zone",
            "city_latitude": "44.05",
            "city_longitude": "12.57",
            "scheme_color": "3"
        },
        {
            "id": "953",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/santarcangelo-di-romagna-ar",
            "introtext": "The Access Regulation (ZTL) of Santarcangelo di Romagna is divided in four areas: <br>\nZona A, B, C, and D.",
            "cityname": "Santarcangelo di Romagna - Limited Traffic Zone",
            "city_latitude": "44.06",
            "city_longitude": "12.45",
            "scheme_color": "3"
        },
        {
            "id": "954",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/sassuolo-ar",
            "introtext": "The Access Regulation (ZTL) of Sassuolo is divided in two areas: <br>\r\nZTL 1 and 2. <br><br>\r\n<p>\r\n\tThere is also a low emission zone in <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/sassuolo\" target=\"_blank\">Sassuolo</a>.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Sassuolo - Limited Traffic Zone",
            "city_latitude": "44.55",
            "city_longitude": "10.78",
            "scheme_color": "3"
        },
        {
            "id": "955",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/friuli-venezia-giulia-region/monfalcone-ar",
            "introtext": "The Access Regulation (ZTL) of Monfalcone is divided in six areas: <br>\r\nZTL A, B, C, E, H and I.",
            "cityname": "Monfalcone - Limited Traffic Zone",
            "city_latitude": "45.80",
            "city_longitude": "13.53",
            "scheme_color": "3"
        },
        {
            "id": "956",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/ariccia-ar",
            "introtext": "The Access Regulation (ZTL) of Ariccia covers part of the historic center.",
            "cityname": "Ariccia - Limited Traffic Zone",
            "city_latitude": "41.72",
            "city_longitude": "12.67",
            "scheme_color": "3"
        },
        {
            "id": "957",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/bracciano-ar",
            "introtext": "The Access Regulation (ZTL) of Bracciano covers part of the historic center.",
            "cityname": "Bracciano - Limited Traffic Zone",
            "city_latitude": "42.08",
            "city_longitude": "12.21",
            "scheme_color": "3"
        },
        {
            "id": "958",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/gaeta-ar",
            "introtext": "The Access Regulation (ZTL) of Gaeta covers part of the historic center with two ZTL:<br>\nZTL A and B.",
            "cityname": "Gaeta - Limited Traffic Zone",
            "city_latitude": "41.21",
            "city_longitude": "13.57",
            "scheme_color": "3"
        },
        {
            "id": "959",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/piglio-ar",
            "introtext": "The Access Regulation (ZTL) of Piglio covers the entire historic center.",
            "cityname": "Piglio - Limited Traffic Zone",
            "city_latitude": "43.40",
            "city_longitude": "11.85",
            "scheme_color": "3"
        },
        {
            "id": "960",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/rieti-ar",
            "introtext": "The Access Regulation (ZTL) of Rieti covers part of the historic center.",
            "cityname": "Rieti - Limited Traffic Zone",
            "city_latitude": "42.40",
            "city_longitude": "12.85",
            "scheme_color": "3"
        },
        {
            "id": "961",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/tivoli-ar",
            "introtext": "The Access Regulation (ZTL) of Tivoli covers part of the historic center and is divided in two parts:<br>\r\n\r\n- ZTL Trevio S.Croce<br>\r\n- ZTL Centro storico medioevale\r\n",
            "cityname": "Tivoli - Limited Traffic Zone",
            "city_latitude": "41.95",
            "city_longitude": "12.80",
            "scheme_color": "3"
        },
        {
            "id": "962",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/ameglia-ar",
            "introtext": "The Access Regulation (ZTL) of Ameglia consists of the final stretch of Via Fabbricotti.",
            "cityname": "Ameglia - Limited Traffic Zone",
            "city_latitude": "44.06",
            "city_longitude": "9.97",
            "scheme_color": "3"
        },
        {
            "id": "963",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/borghetto-santo-spirito-ar",
            "introtext": "The Access Regulation (ZTL) of Borghetto Santo Spirito  currently affects the residential stretch of:Lungomare G.Matteotti, Via Duca degli Abruzzi, Molo Marinai d’Italia, Molo Rosa dei Venti, Lungomare Walter Tobagi. \n",
            "cityname": "Borghetto Santo Spirito - Limited Traffic Zone",
            "city_latitude": "44.10",
            "city_longitude": "8.24",
            "scheme_color": "3"
        },
        {
            "id": "964",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/finale-ligure-ar",
            "introtext": "The Access Regulation (ZTL) of Finale Ligure consists of the following parts: Finalborgo,Finalmarina, \nVarigotti. \nThere are three ZTL in Finale Ligure:<br>\n- Finalborgo<br>\n- Finalmarina<br>\n- Varigotti ",
            "cityname": "Finale Ligure - Limited Traffic Zone",
            "city_latitude": "44.17",
            "city_longitude": "8.34",
            "scheme_color": "3"
        },
        {
            "id": "965",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/lerici-ar",
            "introtext": "The Access Regulation (ZTL) of Lerici covers part of the towns Lerici and San Terenzo.",
            "cityname": "Lerici - Limited Traffic Zone",
            "city_latitude": "44.08",
            "city_longitude": "9.92",
            "scheme_color": "3"
        },
        {
            "id": "966",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/levanto-ar",
            "introtext": "The Access Regulation (ZTL) of Levanto covers part of the historic center.",
            "cityname": "Levanto - Limited Traffic Zone",
            "city_latitude": "44.17",
            "city_longitude": "9.61",
            "scheme_color": "3"
        },
        {
            "id": "967",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/sarzana-ar",
            "introtext": "The Access Regulation (ZTL) of Sarzana covers part of the historic center.",
            "cityname": "Sarzana - Limited Traffic Zone",
            "city_latitude": "44.11",
            "city_longitude": "9.96",
            "scheme_color": "3"
        },
        {
            "id": "968",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/sestri-levante-ar",
            "introtext": "The Access Regulation (ZTL) of Sestri Levante consists of five TZLs:<br>\n- Zona Blu<br>\n- Zona Baia<br>\n- Zona B<br>\n- Zona Riva<br>\n- Zona Rena",
            "cityname": "Sestri Levante - Limited Traffic Zone",
            "city_latitude": "44.27",
            "city_longitude": "9.41",
            "scheme_color": "3"
        },
        {
            "id": "969",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/spotorno-ar",
            "introtext": "The Access Regulation (ZTL) of Spotorno covers mainly Via Garibaldi, Via Mazzini, Via Cavour and Via XXV Aprile.",
            "cityname": "Spotorno - Limited Traffic Zone",
            "city_latitude": "44.23",
            "city_longitude": "8.42",
            "scheme_color": "3"
        },
        {
            "id": "970",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/albino-ar",
            "introtext": "The Access Regulation (ZTL) of Albino covers Via Mazzini, Via Sant’Anna, Via Vittorio Veneto, Via Gasparini and Piazza della Libertà.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Albino - Limited Traffic Zone",
            "city_latitude": "45.76",
            "city_longitude": "9.80",
            "scheme_color": "3"
        },
        {
            "id": "971",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/bariano-ar",
            "introtext": "The Access Regulation (ZTL) of Bariano covers part of the historic center.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Bariano - Limited Traffic Zone",
            "city_latitude": "45.51",
            "city_longitude": "9.70",
            "scheme_color": "3"
        },
        {
            "id": "972",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/bellagio-ar",
            "introtext": "The Access Regulation (ZTL) of Bellagio covers part of the historic center.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Bellagio - Limited Traffic Zone",
            "city_latitude": "45.99",
            "city_longitude": "9.26",
            "scheme_color": "3"
        },
        {
            "id": "973",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/brescia-ar",
            "introtext": "The Access Regulation (ZTL) in Brescia covers a part of the historic center.<br><br>There is also a Low Emission Zone in <a title=\"Brescia\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia\r\n/brescia\">Brescia</a>.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Brescia - Limited Traffic Zone",
            "city_latitude": "45.70",
            "city_longitude": "9.67",
            "scheme_color": "3"
        },
        {
            "id": "974",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/bergamo-ar",
            "introtext": "The Access Regulation (ZTL) in Bergamo covers a part of the historic center.<br>\r\nThe ZTL is divided in 16 different ZTL.<br><br>There is also an LEZ in place in <a title=\"Bergamo\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/Bergamo\">Bergamo</a>.\r\n<p><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<br />\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Bergamo - Limited Traffic Zone",
            "city_latitude": "45.70",
            "city_longitude": "9.67",
            "scheme_color": "3"
        },
        {
            "id": "975",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/busto-arsizio-ar",
            "introtext": "The Access Regulation (ZTL) in Busto Arsizio covers a part of the historic center.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p><p>\r\n\t<br />\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>\r\n",
            "cityname": "Busto Arsizio - Limited Traffic Zone",
            "city_latitude": "45.61",
            "city_longitude": "8.85",
            "scheme_color": "3"
        },
        {
            "id": "976",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/cernusco-sul-naviglio-ar",
            "introtext": "The Access Regulation (ZTL) in Cernusco sul Naviglio covers a part of the historic center.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p><br />\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>",
            "cityname": "Cernusco sul Naviglio - Limited Traffic Zone",
            "city_latitude": "45.53",
            "city_longitude": "9.33",
            "scheme_color": "3"
        },
        {
            "id": "977",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/como-ar",
            "introtext": "Como has an Access Regulation (ZTL) in place which is divided in four parts. The ZTL covers part of the historic center.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p><br />\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>",
            "cityname": "Como - Limited Traffic Zone",
            "city_latitude": "45.80",
            "city_longitude": "9.08",
            "scheme_color": "3"
        },
        {
            "id": "978",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/concorezzo-ar",
            "introtext": "The Access Regulation (ZTL) covers a small part of the historic center of Concorezzo: Via Libertà, Via De Capitani and Via Chiesa.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Concorezzo - Limited Traffic Zone",
            "city_latitude": "45.59",
            "city_longitude": "9.34",
            "scheme_color": "3"
        },
        {
            "id": "979",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/corsico-ar",
            "introtext": "Two streets in Corsico are covered by the Access Regulation (ZTL).<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.<p/> <br>\r\n\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Corsico - Limited Traffic Zone",
            "city_latitude": "45.43",
            "city_longitude": "9.11",
            "scheme_color": "3"
        },
        {
            "id": "980",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/cremona-ar",
            "introtext": "The Access Regulation (ZTL) in Cremona covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Cremona\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/cremona\">Cremona</a>.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p> <br>\r\n\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Cremona - Limited Traffic Zone",
            "city_latitude": "45.13",
            "city_longitude": "10.03",
            "scheme_color": "3"
        },
        {
            "id": "981",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/curtatone-ztl",
            "introtext": "The Access Regulation (ZTL) of Curtatone covers part of the historic center.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Curtatone - Limited Traffic Zone",
            "city_latitude": "43.45",
            "city_longitude": "11.87",
            "scheme_color": "3"
        },
        {
            "id": "982",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/gallarate-ar",
            "introtext": "The Access Regulation (ZTL) of Gallarate covers part of the historic center and is divided in four parts:\r\nZTL centrale, ZTL Via Manzoni, ZTL Vicolo Volpe and ZTL Via Sciarè.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p><br />\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>",
            "cityname": "Gallarate - Limited Traffic Zone",
            "city_latitude": "45.66",
            "city_longitude": "8.79",
            "scheme_color": "3"
        },
        {
            "id": "983",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lecco-ar",
            "introtext": "The Access Regulation (ZTL) of Lecco covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Lecco\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/lecco\">Lecco</a>.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p><br>\r\n\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Lecco - Limited Traffic Zone",
            "city_latitude": "45.85",
            "city_longitude": "9.38",
            "scheme_color": "3"
        },
        {
            "id": "984",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lodi-ar",
            "introtext": "The Access Regulation (ZTL) of Lodi covers part of the historic center.<br>\r\nThere is also a Low Emission Zone in <a title=\"Lodi\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/lodi\">Lodi</a>.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Lodi - Limited Traffic Zone",
            "city_latitude": "45.31",
            "city_longitude": "9.50",
            "scheme_color": "3"
        },
        {
            "id": "985",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lovere-ar",
            "introtext": "The Access Regulation (ZTL) of Lovere covers part of the historic center.\n<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Lovere - Limited Traffic Zone",
            "city_latitude": "45.80",
            "city_longitude": "10.06",
            "scheme_color": "3"
        },
        {
            "id": "986",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/malgrate-access-regulation",
            "introtext": "The Access Regulation (ZTL) in Malgrate covers Via Scatti  and Via S. Dionigi/Reina.Access Regulation (ZTL).<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Malgrate - Limited Traffic Zone",
            "city_latitude": "45.84",
            "city_longitude": "9.37",
            "scheme_color": "3"
        },
        {
            "id": "989",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/mede-ar",
            "introtext": "The Access Regulation (ZTL) in Mede covers a small part of the historic center.\n<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Mede - Limited Traffic Zone",
            "city_latitude": "45.10",
            "city_longitude": "8.74",
            "scheme_color": "3"
        },
        {
            "id": "990",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/mediglia-ar",
            "introtext": "The Access Regulation (ZTL) of Mediglia consists of Martiri della Libertà, Piazza Giovanni XXIII, Via Di Vittorio, Via Miglioli, Via Lizzadri, Via Europa and Strada Comunale Triginto/Bustighera.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Mediglia - Limited Traffic Zone",
            "city_latitude": "45.39",
            "city_longitude": "9.33",
            "scheme_color": "3"
        },
        {
            "id": "991",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/melegnano-ar\n",
            "introtext": "The Access Regulation (ZTL) of Melegnano covers a small part of the historic center.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Melegnano - Limited Traffic Zone",
            "city_latitude": "45.36",
            "city_longitude": "9.32",
            "scheme_color": "3"
        },
        {
            "id": "992",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/melzo-ar",
            "introtext": "The Access Regulation (ZTL) of Melzo covers a small part of the historic center and is divided in a red and a blue area.<br>\nThe red area covers piazza san Francesco, via Matteotti, piazza Vittorio Emanuele II, via A. Pasta, piazza della Repubblica, via Candiani, via Cattaneo, via Sant’Ambrogio, piazza della Vittoria, via Bianchi.<br>\nThe blue area covers via A. Villa,   via Sant’Alessandro, via Montello,  piazza Garibaldi, via Magenta, via Bianchi, piazza della Vittoria al civico n°1.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Melzo - Limited Traffic Zone",
            "city_latitude": "45.50",
            "city_longitude": "9.43",
            "scheme_color": "3"
        },
        {
            "id": "1011",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/london",
            "introtext": "UK-LO",
            "cityname": "London Safer Lorry Scheme",
            "city_latitude": "51.51",
            "city_longitude": "-0.13",
            "scheme_color": "3"
        },
        {
            "id": "1013",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/darmstadt-ar",
            "introtext": "Darmstadt also has a Low Emission Zone, see <a title=\"Darmstadt\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/darmstadt\">Darmstadt</a>.<br>\r\nThe transit ban in \r\n<a title=\"Roßdorf\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/rossdorf-ar\">Roßdorf</a> is also relevant for Darmstadt - AR.",
            "cityname": "Darmstadt - Transit Ban",
            "city_latitude": "50.08",
            "city_longitude": "8.24",
            "scheme_color": "3"
        },
        {
            "id": "1016",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/monza-ar",
            "introtext": "The Access Regulation (ZTL) of Monza covers a part of the historic center.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Monza - Limited Traffic Zone",
            "city_latitude": "45.58",
            "city_longitude": "9.27",
            "scheme_color": "3"
        },
        {
            "id": "1017",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/oggiono-ar",
            "introtext": "The Access Regulation (ZTL) of Oggiono covers a part of the historic center. <p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Oggiono - Limited Traffic Zone",
            "city_latitude": "45.79",
            "city_longitude": "9.35",
            "scheme_color": "3"
        },
        {
            "id": "1018",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/paullo-ar",
            "introtext": "The Access Regulation (ZTL) of Paullo covers all of the historic center.\n<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Paullo - Limited Traffic Zone",
            "city_latitude": "45.42",
            "city_longitude": "9.41",
            "scheme_color": "3"
        },
        {
            "id": "1019",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/pavia-ar",
            "introtext": "The Access Regulation (ZTL) of Pavia covers a part of the historic center.<br>\r\nThere is also an LEZ in place in <a title=\"Pavia\" href=\"/countries-mainmenu-147/italy-mainmenu-81/lombardia/pavia\">Pavia</a>.<p><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Pavia - Limited Traffic Zone",
            "city_latitude": "45.19",
            "city_longitude": "9.16",
            "scheme_color": "3"
        },
        {
            "id": "1020",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/peschiera-borromeo-ar",
            "introtext": "The Access Regulation (ZTL) of Peschiera Borromeo covers a part of the historic center.<br><br>\nThis ZTL is not working from 01.01.2015 to 30.06.2015.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Peschiera Borromeo - Limited Traffic Zone",
            "city_latitude": "45.44",
            "city_longitude": "9.30",
            "scheme_color": "3"
        },
        {
            "id": "1094",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/grosseto-ar",
            "introtext": "The Access Regulation (ZTL) of Grosseto covers part of the historic center.",
            "cityname": "Grosseto - Limited Traffic Zone",
            "city_latitude": "43.72",
            "city_longitude": "10.95",
            "scheme_color": "3"
        },
        {
            "id": "1082",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/cascina-ar",
            "introtext": "The Access Regulation (ZTL) of Cascina covers part of the historic center.",
            "cityname": "Cascina - Limited Traffic Zone",
            "city_latitude": "43.68",
            "city_longitude": "10.56",
            "scheme_color": "3"
        },
        {
            "id": "1236",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/salzburg-ar",
            "introtext": "Salzburg has installed an access regulation for part of the historic center.<br>\nThe access regulation is enforced with rectable bollards.",
            "cityname": "Salzburg - pedestrian",
            "city_latitude": "47.81",
            "city_longitude": "13.06",
            "scheme_color": "3"
        },
        {
            "id": "1023",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/saronno-ar",
            "introtext": "The Access Regulation (ZTL) of Saronno covers part of the historic center.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Saronno - Limited Traffic Zone",
            "city_latitude": "45.62",
            "city_longitude": "9.04",
            "scheme_color": "3"
        },
        {
            "id": "1024",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/seregno-ar",
            "introtext": "The Access Regulation (ZTL) of Seregno covers part of the historic center.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Seregno - Limited Traffic Zone",
            "city_latitude": "45.65",
            "city_longitude": "9.21",
            "scheme_color": "3"
        },
        {
            "id": "1025",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/sesto-calende-ar",
            "introtext": "The Access Regulation (ZTL) of Sesto Calende covers part of the historic center.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Sesto Calende - Limited Traffic Zone",
            "city_latitude": "45.73",
            "city_longitude": "8.64",
            "scheme_color": "3"
        },
        {
            "id": "1026",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/sondrio-ar",
            "introtext": "The Access Regulation (ZTL) of Sondrio covers part of the historic center.\n<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Sondrio - Limited Traffic Zone",
            "city_latitude": "46.17",
            "city_longitude": "9.80",
            "scheme_color": "3"
        },
        {
            "id": "1027",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/spino-d-adda-ar",
            "introtext": "The Access Regulation (ZTL) of Spino d'Adda covers part of the historic center.<p><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p>",
            "cityname": "Spino d Adda - Limited Traffic Zone",
            "city_latitude": "45.40",
            "city_longitude": "9.49",
            "scheme_color": "3"
        },
        {
            "id": "1028",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/treviglio-ar",
            "introtext": "The Access Regulation (ZTL) of Treviglio covers part of the historic center.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Treviglio - Limited Traffic Zone",
            "city_latitude": "45.52",
            "city_longitude": "9.60",
            "scheme_color": "3"
        },
        {
            "id": "1029",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/vizzolo-predabissi-ar",
            "introtext": "The Access Regulation (ZTL) of Vizzolo Predabissi covers part of the historic center to avoid crossing traffic.<p><br><br>\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\n\n<p>\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\n\n<p>",
            "cityname": "Vizzolo Predabissi - Limited Traffic Zone",
            "city_latitude": "45.36",
            "city_longitude": "9.35",
            "scheme_color": "3"
        },
        {
            "id": "1030",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/jesi-ar",
            "introtext": "The Access Regulation (ZTL) of Jesi covers part of the historic center and is diveded in three zones:<br>\nZTL Corso Matteotti<br>\nZTL Pergolesi<br>\nZTL San Pietro ",
            "cityname": "Jesi - Limited Traffic Zone",
            "city_latitude": "43.53",
            "city_longitude": "13.25",
            "scheme_color": "3"
        },
        {
            "id": "1031",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/macerata-ar",
            "introtext": "The Access Regulation (ZTL) of Macerata covers part of the historic center. ",
            "cityname": "Macerata - Limited Traffic Zone",
            "city_latitude": "43.30",
            "city_longitude": "13.45",
            "scheme_color": "3"
        },
        {
            "id": "1032",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/numana-ar",
            "introtext": "The Access Regulation (ZTL) of Numana covers part of the historic center and is diveded in ZTL A and ZTL B.",
            "cityname": "Numana - Limited Traffic Zone",
            "city_latitude": "43.51",
            "city_longitude": "13.62",
            "scheme_color": "3"
        },
        {
            "id": "1033",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/pesaro-ar",
            "introtext": "The Access Regulation (ZTL) of Pesaro covers part of the historic center.",
            "cityname": "Pesaro - Limited Traffic Zone",
            "city_latitude": "43.91",
            "city_longitude": "12.91",
            "scheme_color": "3"
        },
        {
            "id": "1034",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/senigallia-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Senigallia covers part of the historic center.",
            "cityname": "Senigallia - Limited Traffic Zone",
            "city_latitude": "43.72",
            "city_longitude": "13.22",
            "scheme_color": "3"
        },
        {
            "id": "1035",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/urbino-ar",
            "introtext": "The Access Regulation (ZTL) of Urbino covers the historic center.",
            "cityname": "Urbino - Limited Traffic Zone",
            "city_latitude": "43.73",
            "city_longitude": "12.64",
            "scheme_color": "3"
        },
        {
            "id": "1036",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/molise-region/termoli-ar",
            "introtext": "The Access Regulation (ZTL) of Termoli covers part of the historic center.",
            "cityname": "Termoli - Limited Traffic Zone",
            "city_latitude": "42.00",
            "city_longitude": "15.00",
            "scheme_color": "3"
        },
        {
            "id": "1037",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/arona-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Arona covers part of the historic center and is divided in four zones: yellow, red, green and blue zone.",
            "cityname": "Arona - Limited Traffic Zone",
            "city_latitude": "43.47",
            "city_longitude": "12.23",
            "scheme_color": "3"
        },
        {
            "id": "1038",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/asti-access-regulation",
            "introtext": "There is also a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/asti\">Low Emission Zone</a> in place in Asti.<br>The Access Regulation (ZTL) of Asti covers part of the historic center.<br>\n<p>\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\n",
            "cityname": "Asti - Limited Traffic Zone",
            "city_latitude": "44.90",
            "city_longitude": "8.21",
            "scheme_color": "3"
        },
        {
            "id": "1039",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/bardonecchia-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Bardonecchia covers part of the historic center.",
            "cityname": "Bardonecchia - Limited Traffic Zone",
            "city_latitude": "45.07",
            "city_longitude": "6.70",
            "scheme_color": "3"
        },
        {
            "id": "1069",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sardegna-region/cagliari-ar",
            "introtext": "The Access Regulation (ZTL) of Cagliari covers part of the historic center and is divided in six areas:<br>\r\n-ZTL Castello<br>\r\n-ZTL Marina<br>\r\n-ZTL Poetto<br>\r\n-ZTL Stampace alto<br>\r\n-ZTL Stampace basso<br>\r\n-ZTL Villanova",
            "cityname": "Cagliari - Limited Traffic Zone",
            "city_latitude": "39.22",
            "city_longitude": "9.12",
            "scheme_color": "3"
        },
        {
            "id": "1040",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/biella-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Biella covers part of the historic center and is divided in red, green and blue zone.\r\n<br><br>There is also an LEZ in place in <a title=\"Biella\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/biella\">Biella</a>.<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Biella - Limited Traffic Zone",
            "city_latitude": "45.57",
            "city_longitude": "8.05",
            "scheme_color": "3"
        },
        {
            "id": "1041",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/casale-monferrato-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Casale Monferrato covers part of the historic center. Casale Monferrato also has a Low Emission Zone in place since 18 April 2011.<br><br>There is also an LEZ in place in <a title=\"Casale Monferrrato\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/casale-monferrato\">Casale Monferrato</a>.<br><br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Casale Monferrato - Limited Traffic Zone",
            "city_latitude": "45.13",
            "city_longitude": "8.44",
            "scheme_color": "3"
        },
        {
            "id": "1042",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chieri-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Chieri covers part of the historic center and is divided in three different areas: green, purple and yellow.<br><br>There is also an LEZ in place in <a title=\"Chieri\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chieri\">Chieri</a>.<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Chieri - Limited Traffic Zone",
            "city_latitude": "45.01",
            "city_longitude": "7.82",
            "scheme_color": "3"
        },
        {
            "id": "1043",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chivasso-access-regulation",
            "introtext": "There is also a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/chivasso\">Low Emission Zone</a> in place in Chivasso. <br>The Access Regulation (ZTL) of Chivasso covers part of the historic center and is divided in four different zones: zone A, B, C and D.",
            "cityname": "Chivasso - Limited Traffic Zone",
            "city_latitude": "45.19",
            "city_longitude": "7.89",
            "scheme_color": "3"
        },
        {
            "id": "1047",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novara-ar",
            "introtext": "The Access Regulation (ZTL) of Novara covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Novara\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novara\">Novara</a>.<br><br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Novara - Limited Traffic Zone",
            "city_latitude": "45.44",
            "city_longitude": "8.62",
            "scheme_color": "3"
        },
        {
            "id": "1048",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novi-ligure-ar",
            "introtext": "The Access Regulation (ZTL) of Novi Ligure covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Novi Ligure\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/novi-ligure\">Novi Ligure</a>.",
            "cityname": "Novi Ligure - Limited Traffic Zone",
            "city_latitude": "44.77",
            "city_longitude": "8.78",
            "scheme_color": "3"
        },
        {
            "id": "1049",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/orta-san-giulio-ar",
            "introtext": "The Access Regulation (ZTL) of Orta San Giulio covers part of the historic center.",
            "cityname": "Orta San Giulio - Limited Traffic Zone",
            "city_latitude": "45.80",
            "city_longitude": "8.42",
            "scheme_color": "3"
        },
        {
            "id": "1050",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pinerolo-ar",
            "introtext": "There is also a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/pinerolo\">Low Emission Zone</a> in place.<br> The Access Regulation (ZTL) of Pinerolo covers part of the historic center.\r\n<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Pinerolo - Limited Traffic Zone",
            "city_latitude": "44.88",
            "city_longitude": "7.35",
            "scheme_color": "3"
        },
        {
            "id": "1051",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/sauze-d-oulx-ar",
            "introtext": "The Access Regulation (ZTL) of Sauze d'Oulx covers the historic center.",
            "cityname": "Sauze d Oulx - Limited Traffic Zone",
            "city_latitude": "45.03",
            "city_longitude": "6.86",
            "scheme_color": "3"
        },
        {
            "id": "1052",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vercelli-ar",
            "introtext": "The Access Regulation (ZTL) of Vercelli covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Vercelli\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/vercelli\">Vercelli</a>.<br><br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Vercelli - Limited Traffic Zone",
            "city_latitude": "45.32",
            "city_longitude": "8.42",
            "scheme_color": "3"
        },
        {
            "id": "1053",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/altamura-ar",
            "introtext": "The Access Regulation (ZTL) of Altamura covers part of the historic center.",
            "cityname": "Altamura - Limited Traffic Zone",
            "city_latitude": "40.83",
            "city_longitude": "16.55",
            "scheme_color": "3"
        },
        {
            "id": "1054",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/bari-ar",
            "introtext": "The Access Regulation (ZTL) of Bari covers part of the historic center.",
            "cityname": "Bari - Limited Traffic Zone",
            "city_latitude": "41.12",
            "city_longitude": "16.87",
            "scheme_color": "3"
        },
        {
            "id": "1055",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/barletta-ar",
            "introtext": "The Access Regulation (ZTL) of Barletta covers part of the historic center.",
            "cityname": "Barletta - Limited Traffic Zone",
            "city_latitude": "41.32",
            "city_longitude": "16.28",
            "scheme_color": "3"
        },
        {
            "id": "1056",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/bitonto-ar",
            "introtext": "The Access Regulation (ZTL) of Bitonto covers part of the historic center.",
            "cityname": "Bitonto - Limited Traffic Zone",
            "city_latitude": "41.11",
            "city_longitude": "16.69",
            "scheme_color": "3"
        },
        {
            "id": "1057",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/conversano-ar",
            "introtext": "The Access Regulation (ZTL) of Conversano covers part of the historic center.",
            "cityname": "Conversano - Limited Traffic Zone",
            "city_latitude": "40.97",
            "city_longitude": "17.12",
            "scheme_color": "3"
        },
        {
            "id": "1058",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/corato-ar",
            "introtext": "The Access Regulation (ZTL) of Corato covers part of the historic center.",
            "cityname": "Corato - Limited Traffic Zone",
            "city_latitude": "41.15",
            "city_longitude": "16.41",
            "scheme_color": "3"
        },
        {
            "id": "1059",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/foggia-ar",
            "introtext": "The Access Regulation (ZTL) of Foggia covers part of the historic center.",
            "cityname": "Foggia - Limited Traffic Zone",
            "city_latitude": "41.46",
            "city_longitude": "15.54",
            "scheme_color": "3"
        },
        {
            "id": "1060",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/gallipoli-ar",
            "introtext": "The Access Regulation (ZTL) of Gallipoli covers the peninsula.",
            "cityname": "Gallipoli - Limited Traffic Zone",
            "city_latitude": "40.06",
            "city_longitude": "17.99",
            "scheme_color": "3"
        },
        {
            "id": "1062",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/giovinazzo-ar",
            "introtext": "The Access Regulation (ZTL) of Giovinazzo covers part of the historic center.",
            "cityname": "Giovinazzo - Limited Traffic Zone",
            "city_latitude": "41.19",
            "city_longitude": "16.67",
            "scheme_color": "3"
        },
        {
            "id": "1063",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/lecce-ar",
            "introtext": "The Access Regulation (ZTL) of Lecce covers part of the historic center.",
            "cityname": "Lecce - Limited Traffic Zone",
            "city_latitude": "40.35",
            "city_longitude": "18.18",
            "scheme_color": "3"
        },
        {
            "id": "1064",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/lucera-ar",
            "introtext": "The Access Regulation (ZTL) of Lucera covers part of the historic center.",
            "cityname": "Lucera - Limited Traffic Zone",
            "city_latitude": "41.51",
            "city_longitude": "15.34",
            "scheme_color": "3"
        },
        {
            "id": "1065",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/manfredonia-ar",
            "introtext": "The Access Regulation (ZTL) of Manfredonia covers part of the historic center.",
            "cityname": "Manfredonia - Limited Traffic Zone",
            "city_latitude": "41.63",
            "city_longitude": "15.92",
            "scheme_color": "3"
        },
        {
            "id": "1066",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/san-severo-ar",
            "introtext": "The Access Regulation (ZTL) of San Severo covers part of the historic center.",
            "cityname": "San Severo - Limited Traffic Zone",
            "city_latitude": "41.69",
            "city_longitude": "15.38",
            "scheme_color": "3"
        },
        {
            "id": "1067",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/terlizzi-ar",
            "introtext": "The Access Regulation (ZTL) of Terlizzi covers part of the historic center.",
            "cityname": "Terlizzi - Limited Traffic Zone",
            "city_latitude": "41.13",
            "city_longitude": "16.54",
            "scheme_color": "3"
        },
        {
            "id": "1068",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sardegna-region/alghero-ar",
            "introtext": "The Access Regulation (ZTL) of Alghero covers the entire historic center.",
            "cityname": "Alghero - Limited Traffic Zone",
            "city_latitude": "40.56",
            "city_longitude": "8.32",
            "scheme_color": "3"
        },
        {
            "id": "1070",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sardegna-region/nuoro-ar",
            "introtext": "The Access Regulation (ZTL) of Nuoro covers part of the historic center.",
            "cityname": "Nuoro - Limited Traffic Zone",
            "city_latitude": "40.33",
            "city_longitude": "9.46",
            "scheme_color": "3"
        },
        {
            "id": "1071",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sardegna-region/sassari-ar",
            "introtext": "The Access Regulation (ZTL) of Sassari covers part of the historic center.",
            "cityname": "Sassari - Limited Traffic Zone",
            "city_latitude": "40.80",
            "city_longitude": "8.58",
            "scheme_color": "3"
        },
        {
            "id": "1072",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/agrigento-ar",
            "introtext": "The Access Regulation (ZTL) of Agrigento covers part of the historic center.",
            "cityname": "Agrigento - Limited Traffic Zone",
            "city_latitude": "37.31",
            "city_longitude": "13.58",
            "scheme_color": "3"
        },
        {
            "id": "1073",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/catania-ar",
            "introtext": "The Access Regulation (ZTL) of Catania covers part of the historic center.",
            "cityname": "Catania - Limited Traffic Zone",
            "city_latitude": "37.51",
            "city_longitude": "15.08",
            "scheme_color": "3"
        },
        {
            "id": "1074",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/marsala-ar",
            "introtext": "The Access Regulation (ZTL) of Marsala covers part of the historic center.",
            "cityname": "Marsala - Limited Traffic Zone",
            "city_latitude": "37.80",
            "city_longitude": "12.44",
            "scheme_color": "3"
        },
        {
            "id": "1075",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/ragusa-ar",
            "introtext": "The Access Regulation (ZTL) of Ragusa covers part of the historic center.",
            "cityname": "Ragusa - Limited Traffic Zone",
            "city_latitude": "36.93",
            "city_longitude": "14.71",
            "scheme_color": "3"
        },
        {
            "id": "1076",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/siracusa-ar",
            "introtext": "The Access Regulation (ZTL) of Siracusa covers part of the historic center.",
            "cityname": "Siracusa - Limited Traffic Zone",
            "city_latitude": "37.08",
            "city_longitude": "15.29",
            "scheme_color": "3"
        },
        {
            "id": "1077",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/taormina-ar",
            "introtext": "The Access Regulation (ZTL) of Taormina covers part of the historic center and is divided in zone A, B and C.",
            "cityname": "Taormina - Limited Traffic Zone",
            "city_latitude": "37.85",
            "city_longitude": "15.29",
            "scheme_color": "3"
        },
        {
            "id": "1078",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/altopascio-ar",
            "introtext": "The Access Regulation (ZTL) of Altopascio covers part of the historic center.",
            "cityname": "Altopascio - Limited Traffic Zone",
            "city_latitude": "43.81",
            "city_longitude": "10.68",
            "scheme_color": "3"
        },
        {
            "id": "1079",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/arezzo-ar",
            "introtext": "The Access Regulation (ZTL) of Arezzo covers part of the historic center and is divided in area A and B. ",
            "cityname": "Arezzo - Limited Traffic Zone",
            "city_latitude": "43.46",
            "city_longitude": "11.88",
            "scheme_color": "3"
        },
        {
            "id": "1080",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/capoliveri-ar",
            "introtext": "The Access Regulation (ZTL) of Capoliveri covers part of the historic center.",
            "cityname": "Capoliveri - Limited Traffic Zone",
            "city_latitude": "42.75",
            "city_longitude": "10.38",
            "scheme_color": "3"
        },
        {
            "id": "1081",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/carrara-ar",
            "introtext": "The Access Regulation (ZTL) of Carrara covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Carrara\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/carrara\">Carrara</a>.",
            "cityname": "Carrara - Limited Traffic Zone",
            "city_latitude": "44.08",
            "city_longitude": "10.10",
            "scheme_color": "3"
        },
        {
            "id": "1086",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/cecina-ar",
            "introtext": "The Access Regulation (ZTL) of Cecina covers part of the historic center.",
            "cityname": "Cecina - Limited Traffic Zone",
            "city_latitude": "43.32",
            "city_longitude": "10.50",
            "scheme_color": "3"
        },
        {
            "id": "1083",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/casole-val-d-elsa-ar",
            "introtext": "The Access Regulation (ZTL) of Casole val d'Elsa covers part of the historic center.",
            "cityname": "Casole val d Elsa - Limited Traffic Zone",
            "city_latitude": "43.34",
            "city_longitude": "11.05",
            "scheme_color": "3"
        },
        {
            "id": "1087",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/colle-val-d-elsa-ar",
            "introtext": "The Access Regulation (ZTL) of Colle val d'Elsa covers part of the historic center.",
            "cityname": "Colle val d Elsa - Limited Traffic Zone",
            "city_latitude": "43.42",
            "city_longitude": "11.13",
            "scheme_color": "3"
        },
        {
            "id": "1088",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/cortona-ar",
            "introtext": "The Access Regulation (ZTL) of Cortona covers part of the historic center and is divided in two parts: ZTL Gialla and ZTL Rossa.",
            "cityname": "Cortona - Limited Traffic Zone",
            "city_latitude": "43.28",
            "city_longitude": "11.99",
            "scheme_color": "3"
        },
        {
            "id": "1089",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/empoli-ar",
            "introtext": "The Access Regulation (ZTL) of Empoli covers part of the historic center and is divided in two parts: ZTL Gialla and ZTL Rossa.<br><br>There is also an LEZ in place in <a title=\"Empoli\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/empoli\">Empoli</a>.",
            "cityname": "Empoli - Limited Traffic Zone",
            "city_latitude": "43.72",
            "city_longitude": "10.95",
            "scheme_color": "3"
        },
        {
            "id": "1092",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/foiano-della-chiana-ar",
            "introtext": "The Access Regulation (ZTL) of Foiano della Chiana covers part of the historic center and is divided in two parts: ZTL A and B.",
            "cityname": "Foiano della Chiana - Limited Traffic Zone",
            "city_latitude": "43.25",
            "city_longitude": "11.82",
            "scheme_color": "3"
        },
        {
            "id": "1093",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/forte-dei-marmi-ar",
            "introtext": "The Access Regulation (ZTL) of Forte dei Marmi covers part of the historic center.",
            "cityname": "Forte dei Marmi - Limited Traffic Zone",
            "city_latitude": "43.96",
            "city_longitude": "10.18",
            "scheme_color": "3"
        },
        {
            "id": "1099",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/livorno-ar",
            "introtext": "The Access Regulation (ZTL) of Livorno covers part of the historic center.<br>\r\n",
            "cityname": "Livorno - Limited Traffic Zone",
            "city_latitude": "43.55",
            "city_longitude": "10.31",
            "scheme_color": "3"
        },
        {
            "id": "1100",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/lucca-ar",
            "introtext": "The Access Regulation (ZTL) of Lucca covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Lucca\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/lucca\">Lucca</a>.",
            "cityname": "Lucca - Limited Traffic Zone",
            "city_latitude": "43.84",
            "city_longitude": "10.50",
            "scheme_color": "3"
        },
        {
            "id": "1101",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/lucignano-ar",
            "introtext": "The Access Regulation (ZTL) of Lucignano covers part of the historic center.",
            "cityname": "Lucignano - Limited Traffic Zone",
            "city_latitude": "43.63",
            "city_longitude": "11.13",
            "scheme_color": "3"
        },
        {
            "id": "1104",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/montecatini-terme-ar",
            "introtext": "The Access Regulation (ZTL) of Montecatini Terme covers part of the historic center.",
            "cityname": "Montecatini Terme - Limited Traffic Zone",
            "city_latitude": "43.88",
            "city_longitude": "10.78",
            "scheme_color": "3"
        },
        {
            "id": "1103",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/monte-argentario-ar",
            "introtext": "The Access Regulation (ZTL) of Monte Argentario covers part of the historic center.<br>\r\nThe ZTL is divided in three parts: ZTL Umberto I, Pilarella and Porto Ercole.",
            "cityname": "Monte Argentario - Limited Traffic Zone",
            "city_latitude": "42.43",
            "city_longitude": "11.12",
            "scheme_color": "3"
        },
        {
            "id": "1105",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/piombino-ar",
            "introtext": "The Access Regulation (ZTL) of Piombino covers part of the historic center.",
            "cityname": "Piombino - Limited Traffic Zone",
            "city_latitude": "42.93",
            "city_longitude": "10.53",
            "scheme_color": "3"
        },
        {
            "id": "1106",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/pisa-ar",
            "introtext": "The Access Regulation (ZTL) of Pisa covers part of the historic center.<br>There is also an LEZ in place in <a title=\"Pisa\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/pisa\">Pisa</a>.\r\n",
            "cityname": "Pisa - Limited Traffic Zone",
            "city_latitude": "43.72",
            "city_longitude": "10.40",
            "scheme_color": "3"
        },
        {
            "id": "1107",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/pistoia-ar",
            "introtext": "The Access Regulation (ZTL) of Pistoia covers part of the historic center.",
            "cityname": "Pistoia - Limited Traffic Zone",
            "city_latitude": "43.93",
            "city_longitude": "10.92",
            "scheme_color": "3"
        },
        {
            "id": "1108",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/poppi-ar",
            "introtext": "The Access Regulation (ZTL) of Poppi covers part of the historic center. The ZTL is divided in two parts A and B.",
            "cityname": "Poppi - Limited Traffic Zone",
            "city_latitude": "43.72",
            "city_longitude": "11.77",
            "scheme_color": "3"
        },
        {
            "id": "1109",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/portoferraio-ar",
            "introtext": "The Access Regulation (ZTL) of Portoferraio covers part of the historic center.",
            "cityname": "Portoferraio - Limited Traffic Zone",
            "city_latitude": "42.82",
            "city_longitude": "10.33",
            "scheme_color": "3"
        },
        {
            "id": "1110",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/san-giovanni-valdarno-ar",
            "introtext": "The Access Regulation (ZTL) of San Giovanni Valdarno covers part of the historic center.",
            "cityname": "San Giovanni Valdarno - Limited Traffic Zone",
            "city_latitude": "43.57",
            "city_longitude": "11.52",
            "scheme_color": "3"
        },
        {
            "id": "1111",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/sesto-fiorentino-ar",
            "introtext": "The Access Regulation (ZTL) of Sesto Fiorentino covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Sesto Fiorentino\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/sesto-fiorentino\">Sesto Fiorentino</a>.",
            "cityname": "Sesto Fiorentino - Limited Traffic Zone",
            "city_latitude": "43.83",
            "city_longitude": "11.20",
            "scheme_color": "3"
        },
        {
            "id": "1112",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/siena-ar",
            "introtext": "The Access Regulation (ZTL) of Siena covers part of the historic center.",
            "cityname": "Siena - Limited Traffic Zone",
            "city_latitude": "43.32",
            "city_longitude": "11.33",
            "scheme_color": "3"
        },
        {
            "id": "1113",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/volterra-ar",
            "introtext": "The Access Regulation (ZTL) of Volterra covers part of the historic center.",
            "cityname": "Volterra - Limited Traffic Zone",
            "city_latitude": "43.40",
            "city_longitude": "10.86",
            "scheme_color": "3"
        },
        {
            "id": "1114",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/bolzano-province/bolzano-ar",
            "introtext": "There is also a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/italy-mainmenu-81/bolzano-province/bolzano-bozen7\">Low Emission Zone</a> in place in Bolzano.<br>\nThe Access Regulation (ZTL) of Bolzano covers part of the historic center.",
            "cityname": "Bolzano (Bozen) - Limited Traffic Zone",
            "city_latitude": "46.50",
            "city_longitude": "11.35",
            "scheme_color": "3"
        },
        {
            "id": "1115",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/moena-ar",
            "introtext": "The Access Regulation (ZTL) of Moena covers part of the historic center.",
            "cityname": "Moena - Limited Traffic Zone",
            "city_latitude": "46.38",
            "city_longitude": "11.66",
            "scheme_color": "3"
        },
        {
            "id": "1116",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/orvieto-ar",
            "introtext": "The Access Regulation (ZTL) of Orvieto covers part of the historic center.<br>\r\nThe ZTL is divided in five sectors.",
            "cityname": "Orvieto - Limited Traffic Zone",
            "city_latitude": "42.72",
            "city_longitude": "12.11",
            "scheme_color": "3"
        },
        {
            "id": "1117",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/perugia-ar",
            "introtext": "The Access Regulation (ZTL) of Perugia covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Perugia\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/umbria/perugia\">Perugia</a>.",
            "cityname": "Perugia - Limited Traffic Zone",
            "city_latitude": "43.11",
            "city_longitude": "12.39",
            "scheme_color": "3"
        },
        {
            "id": "1119",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/terni-ar",
            "introtext": "The Access Regulation (ZTL) of Terni covers part of the historic center.\r\n<br>\r\nTerni also has a winter LEZ in place.",
            "cityname": "Terni - Limited Traffic Zone",
            "city_latitude": "42.56",
            "city_longitude": "12.64",
            "scheme_color": "3"
        },
        {
            "id": "1120",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/todi-ar",
            "introtext": "The Access Regulation (ZTL) of Todi covers part of the historic center.",
            "cityname": "Todi - Limited Traffic Zone",
            "city_latitude": "42.79",
            "city_longitude": "12.42",
            "scheme_color": "3"
        },
        {
            "id": "1121",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/aosta-valle-d/aosta-ar",
            "introtext": "The Access Regulation (ZTL) of Aosta covers part of the historic center.<br>There is also a LEZ in <a title=\"Aosta\"href=\"/countries-mainmenu-147/italy-mainmenu-81/aosta-valle-d/aosta\">Aosta</a>.",
            "cityname": "Aosta - Limited Traffic Zone",
            "city_latitude": "45.74",
            "city_longitude": "7.32",
            "scheme_color": "3"
        },
        {
            "id": "1529",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/citta-di-ischia-ar",
            "introtext": "The Access Regulation (ZTL) of Citta di Ischia covers part of the historical center.",
            "cityname": "Citta di Ischia - Limited Traffic Zone",
            "city_latitude": "40.74",
            "city_longitude": "13.95",
            "scheme_color": "3"
        },
        {
            "id": "1122",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/asolo-ar",
            "introtext": "The Access Regulation (ZTL) of Asolo covers part of the historic center.\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 2019.</p>\r\n",
            "cityname": "Asolo - Limited Traffic Zone",
            "city_latitude": "45.80",
            "city_longitude": "11.91",
            "scheme_color": "3"
        },
        {
            "id": "1123",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/bassano-del-grappa-ar",
            "introtext": "The Access Regulation (ZTL) of Bassano del Grappa covers part of the historic center.<br />\r\n\t<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Bassano del Grappa - Limited Traffic Zone",
            "city_latitude": "45.77",
            "city_longitude": "11.73",
            "scheme_color": "3"
        },
        {
            "id": "1124",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/conegliano-ar",
            "introtext": "The Access Regulation (ZTL) of Conegliano covers part of the historic center.<br />\r\n\t<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Conegliano - Limited Traffic Zone",
            "city_latitude": "45.89",
            "city_longitude": "12.30",
            "scheme_color": "3"
        },
        {
            "id": "1125",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/lazise-ar",
            "introtext": "The Access Regulation (ZTL) of Lazise covers part of the historic center.",
            "cityname": "Lazise - Limited Traffic Zone",
            "city_latitude": "45.51",
            "city_longitude": "10.73",
            "scheme_color": "3"
        },
        {
            "id": "1126",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/marostica-ar",
            "introtext": "The Access Regulation (ZTL) of Marostica covers part of the historic center.",
            "cityname": "Marostica - Limited Traffic Zone",
            "city_latitude": "45.75",
            "city_longitude": "11.66",
            "scheme_color": "3"
        },
        {
            "id": "1127",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/mestre-ar",
            "introtext": "The Access Regulation (ZTL) of Mestre covers part of the historic center. <br />\r\n\t<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Mestre - Limited Traffic Zone",
            "city_latitude": "45.49",
            "city_longitude": "12.24",
            "scheme_color": "3"
        },
        {
            "id": "1128",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/mirano-ar",
            "introtext": "The Access Regulation (ZTL) of Mirano covers part of the historic center.",
            "cityname": "Mirano - Limited Traffic Zone",
            "city_latitude": "45.49",
            "city_longitude": "12.11",
            "scheme_color": "3"
        },
        {
            "id": "1129",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/montagnana-ar",
            "introtext": "The Access Regulation (ZTL) of Montagnana covers part of the historic center.",
            "cityname": "Montagnana - Limited Traffic Zone",
            "city_latitude": "45.23",
            "city_longitude": "11.47",
            "scheme_color": "3"
        },
        {
            "id": "1130",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/padova-ar",
            "introtext": "The Access Regulation (ZTL) of Padova covers part of the historic center.<p>\r\n\t<br />\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Padova - Limited Traffic Zone",
            "city_latitude": "45.41",
            "city_longitude": "11.88",
            "scheme_color": "3"
        },
        {
            "id": "1131",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/piove-di-sacco-ar",
            "introtext": "The Access Regulation (ZTL) of Piove di Sacco covers part of the historic center.",
            "cityname": "Piove di Sacco - Limited Traffic Zone",
            "city_latitude": "45.30",
            "city_longitude": "12.03",
            "scheme_color": "3"
        },
        {
            "id": "1133",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/rovigo-ar",
            "introtext": "The Access Regulation (ZTL) of Rovigo covers part of the historic center.<p>\r\n\t<br />\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Rovigo - Limited Traffic Zone",
            "city_latitude": "45.07",
            "city_longitude": "11.79",
            "scheme_color": "3"
        },
        {
            "id": "1134",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/selvazzano-ar",
            "introtext": "The Access Regulation (ZTL) of Selvazzano covers part of the historic center. <br />\r\n\t<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Selvazzano - Limited Traffic Zone",
            "city_latitude": "45.39",
            "city_longitude": "11.78",
            "scheme_color": "3"
        },
        {
            "id": "1135",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/valeggio-sul-mincio-ar",
            "introtext": "The Access Regulation (ZTL) of Valeggio sul Mincio covers part of the historic center.",
            "cityname": "Valeggio sul Mincio - Limited Traffic Zone",
            "city_latitude": "45.35",
            "city_longitude": "10.73",
            "scheme_color": "3"
        },
        {
            "id": "1136",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/verona-ar",
            "introtext": "The Access Regulation (ZTL) of Verona covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Verona\"  href=\"/countries-mainmenu-147/italy-mainmenu-81/veneto/verona\">Verona</a>.<br /><br>\n\t<p>\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\n",
            "cityname": "Verona - Limited Traffic Zone",
            "city_latitude": "45.44",
            "city_longitude": "10.99",
            "scheme_color": "3"
        },
        {
            "id": "1137",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/vicenza-ar",
            "introtext": "The Access Regulation (ZTL) of Vicenza covers part of the historic center.<p>\r\n\t<br />\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Vicenza - Limited Traffic Zone",
            "city_latitude": "45.55",
            "city_longitude": "11.55",
            "scheme_color": "3"
        },
        {
            "id": "1669",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/rigi-carfree",
            "introtext": "CH",
            "cityname": "Rigi - car-free",
            "city_latitude": "47.05",
            "city_longitude": "8.46",
            "scheme_color": "3"
        },
        {
            "id": "1509",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/a12-ban-on-overtaking",
            "introtext": "<b>On the A12</b> there are several schemes, please select the one you want information on, and then the details will show below",
            "cityname": "A12 Ban on overtaking",
            "city_latitude": "47.26",
            "city_longitude": "11.45",
            "scheme_color": "3"
        },
        {
            "id": "1670",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/saas-fee-carfree",
            "introtext": "CH",
            "cityname": "Saas-Fee - car-free",
            "city_latitude": "46.06",
            "city_longitude": "7.55",
            "scheme_color": "3"
        },
        {
            "id": "1140",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/atrani-ar",
            "introtext": "The Access Regulation (ZTL) of Atrani covers part of the historic center.",
            "cityname": "Atrani - Limited Traffic Zone",
            "city_latitude": "40.64",
            "city_longitude": "14.61",
            "scheme_color": "3"
        },
        {
            "id": "1141",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/caiazzo-ar",
            "introtext": "The Access Regulation (ZTL) of Caiazzo covers part of the historic center.",
            "cityname": "Caiazzo - Limited Traffic Zone",
            "city_latitude": "41.18",
            "city_longitude": "14.36",
            "scheme_color": "3"
        },
        {
            "id": "1142",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/caserta-ar",
            "introtext": "The Access Regulation (ZTL) of Caserta covers part of the historic center and is divided in two parts:ZTL Cosrso Trieste and ZTL Piazza Dante.",
            "cityname": "Caserta - Limited Traffic Zone",
            "city_latitude": "41.07",
            "city_longitude": "14.33",
            "scheme_color": "3"
        },
        {
            "id": "1143",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/cava-dei-tirreni-ar",
            "introtext": "The Access Regulation (ZTL) of Cava dei Tirreni covers part of the historic center.",
            "cityname": "Cava dei Tirreni - Limited Traffic Zone",
            "city_latitude": "40.70",
            "city_longitude": "14.71",
            "scheme_color": "3"
        },
        {
            "id": "1144",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/forio-ar",
            "introtext": "The Access Regulation (ZTL) of Forio covers part of the historic center.",
            "cityname": "Forio - Limited Traffic Zone",
            "city_latitude": "40.74",
            "city_longitude": "13.86",
            "scheme_color": "3"
        },
        {
            "id": "2200",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/krakow-ltz",
            "introtext": "",
            "cityname": "Krakow - Limited Traffic Zone",
            "city_latitude": "50.06",
            "city_longitude": "19.94",
            "scheme_color": "3"
        },
        {
            "id": "1145",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/maiori-ar",
            "introtext": "The Access Regulation (ZTL) of Maiori covers part of the historic center.",
            "cityname": "Maiori - Limited Traffic Zone",
            "city_latitude": "40.65",
            "city_longitude": "14.64",
            "scheme_color": "3"
        },
        {
            "id": "1149",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/paestum-ar",
            "introtext": "The Access Regulation (ZTL) of Paestum covers part of the entire archaeological area.",
            "cityname": "Paestum - Limited Traffic Zone",
            "city_latitude": "40.42",
            "city_longitude": "15.01",
            "scheme_color": "3"
        },
        {
            "id": "1150",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/pozzuoli-ar",
            "introtext": "The Access Regulation (ZTL) of Pozzuoli covers part of the historical center.",
            "cityname": "Pozzuoli - Limited Traffic Zone",
            "city_latitude": "40.82",
            "city_longitude": "14.12",
            "scheme_color": "3"
        },
        {
            "id": "1148",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/nola-ar",
            "introtext": "The Access Regulation (ZTL) of Nola covers part of the historic center.",
            "cityname": "Nola - Limited Traffic Zone",
            "city_latitude": "40.93",
            "city_longitude": "14.53",
            "scheme_color": "3"
        },
        {
            "id": "1195",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence-ar",
            "introtext": "The Access Regulation (ZTL) of Firenze covers part of the historic center.<br><br>There is also an LEZ in place in <a title=\"Firenze\"  href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence\">Firenze</a>.<br>\r\nThe ZTL consists of five sectors: A, B, O, F and G.\r\n\r\n",
            "cityname": "Firenze (Florence) - Limited Traffic Zone",
            "city_latitude": "43.78",
            "city_longitude": "11.25",
            "scheme_color": "3"
        },
        {
            "id": "1230",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/lari-ar",
            "introtext": "The Access Regulation (ZTL) of Lari covers part of the historic center.",
            "cityname": "Lari - Limited Traffic Zone",
            "city_latitude": "43.57",
            "city_longitude": "10.59",
            "scheme_color": "3"
        },
        {
            "id": "1197",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/rome-coaches",
            "introtext": "<p>\r\n\tThere is an access regulation scheme in Rome called <strong>tour bus system</strong>.<br />\r\n\tIt divides the Rome ZTL in three parts. For each part apply different charges:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\t<b>ZTL 1</b>: Western part of Rome center including Aurelian walls and Vatican area and</li>\r\n\t<li>\r\n\t\t<b>ZTL 2</b>: between G.R.A. (Grande Raccordo Anulare) and ZTL 1</li>\r\n\t<li>\r\n\t\t<strong>Vatican Area</strong></li>\r\n</ul>\r\n\r\n<p>\r\n\tThere is also a Low Emission Zone in <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/rome\" title=\"Rome\">Rome</a> and an access regulation <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/rome\" title=\"Rome - AR\">Rome - AR</a>.</p>\r\n\r\n<p>\r\n\tThere is also the possibility of emergency measures on days with extreme pollution, particularly in the winter. Options include banning alternating number plates, or a ban all vehicles. Notification is by the local press.</p>\r\n",
            "cityname": "Roma (Rome) - Coaches",
            "city_latitude": "41.90",
            "city_longitude": "12.50",
            "scheme_color": "3"
        },
        {
            "id": "1228",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/calabria-region/reggio-calabria-ar",
            "introtext": "The Access Regulation (ZTL) of Reggio Calabria covers part of the historic center.\r\n",
            "cityname": "Reggio Calabria - Limited Traffic Zone",
            "city_latitude": "38.11",
            "city_longitude": "15.65",
            "scheme_color": "3"
        },
        {
            "id": "1200",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/rossdorf-ar",
            "introtext": "The lorry ban for Roßdorf was established because of the enlarged transit ban in Darmstadt called <a title=\"Darmstadt - AR\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/darmstadt-ar\">Darmstadt - AR</a> and the new <a title=\"LEZ\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/darmstadt\">LEZ</a> in Darmstadt. ",
            "cityname": "Roßdorf - Transit Ban",
            "city_latitude": "49.87",
            "city_longitude": "8.65",
            "scheme_color": "3"
        },
        {
            "id": "1415",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lissone-ar",
            "introtext": "The Access Regulation (ZTL) of Lissone covers part of the historic center. The streets covered are:<br>\r\nPiazza della Libertà<br>\r\nVia Pietro e Paolo da Via Sant’Antonio a Via Padre Ugolino da Lissone<br>\r\nVia Sant’Antonio<br>\r\nVia S. Giuseppe<br>\r\nVia Madonna<br>\r\nVia Sant’Ambrogio.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Lissone - Limited Traffic Zone",
            "city_latitude": "45.61",
            "city_longitude": "9.24",
            "scheme_color": "3"
        },
        {
            "id": "1223",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/abruzzo-region/celano-ar",
            "introtext": "The Access Regulation (ZTL) of Celano covers the entire part of the historic center inside the castle walls.",
            "cityname": "Celano - Limited Traffic Zone",
            "city_latitude": "42.08",
            "city_longitude": "13.54",
            "scheme_color": "3"
        },
        {
            "id": "1229",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/casciana-terme-ar",
            "introtext": "The Access Regulation (ZTL) of Casciana Terme covers part of the historic center.",
            "cityname": "Casciana Terme - Limited Traffic Zone",
            "city_latitude": "43.53",
            "city_longitude": "10.62",
            "scheme_color": "3"
        },
        {
            "id": "1231",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/la-spezia-ar",
            "introtext": "The Access Regulation (ZTL) of La Spezia is called 'Centro Torretto' and covers part of the historic center.",
            "cityname": "La Spezia - Limited Traffic Zone",
            "city_latitude": "44.10",
            "city_longitude": "9.82",
            "scheme_color": "3"
        },
        {
            "id": "1232",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/campo-nell-elba-ar",
            "introtext": "The Access Regulation (ZTL) of Campo nell'Elba  is called Marino di Campo and covers part of the waterfront.",
            "cityname": "Campo nell Elba - Limited Traffic Zone",
            "city_latitude": "42.75",
            "city_longitude": "10.23",
            "scheme_color": "3"
        },
        {
            "id": "1233",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/fiano-romano-ar",
            "introtext": "The Access Regulation (ZTL) of Fiano Romano covers part of the historic center.",
            "cityname": "Fiano Romano - Limited Traffic Zone",
            "city_latitude": "42.17",
            "city_longitude": "12.59",
            "scheme_color": "3"
        },
        {
            "id": "1234",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/pioltello-ar",
            "introtext": "The Access Regulation (ZTL) of Pioltello consists of two areas:<br>\r\n \r\nZone 'Pioltello Centro'<br>\r\nZone 'Limito'.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Pioltello - Limited Traffic Zone",
            "city_latitude": "45.50",
            "city_longitude": "9.33",
            "scheme_color": "3"
        },
        {
            "id": "1237",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/trento-access-regulation",
            "introtext": "There is also a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/trento\">Low Emission Zone</a> in Trento.",
            "cityname": "Trento - Limited Traffic Zone",
            "city_latitude": "46.07",
            "city_longitude": "11.13",
            "scheme_color": "3"
        },
        {
            "id": "1239",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/levico-terme-ar",
            "introtext": "The ZTL in Levico Terme is divided in four zones: yellow, white, orange and green and covers part of the historic center.<br><br>\r\n\r\nThere is also a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/levico-terme\">Low Emission Zone</a> in Levico Terme.\r\n\r\n",
            "cityname": "Levico Terme - Limited Traffic Zone",
            "city_latitude": "46.01",
            "city_longitude": "11.30",
            "scheme_color": "3"
        },
        {
            "id": "2136",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/polignano-a-mare-ztl",
            "introtext": "Polignano a Mare has a ZTL access regulation in place.",
            "cityname": "Polignano a Mare - Limited Traffic Zone",
            "city_latitude": "40.99",
            "city_longitude": "17.22",
            "scheme_color": "3"
        },
        {
            "id": "2134",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/liege-ar",
            "introtext": "",
            "cityname": "Liège - pedestrian",
            "city_latitude": "50.63",
            "city_longitude": "5.57",
            "scheme_color": "3"
        },
        {
            "id": "2133",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/paris-pedestrian",
            "introtext": "",
            "cityname": "Paris - pedestrian",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "3"
        },
        {
            "id": "1414",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/wuerzburg-ar",
            "introtext": "",
            "cityname": "Würzburg - Transit Ban",
            "city_latitude": "49.79",
            "city_longitude": "9.95",
            "scheme_color": "3"
        },
        {
            "id": "1419",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/monopoli-ar",
            "introtext": "There is a ZTL in the historic center of Monopoli.",
            "cityname": "Monopoli - Limited Traffic Zone",
            "city_latitude": "40.95",
            "city_longitude": "17.30",
            "scheme_color": "3"
        },
        {
            "id": "1421",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/gela-ar",
            "introtext": "The Access Regulation (ZTL) covers a small part of the historic center of Gela and is divided in ZTL Centro storico and APU Macchitella.",
            "cityname": "Gela - Limited Traffic Zone",
            "city_latitude": "37.07",
            "city_longitude": "14.24",
            "scheme_color": "3"
        },
        {
            "id": "1437",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/nardo-ar",
            "introtext": "The Access Regulation (ZTL) of Nardò covers the entire historic center.",
            "cityname": "Nardò - Limited Traffic Zone",
            "city_latitude": "40.18",
            "city_longitude": "18.03",
            "scheme_color": "3"
        },
        {
            "id": "1424",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/ventimiglia-ar",
            "introtext": "The Access Regulation (ZTL) of Ventimiglia  includes part of the upper town that runs along the axis of Via Garibaldi.",
            "cityname": "Ventimiglia - Limited Traffic Zone",
            "city_latitude": "43.79",
            "city_longitude": "7.61",
            "scheme_color": "3"
        },
        {
            "id": "1428",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/leonforte-ar",
            "introtext": "The Access Regulation (ZTL) of Leonforte covers part of the historic center.",
            "cityname": "Leonforte - Limited Traffic Zone",
            "city_latitude": "37.64",
            "city_longitude": "14.39",
            "scheme_color": "3"
        },
        {
            "id": "1426",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/ancona-ar",
            "introtext": "The Access Regulation (ZTL) of Ancona covers part of the historic center.",
            "cityname": "Ancona - Limited Traffic Zone",
            "city_latitude": "43.62",
            "city_longitude": "13.52",
            "scheme_color": "3"
        },
        {
            "id": "1427",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/imperia-ar",
            "introtext": "The Access Regulation (ZTL) of Imperia covers part of the historic center and is divided in two parts: ZTL Borgo Marina and ZTL Parasio.",
            "cityname": "Imperia - Limited Traffic Zone",
            "city_latitude": "43.89",
            "city_longitude": "8.04",
            "scheme_color": "3"
        },
        {
            "id": "1429",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/massa-ar",
            "introtext": "The Access Regulation (ZTL) of Massa covers part of the historic center.",
            "cityname": "Massa - Limited Traffic Zone",
            "city_latitude": "44.03",
            "city_longitude": "10.14",
            "scheme_color": "3"
        },
        {
            "id": "1432",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/punta-secca-ar",
            "introtext": "The Access Regulation (ZTL) of Punta Secca covers part of the historic center.",
            "cityname": "Punta Secca - Limited Traffic Zone",
            "city_latitude": "36.79",
            "city_longitude": "14.49",
            "scheme_color": "3"
        },
        {
            "id": "1433",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/legnano-limited-traffic-zone",
            "introtext": "The Access Regulation (ZTL) of Legnano covers part of the historic center.<br> There is a permanent and a temporary ZTL in Legnano.<br>\r\n\r\nZTL permanent: vie Cavallotti, Luini, Piazza San Magno, Corso Garibaldi (tratto Piazza San Magno e via Verdi)<br>\r\n\r\nZTL temporary: le vie XXV Aprile, Corso Magenta (tratto XXV Aprile e via Ratti), via Corridoni e Giulini.\r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Legnano - Limited Traffic Zone",
            "city_latitude": "45.12",
            "city_longitude": "11.18",
            "scheme_color": "3"
        },
        {
            "id": "1434",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/frascati-ar",
            "introtext": "The Access Regulation (ZTL) of Frascati covers part of the historic center.The Access Regulation (ZTL) of Frascati covers part of the historic center.",
            "cityname": "Frascati - Limited Traffic Zone",
            "city_latitude": "41.81",
            "city_longitude": "12.68",
            "scheme_color": "3"
        },
        {
            "id": "1435",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/prato-ar",
            "introtext": "<p>\r\n\tThe Access Regulation (ZTL) of Prato covers part of the historic center.<br />\r\n\tThe ZTL Prato consists of a permanent ZTL and a ZTL that is active from 07:30 - 18:30.&nbsp;</p>\r\n\r\n<p>\r\n\tThere is also a low emission zone active in <a href=\"/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/prato\">Prato</a>.</p>\r\n",
            "cityname": "Prato - Limited Traffic Zone",
            "city_latitude": "43.88",
            "city_longitude": "11.10",
            "scheme_color": "3"
        },
        {
            "id": "1436",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/castellaneta-ar",
            "introtext": "The Access Regulation (ZTL) of Castellaneta covers part of the historic center.",
            "cityname": "Castellaneta - Limited Traffic Zone",
            "city_latitude": "40.63",
            "city_longitude": "16.94",
            "scheme_color": "3"
        },
        {
            "id": "1452",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/frosinone-limited-traffic-zone",
            "introtext": "The Access Regulation (ZTL) of Frosinone covers part of the historic center. ",
            "cityname": "Frosinone - Limited Traffic Zone",
            "city_latitude": "41.72",
            "city_longitude": "12.67",
            "scheme_color": "3"
        },
        {
            "id": "1453",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/vitoria-gasteiz-ar",
            "introtext": "<p>\n\tVitoria Gasteiz has been implementing gradually the superblock scheme since 2008. It is supposed to be completed in 2023.</p>\n\n<p>\n\tThe superblock scheme operates a system to keep transit traffic out of certain areas of the city. The city is divided in 77 blocks, transit traffic is kept out of these blocks. The biggest superblock (S1) has a pedestrian area in its centre.</p>\n",
            "cityname": "Vitoria Gasteiz - superblocks",
            "city_latitude": "42.85",
            "city_longitude": "-2.67",
            "scheme_color": "3"
        },
        {
            "id": "2277",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/desenzano-del-garda-ar",
            "introtext": "",
            "cityname": "Desenzano del Garda - Limited Traffic Zone",
            "city_latitude": "45.46",
            "city_longitude": "10.55",
            "scheme_color": "3"
        },
        {
            "id": "2278",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/voghera-ztl",
            "introtext": "The Access Regulation (ZTL) of Voghera covers part of the historic center.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p>",
            "cityname": "Voghera - Limited Traffic Zone",
            "city_latitude": "44.99",
            "city_longitude": "9.00",
            "scheme_color": "3"
        },
        {
            "id": "2287",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/finland/helsinki-studded-tire-ban",
            "introtext": "  ",
            "cityname": "Helsinki - Studded Tyre Ban",
            "city_latitude": "60.16",
            "city_longitude": "24.93",
            "scheme_color": "3"
        },
        {
            "id": "2289",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/strasbourg- limited-traffic-zone",
            "introtext": "",
            "cityname": "Strasbourg - Limited Traffic Zone",
            "city_latitude": "48.57",
            "city_longitude": "7.75",
            "scheme_color": "3"
        },
        {
            "id": "2290",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/toulouse-pedestrian",
            "introtext": "Toulouse has established various pedestrian areas in its city center.",
            "cityname": "Toulouse - pedestrian",
            "city_latitude": "43.60",
            "city_longitude": "1.44",
            "scheme_color": "3"
        },
        {
            "id": "1479",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/taranto-ar",
            "introtext": "The Access Regulation (ZTL) of Taranto covers part of the historic center.",
            "cityname": "Taranto - Limited Traffic Zone",
            "city_latitude": "40.46",
            "city_longitude": "17.26",
            "scheme_color": "3"
        },
        {
            "id": "1482",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trentino-province/riva-del-garda-ar",
            "introtext": "There is an access regulation in the historic part of Riva del Garda .",
            "cityname": "Riva del Garda - Limited Traffic Zone",
            "city_latitude": "45.88",
            "city_longitude": "10.84",
            "scheme_color": "3"
        },
        {
            "id": "1481",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/romano-in-lombardia-ar",
            "introtext": "The Access Regulation (ZTL) of Romano in Lombardia covers part of the historic center. \r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p>",
            "cityname": "Romano in Lombardia - Limited Traffic Zone",
            "city_latitude": "45.52",
            "city_longitude": "9.76",
            "scheme_color": "3"
        },
        {
            "id": "1483",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/castellina-in-chianti-ar",
            "introtext": "The Access Regulation (ZTL) of Castellina in Chianti covers part of the historic center.",
            "cityname": "Castellina in Chianti - Limited Traffic Zone",
            "city_latitude": "43.72",
            "city_longitude": "10.95",
            "scheme_color": "3"
        },
        {
            "id": "1485",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/anagni-ar",
            "introtext": "The Access Regulation (ZTL) of Anagni covers part of the historic center.",
            "cityname": "Anagni - Limited Traffic Zone",
            "city_latitude": "41.74",
            "city_longitude": "13.16",
            "scheme_color": "3"
        },
        {
            "id": "2292",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/bordeaux-pedestrian",
            "introtext": "Bordeaux has established various pedestrian areas in its city center.",
            "cityname": "Bordeaux - pedestrian",
            "city_latitude": "44.84",
            "city_longitude": "-0.58",
            "scheme_color": "3"
        },
        {
            "id": "1490",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence-coaches",
            "introtext": "The entry, driving and parking of tourist coaches in Florence is regulated by the Florence Tourist Ecoprogram Buspass.<br>\r\nThe\r\nTourist coach buses need to get a permit (bus pass) to be able to enter Florence for dropping off and collecting their passengers.<br>\r\nThe permits can be bought at the check points (see 'map' below) but it is easier to buy the permit online in advance.<br>\r\nIf you enter Florence for the first time with your tourist bus you need to get registered (see 'Need to register').<br>\r\n\r\n<br><br>Florence also has a <a title=\"low emission zone\"  href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence\">low emission zone</a>  and <a title=\"access regulation\"  href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/firenze-florence-ar\">access regulation</a> in place.",
            "cityname": "Firenze (Florence) Coaches",
            "city_latitude": "43.78",
            "city_longitude": "11.25",
            "scheme_color": "3"
        },
        {
            "id": "1491",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/friuli-venezia-giulia-region/trieste-ar",
            "introtext": "The Access Regulation (ZTL) of Trieste is divided in two areas: <br>\r\nZTL A and B",
            "cityname": "Trieste - Limited Traffic Zone",
            "city_latitude": "45.65",
            "city_longitude": "13.78",
            "scheme_color": "3"
        },
        {
            "id": "1492",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/cuneo-ar",
            "introtext": "<p>\r\n\tSince 1 November 2016 Cuneo has ZTL active that regulates the access to the historic center. There is also a <a href=\"/countries-mainmenu-147/italy-mainmenu-81/38-countries/italy/piemonte-region/2114-cuneo\">low emission zone</a> in Cuneo in place.</p>\r\n",
            "cityname": "Cuneo - Limited Traffic Zone",
            "city_latitude": "44.38",
            "city_longitude": "7.54",
            "scheme_color": "3"
        },
        {
            "id": "1493",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/friuli-venezia-giulia-region/pordenone-access-regulation",
            "introtext": "Pordenone has an access regulation in place for part of the historic center.",
            "cityname": "Pordenone - Limited Traffic Zone",
            "city_latitude": "45.96",
            "city_longitude": "12.66",
            "scheme_color": "3"
        },
        {
            "id": "1495",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/latina-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Latina covers part of the historic center.",
            "cityname": "Latina - Limited Traffic Zone",
            "city_latitude": "41.47",
            "city_longitude": "12.90",
            "scheme_color": "3"
        },
        {
            "id": "1496",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/romania/suceava",
            "introtext": "Suceava has a pedestrian zone in a part of the historic city center.",
            "cityname": "Suceava - pedestrian",
            "city_latitude": "47.66",
            "city_longitude": "26.27",
            "scheme_color": "3"
        },
        {
            "id": "1499",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/recanati-access-regulation",
            "introtext": "The Access Regulation (ZTL) of Recanati covers part of the historic center.",
            "cityname": "Recanati - Limited Traffic Zone",
            "city_latitude": "43.40",
            "city_longitude": "13.55",
            "scheme_color": "3"
        },
        {
            "id": "1505",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/treviso-ar",
            "introtext": "The Access Regulation (ZTL) of Treviso covers part of the historic center.<p>\r\n\t<br />\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a<a href=\"/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\"> <b>winter emergency scheme</b></a> in place from 1 October 2017 - 31 March 2018.</p>\r\n",
            "cityname": "Treviso - Limited Traffic Zone",
            "city_latitude": "45.66",
            "city_longitude": "12.25",
            "scheme_color": "3"
        },
        {
            "id": "1506",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/toulouse-ar",
            "introtext": "Toulouse has established an access regulation in its city centre for <b>delivery</b> vehicles. ",
            "cityname": "Toulouse - delivery",
            "city_latitude": "43.60",
            "city_longitude": "1.44",
            "scheme_color": "3"
        },
        {
            "id": "1536",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/avellino-ar",
            "introtext": "The Access Regulation (ZTL) of Avellino covers part of the historical center and has been active since 17 February 2017.",
            "cityname": "Avellino - Limited Traffic Zone",
            "city_latitude": "40.91",
            "city_longitude": "14.79",
            "scheme_color": "3"
        },
        {
            "id": "1534",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/brindisi-ar",
            "introtext": "The Access Regulation (ZTL) of Brindisi covers part of the historic center.",
            "cityname": "Brindisi - Limited Traffic Zone",
            "city_latitude": "40.64",
            "city_longitude": "17.94",
            "scheme_color": "3"
        },
        {
            "id": "1542",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-lorry-regulations",
            "introtext": "<p>\r\n\tStockholm also has various schmes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/sweden-mainmenu-248/stockholm\">low emission zone</a></li>\r\n\t<li>\r\n\t\ta <a class=\"new-window nturl\" href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-charging-scheme\" title=\"Charging Scheme\">charging scheme</a></li>\r\n\t<li>\r\n\t\tand <a href=\"/countries-mainmenu-147/sweden-mainmenu-248/stockholm-lorry-regulations\">lorry regulations</a>&nbsp;</li>\r\n</ul>\r\n\r\n<p>\r\n\tStockholm regulates lorries over a certain <strong>length</strong>, <strong>width </strong>and <strong>weight </strong>and also has a <strong>night time ban</strong> for lorries in place.</p>\r\n",
            "cityname": "Stockholm - lorry regulations",
            "city_latitude": "59.33",
            "city_longitude": "18.06",
            "scheme_color": "3"
        },
        {
            "id": "1543",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/groningen-carfree",
            "introtext": "Groningen has several area that are either carfree area or transit bans in its city centre that makes it impossible for cars etc. to transit.",
            "cityname": "Groningen - car-free",
            "city_latitude": "53.22",
            "city_longitude": "6.57",
            "scheme_color": "3"
        },
        {
            "id": "1622",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/pompei-ztl",
            "introtext": "There is an Access Regulation (ZTL)in Pompei.",
            "cityname": "Pompei - Limited Traffic Zone",
            "city_latitude": "40.68",
            "city_longitude": "14.76",
            "scheme_color": "3"
        },
        {
            "id": "1549",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/amsterdam-ar",
            "introtext": "",
            "cityname": "Amsterdam - driving ban",
            "city_latitude": "52.37",
            "city_longitude": "4.89",
            "scheme_color": "3"
        },
        {
            "id": "1569",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/bra-ar",
            "introtext": "<p>\r\n\tThe city of Bra has two access regulations in place.<br />\r\n\tIt also has a low emission zone (ZTL - in Italian) in place:&nbsp;<a href=\"/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/bra\">Bra</a>.</p>\r\n",
            "cityname": "Bra - Limited Traffic Zone",
            "city_latitude": "44.7",
            "city_longitude": "7.85",
            "scheme_color": "3"
        },
        {
            "id": "1594",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/busseto-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Busseto.\r\n",
            "cityname": "Busseto - Limited Traffic Zone",
            "city_latitude": "43.49",
            "city_longitude": "11.62",
            "scheme_color": "3"
        },
        {
            "id": "2275",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/paris-limited-traffic-zone",
            "introtext": "",
            "cityname": "Paris - Limited Traffic Zone",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "3"
        },
        {
            "id": "1621",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/porto-recanati-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Porto Recanati.",
            "cityname": "Porto Recanati - Limited Traffic Zone",
            "city_latitude": "43.53",
            "city_longitude": "13.25",
            "scheme_color": "3"
        },
        {
            "id": "1598",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/campi-bisenzio-ztl",
            "introtext": "<p>\r\n\tThere are three different Access Regulations (ZTL) in Campi Bisenzio: ZTL Galleria Vittorio Veneto, ZTL in the historic centre of Capalle and ZTL in the Historic Centre</p>\r\n",
            "cityname": "Campi Bisenzio - Limited Traffic Zone",
            "city_latitude": "43.82",
            "city_longitude": "11.13",
            "scheme_color": "3"
        },
        {
            "id": "1582",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/abbiategrasso-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Abbiategrasso.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p>",
            "cityname": "Abbiategrasso - Limited Traffic Zone",
            "city_latitude": "45.99",
            "city_longitude": "9.26",
            "scheme_color": "3"
        },
        {
            "id": "1583",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alagna-valsesia-ztl",
            "introtext": "There is an Access Regualtion in Alagna Valesia.\r\n",
            "cityname": "Alagna Valsesia - Limited Traffic Zone",
            "city_latitude": "44.7",
            "city_longitude": "7.85",
            "scheme_color": "3"
        },
        {
            "id": "1584",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/alassio-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Alassio.",
            "cityname": "Alassio - Limited Traffic Zone",
            "city_latitude": "44.06",
            "city_longitude": "9.97",
            "scheme_color": "3"
        },
        {
            "id": "1586",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/amalfi-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Amalfi.",
            "cityname": "Amalfi - Limited Traffic Zone",
            "city_latitude": "40.64",
            "city_longitude": "14.61",
            "scheme_color": "3"
        },
        {
            "id": "1587",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/amelia-ztl",
            "introtext": "The Access Regulation (ZTL) of Amelia covers the historic center.\r\n",
            "cityname": "Amelia - Limited Traffic Zone",
            "city_latitude": "42.72",
            "city_longitude": "12.11",
            "scheme_color": "3"
        },
        {
            "id": "1588",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/anacapri-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Anacapri. ",
            "cityname": "Anacapri - Limited Traffic Zone",
            "city_latitude": "40.64",
            "city_longitude": "14.61",
            "scheme_color": "3"
        },
        {
            "id": "1589",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/ascoli-piceno-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Ascoli Piceno.",
            "cityname": "Ascoli Piceno - Limited Traffic Zone",
            "city_latitude": "43.62",
            "city_longitude": "13.52",
            "scheme_color": "3"
        },
        {
            "id": "1590",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/aversa-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Aversa.",
            "cityname": "Aversa - Limited Traffic Zone",
            "city_latitude": "40.65",
            "city_longitude": "14.64",
            "scheme_color": "3"
        },
        {
            "id": "1591",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/bardolino-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic centre of Bardolino.<p>\r\n\t<br />\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Bardolino - Limited Traffic Zone",
            "city_latitude": "45.41",
            "city_longitude": "11.88",
            "scheme_color": "3"
        },
        {
            "id": "1592",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/bisceglie-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Bisceglie, which covers all of the ancient village. ",
            "cityname": "Bisceglie - Limited Traffic Zone",
            "city_latitude": "41.12",
            "city_longitude": "16.87",
            "scheme_color": "3"
        },
        {
            "id": "1593",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/borgo-san-lorenzo-ztl",
            "introtext": "There is an Access Regulation (ZTL) in San Borgo Lorenzo. ",
            "cityname": "Borgo San Lorenzo - Limited Traffic Zone",
            "city_latitude": "43.46",
            "city_longitude": "11.88",
            "scheme_color": "3"
        },
        {
            "id": "1595",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/comacchio-ztl",
            "introtext": "There  is an Access Regulation (ZTL) in Comacchio.",
            "cityname": "Comacchio - Limited Traffic Zone",
            "city_latitude": "44.13",
            "city_longitude": "12.23",
            "scheme_color": "3"
        },
        {
            "id": "1596",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/camaiore-ztl",
            "introtext": "There are two Access Regulations (ZTL) in Camaiore.",
            "cityname": "Camaiore - Limited Traffic Zone",
            "city_latitude": "43.46",
            "city_longitude": "11.88",
            "scheme_color": "3"
        },
        {
            "id": "1609",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/trani-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Trani.",
            "cityname": "Trani - Limited Traffic Zone",
            "city_latitude": "42.23",
            "city_longitude": "14.39",
            "scheme_color": "3"
        },
        {
            "id": "1597",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/camogli-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Camogli. ",
            "cityname": "Camogli - Limited Traffic Zone",
            "city_latitude": "43.89",
            "city_longitude": "8.04",
            "scheme_color": "3"
        },
        {
            "id": "1599",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/campiglia-marittima-ztl",
            "introtext": "The Access Regulation (ZTL) of Campiglia Marittima covers the historic center.",
            "cityname": "Campiglia Marittima - Limited Traffic Zone",
            "city_latitude": "43.46",
            "city_longitude": "11.88",
            "scheme_color": "3"
        },
        {
            "id": "1601",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/casnate-con-bernate-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Casnate con Bernate.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p>",
            "cityname": "Casnate con Bernate - Limited Traffic Zone",
            "city_latitude": "43.45",
            "city_longitude": "11.87",
            "scheme_color": "3"
        },
        {
            "id": "1603",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/vitorchiano-ztl",
            "introtext": "The Access Regulation (ZTL) of Vitorchiano covers the historic center.",
            "cityname": "Vitorchiano - Limited Traffic Zone",
            "city_latitude": "41.72",
            "city_longitude": "12.67",
            "scheme_color": "3"
        },
        {
            "id": "1604",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/viterbo-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Viterbo.",
            "cityname": "Viterbo - Limited Traffic Zone",
            "city_latitude": "43.40",
            "city_longitude": "11.85",
            "scheme_color": "3"
        },
        {
            "id": "1605",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/vernazza-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Vernazza, also in Corniglia, part of the municipality of Vernazza. ",
            "cityname": "Vernazza - Limited Traffic Zone",
            "city_latitude": "44.06",
            "city_longitude": "9.97",
            "scheme_color": "3"
        },
        {
            "id": "1606",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/varese-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Varese. \r\n<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>",
            "cityname": "Varese - Limited Traffic Zone",
            "city_latitude": "45.80",
            "city_longitude": "8.83",
            "scheme_color": "3"
        },
        {
            "id": "1607",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/friuli-venezia-giulia-region/udine-ar",
            "introtext": "There is a ZTL in Udine.\r\nBut in the following places: Piazza Marconi, Piazza della Libertà and Piazza San Cristoforo it is not active from the 1st of July 2018 until the 31st January 2019.\r\n",
            "cityname": "Udine - Limited Traffic Zone",
            "city_latitude": "46.07",
            "city_longitude": "13.23",
            "scheme_color": "3"
        },
        {
            "id": "1608",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/troia-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Troia.",
            "cityname": "Troia - Limited Traffic Zone",
            "city_latitude": "40.83",
            "city_longitude": "16.55",
            "scheme_color": "3"
        },
        {
            "id": "1610",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/toirano-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Toirano.",
            "cityname": "Toirano - Limited Traffic Zone",
            "city_latitude": "44.4",
            "city_longitude": "8.93",
            "scheme_color": "3"
        },
        {
            "id": "1611",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/abruzzo-region/tagliacozzo-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Tagliacozzo.",
            "cityname": "Tagliacozzo - Limited Traffic Zone",
            "city_latitude": "42.23",
            "city_longitude": "14.39",
            "scheme_color": "3"
        },
        {
            "id": "1612",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/taggia-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Taggia.",
            "cityname": "Taggia - Limited Traffic Zone",
            "city_latitude": "44.17",
            "city_longitude": "9.61",
            "scheme_color": "3"
        },
        {
            "id": "1613",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/sorrento-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Sorrento.",
            "cityname": "Sorrento - Limited Traffic Zone",
            "city_latitude": "45.51",
            "city_longitude": "10.73",
            "scheme_color": "3"
        },
        {
            "id": "1614",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/soave-ztl",
            "introtext": "There is an Access Regulation (ZTL)in Soave.<br />\r\n\t\r\n\r\n<br><p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n",
            "cityname": "Soave - Limited Traffic Zone",
            "city_latitude": "45.89",
            "city_longitude": "12.30",
            "scheme_color": "3"
        },
        {
            "id": "1615",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/santeramo-in-colle-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic centre of Santeramo in Colle.",
            "cityname": "Santeramo in Colle - Limited Traffic Zone",
            "city_latitude": "41.12",
            "city_longitude": "16.87",
            "scheme_color": "3"
        },
        {
            "id": "2380",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/greater-lyon-school-streets",
            "introtext": "Greater Lyon has many school streets - an access regulation - in place.",
            "cityname": "Greater Lyon - school streets",
            "city_latitude": "45.74",
            "city_longitude": "4.84",
            "scheme_color": "3"
        },
        {
            "id": "1616",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/san-casciano-in-val-di-pesa-ztl",
            "introtext": "There is an Access Regulation (ZTL) in San Casciano in Val di Pesa.",
            "cityname": "San Casciano in Val di Pesa - Limited Traffic Zone",
            "city_latitude": "43.68",
            "city_longitude": "10.56",
            "scheme_color": "3"
        },
        {
            "id": "1617",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/ruvo-di-puglia-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Ruvo in Puglia. ",
            "cityname": "Ruvo di Puglia - Limited Traffic Zone",
            "city_latitude": "41.32",
            "city_longitude": "16.28",
            "scheme_color": "3"
        },
        {
            "id": "1618",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sardegna-region/pula-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Pula.",
            "cityname": "Pula - Limited Traffic Zone",
            "city_latitude": "40.56",
            "city_longitude": "8.32",
            "scheme_color": "3"
        },
        {
            "id": "1619",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/abruzzo-region/pratola-peligna-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Pratola Peligna.",
            "cityname": "Pratola Peligna - Limited Traffic Zone",
            "city_latitude": "42.1",
            "city_longitude": "13.87",
            "scheme_color": "3"
        },
        {
            "id": "1620",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/porto-venere-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Porto Venere.",
            "cityname": "Porto Venere - Limited Traffic Zone",
            "city_latitude": "44.06",
            "city_longitude": "9.97",
            "scheme_color": "3"
        },
        {
            "id": "1624",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/pitigliano-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic center of Pitigliano.",
            "cityname": "Pitigliano - Limited Traffic Zone",
            "city_latitude": "42.75",
            "city_longitude": "10.38",
            "scheme_color": "3"
        },
        {
            "id": "1625",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/pietrasanta-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic center of Pietrasanta.",
            "cityname": "Pietrasanta - Limited Traffic Zone",
            "city_latitude": "43.32",
            "city_longitude": "10.50",
            "scheme_color": "3"
        },
        {
            "id": "1626",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/palma-di-montechiaro-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Palma di Montechiaro.",
            "cityname": "Palma di Montechiaro - Limited Traffic Zone",
            "city_latitude": "43.68",
            "city_longitude": "10.56",
            "scheme_color": "3"
        },
        {
            "id": "1627",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/otranto-ztl",
            "introtext": "There are different Access Regulations (ZTL) in Otranto.",
            "cityname": "Otranto - Limited Traffic Zone",
            "city_latitude": "41.32",
            "city_longitude": "16.28",
            "scheme_color": "3"
        },
        {
            "id": "1628",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/ostuni-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic centre of Ostuni.",
            "cityname": "Ostuni - Limited Traffic Zone",
            "city_latitude": "40.06",
            "city_longitude": "17.99",
            "scheme_color": "3"
        },
        {
            "id": "1629",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/montevarchi-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Montevarchi.",
            "cityname": "Montevarchi - Limited Traffic Zone",
            "city_latitude": "43.32",
            "city_longitude": "10.50",
            "scheme_color": "3"
        },
        {
            "id": "1630",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/monterotondo-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic centre of Monterotondo. ",
            "cityname": "Monterotondo - Limited Traffic Zone",
            "city_latitude": "41.21",
            "city_longitude": "13.57",
            "scheme_color": "3"
        },
        {
            "id": "1631",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/monterotondo-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic centre of Monterosso al Mare.",
            "cityname": "Monterosso al Mare - Limited Traffic Zone",
            "city_latitude": "44.23",
            "city_longitude": "8.42",
            "scheme_color": "3"
        },
        {
            "id": "1632",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/montelupo-fiorentino-ztl",
            "introtext": "There are two Access Regulations (ZTL) in Montelupo Fiorentino - ZTL Fibbiana and ZTL Centro Storico.",
            "cityname": "Montelupo Fiorentino - Limited Traffic Zone",
            "city_latitude": "43.32",
            "city_longitude": "10.50",
            "scheme_color": "3"
        },
        {
            "id": "1633",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/minori-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Minori.",
            "cityname": "Minori - Limited Traffic Zone",
            "city_latitude": "40.70",
            "city_longitude": "14.71",
            "scheme_color": "3"
        },
        {
            "id": "1634",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/manduria-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Manduria.",
            "cityname": "Manduria - Limited Traffic Zone",
            "city_latitude": "40.83",
            "city_longitude": "16.55",
            "scheme_color": "3"
        },
        {
            "id": "1635",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/livigno-ztl",
            "introtext": "There are several Access Regulations (ZTL) in Livigno.<br />\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n<br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n",
            "cityname": "Livigno - Limited Traffic Zone",
            "city_latitude": "45.70",
            "city_longitude": "9.67",
            "scheme_color": "3"
        },
        {
            "id": "1636",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/follonica-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Follonica.",
            "cityname": "Follonica - Limited Traffic Zone",
            "city_latitude": "42.75",
            "city_longitude": "10.38",
            "scheme_color": "3"
        },
        {
            "id": "1637",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/castiglion-fiorentino-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Castiglion Fiorentino.",
            "cityname": "Castiglione Fiorentino - Limited Traffic Zone",
            "city_latitude": "44.08",
            "city_longitude": "10.10",
            "scheme_color": "3"
        },
        {
            "id": "1638",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/fucecchio-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Fucecchio.",
            "cityname": "Fucecchio - Limited Traffic Zone",
            "city_latitude": "42.75",
            "city_longitude": "10.38",
            "scheme_color": "3"
        },
        {
            "id": "1639",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/certaldo-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic center of Certaldo.",
            "cityname": "Certaldo - Limited Traffic Zone",
            "city_latitude": "43.32",
            "city_longitude": "10.50",
            "scheme_color": "3"
        },
        {
            "id": "1640",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/castiglione-della-pescaia-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Castiglione della Pescaia.",
            "cityname": "Castiglione della Pescaia - Limited Traffic Zone",
            "city_latitude": "43.34",
            "city_longitude": "11.05",
            "scheme_color": "3"
        },
        {
            "id": "1642",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/mondovi-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the district \"Breo\" of Mondovì.<br>\r\n\r\n\t<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n",
            "cityname": "Mondovi - Limited Traffic Zone",
            "city_latitude": "44.39",
            "city_longitude": "7.82",
            "scheme_color": "3"
        },
        {
            "id": "1643",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/felizzano-ztl",
            "introtext": "There is an Access Regulation (ZTL)in Felizzano.<br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Felizzano - Limited Traffic Zone",
            "city_latitude": "44.90",
            "city_longitude": "8.21",
            "scheme_color": "3"
        },
        {
            "id": "1644",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/colico-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Colico.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p>",
            "cityname": "Colico - Limited Traffic Zone",
            "city_latitude": "45.51",
            "city_longitude": "9.70",
            "scheme_color": "3"
        },
        {
            "id": "1645",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/fideza-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Fideza.\r\n<br><br>\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/322-key-access-regulations/italy-access-regulations/2061-winter-emergency-measures-in-emilia-romagna-lombardia\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 31 March 2019.</p>\r\n",
            "cityname": "Fideza - Limited Traffic Zone",
            "city_latitude": "43.49",
            "city_longitude": "11.62",
            "scheme_color": "3"
        },
        {
            "id": "1646",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/friuli-venezia-giulia-region/grado-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Grado.",
            "cityname": "Grado - Limited Traffic Zone",
            "city_latitude": "45.65",
            "city_longitude": "13.78",
            "scheme_color": "3"
        },
        {
            "id": "2315",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/oxford-traffic-filters",
            "introtext": "Oxford has a low emission zone for buses, a zero emission zone and an access regulation in place.",
            "cityname": "Oxford - Traffic Filters",
            "city_latitude": "51.75",
            "city_longitude": "-1.25",
            "scheme_color": "3"
        },
        {
            "id": "1648",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/iseo-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Iseo.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p>",
            "cityname": "Iseo - Limited Traffic Zone",
            "city_latitude": "45.99",
            "city_longitude": "9.26",
            "scheme_color": "3"
        },
        {
            "id": "1649",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/lacco-ameno-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Lacco Ameno.",
            "cityname": "Lacco Ameno - Limited Traffic Zone",
            "city_latitude": "41.07",
            "city_longitude": "14.33",
            "scheme_color": "3"
        },
        {
            "id": "1650",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/gabbice-mare-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic centre of Gabicce mare. ",
            "cityname": "Gabbice mare - Limited Traffic Zone",
            "city_latitude": "43.53",
            "city_longitude": "13.25",
            "scheme_color": "3"
        },
        {
            "id": "1652",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/crespi-d-adda-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Crespi d'Adda during public holidays.<p><br><br>\r\n\tList of Lombardia comunes that are covered within the Lombardia region LEZ can be found <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/lombarida-comunes\">here</a>.</p>\r\n\r\n<p>\r\n\tFor more details for the winter LEZs, see the <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/outside-the-cities\">Lombardia outside the Cities</a> page.</p>\r\n\r\n<p>",
            "cityname": "Crespi d Adda - Limited Traffic Zone",
            "city_latitude": "45.51",
            "city_longitude": "9.70",
            "scheme_color": "3"
        },
        {
            "id": "1653",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/lastra-a-signa-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Lastra a Signa.",
            "cityname": "Lastra a Signa - Limited Traffic Zone",
            "city_latitude": "43.77",
            "city_longitude": "11.11",
            "scheme_color": "3"
        },
        {
            "id": "1654",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/molfetta-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Molfetta.",
            "cityname": "Molfetta - Limited Traffic Zone",
            "city_latitude": "41.11",
            "city_longitude": "16.69",
            "scheme_color": "3"
        },
        {
            "id": "1656",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/gravina-in-puglia-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Gravina in Puglia.",
            "cityname": "Gravina di Puglia - Limited Traffic Zone",
            "city_latitude": "41.15",
            "city_longitude": "16.41",
            "scheme_color": "3"
        },
        {
            "id": "1657",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/calabria-region/cosenza-ztl",
            "introtext": "There is an Access Regulation (ZTL)in Cosenza.\r\n",
            "cityname": "Cosenza - Limited Traffic Zone",
            "city_latitude": "38.11",
            "city_longitude": "15.65",
            "scheme_color": "3"
        },
        {
            "id": "1658",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/fiumicino-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Fuimicino covering the Airport Leonardoo da Vinci.",
            "cityname": "Fiumicino - Limited Traffic Zone",
            "city_latitude": "42.40",
            "city_longitude": "12.85",
            "scheme_color": "3"
        },
        {
            "id": "1659",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/foligno-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Foligno.",
            "cityname": "Foligno - Limited Traffic Zone",
            "city_latitude": "42.79",
            "city_longitude": "12.42",
            "scheme_color": "3"
        },
        {
            "id": "1660",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/galatina-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Galatina.",
            "cityname": "Galatina - Limited Traffic Zone",
            "city_latitude": "41.32",
            "city_longitude": "16.28",
            "scheme_color": "3"
        },
        {
            "id": "1661",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/nocera-inferiore-ztl",
            "introtext": "There is an Access Regulation (ZTL) in Nocera Inferiore.",
            "cityname": "Nocera Inferiore - Limited Traffic Zone",
            "city_latitude": "41.18",
            "city_longitude": "14.36",
            "scheme_color": "3"
        },
        {
            "id": "1662",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/forli-ztl",
            "introtext": "\r\n<p>\r\n\tThere is an Access Regulation (ZTL) in Forl&igrave;.&nbsp;</p>\r\n\r\n<p>\r\n\tThere is also a LEZ in place in <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/emilia-romagna/forli\" target=\"_blank\">Forl&igrave;</a>.</p>\r\n",
            "cityname": "Forlì - Limited Traffic Zone",
            "city_latitude": "44.23",
            "city_longitude": "12.05",
            "scheme_color": "3"
        },
        {
            "id": "1663",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/ceglie-messapica-ztl",
            "introtext": "There is an Access Regulation (ZTL) in the historic center of Ceglie Messapica.",
            "cityname": "Ceglie Messapica - Limited Traffic Zone",
            "city_latitude": "40.83",
            "city_longitude": "16.55",
            "scheme_color": "3"
        },
        {
            "id": "1664",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/centuripe-ar",
            "introtext": "There is an Access Regulation (ZTL) in Centuripe.",
            "cityname": "Centuripe - Limited Traffic Zone",
            "city_latitude": "37.51",
            "city_longitude": "15.08",
            "scheme_color": "3"
        },
        {
            "id": "1665",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/braunwald-carfree",
            "introtext": "CH",
            "cityname": "Braunwald - car-free",
            "city_latitude": "46.93",
            "city_longitude": "8.98",
            "scheme_color": "3"
        },
        {
            "id": "1666",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/bettmeralp-carfree",
            "introtext": "CH",
            "cityname": "Bettmeralp - car-free",
            "city_latitude": "46.39",
            "city_longitude": "8.06",
            "scheme_color": "3"
        },
        {
            "id": "1679",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/reutlingen-ar",
            "introtext": "",
            "cityname": "Reutlingen - Transit Ban",
            "city_latitude": "48.49",
            "city_longitude": "9.21",
            "scheme_color": "3"
        },
        {
            "id": "2310",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/paris-neighbourhoods",
            "introtext": "",
            "cityname": "Paris - neighbourhoods",
            "city_latitude": "48.86",
            "city_longitude": "2.35",
            "scheme_color": "3"
        },
        {
            "id": "1696",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/poland/gdynia-ar",
            "introtext": "",
            "cityname": "Gdynia - lorry LTZ",
            "city_latitude": "54.51",
            "city_longitude": "18.53",
            "scheme_color": "3"
        },
        {
            "id": "1688",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/koeln-cologne-transit-ban",
            "introtext": "Köln also has a <a title=\"Low Emission Zone\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/köln\">Low Emission Zone</a> in place.",
            "cityname": "Köln (Cologne) - Transit Ban",
            "city_latitude": "50.94",
            "city_longitude": "6.96",
            "scheme_color": "3"
        },
        {
            "id": "1689",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/london-dvs-and-hgv-safety-permit-scheme",
            "introtext": "UK-LO",
            "cityname": "London - Direct Vision Standard and Safety Permit for Lorries",
            "city_latitude": "51.51",
            "city_longitude": "-0.13",
            "scheme_color": "3"
        },
        {
            "id": "1690",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-ar",
            "introtext": "",
            "cityname": "Stockholm car & coach-free",
            "city_latitude": "59.33",
            "city_longitude": "18.06",
            "scheme_color": "3"
        },
        {
            "id": "1703",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/delft-carfree",
            "introtext": "",
            "cityname": "Delft - car-free",
            "city_latitude": "52.02",
            "city_longitude": "4.36",
            "scheme_color": "3"
        },
        {
            "id": "1929",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/trondheim-studded-tire-charge",
            "introtext": "The new Norwegian legislation allows all kinds of measures to reduce PM and NO2. Norway has a congestion charging scheme for studded tyre use in cities. Bergen and Oslo have already established the scheme, Trondheim and Stavenger will follow.\r\nStudded tyres are often used in Norway in winter. However, in urban areas, the studded tyres damage the street surface and also raise the PM levels.\r\n",
            "cityname": "Trondheim - Studded Tyre Charge",
            "city_latitude": "63.44",
            "city_longitude": "10.39",
            "scheme_color": "3"
        },
        {
            "id": "1930",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/goeteborg-gothenberg-studded-tire-ban",
            "introtext": "There is a studded tyre ban in Gothenburg (Friggagatan and Odinsgatan). ",
            "cityname": "Göteborg (Gothenburg) - Studded Tyre Ban",
            "city_latitude": "57.71",
            "city_longitude": "11.97",
            "scheme_color": "3"
        },
        {
            "id": "2334",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/oxford-low traffic-neighbourhoods",
            "introtext": "Oxford has a low emission zone for buses, a zero emission zone and and three access regulation in place: one for coaches, one called traffic filters and one low traffic neighbourhood.",
            "cityname": "Oxford - low traffic neighbourhoods",
            "city_latitude": "51.75",
            "city_longitude": "-1.25",
            "scheme_color": "3"
        },
        {
            "id": "1927",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/bergen-studded-tire-charge",
            "introtext": "The new Norwegian legislation allows all kinds of measures to reduce PM and NO2. Norway has a congestion charging scheme for studded tyre use in cities. Bergen and Oslo have already established the scheme, Trondheim and Stavenger will follow.\r\nStudded tyres are often used in Norway in winter. However, in urban areas, the studded tyres damage the street surface and also raise the PM levels.\r\n",
            "cityname": "Bergen - Studded Tyre Charge",
            "city_latitude": "60.39",
            "city_longitude": "5.32",
            "scheme_color": "3"
        },
        {
            "id": "1926",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/norway-mainmenu-197/oslo-studded-tire-charge",
            "introtext": "The new Norwegian legislation allows all kinds of measures to reduce PM and NO2. Norway has a congestion charging scheme for studded tyre use in cities. Bergen and Oslo have already established the scheme, Trondheim and Stavenger will follow.\nStudded tyres are often used in Norway in winter. However, in urban areas, the studded tyres damage the street surface and also raise the PM levels.\n",
            "cityname": "Oslo - Studded Tyre Charge",
            "city_latitude": "59.91",
            "city_longitude": "10.75",
            "scheme_color": "3"
        },
        {
            "id": "2206",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/poland/gliwice-limited-traffic-zone",
            "introtext": "",
            "cityname": "Gliwice - Limited Traffic Zone",
            "city_latitude": "50.29",
            "city_longitude": "18.67",
            "scheme_color": "3"
        },
        {
            "id": "2083",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/ourense-ar",
            "introtext": "",
            "cityname": "Ourense - Limited Traffic Zone",
            "city_latitude": "42.33",
            "city_longitude": "-7.86",
            "scheme_color": "3"
        },
        {
            "id": "1931",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/stockholm-studded-tire-ban",
            "introtext": "There is a studded tyre ban in Stockholm (streets affected: Hornsgatan, Fleminggatan and Kungsgatan).",
            "cityname": "Stockholm - Studded Tyre Ban",
            "city_latitude": "59.33",
            "city_longitude": "18.06",
            "scheme_color": "3"
        },
        {
            "id": "1932",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/sweden-mainmenu-248/uppsala-studded-tire-ban",
            "introtext": "There is a studded tyre ban in Uppsala (Kungsgatan and Vaksalagatan).",
            "cityname": "Uppsala - Studded Tyre Ban",
            "city_latitude": "59.85",
            "city_longitude": "17.63",
            "scheme_color": "3"
        },
        {
            "id": "1953",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/france/la-rochelle",
            "introtext": "france",
            "cityname": "La Rochelle - delivery",
            "city_latitude": "46.16",
            "city_longitude": "-1.15",
            "scheme_color": "3"
        },
        {
            "id": "1954",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/abano-terme-ztl",
            "introtext": "The Access Regulation (ZTL) of Abano Terme covers part of the historic center.\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 2019.</p>\r\n",
            "cityname": "Abano Terme - Limited Traffic Zone",
            "city_latitude": "45.21",
            "city_longitude": "11.47",
            "scheme_color": "3"
        },
        {
            "id": "1955",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/agropoli-ztl",
            "introtext": "Agropoli has an access regulation in place.",
            "cityname": "Agropoli - Limited Traffic Zone",
            "city_latitude": "40.35",
            "city_longitude": "14.99",
            "scheme_color": "3"
        },
        {
            "id": "1956",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/andria-ztl",
            "introtext": "Andria in Puglia region of Italy has an access regulation in place.",
            "cityname": "Andria - Limited Traffic Zone",
            "city_latitude": "41.23",
            "city_longitude": "16.29",
            "scheme_color": "3"
        },
        {
            "id": "1957",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/bevagna-ztl",
            "introtext": "Bevagna in the Umbria region of Italy has an access regulation in place since 15 July 2020.",
            "cityname": "Bevagna - Limited Traffic Zone",
            "city_latitude": "42.93",
            "city_longitude": "12.60",
            "scheme_color": "3"
        },
        {
            "id": "1972",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/modugno-ztl",
            "introtext": "Modugno has a ZTL access regulation in place.",
            "cityname": "Modugno - Limited Traffic Zone",
            "city_latitude": "41.08",
            "city_longitude": "16.77",
            "scheme_color": "3"
        },
        {
            "id": "1958",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia-region/brivio-ztl",
            "introtext": "The Access Regulation (ZTL) of Brivio covers part of the historic center since 13 June 2016.\r\n<p>\r\n\tEmilia Romagna, Lombardia, Piemonte and Veneto have a <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/winter-emergency-measures-in-emilia-romagna-lombardia-piemont-and-veneto\" target=\"_blank\">winter emergency scheme</a> in place from 1 October 2018 - 2019.</p>\r\n",
            "cityname": "Brivio - Limited Traffic Zone",
            "city_latitude": "45.74",
            "city_longitude": "9.44",
            "scheme_color": "3"
        },
        {
            "id": "1959",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/castellabate-ztl",
            "introtext": "Castellabate has an access regulation ZTL in place.",
            "cityname": "Castellabate - Limited Traffic Zone",
            "city_latitude": "40.28",
            "city_longitude": "14.95",
            "scheme_color": "3"
        },
        {
            "id": "1960",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/castellamare-del-golfo-ztl",
            "introtext": "Castellamare del golfo has a ZTL access regulation in place.",
            "cityname": "Castellamare del golfo - Limited Traffic Zone",
            "city_latitude": "38.02",
            "city_longitude": "12.88",
            "scheme_color": "3"
        },
        {
            "id": "1961",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sardegna-region/castelsardo-ztl",
            "introtext": "Castelsardo has a ZTL access regulation in place.",
            "cityname": "Castelsardo - Limited Traffic Zone",
            "city_latitude": "40.91",
            "city_longitude": "8.71",
            "scheme_color": "3"
        },
        {
            "id": "1962",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/cefalu-ztl",
            "introtext": "Cefalu' has a ZTL access regulation in place.",
            "cityname": "Cefalu - Limited Traffic Zone",
            "city_latitude": "38.03",
            "city_longitude": "14.02",
            "scheme_color": "3"
        },
        {
            "id": "2003",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/spaarndam-ar",
            "introtext": "",
            "cityname": "Spaarndam - transit ban",
            "city_latitude": "52.41",
            "city_longitude": "4.68",
            "scheme_color": "3"
        },
        {
            "id": "1964",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/cerignola-ztl",
            "introtext": "Cerignola has a ZTL access regulation in place.",
            "cityname": "Cerignola - Limited Traffic Zone",
            "city_latitude": "41.26",
            "city_longitude": "15.90",
            "scheme_color": "3"
        },
        {
            "id": "1965",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/frattamaggiore-ztl",
            "introtext": "Frattamaggiore has a ZTL access regulation in place.",
            "cityname": "Frattamaggiore - Limited Traffic Zone",
            "city_latitude": "40.93",
            "city_longitude": "14.27",
            "scheme_color": "3"
        },
        {
            "id": "1966",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/gambassi-terme-ztl",
            "introtext": "Gambassi Terme has a ZTL access regulation in place.",
            "cityname": "Gambassi Terme - Limited Traffic Zone",
            "city_latitude": "43.32",
            "city_longitude": "10.57",
            "scheme_color": "3"
        },
        {
            "id": "1969",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/marciana-marina-ztl",
            "introtext": "Marciana Marina has a ZTL access regulation in place.",
            "cityname": "Marciana Marina - Limited Traffic Zone",
            "city_latitude": "42.80",
            "city_longitude": "10.19",
            "scheme_color": "3"
        },
        {
            "id": "1967",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/giaveno-ztl",
            "introtext": "Giaveno has a ZTL access regulation in place.",
            "cityname": "Giaveno - Limited Traffic Zone",
            "city_latitude": "45.04",
            "city_longitude": "7.34",
            "scheme_color": "3"
        },
        {
            "id": "1968",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/molise-region/isernia-ztl",
            "introtext": "Isernia has a ZTL access regulation in place.",
            "cityname": "Isernia - Limited Traffic Zone",
            "city_latitude": "41.60",
            "city_longitude": "14.23",
            "scheme_color": "3"
        },
        {
            "id": "1970",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/maruggio-ztl",
            "introtext": "Maruggio has a ZTL access regulation in place.",
            "cityname": "Maruggio - Limited Traffic Zone",
            "city_latitude": "40.32",
            "city_longitude": "17.57",
            "scheme_color": "3"
        },
        {
            "id": "1973",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/montepulciano-ztl",
            "introtext": "Montepulciano has a ZTL access regulation in place.",
            "cityname": "Montepulciano - Limited Traffic Zone",
            "city_latitude": "43.09",
            "city_longitude": "11.78",
            "scheme_color": "3"
        },
        {
            "id": "1974",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/narni-ztl",
            "introtext": "Narni has a ZTL access regulation in place.",
            "cityname": "Narni - Limited Traffic Zone",
            "city_latitude": "42.51",
            "city_longitude": "12.52",
            "scheme_color": "3"
        },
        {
            "id": "1975",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/occhieppo-superiore-ztl",
            "introtext": "Occhieppo Superiore has a ZTL access regulation in place.",
            "cityname": "Occhieppo Superiore - Limited Traffic Zone",
            "city_latitude": "45.56",
            "city_longitude": "8.05",
            "scheme_color": "3"
        },
        {
            "id": "1976",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sardegna-region/olbia-ztl",
            "introtext": "Olbia has a ZTL access regulation in place.",
            "cityname": "Olbia - Limited Traffic Zone",
            "city_latitude": "40.92",
            "city_longitude": "9.50",
            "scheme_color": "3"
        },
        {
            "id": "1977",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/orbetello-ztl",
            "introtext": "Orbetello has a ZTL access regulation in place.",
            "cityname": "Orbetello - Limited Traffic Zone",
            "city_latitude": "42.44",
            "city_longitude": "11.22",
            "scheme_color": "3"
        },
        {
            "id": "1978",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/palestrina-ztl",
            "introtext": "Palestrina has a ZTL access regulation in place.",
            "cityname": "Palestrina - Limited Traffic Zone",
            "city_latitude": "41.83",
            "city_longitude": "12.88",
            "scheme_color": "3"
        },
        {
            "id": "1979",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/pietra-ligure-ztl",
            "introtext": "Pietra Ligure has a ZTL access regulation in place.",
            "cityname": "Pietra Ligure - Limited Traffic Zone",
            "city_latitude": "44.14",
            "city_longitude": "8.28",
            "scheme_color": "3"
        },
        {
            "id": "1980",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/pomigliano-d-arco-ztl",
            "introtext": "Pomigliano d'Arco has a ZTL access regulation in place.",
            "cityname": "Pomigliano d Arco - Limited Traffic Zone",
            "city_latitude": "40.90",
            "city_longitude": "14.38",
            "scheme_color": "3"
        },
        {
            "id": "1981",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/ravello-ztl",
            "introtext": "Ravello has a ZTL access regulation in place.",
            "cityname": "Ravello - Limited Traffic Zone",
            "city_latitude": "43.56",
            "city_longitude": "12.30",
            "scheme_color": "3"
        },
        {
            "id": "1982",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/sicilia-region/regalbuto-ztl",
            "introtext": "Regalbuto  has a ZTL access regulation in place from 13 July - 30 September.",
            "cityname": "Regalbuto - Limited Traffic Zone",
            "city_latitude": "37.65",
            "city_longitude": "14.64",
            "scheme_color": "3"
        },
        {
            "id": "1983",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/liguria-region/riva-ligure-ztl",
            "introtext": "Riva Ligure has an access regulation in place.",
            "cityname": "Riva Ligure - Limited Traffic Zone",
            "city_latitude": "43.83",
            "city_longitude": "7.88",
            "scheme_color": "3"
        },
        {
            "id": "1984",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/rutigliano-ztl",
            "introtext": "Rutigliano has an access regulation in place.",
            "cityname": "Rutigliano - Limited Traffic Zone",
            "city_latitude": "41.00",
            "city_longitude": "17.00",
            "scheme_color": "3"
        },
        {
            "id": "1985",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/marche-region/san-benedetto-del-tronto-ztl",
            "introtext": "San Benedetto del Tronto has an access regulation in place.",
            "cityname": "San Benedetto del Tronto - Limited Traffic Zone",
            "city_latitude": "42.90",
            "city_longitude": "13.88",
            "scheme_color": "3"
        },
        {
            "id": "1986",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/campania-region/sant-agata-de-goti-ztl",
            "introtext": "Sant Agata de Goti has an access regulation in place.",
            "cityname": "Sant Agata de Goti - Limited Traffic Zone",
            "city_latitude": "41.08",
            "city_longitude": "14.49",
            "scheme_color": "3"
        },
        {
            "id": "1987",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia-region/senago-ztl",
            "introtext": "Senago has an access regulation in place.",
            "cityname": "Senago - Limited Traffic Zone",
            "city_latitude": "45.57",
            "city_longitude": "9.11",
            "scheme_color": "3"
        },
        {
            "id": "1988",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia/sirmione-ztl",
            "introtext": "Sirmione has an access regulation in place.",
            "cityname": "Sirmione - Limited Traffic Zone",
            "city_latitude": "45.49",
            "city_longitude": "10.60",
            "scheme_color": "3"
        },
        {
            "id": "1989",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/terracina-ztl",
            "introtext": "Terracina has an access regulation in place.",
            "cityname": "Terracina - Limited Traffic Zone",
            "city_latitude": "41.28",
            "city_longitude": "13.20",
            "scheme_color": "3"
        },
        {
            "id": "1990",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/toscana-tuscany/terranuova-bracciolini-ztl",
            "introtext": "Terranuova Bracciolini has an access regulation in place.",
            "cityname": "Terranuova Bracciolini - Limited Traffic Zone",
            "city_latitude": "43.55",
            "city_longitude": "11.58",
            "scheme_color": "3"
        },
        {
            "id": "1991",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/torri-del-benaco-ztl",
            "introtext": "Torri del Benaco has an access regulation in place.",
            "cityname": "Torri del Benaco - Limited Traffic Zone",
            "city_latitude": "45.60",
            "city_longitude": "10.68",
            "scheme_color": "3"
        },
        {
            "id": "1992",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lombardia-region/tremezzina-ztl",
            "introtext": "Tremezzina has an access regulation in place.",
            "cityname": "Tremezzina - Limited Traffic Zone",
            "city_latitude": "45.98",
            "city_longitude": "9.22",
            "scheme_color": "3"
        },
        {
            "id": "1993",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/vieste-ztl",
            "introtext": "Vieste has an access regulation in place.",
            "cityname": "Vieste - Limited Traffic Zone",
            "city_latitude": "41.88",
            "city_longitude": "16.17",
            "scheme_color": "3"
        },
        {
            "id": "1994",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/cerveteri-ztl",
            "introtext": "Cerveteri has an access regulation in place.",
            "cityname": "Cerveteri - Limited Traffic Zone",
            "city_latitude": "41.99",
            "city_longitude": "12.09",
            "scheme_color": "3"
        },
        {
            "id": "1995",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/martignano-ztl",
            "introtext": "Martignano has an access regulation in place.",
            "cityname": "Martignano - Limited Traffic Zone",
            "city_latitude": "40.23",
            "city_longitude": "18.25",
            "scheme_color": "3"
        },
        {
            "id": "1996",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/lazio-region/veroli-ztl",
            "introtext": "Veroli has an access regulation in place.",
            "cityname": "Veroli - Limited Traffic Zone",
            "city_latitude": "41.69",
            "city_longitude": "13.41",
            "scheme_color": "3"
        },
        {
            "id": "1997",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/grottaglie-ztl",
            "introtext": "Grottaglie has an access regulation in place.",
            "cityname": "Grottaglie - Limited Traffic Zone",
            "city_latitude": "40.53",
            "city_longitude": "17.43",
            "scheme_color": "3"
        },
        {
            "id": "1998",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/oria-ztl",
            "introtext": "Oria has an access regulation in place.",
            "cityname": "Oria - Limited Traffic Zone",
            "city_latitude": "40.49",
            "city_longitude": "17.64",
            "scheme_color": "3"
        },
        {
            "id": "1999",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/porto-cesareo-ztl",
            "introtext": "Porto Cesareo has an access regulation in place.",
            "cityname": "Porto Cesareo - Limited Traffic Zone",
            "city_latitude": "40.26",
            "city_longitude": "17.89",
            "scheme_color": "3"
        },
        {
            "id": "2000",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/puglia-region/sannicandro-ztl",
            "introtext": "Sannicandro has an access regulation in place.",
            "cityname": "Sannicandro - Limited Traffic Zone",
            "city_latitude": "41.83",
            "city_longitude": "15.56",
            "scheme_color": "3"
        },
        {
            "id": "2001",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/umbria/gubbio-ztl",
            "introtext": "Gubbio has an access regulation in place.",
            "cityname": "Gubbio - Limited Traffic Zone",
            "city_latitude": "43.35",
            "city_longitude": "12.57",
            "scheme_color": "3"
        },
        {
            "id": "2002",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/veneto/carmignano-di-brenta-ztl",
            "introtext": "Carmignano di Brenta has an access regulation in place.",
            "cityname": "Carmignano di Brenta - Limited Traffic Zone",
            "city_latitude": "45.62",
            "city_longitude": "11.70",
            "scheme_color": "3"
        },
        {
            "id": "2004",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/dortmund-transit-ban",
            "introtext": "",
            "cityname": "Dortmund - Transit Ban",
            "city_latitude": "51.51",
            "city_longitude": "7.46",
            "scheme_color": "3"
        },
        {
            "id": "2034",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/amersfoort-carfree",
            "introtext": "",
            "cityname": "Amersfoort - car-free",
            "city_latitude": "52.02",
            "city_longitude": "4.36",
            "scheme_color": "3"
        },
        {
            "id": "2035",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/nantes-ar",
            "introtext": "",
            "cityname": "Nantes - Limited Traffic Zone",
            "city_latitude": "47.21",
            "city_longitude": "-1.55",
            "scheme_color": "3"
        },
        {
            "id": "2033",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/leuven-ar",
            "introtext": "",
            "cityname": "Leuven - car-free",
            "city_latitude": "50.87",
            "city_longitude": "4.70",
            "scheme_color": "3"
        },
        {
            "id": "2032",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/pamplona-ar",
            "introtext": "",
            "cityname": "Pamplona - Limited Traffic Zone",
            "city_latitude": "42.81",
            "city_longitude": "-1.64",
            "scheme_color": "3"
        },
        {
            "id": "2443",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/ponferrada-ar",
            "introtext": "",
            "cityname": "Ponferrada - Limited Traffic Zone",
            "city_latitude": "42.55",
            "city_longitude": "-6.59",
            "scheme_color": "3"
        },
        {
            "id": "2322",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/monaco/monaco-delivery",
            "introtext": "Monaco has established an access regulation in its city centre for <b>delivery</b> vehicles. ",
            "cityname": "Monaco - delivery",
            "city_latitude": "43.37",
            "city_longitude": "7.42",
            "scheme_color": "3"
        },
        {
            "id": "2103",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/granada-ar",
            "introtext": "",
            "cityname": "Granada - Limited Traffic Zone",
            "city_latitude": "37.17",
            "city_longitude": "-3.59",
            "scheme_color": "3"
        },
        {
            "id": "2084",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/oviedo-ar",
            "introtext": "",
            "cityname": "Oviedo - Limited Traffic Zone",
            "city_latitude": "43.36",
            "city_longitude": "-5.84",
            "scheme_color": "3"
        },
        {
            "id": "2114",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/amsterdam-coaches",
            "introtext": "",
            "cityname": "Amsterdam - Coaches",
            "city_latitude": "52.37",
            "city_longitude": "4.89",
            "scheme_color": "3"
        },
        {
            "id": "2079",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/burgos-ar",
            "introtext": "",
            "cityname": "Burgos - Limited Traffic Zone",
            "city_latitude": "42.35",
            "city_longitude": "-3.7",
            "scheme_color": "3"
        },
        {
            "id": "2224",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/rennes-limited-traffic-zone",
            "introtext": "LTZ",
            "cityname": "Rennes - Limited Traffic Zone",
            "city_latitude": "45.11",
            "city_longitude": "1.67",
            "scheme_color": "3"
        },
        {
            "id": "2115",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/oxford-coaches",
            "introtext": "",
            "cityname": "Oxford - Coaches",
            "city_latitude": "51.75",
            "city_longitude": "-1.25",
            "scheme_color": "3"
        },
        {
            "id": "2116",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/antwerpen-antwerp-ar",
            "introtext": "",
            "cityname": "Antwerpen - car-free & pedestrian zones",
            "city_latitude": "51.22",
            "city_longitude": "4.40",
            "scheme_color": "3"
        },
        {
            "id": "2130",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-regulation",
            "introtext": "<p>\r\n\tMadrid has various schemes in place:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid\" title=\"low emission zone\">low emission parking scheme</a>&nbsp;that favours less polluting vehicles</li>\r\n\t<li>\r\n\t\ta <a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">low emission traffic limited zone</a>&nbsp;vehicles have to be owned by residents or zero emission</li>\r\n\t<li>\r\n\t\tan <a href=\"/countries-mainmenu-147/spain/madrid-odd-and-even-numberplates\">emergency scheme</a>&nbsp;</li>\r\n\t<li>\r\n\t\ta <a href=\"/countries-mainmenu-147/spain/madrid-weight\" title=\"weight restriction\">weight regulation</a></li>\r\n</ul>\r\n\r\n<p>\r\n\t<strong>NEW! From&nbsp;30 November 2018&nbsp;<a href=\"http://urbanaccessregulations.eu/countries-mainmenu-147/spain/madrid-access-restriction\">Central Madrid</a>&nbsp;</strong>is in place. The&nbsp;existing APRs (&Aacute;reas de Prioridad Residencial &nbsp;= areas where residents have priority) be extended and united into one big APR that is called Madrid Central.</p>\r\n\r\n<p>\r\n\tIt will be of informative character for the first two months and will be fully enforced from <strong>February 2019 on</strong>. The APR Central Madrid will cover practically the entire downtown area of Madrid.&nbsp;</p>\r\n\r\n<p>\r\n\tThe standards in the Central Madrid low emission zone are gradually tightened until a zero emission zone is reached in 2025.</p>\r\n\r\n<p>\r\n\tThe Grand Via is planned to be car-free by summer 2019.<br />\r\n\tMadrid is one of 4 cities that have stated they wish to remove diesel vehicles from the city. As part of this, the city plans to increase the numbers of access restrictions for private cars.</p>\r\n",
            "cityname": "Madrid - pedestrian",
            "city_latitude": "40.42",
            "city_longitude": "-3.70",
            "scheme_color": "3"
        },
        {
            "id": "2144",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/coimbra-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Coimbra - Limited Traffic Zone",
            "city_latitude": "40.20",
            "city_longitude": "-8.41",
            "scheme_color": "3"
        },
        {
            "id": "2145",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/chaves-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Chaves - Limited Traffic Zone",
            "city_latitude": "41.74",
            "city_longitude": "-7.46",
            "scheme_color": "3"
        },
        {
            "id": "2146",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/lisbon-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Lisbon - Limited Traffic Zone",
            "city_latitude": "38.72",
            "city_longitude": "-9.13",
            "scheme_color": "3"
        },
        {
            "id": "2148",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/moncao-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Moncao - Limited Traffic Zone",
            "city_latitude": "42.07",
            "city_longitude": "-8.48",
            "scheme_color": "3"
        },
        {
            "id": "2204",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/france/grenoble-limited-traffic-zone",
            "introtext": "LTZ",
            "cityname": "Grenoble - Limited Traffic Zone",
            "city_latitude": "45.18",
            "city_longitude": "5.72",
            "scheme_color": "3"
        },
        {
            "id": "2149",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/santa-maria-da-feira-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Santa Maria da Feira - Limited Traffic Zone",
            "city_latitude": "40.92",
            "city_longitude": "-8.54",
            "scheme_color": "3"
        },
        {
            "id": "2152",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/gaia-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Gaia - Limited Traffic Zone",
            "city_latitude": "41.21",
            "city_longitude": "-8.61",
            "scheme_color": "3"
        },
        {
            "id": "2153",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/seixal-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Seixal - Limited Traffic Zone",
            "city_latitude": "38.64",
            "city_longitude": "-9.09",
            "scheme_color": "3"
        },
        {
            "id": "2155",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/guimaraes-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Guimaraes - Limited Traffic Zone",
            "city_latitude": "41.44",
            "city_longitude": "-8.29",
            "scheme_color": "3"
        },
        {
            "id": "2156",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/portugal/porto-ltz",
            "introtext": "There are several (13) LTZs in Portugal. Probably more. These limit access to a certain part of the city for certain vehicles. ",
            "cityname": "Porto - Limited Traffic Zone",
            "city_latitude": "41.15",
            "city_longitude": "-8.62",
            "scheme_color": "3"
        },
        {
            "id": "2286",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/bruxelles-brussel-brussels-circulation-plan",
            "introtext": "",
            "cityname": "Bruxelles - Brussel (Brussels) - low traffic neighbourhoods",
            "city_latitude": "50.85",
            "city_longitude": "4.35",
            "scheme_color": "3"
        },
        {
            "id": "2202",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/valencia-ltz",
            "introtext": "Valencia has an emergency scheme that comes into place in cases of high pollution events, a limited traffic zone and a low emission zone in place.",
            "cityname": "Valencia - Limited Traffic Zone",
            "city_latitude": "39.47",
            "city_longitude": "-0.38",
            "scheme_color": "3"
        },
        {
            "id": "2271",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/belgium/mechelen-ar",
            "introtext": "",
            "cityname": "Mechelen - car-free",
            "city_latitude": "51.02",
            "city_longitude": "4.47",
            "scheme_color": "3"
        },
        {
            "id": "2273",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/spain/rivas-vaciamadrid-limited-traffic-zone",
            "introtext": "Rivas-Vaciamadrid has implemented limited traffic zones around schools in 2021.",
            "cityname": "Rivas-Vaciamadrid - school streets",
            "city_latitude": "40.33",
            "city_longitude": "-3.51",
            "scheme_color": "3"
        },
        {
            "id": "2274",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/united-kingdom-mainmenu-205/newcastle-limited-traffic-zone",
            "introtext": "",
            "cityname": "Newcastle - Limited Traffic Zone",
            "city_latitude": "54.97",
            "city_longitude": "-1.61",
            "scheme_color": "3"
        },
        {
            "id": "2314",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/italy-mainmenu-81/piemonte-region/alessandria-limited-traffic-zone",
            "introtext": "",
            "cityname": "Alessandria - Limited Traffic Zone",
            "city_latitude": "44.55",
            "city_longitude": "8.37",
            "scheme_color": "3"
        },
        {
            "id": "2348",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/haarlem-car-free",
            "introtext": "",
            "cityname": "Haarlem - car-free",
            "city_latitude": "52.38",
            "city_longitude": "4.64",
            "scheme_color": "3"
        },
        {
            "id": "2350",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/gimmelwald-carfree",
            "introtext": "CH",
            "cityname": "Gimmelwald - car-free",
            "city_latitude": "46.55",
            "city_longitude": "7.88",
            "scheme_color": "3"
        },
        {
            "id": "2345",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/roosendaal-car-free",
            "introtext": "",
            "cityname": "Roosendaal - car-free",
            "city_latitude": "51.53",
            "city_longitude": "4.46",
            "scheme_color": "3"
        },
        {
            "id": "2338",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/culemborg-car-free",
            "introtext": "",
            "cityname": "Culemborg - car-free",
            "city_latitude": "51.95",
            "city_longitude": "5.22",
            "scheme_color": "3"
        },
        {
            "id": "2339",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/heerenveen-car-free",
            "introtext": "",
            "cityname": "Heerenveen - car-free",
            "city_latitude": "52.95",
            "city_longitude": "5.91",
            "scheme_color": "3"
        },
        {
            "id": "2340",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/katwijk-car-free",
            "introtext": "",
            "cityname": "Katwijk - car-free",
            "city_latitude": "52.20",
            "city_longitude": "4.39",
            "scheme_color": "3"
        },
        {
            "id": "2341",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/leeuwarden-car-free",
            "introtext": "",
            "cityname": "Leeuwarden - car-free",
            "city_latitude": "53.20",
            "city_longitude": "5.80",
            "scheme_color": "3"
        },
        {
            "id": "2342",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/netherlands-mainmenu-88/leiden-car-free",
            "introtext": "",
            "cityname": "Leiden - car-free",
            "city_latitude": "52.16",
            "city_longitude": "4.49",
            "scheme_color": "3"
        },
        {
            "id": "2352",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/stuttgart-superblock",
            "introtext": "Stuttgart also has a <a title=\"lorry transit ban\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/stuttgart-ar\">lorry transit ban</a> and a <a title=\"lorry transit ban\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/germany-mainmenu-61/stuttgart\">low emission zone in place.<br>\n",
            "cityname": "Stuttgart - superblock",
            "city_latitude": "48.91",
            "city_longitude": "9.14",
            "scheme_color": "3"
        },
        {
            "id": "2354",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/a-coruna-limited-traffic-zone",
            "introtext": "",
            "cityname": "A Coruna - Limited Traffic Zone",
            "city_latitude": "43.36",
            "city_longitude": "-8.41",
            "scheme_color": "3"
        },
        {
            "id": "2357",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/cartagena",
            "introtext": "Cartagena has a superblock / pedestrian and an emergency scheme in place.",
            "cityname": "Cartagena pedestrian / superblocks",
            "city_latitude": "37.59",
            "city_longitude": "-0.98",
            "scheme_color": "3"
        },
        {
            "id": "2373",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/la-linea-de-la-concepcion-park",
            "introtext": "La Línea de la Concepción has implemented a ZBE end of 2024.",
            "cityname": "La Linea de la Concepcion - park",
            "city_latitude": "36.16",
            "city_longitude": "-5.34",
            "scheme_color": "3"
        },
        {
            "id": "2374",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/ireland/dublin-transit-ban",
            "introtext": "Dublin has a transit ban in place from August 2024.",
            "cityname": "Dublin - Transit ban",
            "city_latitude": "53.33",
            "city_longitude": "-6.25",
            "scheme_color": "3"
        },
        {
            "id": "2430",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/basel-superblocks",
            "introtext": "Basel has a pilot for superblocks in place.",
            "cityname": "Basel - superblocks",
            "city_latitude": "47.55",
            "city_longitude": "7.58",
            "scheme_color": "3"
        },
        {
            "id": "2412",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/czech-republic-mainmenu-448/praha-prague-night-driving-ban",
            "introtext": "Prague is considering a Low Emission Zone, the start date is unknown. The earliest Czech law allows is 2019.<br>\r\n\r\nPlease note that there is also a <a title=\"Praha (Prague permit scheme)\" class=\"nturl\" href=\"/countries-mainmenu-147/czech-republic-mainmenu-448/praha-prague-permit\">traffic regulation / permit scheme</a> in Praha (Prague) that requires your vehicle to meet certain emission standards. <br>\r\n\r\nAnd an access regulation for <a title=\"coaches\" class=\"new-window nturl\" href=\"/countries-mainmenu-147/czech-republic-mainmenu-448/praha-prague-coaches\">tourist buses</a> in Prague.<br>Prague 1 district initiates ban on motorized traffic at night.\r\n\r\n\r\n\r\n\r\n",
            "cityname": "Praha (Prague) Night driving ban",
            "city_latitude": "50.09",
            "city_longitude": "14.42",
            "scheme_color": "3"
        },
        {
            "id": "2405",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/austria-mainmenu-78/tirol-motorcycle-noise-ban",
            "introtext": "Temporary motorcycle ban in Tirol.",
            "cityname": "Tirol Motorcycle Noise Ban",
            "city_latitude": "47.26",
            "city_longitude": "11.45",
            "scheme_color": "3"
        },
        {
            "id": "2406",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/germany-mainmenu-61/germany-motorcycle-noise-bans",
            "introtext": "Germany has various motorcycle noise bans.",
            "cityname": "Germany Motorcycle Noise Bans",
            "city_latitude": "51.51",
            "city_longitude": "9.91",
            "scheme_color": "3"
        },
        {
            "id": "2407",
            "citypath": "https://urbanaccessregulations.eu/countries-mainmenu-147/switzerland/switzerland-motorcycle-noise-bans",
            "introtext": "Switzerland has various motorcycle noise bans.",
            "cityname": "Switzerland Motorcycle Noise Bans",
            "city_latitude": "47.00",
            "city_longitude": "8.00",
            "scheme_color": "3"
        },
        {
            "id": "2440",
            "citypath": "http://urbanaccessregulations.eu/countries-mainmenu-147/spain/vitoria-gasteiz-limited-traffic-zone",
            "introtext": "",
            "cityname": "Vitoria Gasteiz - Limited Traffic Zone",
            "city_latitude": "42.85",
            "city_longitude": "-2.67",
            "scheme_color": "3"
        }
    ]}




# Extract data for Italy (assuming "italy" is in citypath)
italy_stations = [station for station in data["data"] if "italy" in station["citypath"].lower()]

# Create a map centered around Italy
italy_map = folium.Map(location=[41.8719, 12.5674], zoom_start=6)

color_map = {
    "1": "red",  # Tomato red Low Emission zone
    "2": "blue",  # Steel blue Urban Road Tolls
    "3": "green",  # Lime green Other (Limited Trafic Zone)
    "4": "violet",  # Blue violet Pollution Emergency
    "5": "orange"   # Dark orange
}

# Add markers for each station
station_groups = defaultdict(set)
for station in italy_stations:
    key = (float(station["city_latitude"]), float(station["city_longitude"]))
    station_groups[key].add(station["scheme_color"])  # Use a set to avoid duplicates

# Create a map centered around Italy
italy_map = folium.Map(location=[ 45.464664, 9.188540], zoom_start=7.5)

# Add concentric bands for each location, drawing the outer circles first
for (lat, lon), scheme_colors in station_groups.items():
    
    unique_colors = sorted(scheme_colors)  # Ensure colors appear in order
    if '3' in unique_colors:
        unique_colors.remove('3')
    
    # Iterate over unique colors in reverse order to plot the outer circles first
    for i in range(len(unique_colors)-1, -1, -1):  # Start from the last element and go backward
        scheme = unique_colors[i]
        color = color_map.get(scheme, "gray")  # Default to gray if not found
        inner_radius = i * 1100  # Inner boundary of the band
        outer_radius = (i + 1) * 1100  # Outer boundary of the band
        
        # Create a filled circle (band effect)
        folium.Circle(
            location=[lat, lon],
            radius=outer_radius,  # Outer radius
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8-i*0.1,
            popup=f"Regulation {scheme}",
            tooltip=f"Regulation {scheme}"
        ).add_to(italy_map)


# Create a legend using DivIcon
legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; 
                width: 150px; height: 180px; 
                background-color: white; 
                border: 2px solid grey; 
                z-index: 9999; 
                font-size: 14px;
                padding: 10px;">
        <b>Regulation Legend</b><br>
        <i style="background-color:red; width: 20px; height: 20px; display: inline-block;"></i> Low Emission Zone<br>
        <i style="background-color:blue; width: 20px; height: 20px; display: inline-block;"></i> Urban Road Toll<br>
        <i style="background-color:violet; width: 20px; height: 20px; display: inline-block;"></i> Pollution Emergency<br>
        
    </div>
'''
#<i style="background-color:#FF8C00; width: 20px; height: 20px; display: inline-block;"></i> Zero Emission Zone
#<i style="background-color:#32CD32; width: 20px; height: 20px; display: inline-block;"></i> Other (Limited Traffic Zone)<br>
# Read Excel file with the station data
# Replace this with the actual file path
df = pd.read_excel("class_impact.xlsx")

square_svg = """
<svg width="10" height="10" xmlns="http://www.w3.org/2000/svg">
  <rect width="10" height="10" style="fill:{color};stroke:black;stroke-width:1;"/>
</svg>
"""

# Color mapping for categories
# category_colors = {
#     0: "white",    # Category 0 -> red
#     1: "grey",   # Category 1 -> blue
#     2: "black"   # Category 2 -> green
# }
category_colors = {
    "Cumulative > 0": "white",    # Category 0 -> red
    "Solo cumulative < 0": "grey",   # Category 1 -> blue
    "Intervallo < 0": "black"   # Category 2 -> green
}
# Definisci il sistema di riferimento UTM e WGS84 (EPSG:4326)
utm_proj = Proj(proj='utm', zone=32, ellps='WGS84', south=False)  # Lombardia è nella zona UTM 32N
wgs84_proj = Proj(proj='latlong', datum='WGS84')

# Funzione di conversione
def utm_to_latlon(easting, northing):
    lon, lat = transform(utm_proj, wgs84_proj, easting, northing)
    return lat, lon

# Applica la conversione
df['lat'], df['lon'] = zip(*df.apply(lambda row: utm_to_latlon(row['Utm_Est']*1000, row['Utm_Nord']*1000), axis=1))

print(df)

for _, row in df.iterrows():
    lat, lon, category = row["lat"], row["lon"], row["category"]
    
    
    # Get the color based on category (default to gray if missing)
    color = category_colors.get(category, "gray")
    
    icon = folium.CustomIcon(icon_image=f"data:image/svg+xml;utf8,{square_svg.format(color=color)}", icon_size=(10, 10))

    # Add marker to the map
    folium.Marker(
        location=[lat, lon],
        radius=5,  # Adjust size as needed
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=1,
        popup=f"Category {category}",
        icon=icon,
        tooltip=f"Category {category}"
    ).add_to(italy_map)
    if row["Utm_Est"] == 484773 or row["Utm_Est"] == 486035 or row["Utm_Est"] == 596168:
        folium.CircleMarker(
        location=[lat, lon],
        radius=5,  # Adjust size as needed
        color="yellow",
        fill=True,
        fill_color=color,
        fill_opacity=1,
        popup=f"Category {category}",
        tooltip=f"Category {category}"
    ).add_to(italy_map)

legend_html_stations = """
<div style="
    position: fixed; 
    bottom: 20px; right: 20px; width: 200px; height: 120px; 
    background-color: white; z-index:9999; font-size:14px;
    padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
">
    <b>Legend</b><br>
    <i style="background:white; width: 15px; height: 15px; display: inline-block; border: 1px solid black;"></i> No Effect<br>
    <i style="background:grey; width: 15px; height: 15px; display: inline-block; border: 1px solid black;"></i> Partial Effect<br>
    <i style="background:black; width: 15px; height: 15px; display: inline-block; border: 1px solid black;"></i> Total Effect
</div>
"""

# Add the legend to the map
italy_map.get_root().html.add_child(folium.Element(legend_html_stations))
# Add the legend to the map
italy_map.get_root().html.add_child(folium.Element(legend_html))





print(italy_stations[100])
milano = []
for station in italy_stations: 
    if "Milano" in station["cityname"]: 
        milano.append(station)
        print(station["cityname"],station['scheme_color'],station["city_latitude"],station["city_longitude"])





# # Add markers for each station
# station_groups = defaultdict(set)
# for station in italy_stations:
#     key = (float(station["city_latitude"]), float(station["city_longitude"]))
#     station_groups[key].add(station["scheme_color"])  # Use a set to avoid duplicates

# # Create a map centered around Italy
# italy_map = folium.Map(location=[41.8719, 12.5674], zoom_start=6)

# # Add concentric bands for each location
# for (lat, lon), scheme_colors in station_groups.items():
#     unique_colors = sorted(scheme_colors)  # Ensure colors appear in order
    
#     for i, scheme in enumerate(unique_colors):
#         color = color_map.get(scheme, "gray")  # Default to gray if not found
#         inner_radius = i * 500  # Inner boundary of the band
#         outer_radius = (i + 1) * 500  # Outer boundary of the band
        
#         # Create a filled circle (band effect)
#         folium.Circle(
#             location=[lat, lon],
#             radius=outer_radius,  # Outer radius
#             color=color,
#             fill=True,
#             fill_color=color,
#             fill_opacity=0.9,
#             popup=f"Regulation {scheme}",
#             tooltip=f"Regulation {scheme}"
#         ).add_to(italy_map)

italy_map.save("italy_stations_map_impact_2.html")












