from transformers import pipeline
ner_pipe = pipeline(task="ner", model ="PlanTL-GOB-ES/roberta-base-bne-capitel-ner")
ner_pipe_plus = pipeline(task="ner", model ="PlanTL-GOB-ES/roberta-base-bne-capitel-ner-plus")
ner_pipe_large = pipeline(task="ner", model ="PlanTL-GOB-ES/roberta-large-bne-capitel-ner")
sequence = """Datos del paciente.
Nombre:  Ernesto.
Apellidos: Rivera Bueno.
NHC: 368503.
NASS: 26 63514095.
Domicilio:  Calle Miguel Benitez 90.
Localidad/ Provincia: Madrid.
CP: 28016.
Datos asistenciales.
Fecha de nacimiento: 03/03/1946.
País: España.
Edad: 70 años Sexo: H.
Fecha de Ingreso: 12/12/2016.
Médico:  Ignacio Navarro Cuéllar NºCol: 28 28 70973.
Informe clínico del paciente: Paciente de 70 años de edad, minero jubilado, sin alergias medicamentosas conocidas, que presenta como antecedentes personales: accidente laboral antiguo con fracturas vertebrales y costales; intervenido de enfermedad de Dupuytren en mano derecha y by-pass iliofemoral izquierdo; Diabetes Mellitus tipo II, hipercolesterolemia e hiperuricemia; enolismo activo, fumador de 20 cigarrillos / día.
Es derivado desde Atención Primaria por presentar hematuria macroscópica postmiccional en una ocasión y microhematuria persistente posteriormente, con micciones normales.
En la exploración física presenta un buen estado general, con abdomen y genitales normales; tacto rectal compatible con adenoma de próstata grado I/IV.
En la analítica de orina destaca la existencia de 4 hematíes/ campo y 0-5 leucocitos/campo; resto de sedimento normal.
Hemograma normal; en la bioquímica destaca una glucemia de 169 mg/dl y triglicéridos de 456 mg/dl; función hepática y renal normal. PSA de 1.16 ng/ml.
Las citologías de orina son repetidamente sospechosas de malignidad.
En la placa simple de abdomen se valoran cambios degenerativos en columna lumbar y calcificaciones vasculares en ambos hipocondrios y en pelvis.
La ecografía urológica pone de manifiesto la existencia de quistes corticales simples en riñón derecho, vejiga sin alteraciones con buena capacidad y próstata con un peso de 30 g.
En la UIV se observa normofuncionalismo renal bilateral, calcificaciones sobre silueta renal derecha y uréteres arrosariados con imágenes de adición en el tercio superior de ambos uréteres, en relación a pseudodiverticulosis ureteral. El cistograma demuestra una vejiga con buena capacidad, pero paredes trabeculadas en relación a vejiga de esfuerzo. La TC abdominal es normal.
La cistoscopia descubre la existencia de pequeñas tumoraciones vesicales, realizándose resección transuretral con el resultado anatomopatológico de carcinoma urotelial superficial de vejiga.
Remitido por: Ignacio Navarro Cuéllar c/ del Abedul 5-7, 2º dcha 28036 Madrid, España E-mail: nnavcu@hotmail.com.
"""
for entity in ner_pipe(sequence):
    print(entity)