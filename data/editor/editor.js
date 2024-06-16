function format(command) {
    document.execCommand(command, false, null);
}

function changeFontSize() {
    const size = document.getElementById('fontSize').value;
    document.execCommand('fontSize', false, size);
}

function changeFontColor() {
    const color = document.getElementById('fontColor').value;
    document.execCommand('foreColor', false, color);
}

function downloadAsJSON() {
    const content = document.getElementById('editorContainer').innerHTML;
    const json = JSON.stringify({ content });
    const blob = new Blob([json], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'document.json';
    link.click();
}

function loadJSON() {
    const input = document.getElementById('fileInput');
    const file = input.files[0];
    const reader = new FileReader();

    reader.onload = function(event) {
        const json = event.target.result;
        const data = JSON.parse(json);
        document.getElementById('editorContainer').innerHTML = data.content;
    };

    reader.readAsText(file);
}

function downloadAsText() {
    const text = document.getElementById('editor').innerText;
    const blob = new Blob([text], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'document.txt';
    link.click();
}

function undo() {
    document.execCommand('undo');
}

function redo() {
    document.execCommand('redo');
}

function clearFormatting() {
    document.execCommand('removeFormat', false, null);
}

function alignText(align) {
    document.execCommand('justify' + align, false, null);
}

function toggleList(command) {
    document.execCommand(command, false, null);
}

function insertLink() {
    const url = document.getElementById('linkURL').value.trim();
    if (url !== '') {
        document.execCommand('createLink', false, url);
    } else {
        alert('Bitte geben Sie eine URL ein.');
    }
}

function preview() {
    const printWindow = window.open('', 'Print Preview', 'height=600,width=800');
    printWindow.document.write('<html><head><title>Druckvorschau</title></head><body>');
    printWindow.document.write('<div id="editorContainer">');
    printWindow.document.write(document.getElementById('editorContainer').innerHTML);
    printWindow.document.write('</div>');
    printWindow.document.write('</body></html>');
}

const editor = document.getElementById('editor');
const wordCountDisplay = document.getElementById('wordCount');
const charCountDisplay = document.getElementById('charCount');

editor.addEventListener('input', function() {
    const text = editor.innerText;
    const words = text.trim().split(/\s+/).filter(Boolean);
    const wordCount = words.length;
    const charCount = text.length;
    wordCountDisplay.textContent = wordCount;
    charCountDisplay.textContent = charCount;
});
