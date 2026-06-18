import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    background: radial-gradient(circle, #000000, #020024);
    display: flex;
    justify-content: center;
}

canvas {
    border: 2px solid #0ff;
    box-shadow: 0 0 25px #0ff;
    margin-top: 20px;
}

/* Mobile buttons */
.controls {
    text-align:center;
    margin-top:10px;
}
button {
    padding:10px;
    margin:5px;
    font-size:18px;
}
</style>
</head>

<body>

<div>
<canvas id="game" width="900" height="500"></canvas>

<div class="controls">
<button onclick="moveUp()">⬆️</button>
<button onclick="moveDown()">⬇️</button>
</div>
</div>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

// Sounds
let hitSound = new Audio("https://www.soundjay.com/button/beep-07.wav");

// Paddle
let playerY = 200;
let aiY = 200;

// Ball
let x = 450;
let y = 250;
let dx = 4;
let dy = 4;

// Score
let playerScore = 0;
let aiScore = 0;

// Power-up
let powerX = Math.random()*800;
let powerY = Math.random()*400;

// Keyboard control
document.addEventListener("keydown", (e) => {
    if(e.key === "ArrowUp") playerY -= 20;
    if(e.key === "ArrowDown") playerY += 20;
});

// Mobile control
function moveUp(){ playerY -= 20; }
function moveDown(){ playerY += 20; }

// Draw game
function draw() {
    ctx.clearRect(0,0,900,500);

    // Neon center line
    ctx.strokeStyle="#0ff";
    ctx.setLineDash([5,5]);
    ctx.beginPath();
    ctx.moveTo(450,0);
    ctx.lineTo(450,500);
    ctx.stroke();

    // Ball glow
    ctx.shadowBlur = 20;
    ctx.shadowColor = "#fff";
    ctx.beginPath();
    ctx.arc(x,y,10,0,Math.PI*2);
    ctx.fillStyle="white";
    ctx.fill();

    ctx.shadowBlur = 0;

    // Player paddle
    ctx.fillStyle="#0f0";
    ctx.fillRect(20, playerY, 10, 100);

    // AI paddle
    ctx.fillStyle="#f00";
    ctx.fillRect(870, aiY, 10, 100);

    // Score
    ctx.fillStyle="#0ff";
    ctx.font="40px Arial";
    ctx.fillText(playerScore, 350, 50);
    ctx.fillText(aiScore, 500, 50);

    // Power-up
    ctx.fillStyle="yellow";
    ctx.beginPath();
    ctx.arc(powerX,powerY,8,0,Math.PI*2);
    ctx.fill();
}

// AI movement
function aiMove() {
    if(aiY + 50 < y) aiY += 3;
    else aiY -= 3;
}

// Game update
function update() {
    x += dx;
    y += dy;

    // Wall bounce
    if(y < 0 || y > 500) dy *= -1;

    // Paddle collision
    if(x < 40 && y > playerY && y < playerY+100){
        dx *= -1;
        hitSound.play();
    }

    if(x > 860 && y > aiY && y < aiY+100){
        dx *= -1;
        hitSound.play();
    }

    // Score
    if(x < 0){
        aiScore++;
        reset();
    }
    if(x > 900){
        playerScore++;
        reset();
    }

    // Power-up hit
    if(Math.abs(x-powerX)<15 && Math.abs(y-powerY)<15){
        playerY -= 20; // boost paddle
        powerX = Math.random()*800;
        powerY = Math.random()*400;
    }

    aiMove();
}

function reset(){
    x=450;
    y=250;
    dx = -dx;
}

// Loop
function loop(){
    update();
    draw();
    requestAnimationFrame(loop);
}

loop();

</script>
</body>
</html>
"""

st.title("🔥 Neon Pong (Advanced Edition)")
st.markdown("""
✅ **Single Player vs AI**  
✅ **Keyboard + Mobile Controls**  
✅ **Sound + Power-ups + Neon Glow**  

### Controls:
- Desktop: Arrow Keys ⬆️⬇️  
- Mobile: Buttons below ⬇️  
""")

components.html(html_code, height=600)
