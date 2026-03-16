const worksheetContainer = document.getElementById('worksheet');
const generateBtn = document.getElementById('generateBtn');
const regenerateBtn = document.getElementById('regenerateBtn');
const downloadBtn = document.getElementById('downloadBtn');

let currentWorksheet = null;

function collectPayload(seed = null) {
  return {
    grade: document.getElementById('grade').value,
    topic: document.getElementById('topic').value,
    difficulty: document.getElementById('difficulty').value,
    seed,
  };
}

function renderWorksheet(data) {
  const exercisesHtml = data.exercises.map((item) => `<li>${item}</li>`).join('');
  worksheetContainer.innerHTML = `
    <h2>${data.title}</h2>
    <div class="header-line">
      <span><strong>Aluno(a):</strong> ____________________</span>
      <span><strong>Data:</strong> ____/____/______</span>
    </div>
    <p><strong>Instruções:</strong> ${data.instructions}</p>
    <p><strong>Ano:</strong> ${data.grade} | <strong>Tema:</strong> ${data.topic} | <strong>Dificuldade:</strong> ${data.difficulty}</p>
    <ol class="exercise-list">${exercisesHtml}</ol>
    <div class="challenge"><strong>Desafio Final:</strong> ${data.final_challenge}</div>
    <p class="illustrations">${data.illustrations.join(' ')}</p>
  `;
}

async function generate(seed = null) {
  const response = await fetch('/api/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(collectPayload(seed)),
  });
  currentWorksheet = await response.json();
  renderWorksheet(currentWorksheet);
}

generateBtn.addEventListener('click', () => generate());
regenerateBtn.addEventListener('click', () => generate());

downloadBtn.addEventListener('click', async () => {
  if (!currentWorksheet) {
    await generate();
  }

  const response = await fetch('/api/export-pdf', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(currentWorksheet),
  });

  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'atividade-portugues.pdf';
  a.click();
  URL.revokeObjectURL(url);
});

generate();
