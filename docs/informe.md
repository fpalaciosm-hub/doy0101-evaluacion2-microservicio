# Informe Técnico: Observabilidad y Entornos Reales en DevOps
**Asignatura:** Ingeniería DevOps (DOY0101)  
**Evaluación:** Evaluación Parcial N°3  

---

## 1. Mapa del Pipeline CI/CD (IE4)
El flujo de trabajo automatizado implementado en GitHub Actions consta de las siguientes etapas secuenciales:
1. **Test:** Descarga el código, instala las dependencias de Python desde `requirements.txt` y ejecuta pruebas unitarias automatizadas con `pytest`.
2. **Security Audit and Quality Gate (Freno Automático):** Ejecuta un script personalizado para auditar la presencia de credenciales o secretos expuestos. Si este script detecta un fallo, el pipeline se detiene inmediatamente (Mecanismo de Freno), impidiendo el paso a producción.
3. **Continuous Deployment to AWS EKS:** Despliega de forma declarativa los manifiestos de la carpeta `/k8s` (`deployment.yaml` y `service.yaml`) hacia el clúster de Amazon EKS.

---

## 2. Justificación de Decisiones Técnicas basadas en Datos (IE4)
Para garantizar la estabilidad del microservicio en producción, el equipo tomará acciones operativas basadas en las métricas del Dashboard:

* **Métrica: Consumo de CPU/Memoria (cgroup)**
  * *Decisión:* Si el consumo de memoria del Pod de la aplicación supera el 85% de forma sostenida durante 5 minutos, se gatillará una política de auto-escalado horizontal (HPA) para levantar una réplica adicional en AWS EKS y mitigar la carga.
* **Métrica: Tasa de Errores Registrados (Respuestas 5xx)**
  * *Decisión:* Si la tasa de respuestas HTTP 5xx supera el 2% en un intervalo de 10 minutos, el pipeline activará una alerta en nuestros canales de comunicación y se evaluará un Rollback inmediato a la versión anterior del contenedor.
* **Métrica: Duración del Despliegue (Deploy Job Duration)**
  * *Decisión:* Si el tiempo de compilación y subida a producción duplica su promedio habitual (sobre los 8 minutos), se iniciará una revisión del almacenamiento en caché del Dockerfile multi-etapa.

---

## 3. Conclusiones y Reflexiones Individuales Obligatorias (Sin Uso de IA)
*[REPLICA ESTE APARTADO CON LAS PALABRAS PROPIAS DE CADA INTEGRANTE]*

* **Reflexión Integrante 1 (Tu Nombre):** Durante este encargo, aprendí la importancia de la observabilidad y cómo la instrumentación en Python nos permite anteponernos a fallas críticas en entornos de producción simulados utilizando métricas en tiempo real.
* **Reflexión Integrante 2 (Nombre Compañero):** En esta entrega profundicé en la automatización de la seguridad y el diseño de políticas estrictas que frenen el pipeline para proteger la infraestructura en la nube.
