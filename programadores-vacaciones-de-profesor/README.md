# Programadores con vacaciones de profesor

*Por qué la inteligencia artificial nos obliga a decidir quién se queda con el tiempo que ahorra.*

Aclaro el titular antes de nada: no pido literalmente tres meses de vacaciones para cada programador. Los tres meses son un lema. Lo que defiendo va en serio: si las máquinas ya hacen una parte creciente de nuestro trabajo, alguien tiene que decidir qué se hace con el tiempo que liberan. Hoy esa decisión se toma sola, por defecto, y casi siempre en la misma dirección: más trabajo.

## 1. El programador ya no solo programa: enseña

Durante décadas, programar fue traducir necesidades humanas a instrucciones que una máquina pudiera ejecutar. Pensábamos, escribíamos, depurábamos y respondíamos de lo que fallaba.

Con los agentes de IA, una parte de esa escritura la hace otro. Pero el agente no llega sabiendo. Hay que darle el contexto del proyecto, las convenciones, los límites de seguridad y los errores que no debe repetir. Hay que partir el problema en tareas que se puedan comprobar, revisar lo que entrega y corregir el rumbo cuando se equivoca. Y cuando trabajan varios a la vez, hay que coordinarlos para que cada uno no resuelva su parte de una forma incompatible con la de los demás.

Eso se parece mucho más al trabajo de un profesor que al de un operario: preparar el temario, poner los ejercicios, corregir los exámenes, enseñar criterio. El programador está pasando de producir la solución a construir las condiciones para que otros la produzcan bien.

Con una diferencia importante: este alumno no duerme.

## 2. El alumno que nunca duerme y el profesor que no puede desconectar

Supongamos que un agente escribe en diez minutos lo que a una persona le llevaba dos horas, y que puede hacerlo de madrugada. Que se puedan generar mil respuestas no significa que alguien pueda evaluarlas bien en cinco minutos. La IA abarata producir código; garantizar que ese código es correcto y seguro sigue costando lo mismo, o más.

Y ni siquiera la velocidad está garantizada. En 2025, METR hizo un ensayo controlado con 16 programadores experimentados en 246 tareas reales de sus propios proyectos. Con IA tardaron un 19 % más. Más revelador aún fue lo que creían: antes de empezar esperaban ir un 24 % más rápido y, al terminar, seguían convencidos de haber ganado un 20 %. En 2026 repitieron el estudio con herramientas nuevas, y esta vez los datos apuntaban a cierta aceleración, pero los propios autores concluyeron que su experimento ya no servía para medirla con fiabilidad. La lección que sí se mantiene es incómoda: medimos muy mal cuánto tiempo nos ahorra la IA.

Allí donde lo ahorra, además, el ahorro rara vez se queda en nosotros. Se va a revisar y a supervisar. El programador termina escribiendo menos líneas y respondiendo de muchas más.

Si una organización convierte cada hora que ganan las máquinas en más entregas, el beneficio de la tecnología se transforma en una obligación. La productividad artificial no puede convertirse en una condena humana a la disponibilidad infinita.

## 3. La pregunta que Keynes ya hizo en 1930

En 1930, John Maynard Keynes calculó que en un siglo el nivel de vida de los países ricos se multiplicaría por entre cuatro y ocho, y que la generación de nuestros nietos podría repartirse el poco trabajo que quedara en turnos de tres horas o semanas de quince. Acertó en la riqueza y falló en el tiempo libre: hacia 1929, un trabajador industrial a tiempo completo hacía unas 48 horas semanales; hoy seguimos en torno a 38-40.

La explicación tiene más de siglo y medio. En 1865, William Stanley Jevons sostuvo que las máquinas de vapor más eficientes harían que Inglaterra gastara más carbón, no menos: al abaratarse su uso, se usaría para más cosas. Con el software ya está pasando. Cuando escribir código cuesta menos, se escribe mucho más código.

Por eso la pregunta importante es otra. **Cuando una máquina hace en diez minutos lo que antes costaba dos horas, ¿quién se queda con la hora y cincuenta minutos?** Puede quedársela la empresa, en forma de más producción. Puede quedársela la calidad, en forma de más revisión. O puede volver, en parte, a la persona.

La primera opción es la más fácil de medir y la que ocurre por defecto. No es la única legítima. La tecnología no elige entre ellas: eligen las organizaciones y las leyes.

## 4. Por qué el profesor (y dónde falla la comparación)

Un modelo de IA no es un niño. La mayoría de los programadores ni siquiera lo entrenan: configuran un sistema ya entrenado con instrucciones, contexto, herramientas y pruebas. Decir que educamos agentes igual que los profesores educan niños sería falso.

Tampoco es verdad que los profesores tengan tres meses libres. En España, el periodo sin clases ronda los dos meses y medio, y sus vacaciones son agosto. Julio es un mes sin clases, no sin trabajo: cierre del curso, memorias, formación y preparación del siguiente. Quien conoce el oficio sabe que un profesor no está de vacaciones en julio.

Pero justo ahí está lo útil de la comparación. El trabajo docente se organiza en ciclos: periodos intensos con el aula llena y periodos para preparar, evaluar y recuperarse. Lo que la comparación cuestiona es una costumbre de nuestro sector: creer que la presencia continua de una persona equivale a productividad.

## 5. El puente que falta: solo se descansa si la verificación no depende de ti

Esta propuesta tiene un punto débil. Si el cuello de botella es la revisión humana, más agentes significan más trabajo, no menos. Para que el programador pueda irse, el sistema tiene que poder seguir sin él, y eso se construye:

- **Pruebas que deciden solas** si algo está bien, en lugar de una persona leyéndolo todo.
- **Un revisor distinto del que construye.** El agente que hace el trabajo no puede ser el que lo da por bueno.
- **Pasos que se pueden deshacer.** Cada cambio con su copia previa y su vuelta atrás automática si algo deja de responder.
- **Límites y frenos:** qué puede tocar cada agente, cuánto puede gastar y quién lo para.
- **Guardias para lo que de verdad importa,** y nadie de guardia para lo que no.

Ese andamiaje cuesta, y mucho: escribir las pruebas, las reglas y los revisores también es trabajo humano. Es, precisamente, el julio del profesor. La diferencia es que se paga una vez y se amortiza cada noche.

Con todo eso se puede separar algo que solemos mezclar: la continuidad del servicio y la continuidad de la persona. Un sistema puede funcionar permanentemente sin exigir que la misma persona permanezca permanentemente trabajando. Los hospitales y los aeropuertos llevan décadas haciéndolo con turnos. Lo nuevo es que parte de esos turnos los puede cubrir software, siempre que sepamos comprobar lo que hace.

## 6. Lo que he aprendido en Acrònims

Esto lo escribo desde dentro. En Acrònims, un pequeño grupo de proyectos que estoy montando, buena parte del trabajo técnico lo hacen agentes de IA coordinados por un agente central que me rinde cuentas.

Mucho de ese trabajo ocurre de madrugada: actualizaciones, cambios de configuración, revisiones. La regla es que cada tanda lleve su copia de seguridad y su vuelta atrás automática, y que después un agente distinto del que hizo el cambio compruebe que todo responde igual que antes. Nada cuenta como hecho hasta que hay una prueba que alguien que no lo hizo puede repetir. Por la mañana me llega un resumen corto con lo que se ha hecho y lo que necesita mi decisión.

Mi trabajo ha cambiado: escribo poco código. Decido qué hay que hacer, defino cómo sabremos que está bien hecho y apruebo lo que tiene riesgo.

No funciona sin errores. Hemos roto cosas nosotros mismos, y hemos tenido agentes que daban por terminado un trabajo que no lo estaba. Pero cada fallo deja una regla nueva, y cada regla nueva es una noche menos en la que hace falta que alguien esté despierto.

Conviene ser honesto sobre lo que esto demuestra. Aquí no hay una plantilla con la que repartir el tiempo ganado, así que no prueba la parte social de la tesis. Prueba la técnica: que el puente del apartado anterior se puede construir hoy, con herramientas que ya existen. Lo que falta para repartirlo no es tecnología.

## 7. Una propuesta concreta: el calendario por ciclos

En lugar de exigir tres meses para todos, propongo que los equipos que trabajan intensivamente con agentes se organicen por ciclos:

1. **Planificar y enseñar.** Objetivos, arquitectura, documentación y, sobre todo, los criterios con los que se comprobará cada entrega.
2. **Ejecutar con agentes.** Las personas resuelven excepciones y toman las decisiones con riesgo.
3. **Evaluar y consolidar.** Pruebas completas, seguridad y rendimiento. Cada fallo se convierte en una instrucción o una regla mejor.
4. **Descansar y renovarse.** Periodos protegidos de descanso, formación e investigación, sin quedar disponibles solo porque las máquinas siguen trabajando.

No todos los ciclos durarán lo mismo, y no todos los servicios podrán quedarse sin supervisión: lo crítico necesitará guardias y redundancia. Pero cuando el modelo demuestre que mantiene la calidad y el servicio, tocará negociar cómo se reparte lo ganado: semana de cuatro días, jornadas más cortas, permisos más largos o, por qué no, veranos más largos.

En 2022, 61 empresas británicas probaron durante seis meses la semana de cuatro días: el 80 % de las horas por el mismo sueldo. Al terminar, 56 quisieron seguir; un año después, al menos 54 la mantenían, 31 ya de forma permanente, según declararon las propias empresas. No eran empresas de agentes de IA. Con agentes hay más margen que repartir; que se reparta depende, otra vez, de quién lo decida.

## 8. Conclusión: que la IA también nos haga más libres

Estamos invirtiendo cantidades enormes en construir máquinas que trabajan más rápido y con más autonomía. Es razonable preguntar qué gana con ello la persona que tiene que diseñarlas, vigilarlas y responder cuando se equivocan.

Si cada hora humana rinde cada vez más, no hay ninguna razón técnica para que el tiempo libre de quienes producen el software siga igual. Hay razones económicas y políticas, y esas se pueden cambiar.

La verdadera revolución de la IA no será solo que las máquinas hagan parte del trabajo de las personas. Será que las personas dejen de estar obligadas a llenar con más trabajo todo el tiempo que las máquinas les ahorran.

Si para conseguirlo hay que empezar a llamar profesores a los programadores, alumnos a los agentes y verano a la desconexión, quizá la broma esté señalando algo más serio de lo que parece. Al fin y al cabo, si ya hemos creado máquinas que trabajan mientras dormimos, lo mínimo es empezar a hablar de cuándo nos toca dormir a nosotros.

*Raúl Illana, profesor de agentes que no conocen el concepto de vacaciones.*

---

### Fuentes

- METR (2025), *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR (2026), actualización del estudio: https://metr.org/blog/2026-02-24-uplift-update/
- J. M. Keynes (1930), *Economic Possibilities for our Grandchildren*. Contexto de la cita de las quince horas: https://quoteinvestigator.com/2025/02/03/work-week/
- M. Huberman y C. Minns (2007), *The times they are not changin': Days and hours of work in Old and New Worlds, 1870–2000*: https://personal.lse.ac.uk/minns/Huberman_Minns_EEH_2007.pdf
- W. S. Jevons (1865), *The Coal Question*.
- Prueba británica de la semana de cuatro días (2022): https://www.npr.org/2023/02/21/1158507132/uk-study-companies-four-day-workweek · seguimiento a un año, Autonomy (2024): https://autonomy.work/2024/02/21/make-it-stick/

*Escrito con ayuda de herramientas de IA. Las ideas y la firma son mías.*
