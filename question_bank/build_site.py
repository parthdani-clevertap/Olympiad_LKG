import json

def build_site():
    print("Reading questions...")
    try:
        with open("questions.json", "r") as f:
            questions_data = json.load(f)
    except FileNotFoundError:
        print("Error: questions.json not found. Run generate_questions.py first.")
        return

    # Using a standard string to avoid f-string escaping hell with CSS/JS
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Science Olympiad Prep</title>
    <style>
        :root {
            --primary: #FF6B6B;
            --secondary: #4ECDC4;
            --accent: #FFE66D;
            --dark: #2C3E50;
            --light: #F7F9FC;
            --success: #2ecc71;
            --error: #e74c3c;
        }
        
        * {
            box-sizing: border-box;
            font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
            user-select: none;
            -webkit-user-select: none;
        }

        body {
            margin: 0;
            padding: 0;
            background-color: var(--light);
            color: var(--dark);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Header */
        header {
            background: var(--primary);
            color: white;
            width: 100%;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            position: relative;
        }

        h1 { margin: 0; font-size: 1.5rem; }
        h2 { margin: 0; font-size: 1.2rem; }

        .home-btn {
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            background: white;
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            font-size: 1.5rem;
            cursor: pointer;
            display: none;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }

        /* Container */
        .container {
            width: 100%;
            max-width: 800px;
            padding: 1rem;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        /* Module Grid */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
            padding: 1rem;
        }

        .card {
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
            border: 4px solid transparent;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border-color: var(--secondary);
        }

        .card-icon { font-size: 3rem; }
        .card-title { font-size: 1.2rem; font-weight: bold; }

        /* Quiz View */
        .quiz-container {
            display: none;
            flex-direction: column;
            align-items: center;
            width: 100%;
            height: 100%;
        }

        .progress-bar {
            width: 100%;
            height: 12px;
            background: #ddd;
            border-radius: 6px;
            margin-bottom: 2rem;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: var(--secondary);
            width: 0%;
            transition: width 0.3s ease;
        }

        .question-text {
            font-size: 2rem;
            text-align: center;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            gap: 10px;
            justify-content: center;
        }

        .speak-btn {
            background: var(--accent);
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 1.5rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            transition: transform 0.1s;
        }

        .speak-btn:active {
            transform: scale(0.95);
        }

        .options-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            width: 100%;
            max-width: 600px;
            margin-bottom: 2rem;
        }

        .option-card {
            background: white;
            border-radius: 20px;
            padding: 2rem;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 6rem;
            cursor: pointer;
            border: 6px solid #e0e0e0;
            transition: all 0.2s;
            min-height: 200px;
        }

        .option-card:active { transform: scale(0.95); }
        
        .option-card.correct {
            background-color: #d4edda;
            border-color: var(--success);
            animation: bounce 0.5s;
        }
        
        .option-card.wrong {
            background-color: #f8d7da;
            border-color: var(--error);
            opacity: 0.6;
            animation: shake 0.4s;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
            40% {transform: translateY(-20px);}
            60% {transform: translateY(-10px);}
        }

        @keyframes shake {
            0%, 100% {transform: translateX(0);}
            25% {transform: translateX(-10px);}
            75% {transform: translateX(10px);}
        }

        .feedback-text {
            font-size: 1.5rem;
            height: 2rem;
            margin-bottom: 1rem;
            font-weight: bold;
        }

        .next-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 1rem 3rem;
            font-size: 1.5rem;
            border-radius: 50px;
            cursor: pointer;
            visibility: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        /* Results View */
        .results-container {
            display: none;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 2rem;
        }

        .score-display {
            font-size: 4rem;
            color: var(--primary);
            margin: 2rem 0;
            font-weight: bold;
        }

        .star-rating { font-size: 3rem; margin-bottom: 2rem; }

    </style>
</head>
<body>

    <header>
        <button class="home-btn" onclick="showHome()">🏠</button>
        <h1 id="header-title">Science Olympiad Prep</h1>
    </header>

    <div class="container" id="app-root">
        <!-- Views will be injected here -->
    </div>

    <!-- DATA EMBED -->
    <script>
        const QUESTION_DATA = __DATA_PLACEHOLDER__;
    </script>

    <!-- LOGIC -->
    <script>
        let currentModuleKey = null;
        let currentQuestionIndex = 0;
        let score = 0;
        let questions = [];
        let canAnswer = true;
        let synth = window.speechSynthesis;

        const appRoot = document.getElementById('app-root');
        const homeBtn = document.querySelector('.home-btn');
        const headerTitle = document.getElementById('header-title');

        // Initial Load
        renderHome();

        function renderHome() {
            homeBtn.style.display = 'none';
            headerTitle.textContent = "Science Olympiad Prep";
            
            let gridHtml = '<div class="grid">';
            for (const [key, value] of Object.entries(QUESTION_DATA)) {
                let icon = "📚";
                if(key.includes("Body")) icon = "💪";
                if(key.includes("Sense")) icon = "👀";
                if(key.includes("Helpers")) icon = "👮";
                if(key.includes("Animal")) icon = "🦁";
                if(key.includes("Plant")) icon = "🌲";
                if(key.includes("Transport")) icon = "🚗";
                if(key.includes("Weather")) icon = "☀️";
                if(key.includes("Safety")) icon = "🚦";
                if(key.includes("Living")) icon = "🐌";
                if(key.includes("Objects")) icon = "🧸";

                gridHtml += `
                    <div class="card" onclick="startModule('${key}')">
                        <div class="card-icon">${icon}</div>
                        <div class="card-title">${key}</div>
                        <div>${value.length} Questions</div>
                    </div>
                `;
            }
            gridHtml += '</div>';
            appRoot.innerHTML = gridHtml;
        }

        function startModule(key) {
            currentModuleKey = key;
            questions = QUESTION_DATA[key];
            currentQuestionIndex = 0;
            score = 0;
            
            homeBtn.style.display = 'flex';
            headerTitle.textContent = key;
            
            renderQuestion();
        }

        function renderQuestion() {
            canAnswer = true;
            const q = questions[currentQuestionIndex];
            const progressPct = ((currentQuestionIndex) / questions.length) * 100;

            appRoot.innerHTML = `
                <div class="quiz-container" style="display:flex">
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: ${progressPct}%"></div>
                    </div>
                    
                    <div class="question-text">
                        <span>${q.question}</span>
                        <button class="speak-btn" onclick="speakText('${q.question.replace(/'/g, "\\'")}')">🔊</button>
                    </div>
                    
                    <div class="options-grid">
                        <div class="option-card" onclick="handleAnswer('a', this)">${q.options[0].content}</div>
                        <div class="option-card" onclick="handleAnswer('b', this)">${q.options[1].content}</div>
                    </div>

                    <div class="feedback-text" id="feedback"></div>
                    <button class="next-btn" onclick="nextQuestion()">Next ➡️</button>
                    <div style="margin-top:20px; font-size:1.2rem; color:#aaa">Question ${currentQuestionIndex + 1} / ${questions.length}</div>
                </div>
            `;
            
            // Auto-speak question for better UX for a 4 yo?
            // Let's stick to button click unless requested, but usually for kids auto-speak is good.
            // The prompt asked for "an option to read it", so button is safest.
        }

        function speakText(text) {
            if (synth.speaking) {
                synth.cancel();
            }
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 0.9; // Slightly slower for kids
            synth.speak(utterance);
        }

        function handleAnswer(selectedId, element) {
            if (!canAnswer) return;
            canAnswer = false;

            const q = questions[currentQuestionIndex];
            const isCorrect = (selectedId === q.correctAnswer);
            const feedbackEl = document.getElementById('feedback');
            const nextBtn = document.querySelector('.next-btn');

            if (isCorrect) {
                element.classList.add('correct');
                feedbackEl.textContent = "Correct! 🎉";
                feedbackEl.style.color = "var(--success)";
                speakText("Correct!");
                score++;
            } else {
                element.classList.add('wrong');
                feedbackEl.textContent = "Oops! The correct answer is " + q.correctContent;
                feedbackEl.style.color = "var(--error)";
                speakText("Oops! Try again next time.");
                
                const cards = document.querySelectorAll('.option-card');
                cards.forEach(card => {
                    if (card.textContent.trim() === q.correctContent) {
                        card.classList.add('correct');
                    }
                });
            }

            nextBtn.style.visibility = 'visible';
        }

        function nextQuestion() {
            currentQuestionIndex++;
            if (currentQuestionIndex >= questions.length) {
                showResults();
            } else {
                renderQuestion();
            }
        }

        function showResults() {
            const percentage = Math.round((score / questions.length) * 100);
            let stars = "⭐⭐⭐";
            let msg = "Amazing Job!";
            
            if (percentage < 50) { stars = "⭐"; msg = "Good Try!"; }
            else if (percentage < 80) { stars = "⭐⭐"; msg = "Great Work!"; }

            appRoot.innerHTML = `
                <div class="results-container" style="display:flex">
                    <h2>Module Complete!</h2>
                    <div class="score-display">${score} / ${questions.length}</div>
                    <div class="star-rating">${stars}</div>
                    <h1>${msg}</h1>
                    <button class="next-btn" style="visibility:visible; margin-top:2rem;" onclick="renderHome()">Back to Menu</button>
                </div>
            `;
            speakText(msg);
        }

        function showHome() {
            if(confirm("Exit this module? Progress will be lost.")) {
                renderHome();
            }
        }

    </script>
</body>
</html>
"""
    
    # Inject the JSON data
    final_html = html_template.replace("__DATA_PLACEHOLDER__", json.dumps(questions_data))

    with open("index.html", "w") as f:
        f.write(final_html)
    print("Successfully built index.html")

if __name__ == "__main__":
    build_site()
