const submitBtn = document.getElementById('submit-btn');
const journalInput = document.getElementById('journal-input');
const resultDiv = document.getElementById('result');
const loadingDiv = document.getElementById('loading');

submitBtn.addEventListener('click', function() {
    const text = journalInput.value;

    if (text.trim() === '') {
        resultDiv.textContent = 'Please write something first.';
        return;
    }

    loadingDiv.style.display = 'block';
    resultDiv.textContent = '';

    fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {
        loadingDiv.style.display = 'none';
        resultDiv.textContent = 'Mood: ' + data.label + ' (confidence: ' + Math.round(data.score * 100) + '%)';
        journalInput.value = '';
    })
    .catch(error => {
        loadingDiv.style.display = 'none';
        resultDiv.textContent = 'Something went wrong. Please try again.';
    });
});

function loadChart() {
    fetch('/entries')
        .then(res => res.json())
        .then(data => {
            const last7 = data.slice(-7);

            const labels = last7.map(entry => {
                const date = new Date(entry.timestamp);
                return date.toLocaleDateString();
            });

            const scores = last7.map(entry => {
                return entry.label === 'POSITIVE' ? entry.score * 100 : -(entry.score * 100);
            });

            const ctx = document.getElementById('mood-chart');

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Mood Score',
                        data: scores,
                        backgroundColor: scores.map(s => s >= 0 ? '#00c896' : '#e94560')
                    }]
                },
                options: {
                    scales: {
                        y: {
                            min: -100,
                            max: 100
                        }
                    }
                }
            });
        });
}

loadChart();
