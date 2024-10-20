function generatePDF(service, windowNumber) {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    doc.setFontSize(20);
    doc.text("Талон", 20, 30);
    doc.setFontSize(14);
    doc.text(`Номер: ${Math.floor(Math.random() * 1000)}`, 20, 50);
    doc.text(`Выбранная услуга: ${service}`, 20, 70);
    doc.text(`Окно: ${windowNumber}`, 20, 90);

    doc.save("Талон.pdf");
}
