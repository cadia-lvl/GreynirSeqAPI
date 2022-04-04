# -*- coding: utf-8 -*-
import requests
import json

LOC="/translate/isen"
LOC="/process/service"

inp =  "Þetta er setning. Og önnur!"
print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content":inp})
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()

inp = """
Í hópi þeirra 140 einkafjárfesta sem tóku þátt í útboði ríkissjóðs á stórum hlut í Íslandsbanka og keyptu hvað mest, eða fyrir á bilinu um 200 til 500 milljónir hvor um sig, voru meðal annars Ólafur D. Torfason, aðaleigandi Íslandshótela, Byggingarfélag Gylfa og Gunnars (BYGG), fjárfestingafélagið Stálskip, útgerðarfélagið Jakob Valgeir, Hannes Hilmarsson, stjórnarformaður Air Atlanta, og eignarhaldsfélagið Kadúseus sem er í meirihlutaeigu Sveins Valfells.

Þá fer SKEL fjárfestingafélag (áður Skeljungur) núna með 0,19 prósenta eignarhlut í Íslandsbanka, sem var keyptur að langmestu í útboðinu, en miðað við núverandi markaðsgengi bankans er sá hlutur metinn á tæplega 500 milljónir. Meirihlutaeigandi SKEL er fjárfestingafélagið Strengur en Jón Ásgeir Jóhannesson, einn aðaleigenda Glitnis banka á sínum tíma, er stjórnarformaður beggja félaganna.

Þetta sýnir listi yfir alla hluthafa Íslandsbanka miðvikudaginn 30. mars síðastliðinn, sem Innherji hefur séð, tveimur dögum eftir að uppgjör viðskipta vegna sölu ríkissjóðs á 22,5 prósenta hlut í bankanum fyrir tæplega 53 milljarða króna hafði farið fram.
"""

print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content":inp})
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()
