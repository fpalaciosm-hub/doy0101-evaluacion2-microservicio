#!/bin/bash
echo "====================================================="
echo "🔒 Ejecutando Auditoría de Seguridad Automatizada..."
echo "====================================================="

# Buscar posibles secretos hardcodeados en los archivos Python
if grep -rniE "(password|passwd|secret|api_key|token|private_key) *=" --exclude-dir=.git --exclude="security-check.sh" .; then
    echo "❌ ERROR CRÍTICO: Se detectaron posibles secretos expuestos en el código fuente."
    exit 1
else
    echo "✅ Cumplimiento de Seguridad: No se encontraron secretos evidentes en el código."
    echo "====================================================="
    exit 0
fi
