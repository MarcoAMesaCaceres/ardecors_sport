// Función para exportar a PDF
function exportToPDF() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Agregar el encabezado
    doc.setFontSize(18);
    doc.text("Empresa de balones Ardecors", 14, 22);
    
    // Agregar la tabla
    doc.autoTable({
        html: '.table',
        startY: 30,
        styles: {
            fontSize: 10,
            cellPadding: 2,
            overflow: 'linebreak',
            cellWidth: 'wrap'
        },
        columnStyles: {
            0: {cellWidth: 20},
            1: {cellWidth: 30},
            2: {cellWidth: 40},
            3: {cellWidth: 30},
            4: {cellWidth: 20},
            5: {cellWidth: 25},
            6: {cellWidth: 25}
        }
    });

    // Guardar el PDF
    doc.save('ventas_ardecors.pdf');
}

// Función para exportar a Excel
function exportToExcel() {
    // Crear una nueva hoja de cálculo
    let wb = XLSX.utils.book_new();
    
    // Obtener la tabla
    let table = document.querySelector(".table");
    
    // Convertir la tabla a una hoja de cálculo
    let ws = XLSX.utils.table_to_sheet(table);
    
    // Agregar el encabezado
    XLSX.utils.sheet_add_aoa(ws, [["Empresa de balones Ardecors"]], { origin: "A1" });
    
    // Combinar celdas para el encabezado
    if(!ws['!merges']) ws['!merges'] = [];
    ws['!merges'].push(XLSX.utils.decode_range("A1:G1"));
    
    // Ajustar el estilo del encabezado
    ws['A1'].s = { font: { bold: true, sz: 16 }, alignment: { horizontal: "center" } };
    
    // Agregar la hoja al libro
    XLSX.utils.book_append_sheet(wb, ws, "Ventas");
    
    // Guardar el archivo
    XLSX.writeFile(wb, "ventas_ardecors.xlsx");
}

// Asignar las funciones a los botones (asegúrate de tener botones con estos IDs en tu HTML)
document.getElementById('exportPDF').addEventListener('click', exportToPDF);
document.getElementById('exportExcel').addEventListener('click', exportToExcel);