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
