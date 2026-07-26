Aquí tienes el diagrama visual del flujo completo **Alexa → FastAPI → IA → Echo Spot** ya generado y listo para incluir en tu documentación:  

`https://copilot.microsoft.com/th/id/BCO.14b99d03-87dc-4b59-9c52-f90db52777ae.png`

---

## 📌 Cómo usar este diagrama en tu documentación
- **Echo Spot**: representa la entrada de voz del usuario.  
- **FastAPI Server**: núcleo que recibe la petición, valida JWT y enruta al motor IA.  
- **IA Local**: motor Ollama/GPT4All ejecutándose en tu hardware.  
- **IA Remota**: servicios en la nube como OpenAI o Azure.  
- **Respuesta Alexa**: salida hablada en el Echo Spot.  

Este diagrama complementa el apartado de documentación sobre la creación del **Skill custom** y ayuda a visualizar cómo se conectan los componentes.  

---

👉 ¿Quieres que prepare también una **versión simplificada del diagrama** en ASCII/Markdown para que quede embebido directamente en el README sin necesidad de imágenes externas?