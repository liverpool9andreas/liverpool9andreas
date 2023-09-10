'''
created by andreas liosis
thessaloniki 6/2/2023
'''

from flask import Flask,render_template
def ypologismos_mesou_orou():
    metavliti_sinexeias = True
    while metavliti_sinexeias == True:
        print("YPOLOGISMOS MESOY OROY")
        print("doyleyei mono gia mthites gymnasiou")
        erotisi=input("ti taji pate? prvth or deytera or trith?")
        if erotisi=="prvth":
            mathimata = 15
            ma = int(input("doste ton bathmo tvn mathimatikvn"))
            if ma == 0:
                mathimata = mathimata - 1
            f = int(input("doste ton bathmo tis fysikhs"))
            if f == 0:
                mathimata = mathimata - 1
            x = int(input("doste ton bathmo tis geografias"))
            if x == 0:
                mathimata = mathimata - 1
            b = int(input("doste ton bathmo tis biologias"))
            if b == 0:
                mathimata = mathimata - 1
            texnologiapliroforiki = 2
            p = int(input("doste ton bathmo pliroforikhs"))
            if p == 0:
                texnologiapliroforiki = texnologiapliroforiki - 1
            t = int(input("doste ton bathmo tis texnologias"))
            if t == 0:
                texnologiapliroforiki = texnologiapliroforiki - 1
            tp =(t + p) / texnologiapliroforiki
            oi = int(input("doste ton bathmo ths oikiakhs"))
            if oi == 0:
                mathimata = mathimata - 1
            i = int(input("doste ton bathmo tis istorias"))
            if i == 0:
                mathimata = mathimata - 1
            d = int(input("doste ton bathmo tvn dejiothtvn"))
            if d == 0:
                mathimata = mathimata - 1
            th = int(input("doste ton bathmo tvn thriskeytikvn"))
            if th == 0:
                mathimata = mathimata - 1
            kalitexnikamoysiki = 2
            m = int(input("doste ton bathmo tis moysikhs"))
            if m == 0:
                kalitexnikamoysiki = kalitexnikamoysiki - 1
            gy = int(input("doste ton bathmo tis gymnastikhs"))
            if gy == 0:
                mathimata = mathimata - 1
            j = int(input("doste ton bathmo tis 2hs jenhs glvsas"))
            if j == 0:
                mathimata = mathimata - 1
            ag = int(input("doste ton bathmo tvn agglikon"))
            if ag == 0:
                mathimata = mathimata - 1
            ka = int(input("doste ton bathmo tvn kalitexnikon"))
            if m == 0:
                kalitexnikamoysiki = kalitexnikamoysiki - 1
            km = (ka + m) / kalitexnikamoysiki
            arxeaeleni = 2
            a = int(input("doste ton bathmo tvn arxaion"))
            if a == 0:
                arxeaeleni = arxeaeleni - 1
            o = int(input("doste ton bathmo tis odisias"))
            if o == 0:
                arxeaeleni = arxeaeleni - 1
            ae = (a + o) / arxeaeleni
            keimenaglvssa = 2
            n = int(input("doste ton bathmo tis glossas"))
            if n == 0:
                keimenaglvssa = keimenaglvssa - 1
            k = int(input("doste ton bathmo tvn keimenon"))
            if k == 0:
                keimenaglvssa = keimenaglvssa - 1
            ne = (n + k) / keimenaglvssa
            mesi_timi = (ma + f + x + b + tp + oi + i + d + th + gy + j + ag + km + ae + ne) / mathimata
            mesi_timi = (ma + f + x + b + tp + oi + i + d + th + gy + j + ag + km + ae + ne) / mathimata
            bathmos_se_15= (mesi_timi - int(mesi_timi)) * mathimata
            import math
            bathmos_se15_strog = math.ceil(bathmos_se_15)
            print("\n")
            print("o bathmos sas einai {} +  {}/{}".format(int(mesi_timi) ,bathmos_se15_strog ,mathimata))
            print("\n")
        if erotisi=="deytera":
            mathimata = 15
            ma = int(input("doste ton bathmo tvn mathimatikvn"))
            if ma == 0:
                mathimata = mathimata - 1
            f = int(input("doste ton bathmo tis fysikhs"))
            if f == 0:
                mathimata = mathimata - 1
            x = int(input("doste ton bathmo tis xhmias"))
            if x == 0:
                mathimata = mathimata - 1
            b = int(input("doste ton bathmo tis biologias"))
            if b == 0:
                mathimata = mathimata - 1
            texnologiapliroforiki = 2
            p = int(input("doste ton bathmo pliroforikhs"))
            if p == 0:
                texnologiapliroforiki = texnologiapliroforiki - 1
            t = int(input("doste ton bathmo tis texnologias"))
            if t == 0:
                texnologiapliroforiki = texnologiapliroforiki - 1
            tp =(t + p) / texnologiapliroforiki
            oi = int(input("doste ton bathmo kpa"))
            if oi == 0:
                mathimata = mathimata - 1
            i = int(input("doste ton bathmo tis istorias"))
            if i == 0:
                mathimata = mathimata - 1
            d = int(input("doste ton bathmo tvn dejiothtvn"))
            if d == 0:
                mathimata = mathimata - 1
            th = int(input("doste ton bathmo tvn thriskeytikvn"))
            if th == 0:
                mathimata = mathimata - 1
            kalitexnikamoysiki = 2
            m = int(input("doste ton bathmo tis moysikhs"))
            if m == 0:
                kalitexnikamoysiki = kalitexnikamoysiki - 1
            gy = int(input("doste ton bathmo tis gymnastikhs"))
            if gy == 0:
                mathimata = mathimata - 1
            j = int(input("doste ton bathmo tis 2hs jenhs glvsas"))
            if j == 0:
                mathimata = mathimata - 1
            ag = int(input("doste ton bathmo tvn agglikon"))
            if ag == 0:
                mathimata = mathimata - 1
            ka = int(input("doste ton bathmo tvn kalitexnikon"))
            if m == 0:
                kalitexnikamoysiki = kalitexnikamoysiki - 1
            km = (ka + m) / kalitexnikamoysiki
            arxeaeleni = 2
            a = int(input("doste ton bathmo tvn arxaion"))
            if a == 0:
                arxeaeleni = arxeaeleni - 1
            o = int(input("doste ton bathmo tis iliadas"))
            if o == 0:
                arxeaeleni = arxeaeleni - 1
            ae = (a + o) / arxeaeleni
            keimenaglvssa = 2
            n = int(input("doste ton bathmo tis glossas"))
            if n == 0:
                keimenaglvssa = keimenaglvssa - 1
            k = int(input("doste ton bathmo tvn keimenon"))
            if k == 0:
                keimenaglvssa = keimenaglvssa - 1
            ne = (n + k) / keimenaglvssa
            mesi_timi = (ma + f + x + b + tp + oi + i + d + th + gy + j + ag + km + ae + ne) / mathimata
            mesi_timi = (ma + f + x + b + tp + oi + i + d + th + gy + j + ag + km + ae + ne) / mathimata
            bathmos_se_15= (mesi_timi - int(mesi_timi)) * mathimata
            import math
            bathmos_se15_strog = math.ceil(bathmos_se_15)
            print("\n")
            print("o bathmos sas einai {} +  {}/{}".format(int(mesi_timi) ,bathmos_se15_strog ,mathimata))
            print("\n")
        if erotisi=="trith":
            mathimata = 15
            ma = int(input("doste ton bathmo tvn mathimatikvn"))
            if ma == 0:
                mathimata = mathimata - 1
            f = int(input("doste ton bathmo tis fysikhs"))
            if f == 0:
                mathimata = mathimata - 1
            x = int(input("doste ton bathmo tis xhmias"))
            if x == 0:
                mathimata = mathimata - 1
            b = int(input("doste ton bathmo tis biologias"))
            if b == 0:
                mathimata = mathimata - 1
            texnologiapliroforiki = 2
            p = int(input("doste ton bathmo pliroforikhs"))
            if p == 0:
                texnologiapliroforiki = texnologiapliroforiki - 1
            t = int(input("doste ton bathmo tis texnologias"))
            if t == 0:
                texnologiapliroforiki = texnologiapliroforiki - 1
            tp =(t + p) / texnologiapliroforiki
            oi = int(input("doste ton bathmo kpa"))
            if oi == 0:
                mathimata = mathimata - 1
            i = int(input("doste ton bathmo tis istorias"))
            if i == 0:
                mathimata = mathimata - 1
            d = int(input("doste ton bathmo tvn dejiothtvn"))
            if d == 0:
                mathimata = mathimata - 1
            th = int(input("doste ton bathmo tvn thriskeytikvn"))
            if th == 0:
                mathimata = mathimata - 1
            kalitexnikamoysiki = 2
            m = int(input("doste ton bathmo tis moysikhs"))
            if m == 0:
                kalitexnikamoysiki = kalitexnikamoysiki - 1
            gy = int(input("doste ton bathmo tis gymnastikhs"))
            if gy == 0:
                mathimata = mathimata - 1
            j = int(input("doste ton bathmo tis 2hs jenhs glvsas"))
            if j == 0:
                mathimata = mathimata - 1
            ag = int(input("doste ton bathmo tvn agglikon"))
            if ag == 0:
                mathimata = mathimata - 1
            ka = int(input("doste ton bathmo tvn kalitexnikon"))
            if m == 0:
                kalitexnikamoysiki = kalitexnikamoysiki - 1
            km = (ka + m) / kalitexnikamoysiki
            arxeaeleni = 2
            a = int(input("doste ton bathmo tvn arxaion"))
            if a == 0:
                arxeaeleni = arxeaeleni - 1
            o = int(input("doste ton bathmo tis elenis"))
            if o == 0:
                arxeaeleni = arxeaeleni - 1
            ae = (a + o) / arxeaeleni
            keimenaglvssa = 2
            n = int(input("doste ton bathmo tis glossas"))
            if n == 0:
                keimenaglvssa = keimenaglvssa - 1
            k = int(input("doste ton bathmo tvn keimenon"))
            if k == 0:
                keimenaglvssa = keimenaglvssa - 1
            ne = (n + k) / keimenaglvssa
            mesi_timi = (ma + f + x + b + tp + oi + i + d + th + gy + j + ag + km + ae + ne) / mathimata
            mesi_timi = (ma + f + x + b + tp + oi + i + d + th + gy + j + ag + km + ae + ne) / mathimata
            bathmos_se_15= (mesi_timi - int(mesi_timi)) * mathimata
            import math
            bathmos_se15_strog = math.ceil(bathmos_se_15)
            print("\n")
            print("o bathmos sas einai {} +  {}/{}".format(int(mesi_timi) ,bathmos_se15_strog ,mathimata))
            print("\n")
        erotisi=input("Thelete na sinexisete? yes or no?")
        if erotisi=="yes":
            metavliti_sinexeias=True
        else:
            metavliti_sinexeias=False
            #metavliti_sinexeias=True
    return render_template('index.html',ypologismos_mesou_orou= bathmos_se15_strog )