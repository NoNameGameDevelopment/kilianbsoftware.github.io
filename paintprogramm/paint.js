const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const colorPicker = document.getElementById('color');
const sizePicker = document.getElementById('size');
const brushButton = document.getElementById('brush');
const eraserButton = document.getElementById('eraser');
const clearButton = document.getElementById('clear');
const downloadButton = document.getElementById('download');
const colorButtons = document.querySelectorAll('.color-btn');

let painting = false;
let color = colorPicker.value;
let size = sizePicker.value;
let tool = 'brush';  // 'brush' or 'eraser'

canvas.addEventListener('mousedown', startPainting);
canvas.addEventListener('mouseup', stopPainting);
canvas.addEventListener('mousemove', draw);

colorPicker.addEventListener('input', (e) => {
    color = e.target.value;
});

sizePicker.addEventListener('input', (e) => {
    size = e.target.value;
});

brushButton.addEventListener('click', () => {
    tool = 'brush';
    color = colorPicker.value;
});

eraserButton.addEventListener('click', () => {
    tool = 'eraser';
});

clearButton.addEventListener('click', clearCanvas);

downloadButton.addEventListener('click', downloadCanvas);

colorButtons.forEach(button => {
    button.addEventListener('click', () => {
        color = button.dataset.color;
        colorPicker.value = color;  // Aktualisiert den Farb-Picker
        tool = 'brush';
    });
});

function startPainting(e) {
    painting = true;
    draw(e);
}

function stopPainting() {
    painting = false;
    ctx.beginPath();
}

function draw(e) {
    if (!painting) return;

    ctx.lineWidth = size;
    ctx.lineCap = 'round';

    if (tool === 'brush') {
        ctx.strokeStyle = color;
    } else if (tool === 'eraser') {
        ctx.strokeStyle = '#FFFFFF';
    }

    ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function downloadCanvas() {
    const link = document.createElement('a');
    link.download = 'drawing.png';
    link.href = canvas.toDataURL();
    link.click();
}
