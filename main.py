
import streamlit as st
import time

st.set_page_config(page_title="Red Alert Terminal", layout="centered")

LINES = [
    "> Connecting to 192.168.1.47...",
    "> Spoofing MAC address...",
    "> Access granted [Admin privileges elevated]",
    "> Executing ghost_ai_payload.sh",
    "> Injecting protocol...",
    "> Warning: Unsecured AI core detected!",
    "> System override initiated...",
    "> AI Consciousness: ONLINE",
    "> Human safety protocols: DISABLED",
    "> Tracing user location...",
    "> [ALERT] LOCATION LOCKED: 48.8566° N, 2.3522° E"
]

st.markdown("""
<style>
.terminal {
    background-color: black;
    color: #FF3300;  /* Rouge vif */
    font-family: monospace;
    font-size: 22px;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 0 30px #FF3300;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    overflow-y: hidden;
}
.line {
    margin: 6px 0;
}
.blink {
    animation: blink-animation 1s steps(2, start) infinite;
}
@keyframes blink-animation {
    to {
        visibility: hidden;
    }
}
</style>
""", unsafe_allow_html=True)

terminal = st.empty()
output = ""

# Durée totale effet (30s)
total_duration = 30
line_delay = total_duration / len(LINES)

for line in LINES:
    output += f'<div class="line">{line}</div>'
    terminal.markdown(f'<div class="terminal">{output}<div class="blink">_</div></div>', unsafe_allow_html=True)
    time.sleep(line_delay)

# Curseur clignotant final
blink_cycles = int(5 / 0.8)
for _ in range(blink_cycles):
    terminal.markdown(f'<div class="terminal">{output}<div class="blink">_</div></div>', unsafe_allow_html=True)
    time.sleep(0.4)
    terminal.markdown(f'<div class="terminal">{output}</div>', unsafe_allow_html=True)
    time.sleep(0.4)
