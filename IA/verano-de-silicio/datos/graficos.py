import csv, math
import os; _H=os.path.dirname(os.path.abspath(__file__)); D=_H; OUT=os.path.join(_H,"..","img")
THEMES={
 "light":dict(bg="#fcfcfb",t1="#0b0b0b",t2="#52514e",mut="#898781",grid="#e1e0d9",s=["#2a78d6","#eb6834","#1baf7a","#eda100","#e87ba4"]),
 "dark":dict(bg="#1a1a19",t1="#f0efec",t2="#c3c2b7",mut="#898781",grid="#2c2c2a",s=["#3987e5","#d95926","#199e70","#c98500","#d55181"]),
}
FONT="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
ES={"Spain":"España","United Kingdom":"Reino Unido","United States":"EE. UU.","Germany":"Alemania","France":"Francia"}
ORDER=["Spain","Germany","France","United Kingdom","United States"]
def fmt(n,d=0):
    s=f"{n:,.{d}f}".replace(",","X").replace(".",",").replace("X",".")
    return s
def svg(w,h,th,body,title,desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">'
            f'<title id="t">{title}</title><desc id="d">{desc}</desc>'
            f'<rect width="{w}" height="{h}" rx="8" fill="{th["bg"]}"/><g style="{FONT}">{body}</g></svg>')
def text(x,y,s,fill,size=13,anchor="start",weight=400):
    return f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

# ---------- Fig 1: horas anuales por trabajador 1870-2023 ----------
rows=list(csv.DictReader(open(f"{D}/annual_hours_per_worker_5countries.csv")))
series={c:sorted((int(r["year"]),float(r["annual_hours_per_worker"])) for r in rows if r["country"]==c and r["annual_hours_per_worker"]) for c in ORDER}
def fig1(th,name):
    W,H=880,520; L,R,T,B=64,150,92,84
    x0,x1=1870,2023; y0,y1=0,3500
    X=lambda v:L+(v-x0)/(x1-x0)*(W-L-R); Y=lambda v:H-B-(v-y0)/(y1-y0)*(H-T-B)
    b=[text(L,34,"Las horas bajaron. Mucho menos de lo que predijo Keynes",th["t1"],19,weight=650),
       text(L,58,"Horas trabajadas al año por trabajador, 1870–2023",th["t2"],13.5)]
    for v in range(0,3501,500):
        b.append(f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{th["grid"]}" stroke-width="1"/>')
        b.append(text(L-8,Y(v)+4,fmt(v),th["mut"],12,"end"))
    for v in range(1870,2021,25):
        b.append(text(X(v),H-B+20,str(v),th["mut"],12,"middle"))
    # Keynes 15 h/semana ~ 750 h/año (15 h x 50 semanas)
    yk=Y(750)
    b.append(f'<line x1="{L}" x2="{W-R}" y1="{yk:.1f}" y2="{yk:.1f}" stroke="{th["t2"]}" stroke-width="1.5" stroke-dasharray="6 5"/>')
    b.append(text(X(1872),yk-8,"Keynes (1930): «semanas de quince horas» ≈ 750 h/año",th["t2"],12.5))
    b.append(f'<line x1="{X(1950):.1f}" x2="{X(1950):.1f}" y1="{T-6}" y2="{H-B}" stroke="{th["grid"]}" stroke-width="1"/>')
    b.append(text(X(1950)+6,T+6,"Antes de 1950: obreros industriales, datos dispersos",th["mut"],11.5))
    ends=[]
    for i,c in enumerate(ORDER):
        pts=series[c]; col=th["s"][i]
        post=[p for p in pts if p[0]>=1950]; pre=[p for p in pts if p[0]<1950]
        if pre:
            d="M"+" L".join(f"{X(x):.1f},{Y(y):.1f}" for x,y in pre+[post[0]])
            b.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.5" stroke-dasharray="3 4" stroke-linecap="round" opacity="0.9"/>')
            for x,y in pre: b.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="3.5" fill="{col}" stroke="{th["bg"]}" stroke-width="1.5"/>')
        d="M"+" L".join(f"{X(x):.1f},{Y(y):.1f}" for x,y in post)
        b.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
        xe,ye=post[-1]; b.append(f'<circle cx="{X(xe):.1f}" cy="{Y(ye):.1f}" r="4" fill="{col}" stroke="{th["bg"]}" stroke-width="2"/>')
        ends.append([Y(ye),c,ye,col])
    ends.sort(); 
    for k in range(1,len(ends)):
        if ends[k][0]-ends[k-1][0]<16: ends[k][0]=ends[k-1][0]+16
    for yy,c,v,col in ends:
        b.append(text(W-R+10,yy+4,f'{ES[c]} {fmt(v)}',th["t1"],12.5))
    # leyenda
    lx=L
    for i,c in enumerate(ORDER):
        b.append(f'<rect x="{lx}" y="{H-46}" width="14" height="4" rx="2" fill="{th["s"][i]}"/>'); b.append(text(lx+20,H-40,ES[c],th["t2"],12)); lx+=20+len(ES[c])*7.4+22
    b.append(text(L,H-14,"Fuente: Huberman y Minns (2007); Penn World Table 11.0, vía Our World in Data",th["mut"],11))
    open(f"{OUT}/{name}-{th['_n']}.svg","w").write(svg(W,H,th,"".join(b),"Horas trabajadas al año por trabajador, 1870–2023","Líneas para España, Alemania, Francia, Reino Unido y EE. UU. Todas bajan de unas 3.000 horas en 1870 a entre 1.335 y 1.790 en 2023, lejos de las unas 750 horas que implicaría la semana de quince horas de Keynes."))

# ---------- Fig 2: productividad x vs horas % 1950-2023 (dos paneles) ----------
pv={r["country"]:r for r in csv.DictReader(open(f"{D}/productivity_vs_hours_1950_2023.csv"))}
def fig2(th,name):
    W,H=880,380; T=96; rowh=44; L=120; pw=300; gap=90
    b=[text(24,34,"Cada hora rinde de 4 a 15 veces más que en 1950; las horas bajaron un 12–45 %",th["t1"],18,weight=650),
       text(24,58,"Cambio entre 1950 y 2023. Productividad: PIB por hora trabajada, precios constantes",th["t2"],13.5)]
    p1x=L; p2x=L+pw+gap
    b.append(text(p1x,T-12,"Productividad por hora (veces)",th["t1"],13,weight=600))
    b.append(text(p2x,T-12,"Horas al año por trabajador (%)",th["t1"],13,weight=600))
    m1=16; m2=50
    for v in (0,5,10,15):
        x=p1x+v/m1*pw; b.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T}" y2="{T+rowh*5}" stroke="{th["grid"]}"/>'); b.append(text(x,T+rowh*5+18,f"×{v}" if v else "0",th["mut"],12,"middle"))
    for v in (0,-10,-20,-30,-40,-50):
        x=p2x+(-v)/m2*pw; b.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T}" y2="{T+rowh*5}" stroke="{th["grid"]}"/>'); b.append(text(x,T+rowh*5+18,f"−{-v} %" if v else "0",th["mut"],12,"middle"))
    order=sorted(ORDER,key=lambda c:-float(pv[c]["prod_multiple"]))
    for i,c in enumerate(order):
        y=T+i*rowh+rowh/2
        b.append(text(L-12,y+4,ES[c],th["t1"],13,"end"))
        m=float(pv[c]["prod_multiple"]); w=m/m1*pw
        b.append(f'<path d="M{p1x},{y-10} h{w-4:.1f} a4,4 0 0 1 4,4 v12 a4,4 0 0 1 -4,4 h-{w-4:.1f} z" fill="{th["s"][0]}"/>')
        b.append(text(p1x+w+6,y+4,"×"+fmt(m,1),th["t1"],12.5))
        hc=float(pv[c]["hours_change_pct"]); w2=(-hc)/m2*pw
        b.append(f'<path d="M{p2x},{y-10} h{w2-4:.1f} a4,4 0 0 1 4,4 v12 a4,4 0 0 1 -4,4 h-{w2-4:.1f} z" fill="{th["s"][1]}"/>')
        b.append(text(p2x+w2+6,y+4,"−"+fmt(-hc,1)+" %",th["t1"],12.5))
    b.append(text(W-12,H-14,"Fuente: Penn World Table 11.0 vía Our World in Data. Alemania antes de 1991: RFA",th["mut"],11,"end"))
    open(f"{OUT}/{name}-{th['_n']}.svg","w").write(svg(W,H,th,"".join(b),"Productividad por hora frente a horas trabajadas, 1950–2023","Dos paneles de barras. Productividad por hora en 2023 respecto a 1950: Alemania ×15,3, España ×13,6, Francia ×10,0, Reino Unido ×5,5, EE. UU. ×3,9. Horas al año por trabajador: Alemania −45 %, Francia −36,7 %, España −25,7 %, Reino Unido −24,7 %, EE. UU. −11,5 %."))

# ---------- Fig 3: horas reales 2023 vs horas que bastarían para producir lo de 1950 ----------
def fig3(th,name):
    W,H=880,360; T=110; rowh=40; L=120; pw=640; mx=1800
    b=[text(24,34,"Con la productividad de hoy, lo que se producía en 1950 cabría en 3–10 horas a la semana",th["t1"],18,weight=650),
       text(24,58,"Horas al año por trabajador en 2023 frente a las necesarias para igualar la producción por trabajador de 1950",th["t2"],13.5)]
    lx=L
    for lab,col in (("Horas trabajadas en 2023",th["s"][1]),("Horas que bastarían con la productividad de 2023",th["s"][0])):
        b.append(f'<rect x="{lx}" y="76" width="14" height="10" rx="2" fill="{col}"/>'); b.append(text(lx+20,85,lab,th["t2"],12.5)); lx+=20+len(lab)*7+28
    for v in range(0,1801,300):
        x=L+v/mx*pw; b.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T-6}" y2="{T+rowh*5}" stroke="{th["grid"]}"/>'); b.append(text(x,T+rowh*5+18,fmt(v),th["mut"],12,"middle"))
    order=sorted(ORDER,key=lambda c:float(pv[c]["hours_1950"])/float(pv[c]["prod_multiple"]))
    for i,c in enumerate(order):
        y=T+i*rowh
        real=float(pv[c]["hours_2023"]); need=float(pv[c]["hours_1950"])/float(pv[c]["prod_multiple"])
        b.append(text(L-12,y+16,ES[c],th["t1"],13,"end"))
        for j,(v,col) in enumerate(((real,th["s"][1]),(need,th["s"][0]))):
            w=v/mx*pw; yy=y+j*15
            b.append(f'<path d="M{L},{yy} h{w-3:.1f} a3,3 0 0 1 3,3 v7 a3,3 0 0 1 -3,3 h-{w-3:.1f} z" fill="{col}"/>')
            lab=fmt(v) + (f" h (≈ {fmt(v/50,1)} h/semana)" if j==1 else " h")
            b.append(text(L+w+6,yy+10.5,lab,th["t1"] if j==1 else th["t2"],12))
    b.append(text(W-12,H-14,"Cálculo propio: horas de 1950 ÷ multiplicador de productividad por hora 1950–2023. 50 semanas/año. Fuente: PWT 11.0 vía OWID",th["mut"],11,"end"))
    open(f"{OUT}/{name}-{th['_n']}.svg","w").write(svg(W,H,th,"".join(b),"Horas reales en 2023 frente a horas suficientes para la producción de 1950","Barras pareadas por país. Con la productividad de 2023, igualar la producción por trabajador de 1950 requeriría entre 159 y 522 horas al año, frente a entre 1.335 y 1.789 horas trabajadas."))

for n,th in THEMES.items():
    th["_n"]=n; fig1(th,"fig1-horas-1870-2023"); fig2(th,"fig2-productividad-vs-horas"); fig3(th,"fig3-horas-necesarias")
print("ok")
for c in ORDER:
    r=pv[c]; print(ES[c], round(float(r["hours_1950"])/float(r["prod_multiple"])), "h/año", round(float(r["hours_1950"])/float(r["prod_multiple"])/50,1),"h/sem")

# ---------- Fig 4: la paradoja de la productividad (Faros AI 2025) ----------
def fig4(th,name):
    W,H=880,360; T=112; rowh=40; L=300; pw=460; mx=160
    items=[("Tareas completadas por desarrollador",21),("Pull requests fusionadas",98),("Tiempo de revisión de cada PR",91),("Tamaño medio de cada PR",154),("Bugs por desarrollador",9)]
    b=[text(24,34,"Casi el doble de PR. Casi el doble de tiempo de revisión",th["t1"],18,weight=650),
       text(24,58,"Equipos con mucha adopción de IA frente a poca. Cambio en %, Faros AI 2025 (10.000+ desarrolladores, 1.255 equipos)",th["t2"],13.5)]
    for v in (0,50,100,150):
        x=L+v/mx*pw; b.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T-6}" y2="{T+rowh*5}" stroke="{th["grid"]}"/>'); b.append(text(x,T+rowh*5+18,f"+{v} %" if v else "0",th["mut"],12,"middle"))
    for i,(lab,v) in enumerate(items):
        y=T+i*rowh+rowh/2; col=th["s"][0] if i<2 else th["s"][1]
        b.append(text(L-12,y+4,lab,th["t1"],13,"end"))
        w=v/mx*pw
        b.append(f'<path d="M{L},{y-10} h{w-4:.1f} a4,4 0 0 1 4,4 v12 a4,4 0 0 1 -4,4 h-{w-4:.1f} z" fill="{col}"/>')
        b.append(text(L+w+6,y+4,f"+{v} %",th["t1"],12.5))
    lx=L
    lx=24
    for lab,col in (("Producción",th["s"][0]),("Carga de revisión y calidad",th["s"][1])):
        b.append(f'<rect x="{lx}" y="74" width="14" height="10" rx="2" fill="{col}"/>'); b.append(text(lx+20,83,lab,th["t2"],12.5)); lx+=20+len(lab)*7+28
    b.append(text(24,H-12,"Fuente: Faros AI, «The AI Productivity Paradox» (julio de 2025). Datos correlacionales de telemetría; sin mejora medible en el conjunto de la empresa",th["mut"],11))
    open(f"{OUT}/{name}-{th['_n']}.svg","w").write(svg(W,H,th,"".join(b),"La paradoja de la productividad con IA","Barras horizontales: tareas completadas +21 %, PR fusionadas +98 %, tiempo de revisión +91 %, tamaño de PR +154 %, bugs por desarrollador +9 %."))

# ---------- Fig 5: el calendario por ciclos ----------
def fig5(th,name):
    W,H=880,320; L=40; R=40; T=96; bh=46
    phases=[("Planificar y enseñar","objetivos y criterios; pruebas de aceptación",3),("Ejecutar con agentes","los agentes producen; las personas deciden y resuelven excepciones",5),("Evaluar","pruebas completas; cada fallo, una regla",2),("Descansar","formación; sin guardia salvo lo crítico",2)]
    b=[text(L,34,"Un año por ciclos: el calendario escolar del software",th["t1"],18,weight=650),
       text(L,58,"Propuesta ilustrativa: un ciclo de 12 semanas que se repite. Las guardias cubren solo los servicios críticos",th["t2"],13.5)]
    tot=sum(p[2] for p in phases); x=L; pw=W-L-R
    for i,(n,d,wk) in enumerate(phases):
        w=wk/tot*pw; col=th["s"][i]
        b.append(f'<rect x="{x+1:.1f}" y="{T}" width="{w-2:.1f}" height="{bh}" rx="4" fill="{col}"/>')
        b.append(text(x+w/2,T+bh/2+5,f"{wk} sem.","#0b0b0b",13,"middle",650))
        b.append(text(x+6,T+bh+22,n,th["t1"],13,weight=600))
        for k,part in enumerate(d.split("; ")):
            b.append(text(x+6,T+bh+40+k*16,part,th["t2"],11.5))
        x+=w
    gy=H-56
    b.append(f'<rect x="{L}" y="{gy}" width="{pw}" height="8" rx="4" fill="{th["grid"]}"/>')
    b.append(text(L,gy+26,"Continuidad del servicio: los sistemas siguen funcionando las 12 semanas, con vuelta atrás automática y un revisor independiente",th["t2"],12))
    open(f"{OUT}/{name}-{th['_n']}.svg","w").write(svg(W,H,th,"".join(b),"Calendario por ciclos","Cuatro fases en un ciclo de 12 semanas: planificar y enseñar (3), ejecutar con agentes (5), evaluar y consolidar (2), descansar y renovarse (2)."))

for n,th in THEMES.items():
    fig4(th,"fig4-paradoja-productividad"); fig5(th,"fig5-calendario-ciclos")
