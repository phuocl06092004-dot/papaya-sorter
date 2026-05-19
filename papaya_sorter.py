import streamlit as st
import streamlit.components.v1 as components
import base64

# =========================
# PAGE
# =========================

st.set_page_config(
    page_title="Papaya Factory",
    layout="wide"
)

st.title("🥭 HỆ THỐNG PHÂN LOẠI ĐU ĐỦ")

# =========================
# LOAD IMAGE
# =========================

with open("factory.png", "rb") as image_file:

    encoded_image = base64.b64encode(
        image_file.read()
    ).decode()

# =========================
# CONTROL PANEL
# =========================

st.subheader("⚙️ CÀI ĐẶT HỆ THỐNG")

col1, col2, col3 = st.columns(3)

# SPEED

with col1:

    belt_speed_mps = st.slider(

        "🚀 TỐC ĐỘ BĂNG TẢI",

        0.1,
        2.0,
        0.6,
        0.01
    )

# SPAWN

with col2:

    papaya_spawn = st.slider(

        "🥭 THỜI GIAN RA QUẢ (s)",

        1,
        10,
        2
    )

# CYLINDER

with col3:

    cylinder_time = st.slider(

        "⚙️ THỜI GIAN XY LANH (ms)",

        100,
        1000,
        240,
        10
    )

# =========================
# HTML
# =========================

components.html(
    f"""
<html>

<head>

<style>

body {{

    margin:0;
    padding:0;

    overflow:hidden;

    background:#f2f2f2;
}}

.factory {{

    position:relative;

    width:100%;
    height:720px;

    background-image:
        url("data:image/png;base64,{encoded_image}");

    background-size:60%;

    background-repeat:no-repeat;

    background-position:center 50px;
}}

/* =========================
   BUTTON
========================= */

.control-btn {{

    position:absolute;

    width:140px;
    height:55px;

    border:none;

    border-radius:12px;

    color:white;

    font-size:22px;
    font-weight:bold;

    cursor:pointer;

    box-shadow:
        0 0 12px rgba(0,0,0,0.4);
}}

.start-btn {{

    top:80px;
    left:500px;

    background:green;
}}

.stop-btn {{

    top:80px;
    left:680px;

    background:red;
}}

/* =========================
   INFO
========================= */

.info {{

    position:absolute;

    width:250px;
    height:60px;

    background:white;

    border-radius:12px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:22px;
    font-weight:bold;

    box-shadow:
        0 0 12px rgba(0,0,0,0.4);
}}

.belt-info {{

    top:80px;
    left:100px;
}}

.cylinder-info {{

    top:160px;
    left:100px;
}}

.success-info {{

    top:240px;
    left:100px;
}}

/* =========================
   COUNTER
========================= */

.counter {{

    position:absolute;

    width:250px;
    height:60px;

    background:white;

    border-radius:12px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:24px;
    font-weight:bold;

    box-shadow:
        0 0 12px rgba(0,0,0,0.4);
}}

.counter1 {{

    top:340px;
    left:100px;

    color:green;
}}

.counter2 {{

    top:420px;
    left:100px;

    color:orange;
}}

.counter3 {{

    top:500px;
    left:100px;

    color:black;
}}

/* =========================
   CAMERA
========================= */

.camera {{

    position:absolute;

    top:300px;
    left:800px;

    width:100px;
    height:45px;

    background:#2196f3;

    color:white;

    border-radius:10px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-weight:bold;

    box-shadow:
        0 0 10px rgba(0,0,0,0.4);
}}

/* =========================
   XY LANH
========================= */

.cylinder {{

    position:absolute;

    width:120px;
    height:45px;

    color:white;

    border-radius:10px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-weight:bold;

    transition:0.3s;

    background:#666;

    box-shadow:
        0 0 10px rgba(0,0,0,0.4);
}}

.cylinder1 {{

    top:355px;
    left:900px;
}}

.cylinder2 {{

    top:355px;
    left:1250px;
}}

/* =========================
   SENSOR
========================= */

.sensor {{

    position:absolute;

    width:100px;
    height:45px;

    color:white;

    border-radius:10px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-weight:bold;

    transition:0.3s;

    box-shadow:
        0 0 10px rgba(0,0,0,0.4);
}}

.sensor1 {{

    top:500px;
    left:750px;

    background:red;
}}

.sensor2 {{

    top:500px;
    left:1180px;

    background:#2196f3;
}}

.sensor3 {{

    top:500px;
    left:1570px;

    background:#af874c;
}}

/* =========================
   PAPAYA
========================= */

.papaya {{

    position:absolute;

    width:60px;
    height:60px;

    border-radius:50%;

    left:450px;
    top:400px;

    box-shadow:
        0 0 20px rgba(0,0,0,0.5);
}}

/* =========================
   KHAY
========================= */

.bin {{

    position:absolute;

    width:170px;
    height:90px;

    border-radius:15px;

    opacity:0.9;

    box-shadow:
        0 0 15px rgba(0,0,0,0.4);
}}

.left-bin {{

    left:800px;
    top:550px;

    background:green;
}}

.center-bin {{

    left:1250px;
    top:550px;

    background:gold;
}}

.right-bin {{

    left:1750px;
    top:550px;

    background:black;
}}

/* =========================
   LABEL
========================= */

.label {{

    position:absolute;

    font-size:24px;

    font-weight:bold;

    color:white;
}}

.left-label {{

    left:850px;
    top:580px;
}}

.center-label {{

    left:1300px;
    top:580px;

    color:black;
}}

.right-label {{

    left:1800px;
    top:580px;
}}

/* =========================
   ANIMATION
========================= */

@keyframes moveLeft {{

    0% {{
        left:450px;
        top:400px;
    }}

    50% {{
        left:910px;
        top:400px;
    }}

    100% {{
        left:850px;
        top:580px;
    }}
}}

@keyframes moveCenter {{

    0% {{
        left:450px;
        top:400px;
    }}

    55% {{
        left:1290px;
        top:400px;
    }}

    100% {{
        left:1300px;
        top:580px;
    }}
}}

@keyframes moveRight {{

    0% {{
        left:450px;
        top:400px;
    }}

    70% {{
        left:1570px;
        top:400px;
    }}

    100% {{
        left:1800px;
        top:580px;
    }}
}}

</style>

</head>

<body>

<div class="factory">

    <!-- BUTTON -->

    <button id="startBtn" class="control-btn start-btn">
        START
    </button>

    <button id="stopBtn" class="control-btn stop-btn">
        STOP
    </button>

    <!-- INFO -->

    <div class="info belt-info">
        🚀 {belt_speed_mps:.2f} m/s
    </div>

    <div class="info cylinder-info">
        ⚙️ {cylinder_time:.0f} ms
    </div>

    <div class="info success-info">
        🎯 SUCCESS:
        <span id="successText"></span>
    </div>

    <!-- COUNTER -->

    <div class="counter counter1">
        🟢 XANH:
        <span id="count1">0</span>
    </div>

    <div class="counter counter2">
        🟡 CHÍN:
        <span id="count2">0</span>
    </div>

    <div class="counter counter3">
        ⚫ HỎNG:
        <span id="count3">0</span>
    </div>

    <!-- CAMERA -->

    <div class="camera">
        CAMERA
    </div>

    <!-- XY LANH -->

    <div
        class="cylinder cylinder1"
        id="cylinder1">

        XY LANH 1

    </div>

    <div
        class="cylinder cylinder2"
        id="cylinder2">

        XY LANH 2

    </div>

    <!-- SENSOR -->

    <div class="sensor sensor1" id="sensor1">
        SENSOR 1
    </div>

    <div class="sensor sensor2" id="sensor2">
        SENSOR 2
    </div>

    <div class="sensor sensor3" id="sensor3">
        SENSOR 3
    </div>

    <!-- KHAY -->

    <div class="bin left-bin"></div>

    <div class="bin center-bin"></div>

    <div class="bin right-bin"></div>

    <!-- LABEL -->

    <div class="label left-label">
        XANH
    </div>

    <div class="label center-label">
        CHÍN
    </div>

    <div class="label right-label">
        HỎNG
    </div>

</div>

<script>

const factory =
    document.querySelector(".factory");

// =========================
// START STOP
// =========================

let running = true;

document.getElementById(
    "startBtn"
).onclick = () => {{

    running = true;
}}

document.getElementById(
    "stopBtn"
).onclick = () => {{

    running = false;
}}

// =========================
// COUNTER
// =========================

let greenCount = 0;
let yellowCount = 0;
let blackCount = 0;

// =========================
// HỒI QUY
// =========================

let x1 =
    {cylinder_time};

let x2 =
    {belt_speed_mps};

let successRate =

    (
        -0.0008 * x1 * x1
    )

    +

    (
        -40.179 * x2 * x2
    )

    +

    (
        0.384 * x1
    )

    +

    (
        48.18 * x2
    )

    +

    35.476;

// LIMIT

if (successRate > 100) {{

    successRate = 100;
}}

if (successRate < 0) {{

    successRate = 0;
}}

// MISS RATE

let missRate =
    1 - (successRate / 100);

// SHOW

document.getElementById(
    "successText"
).innerText =

    successRate.toFixed(1) + "%";

// =========================
// RANDOM LIST
// =========================

let types = [

    {{
        color:"green",
        animation:"moveLeft"
    }},

    {{
        color:"gold",
        animation:"moveCenter"
    }},

    {{
        color:"black",
        animation:"moveRight"
    }}
];

types.sort(() => Math.random() - 0.5);

// =========================
// CREATE PAPAYA
// =========================

function createPapaya() {{

    const randomType =
        types.shift();

    if (types.length == 0) {{

        types = [

            {{
                color:"green",
                animation:"moveLeft"
            }},

            {{
                color:"gold",
                animation:"moveCenter"
            }},

            {{
                color:"black",
                animation:"moveRight"
            }}
        ];

        types.sort(
            () => Math.random() - 0.5
        );
    }}

    const papaya =
        document.createElement("div");

    papaya.classList.add(
        "papaya"
    );

    papaya.dataset.sensor1 = "0";
    papaya.dataset.sensor2 = "0";
    papaya.dataset.sensor3 = "0";

    papaya.dataset.cylinder1 = "0";
    papaya.dataset.cylinder2 = "0";

    papaya.style.background =
        randomType.color;

    let duration = 8;

    papaya.style.animation =

        randomType.animation +

        " " +

        duration / ({belt_speed_mps} * 1.5) +

        "s linear forwards";

    factory.appendChild(
        papaya
    );

    papaya.addEventListener(

        "animationend",

        () => {{

            papaya.remove();

        }}
    );
}}

// =========================
// RANDOM QUẢ
// =========================

setInterval(() => {{

    if (running) {{

        createPapaya();
    }}

}}, {papaya_spawn * 1000});

// =========================
// SENSOR
// =========================

setInterval(() => {{

    if (!running) return;

    const papayas =
        document.querySelectorAll(
            ".papaya"
        );

    papayas.forEach((papaya) => {{

        const rect =
            papaya.getBoundingClientRect();

        // SENSOR 1

        if (

            rect.left > 750 &&
            rect.left < 1100 &&
            rect.top > 500 &&

            papaya.dataset.sensor1 == "0"
        ) {{

            papaya.dataset.sensor1 = "1";

            document.getElementById(
                "sensor1"
            ).style.background = "lime";

            greenCount++;

            document.getElementById(
                "count1"
            ).innerText = greenCount;

            setTimeout(() => {{

                document.getElementById(
                    "sensor1"
                ).style.background = "red";

            }}, 300);
        }}

        // XY LANH 1

        if (

            rect.left > 900 &&
            rect.left < 1000 &&
            rect.top > 400 &&

            papaya.dataset.cylinder1 != "1"
        ) {{

            papaya.dataset.cylinder1 = "1";

            document.getElementById(
                "cylinder1"
            ).style.background = "lime";

            let missed =
                Math.random() < missRate;

            if (missed) {{

                papaya.style.animation =
                    "moveRight 3s linear forwards";
            }}

            setTimeout(() => {{

                document.getElementById(
                    "cylinder1"
                ).style.background = "#666";

            }}, {cylinder_time});
        }}

        // SENSOR 2

        if (

            rect.left > 1180 &&
            rect.left < 1480 &&
            rect.top > 500 &&

            papaya.dataset.sensor2 == "0"
        ) {{

            papaya.dataset.sensor2 = "1";

            document.getElementById(
                "sensor2"
            ).style.background = "lime";

            yellowCount++;

            document.getElementById(
                "count2"
            ).innerText = yellowCount;

            setTimeout(() => {{

                document.getElementById(
                    "sensor2"
                ).style.background =
                    "#2196f3";

            }}, 300);
        }}

        // XY LANH 2

        if (

            rect.left > 1100 &&
            rect.left < 1350 &&
            rect.top > 400 &&

            papaya.dataset.cylinder2 != "1"
        ) {{

            papaya.dataset.cylinder2 = "1";

            document.getElementById(
                "cylinder2"
            ).style.background = "lime";

            let missed =
                Math.random() < missRate;

            if (missed) {{

                papaya.style.animation =
                    "moveRight 3s linear forwards";
            }}

            setTimeout(() => {{

                document.getElementById(
                    "cylinder2"
                ).style.background = "#666";

            }}, {cylinder_time});
        }}

        // SENSOR 3

        if (

            rect.left > 1570 &&
            rect.top > 500 &&

            papaya.dataset.sensor3 == "0"
        ) {{

            papaya.dataset.sensor3 = "1";

            document.getElementById(
                "sensor3"
            ).style.background = "lime";

            blackCount++;

            document.getElementById(
                "count3"
            ).innerText = blackCount;

            setTimeout(() => {{

                document.getElementById(
                    "sensor3"
                ).style.background =
                    "#af874c";

            }}, 300);
        }}

    }});

}}, 50);

</script>

</body>

</html>
""",
    height=720
)
