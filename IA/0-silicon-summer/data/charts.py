"""Gráficos / charts — «Programadores con vacaciones de profesor» / «Programmers with Teachers' Holidays».
Uso / usage: python3 graficos.py  (en datos/: español)  ·  python3 charts.py  (in data/: English)
Lee los CSV de esta carpeta y escribe los SVG en ../img/ en modo claro y oscuro."""
import csv, os
_H=os.path.dirname(os.path.abspath(__file__)); D=_H; OUT=os.path.join(_H,"..","img")
LANG="es" if os.path.basename(_H)=="datos" else "en"
THEMES={
 "light":dict(bg="#fcfcfb",t1="#0b0b0b",t2="#52514e",mut="#898781",grid="#e1e0d9",s=["#2a78d6","#eb6834","#1baf7a","#eda100","#e87ba4"]),
 "dark":dict(bg="#1a1a19",t1="#f0efec",t2="#c3c2b7",mut="#898781",grid="#2c2c2a",s=["#3987e5","#d95926","#199e70","#c98500","#d55181"]),
}
FONT="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
ORDER=["Spain","Germany","France","United Kingdom","United States"]
NAMES={"es":{"Spain":"España","United Kingdom":"Reino Unido","United States":"EE. UU.","Germany":"Alemania","France":"Francia"},
       "en":{"Spain":"Spain","United Kingdom":"UK","United States":"US","Germany":"Germany","France":"France"}}[LANG]
S={
"es":dict(
 f1="fig1-horas-1870-2023", f2="fig2-productividad-vs-horas", f3="fig3-horas-necesarias", f4="fig4-paradoja-productividad", f5="fig5-calendario-ciclos",
 f1t="Las horas bajaron. Mucho menos de lo que predijo Keynes", f1s="Horas trabajadas al año por trabajador, 1870–2023",
 f1k="Keynes (1930): «semanas de quince horas» ≈ 750 h/año", f1n="Antes de 1950: obreros industriales, datos dispersos",
 f1src="Fuente: Huberman y Minns (2007); Penn World Table 11.0, vía Our World in Data",
 f1title="Horas trabajadas al año por trabajador, 1870–2023",
 f1desc="Líneas para España, Alemania, Francia, Reino Unido y EE. UU. Todas bajan de unas 3.000 horas en 1870 a entre 1.335 y 1.790 en 2023, lejos de las unas 750 horas que implicaría la semana de quince horas de Keynes.",
 f2t="Cada hora rinde de 4 a 15 veces más que en 1950; las horas bajaron un 12–45 %", f2s="Cambio entre 1950 y 2023. Productividad: PIB por hora trabajada, precios constantes",
 f2a="Productividad por hora (veces)", f2b="Horas al año por trabajador (%)", f2src="Fuente: Penn World Table 11.0 vía Our World in Data. Alemania antes de 1991: RFA",
 f2title="Productividad por hora frente a horas trabajadas, 1950–2023",
 f2desc="Dos paneles de barras. Productividad por hora en 2023 respecto a 1950: Alemania ×15,3, España ×13,6, Francia ×10,0, Reino Unido ×5,5, EE. UU. ×3,9. Horas al año por trabajador: Alemania −45 %, Francia −36,7 %, España −25,7 %, Reino Unido −24,7 %, EE. UU. −11,5 %.",
 f3t="Con la productividad de hoy, lo que se producía en 1950 cabría en 3–10 horas a la semana", f3s="Horas al año por trabajador en 2023 frente a las necesarias para igualar la producción por trabajador de 1950",
 f3l1="Horas trabajadas en 2023", f3l2="Horas que bastarían con la productividad de 2023", f3wk="h/semana",
 f3src="Cálculo propio: horas de 1950 ÷ multiplicador de productividad por hora 1950–2023. 50 semanas/año. Fuente: PWT 11.0 vía OWID",
 f3title="Horas reales en 2023 frente a horas suficientes para la producción de 1950",
 f3desc="Barras pareadas por país. Con la productividad de 2023, igualar la producción por trabajador de 1950 requeriría entre 159 y 522 horas al año, frente a entre 1.335 y 1.789 horas trabajadas.",
 f4t="Casi el doble de PR. Casi el doble de tiempo de revisión", f4s="Equipos con mucha adopción de IA frente a poca. Cambio en %, Faros AI 2025 (10.000+ desarrolladores, 1.255 equipos)",
 f4i=["Tareas completadas por desarrollador","Pull requests fusionadas","Tiempo de revisión de cada PR","Tamaño medio de cada PR","Bugs por desarrollador"],
 f4l=["Producción","Carga de revisión y calidad"], f4src="Fuente: Faros AI, «The AI Productivity Paradox» (julio de 2025). Datos correlacionales de telemetría; sin mejora medible en el conjunto de la empresa",
 f4title="La paradoja de la productividad con IA", f4desc="Barras horizontales: tareas completadas +21 %, PR fusionadas +98 %, tiempo de revisión +91 %, tamaño de PR +154 %, bugs por desarrollador +9 %.",
 f5t="Un año por ciclos: el calendario escolar del software", f5s="Propuesta ilustrativa: un ciclo de 12 semanas que se repite. Las guardias cubren solo los servicios críticos",
 f5p=[("Planificar y enseñar","objetivos y criterios; pruebas de aceptación",3),("Ejecutar con agentes","los agentes producen; las personas deciden y resuelven excepciones",5),("Evaluar","pruebas completas; cada fallo, una regla",2),("Descansar","formación; sin guardia salvo lo crítico",2)],
 f5w="sem.", f5c="Continuidad del servicio: los sistemas siguen funcionando las 12 semanas, con vuelta atrás automática y un revisor independiente",
 f5title="Calendario por ciclos", f5desc="Cuatro fases en un ciclo de 12 semanas: planificar y enseñar (3), ejecutar con agentes (5), evaluar y consolidar (2), descansar y renovarse (2)."),
"en":dict(
 f1="fig1-hours-1870-2023", f2="fig2-productivity-vs-hours", f3="fig3-hours-needed", f4="fig4-productivity-paradox", f5="fig5-cycle-calendar",
 f1t="Working hours fell — but far less than Keynes predicted", f1s="Annual hours worked per worker, 1870–2023",
 f1k="Keynes (1930): “a fifteen-hour week” ≈ 750 h/year", f1n="Before 1950: industrial workers, sparse data",
 f1src="Source: Huberman and Minns (2007); Penn World Table 11.0, via Our World in Data",
 f1title="Annual hours worked per worker, 1870–2023",
 f1desc="Lines for Spain, Germany, France, the UK and the US. All fall from about 3,000 hours in 1870 to between 1,335 and 1,790 in 2023, far from the roughly 750 hours implied by Keynes's fifteen-hour week.",
 f2t="Each hour now yields 4–15 times more than in 1950; hours fell by 12–45%", f2s="Change between 1950 and 2023. Productivity: GDP per hour worked, constant prices",
 f2a="Productivity per hour (times)", f2b="Annual hours per worker (%)", f2src="Source: Penn World Table 11.0 via Our World in Data. Germany before 1991: West Germany",
 f2title="Productivity per hour versus hours worked, 1950–2023",
 f2desc="Two bar panels. Productivity per hour in 2023 relative to 1950: Germany ×15.3, Spain ×13.6, France ×10.0, UK ×5.5, US ×3.9. Annual hours per worker: Germany −45%, France −36.7%, Spain −25.7%, UK −24.7%, US −11.5%.",
 f3t="At today's productivity, 1950's output would fit in 3–10 hours a week", f3s="Annual hours per worker in 2023 versus the hours needed to match 1950 output per worker",
 f3l1="Hours worked in 2023", f3l2="Hours needed at 2023 productivity", f3wk="h/week",
 f3src="Own calculation: 1950 hours ÷ productivity-per-hour multiplier 1950–2023. 50 weeks/year. Source: PWT 11.0 via OWID",
 f3title="Actual hours in 2023 versus hours sufficient for 1950 output",
 f3desc="Paired bars by country. At 2023 productivity, matching 1950 output per worker would take between 159 and 522 hours a year, against 1,335 to 1,789 hours actually worked.",
 f4t="Nearly twice the PRs. Nearly twice the review time", f4s="Teams with high versus low AI adoption. Change in %, Faros AI 2025 (10,000+ developers, 1,255 teams)",
 f4i=["Tasks completed per developer","Pull requests merged","Review time per PR","Average PR size","Bugs per developer"],
 f4l=["Output","Review load and quality"], f4src="Source: Faros AI, “The AI Productivity Paradox” (July 2025). Correlational telemetry data; no measurable gain company-wide",
 f4title="The AI productivity paradox", f4desc="Horizontal bars: tasks completed +21%, PRs merged +98%, review time +91%, PR size +154%, bugs per developer +9%.",
 f5t="A year in cycles: the school calendar of software", f5s="Illustrative proposal: a repeating 12-week cycle. On-call covers critical services only",
 f5p=[("Plan and teach","goals and criteria; acceptance tests",3),("Run with agents","agents produce; people decide and handle exceptions",5),("Evaluate","full test runs; every failure, a rule",2),("Rest","training; on call for critical systems only",2)],
 f5w="wks", f5c="Service continuity: systems keep running all 12 weeks, with automatic rollback and an independent reviewer",
 f5title="Cycle calendar", f5desc="Four phases in a 12-week cycle: plan and teach (3), run with agents (5), evaluate and consolidate (2), rest and renew (2)."),
}[LANG]
def fmt(n,d=0):
    s=f"{n:,.{d}f}"
    return s.replace(",","X").replace(".",",").replace("X",".") if LANG=="es" else s
def pct(v,d=1):  # v already signed text-ready number
    return (f"{fmt(v,d)} %" if LANG=="es" else f"{fmt(v,d)}%")
def svg(w,h,th,body,title,desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d" lang="{LANG}">'
            f'<title id="t">{title}</title><desc id="d">{desc}</desc>'
            f'<rect width="{w}" height="{h}" rx="8" fill="{th["bg"]}"/><g style="{FONT}">{body}</g></svg>')
def text(x,y,s,fill,size=13,anchor="start",weight=400):
    return f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'
def bar(x,y,w,col,h=20,r=4):
    return f'<path d="M{x},{y} h{w-r:.1f} a{r},{r} 0 0 1 {r},{r} v{h-2*r} a{r},{r} 0 0 1 -{r},{r} h-{w-r:.1f} z" fill="{col}"/>'
def save(name,th,W,H,b,title,desc):
    open(f"{OUT}/{name}-{th['_n']}.svg","w").write(svg(W,H,th,"".join(b),title,desc))

rows=list(csv.DictReader(open(f"{D}/annual_hours_per_worker_5countries.csv")))
series={c:sorted((int(r["year"]),float(r["annual_hours_per_worker"])) for r in rows if r["country"]==c and r["annual_hours_per_worker"]) for c in ORDER}
pv={r["country"]:r for r in csv.DictReader(open(f"{D}/productivity_vs_hours_1950_2023.csv"))}

def fig1(th):
    W,H=880,520; L,R,T,B=64,150,92,84; x0,x1=1870,2023; y1=3500
    X=lambda v:L+(v-x0)/(x1-x0)*(W-L-R); Y=lambda v:H-B-v/y1*(H-T-B)
    b=[text(L,34,S["f1t"],th["t1"],19,weight=650),text(L,58,S["f1s"],th["t2"],13.5)]
    for v in range(0,3501,500):
        b+=[f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{th["grid"]}" stroke-width="1"/>',text(L-8,Y(v)+4,fmt(v),th["mut"],12,"end")]
    for v in range(1870,2021,25): b.append(text(X(v),H-B+20,str(v),th["mut"],12,"middle"))
    yk=Y(750)
    b+=[f'<line x1="{L}" x2="{W-R}" y1="{yk:.1f}" y2="{yk:.1f}" stroke="{th["t2"]}" stroke-width="1.5" stroke-dasharray="6 5"/>',text(X(1872),yk-8,S["f1k"],th["t2"],12.5),
        f'<line x1="{X(1950):.1f}" x2="{X(1950):.1f}" y1="{T-6}" y2="{H-B}" stroke="{th["grid"]}" stroke-width="1"/>',text(X(1950)+6,T+6,S["f1n"],th["mut"],11.5)]
    ends=[]
    for i,c in enumerate(ORDER):
        pts=series[c]; col=th["s"][i]; post=[p for p in pts if p[0]>=1950]; pre=[p for p in pts if p[0]<1950]
        if pre:
            d="M"+" L".join(f"{X(x):.1f},{Y(y):.1f}" for x,y in pre+[post[0]])
            b.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.5" stroke-dasharray="3 4" stroke-linecap="round" opacity="0.9"/>')
            b+= [f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="3.5" fill="{col}" stroke="{th["bg"]}" stroke-width="1.5"/>' for x,y in pre]
        d="M"+" L".join(f"{X(x):.1f},{Y(y):.1f}" for x,y in post)
        b.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
        xe,ye=post[-1]; b.append(f'<circle cx="{X(xe):.1f}" cy="{Y(ye):.1f}" r="4" fill="{col}" stroke="{th["bg"]}" stroke-width="2"/>'); ends.append([Y(ye),c,ye])
    ends.sort()
    for k in range(1,len(ends)):
        if ends[k][0]-ends[k-1][0]<16: ends[k][0]=ends[k-1][0]+16
    b+=[text(W-R+10,yy+4,f"{NAMES[c]} {fmt(v)}",th["t1"],12.5) for yy,c,v in ends]
    lx=L
    for i,c in enumerate(ORDER):
        b+=[f'<rect x="{lx}" y="{H-46}" width="14" height="4" rx="2" fill="{th["s"][i]}"/>',text(lx+20,H-40,NAMES[c],th["t2"],12)]; lx+=20+len(NAMES[c])*7.4+22
    b.append(text(L,H-14,S["f1src"],th["mut"],11))
    save(S["f1"],th,W,H,b,S["f1title"],S["f1desc"])

def fig2(th):
    W,H=880,380; T=96; rowh=44; L=120; pw=300; gap=90; p1x=L; p2x=L+pw+gap; m1=16; m2=50
    b=[text(24,34,S["f2t"],th["t1"],18,weight=650),text(24,58,S["f2s"],th["t2"],13.5),text(p1x,T-12,S["f2a"],th["t1"],13,weight=600),text(p2x,T-12,S["f2b"],th["t1"],13,weight=600)]
    for v in (0,5,10,15):
        x=p1x+v/m1*pw; b+=[f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T}" y2="{T+rowh*5}" stroke="{th["grid"]}"/>',text(x,T+rowh*5+18,f"×{v}" if v else "0",th["mut"],12,"middle")]
    for v in (0,10,20,30,40,50):
        x=p2x+v/m2*pw; b+=[f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T}" y2="{T+rowh*5}" stroke="{th["grid"]}"/>',text(x,T+rowh*5+18,("−"+pct(v,0)) if v else "0",th["mut"],12,"middle")]
    for i,c in enumerate(sorted(ORDER,key=lambda c:-float(pv[c]["prod_multiple"]))):
        y=T+i*rowh+rowh/2; m=float(pv[c]["prod_multiple"]); w=m/m1*pw; hc=-float(pv[c]["hours_change_pct"]); w2=hc/m2*pw
        b+=[text(L-12,y+4,NAMES[c],th["t1"],13,"end"),bar(p1x,y-10,w,th["s"][0]),text(p1x+w+6,y+4,"×"+fmt(m,1),th["t1"],12.5),
            bar(p2x,y-10,w2,th["s"][1]),text(p2x+w2+6,y+4,"−"+pct(hc),th["t1"],12.5)]
    b.append(text(W-12,H-14,S["f2src"],th["mut"],11,"end"))
    save(S["f2"],th,W,H,b,S["f2title"],S["f2desc"])

def fig3(th):
    W,H=880,360; T=110; rowh=40; L=120; pw=640; mx=1800
    b=[text(24,34,S["f3t"],th["t1"],18,weight=650),text(24,58,S["f3s"],th["t2"],13.5)]
    lx=L
    for lab,col in ((S["f3l1"],th["s"][1]),(S["f3l2"],th["s"][0])):
        b+=[f'<rect x="{lx}" y="76" width="14" height="10" rx="2" fill="{col}"/>',text(lx+20,85,lab,th["t2"],12.5)]; lx+=20+len(lab)*7+28
    for v in range(0,1801,300):
        x=L+v/mx*pw; b+=[f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T-6}" y2="{T+rowh*5}" stroke="{th["grid"]}"/>',text(x,T+rowh*5+18,fmt(v),th["mut"],12,"middle")]
    for i,c in enumerate(sorted(ORDER,key=lambda c:float(pv[c]["hours_1950"])/float(pv[c]["prod_multiple"]))):
        y=T+i*rowh; real=float(pv[c]["hours_2023"]); need=float(pv[c]["hours_1950"])/float(pv[c]["prod_multiple"])
        b.append(text(L-12,y+16,NAMES[c],th["t1"],13,"end"))
        for j,(v,col) in enumerate(((real,th["s"][1]),(need,th["s"][0]))):
            w=v/mx*pw; yy=y+j*15; b.append(bar(L,yy,w,col,13,3))
            lab=fmt(v)+(f" h (≈ {fmt(v/50,1)} {S['f3wk']})" if j==1 else " h")
            b.append(text(L+w+6,yy+10.5,lab,th["t1"] if j==1 else th["t2"],12))
    b.append(text(W-12,H-14,S["f3src"],th["mut"],11,"end"))
    save(S["f3"],th,W,H,b,S["f3title"],S["f3desc"])

def fig4(th):
    W,H=880,360; T=112; rowh=40; L=300; pw=460; mx=160; vals=[21,98,91,154,9]
    b=[text(24,34,S["f4t"],th["t1"],18,weight=650),text(24,58,S["f4s"],th["t2"],13.5)]
    lx=24
    for lab,col in zip(S["f4l"],(th["s"][0],th["s"][1])):
        b+=[f'<rect x="{lx}" y="74" width="14" height="10" rx="2" fill="{col}"/>',text(lx+20,83,lab,th["t2"],12.5)]; lx+=20+len(lab)*7+28
    for v in (0,50,100,150):
        x=L+v/mx*pw; b+=[f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T-6}" y2="{T+rowh*5}" stroke="{th["grid"]}"/>',text(x,T+rowh*5+18,("+"+pct(v,0)) if v else "0",th["mut"],12,"middle")]
    for i,(lab,v) in enumerate(zip(S["f4i"],vals)):
        y=T+i*rowh+rowh/2; w=v/mx*pw
        b+=[text(L-12,y+4,lab,th["t1"],13,"end"),bar(L,y-10,w,th["s"][0] if i<2 else th["s"][1]),text(L+w+6,y+4,"+"+pct(v,0),th["t1"],12.5)]
    b.append(text(24,H-12,S["f4src"],th["mut"],11))
    save(S["f4"],th,W,H,b,S["f4title"],S["f4desc"])

def fig5(th):
    W,H=880,320; L=40; R=40; T=96; bh=46; pw=W-L-R; tot=sum(p[2] for p in S["f5p"]); x=L
    b=[text(L,34,S["f5t"],th["t1"],18,weight=650),text(L,58,S["f5s"],th["t2"],13.5)]
    for i,(n,d,wk) in enumerate(S["f5p"]):
        w=wk/tot*pw
        b+=[f'<rect x="{x+1:.1f}" y="{T}" width="{w-2:.1f}" height="{bh}" rx="4" fill="{th["s"][i]}"/>',text(x+w/2,T+bh/2+5,f"{wk} {S['f5w']}","#0b0b0b",13,"middle",650),text(x+6,T+bh+22,n,th["t1"],13,weight=600)]
        b+=[text(x+6,T+bh+40+k*16,part,th["t2"],11.5) for k,part in enumerate(d.split("; "))]; x+=w
    gy=H-56; b+=[f'<rect x="{L}" y="{gy}" width="{pw}" height="8" rx="4" fill="{th["grid"]}"/>',text(L,gy+26,S["f5c"],th["t2"],12)]
    save(S["f5"],th,W,H,b,S["f5title"],S["f5desc"])

if __name__=="__main__":
    os.makedirs(OUT,exist_ok=True)
    for n,th in THEMES.items():
        th["_n"]=n
        for f in (fig1,fig2,fig3,fig4,fig5): f(th)
    print(LANG,"ok")
