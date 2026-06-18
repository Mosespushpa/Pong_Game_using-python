import streamlit as st
import streamlit.components.v1 as components

# --- HTML + JS Game ---
html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        background: black;
        overflow: hidden;
    }
    canvas {
        display: block;
        margin: auto;
        background: black;
    }
</style>
</head>

<body>

<canvas id="gameCanvas" width="800" height="500"></canvas>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// --- Paddle ---
const paddleWidth = 10;
const paddleHeight = 100;

// Left paddle
let lY = 200;
// Right paddle
let rY = 200;

// Ball
let ballX = 400;
let ballY = 250;
let dx = 4;
let dy = 4;

// Score
let lScore = 0;
let rScore = 0;

// Controls
document.addEventListener("keydown", function(e) {
    if (e.key === "w") lY -= 20;
    if (e.key === "s") lY += 20;

    if (e.key === "i") rY -= 20;
    if (e.key === "k") rY += 20;
});

// Draw everything
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Middle line
    ctx.strokeStyle = "white";
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(400, 0);
    ctx.lineTo(400, 500);
    ctx.stroke();

    // Ball
    ctx.beginPath();
    ctx.arc(ballX, ballY, 10, 0, Math.PI * 2);
    ctx.fillStyle = "white";
    ctx.fill();

    // Left paddle
    ctx.fillRect(10, lY, paddleWidth, paddleHeight);

    // Right paddle
    ctx.fillRect(780, rY, paddleWidth, paddleHeight);

    // Score
    ctx.font = "40px Arial";
    ctx.fillText(lScore, 300, 50);
    ctx.fillText(rScore, 480, 50);
}

// Update logic
function update() {
    ballX += dx;
    ballY += dy;

    // Wall collision
    if (ballY > 490 || ballY < 10) {
        dy *= -1;
    }

    // Right paddle collision
    if (ballX > 770 && ballY > rY && ballY < rY + paddleHeight) {
        dx *= -1;
        dx *= 1.05; // speed increase
    }

    // Left paddle collision
    if (ballX < 30 && ballY > lY && ballY < lY + paddleHeight) {
        dx *= -1;
        dx *= 1.05;
    }

    // Score
    if (ballX > 800) {
        lScore++;
        resetBall();
    }

    if (ballX < 0) {
        rScore++;
        resetBall();
    }
}

function resetBall() {
    ballX = 400;
    ballY = 250;
    dx = -dx;
}

// Game loop
function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

gameLoop();
</script>

</body>
</html>
"""

# --- Streamlit UI ---
st.title("🏓 Advanced Pong Game")
st.markdown("### Controls:")
st.markdown("""
- **Left Player:** W / S  
- **Right Player:** I / L  
""")

components.html(html_code, height=520)
