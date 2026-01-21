<!DOCTYPE html>
<html>
<head>
<title>Cyber Clock Pro</title>
<style>
/* ===== THEME COLORS ===== */
:root{
    --bg:#000000;
    --panel:#050505;
    --neon:#ff0033;
    --text:#ffffff;
}
.light{
    --bg:#f2f2f2;
    --panel:#ffffff;
    --neon:#ff0033;
    --text:#000000;
}

/* ===== RESET ===== */
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Segoe UI, Arial, sans-serif;
}

/* ===== BODY ===== */
body{
    background:var(--bg);
    color:var(--text);
    width:100vw;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:hidden;
}

/* ===== APP CONTAINER ===== */
.app{
    width:420px;
    background:var(--panel);   /* FULL SOLID */
    border-radius:18px;
    padding:12px;
    box-shadow:0 0 30px var(--neon);
    border:1px solid var(--neon);
}

/* ===== TOP BAR ===== */
.top{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:10px;
}
.tabs button,
.ctrl button{
    background:transparent;
    border:1px solid var(--neon);
    color:var(--neon);
    padding:5px 10px;
    margin:2px;
    border-radius:6px;
    cursor:pointer;
    font-size:12px;
}
.tabs button.active{
    background:var(--neon);
    color:black;
}

/* ===== SECTIONS ===== */
.section{display:none;text-align:center;}
.section.active{display:block}

/* ===== ANALOG CLOCK ===== */
.clock{
    margin:10px auto;
    width:220px;
    height:220px;
    border:4px solid var(--neon);
    border-radius:50%;
    position:relative;
    box-shadow:0 0 20px var(--neon);
}
.hand{
    position:absolute;
    bottom:50%;
    left:50%;
    transform-origin:bottom;
}
.hour{width:6px;height:60px;background:white;}
.minute{width:4px;height:85px;background:var(--neon);}
.second{width:2px;height:100px;background:red;}

.center{
    width:10px;
    height:10px;
    background:white;
    border-radius:50%;
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
}

.digital{
    color:var(--neon);
    font-size:20px;
    margin-top:8px;
}

/* ===== WORLD CLOCK ===== */
select{
    background:black;
    color:var(--neon);
    border:1px solid var(--neon);
    padding:5px;
    border-radius:5px;
    margin-bottom:8px;
}

/* ===== STOPWATCH & TIMER ===== */
.time{
    font-size:22px;
    color:var(--neon);
    margin:10px 0;
}
input{
    background:black;
    color:white;
    border:1px solid var(--neon);
    padding:5px;
    width:70px;
    border-radius:5px;
}
button{
    background:transparent;
    border:1px solid var(--neon);
    color:var(--neon);
    padding:5px 10px;
    border-radius:6px;
    cursor:pointer;
    margin:3px;
}
</style>
</head>

<body>
<div class="app">

<div class="top">
    <div class="tabs">
        <button class="tab active" onclick="show(0)">Clock</button>
        <button class="tab" onclick="show(1)">World</button>
        <button class="tab" onclick="show(2)">Stopwatch</button>
        <button class="tab" onclick="show(3)">Timer</button>
    </div>
    <div class="ctrl">
        <button onclick="theme()">🌗</button>
    </div>
</div>

<!-- CLOCK -->
<div class="section active">
    <div class="clock">
        <div class="hand hour" id="h"></div>
        <div class="hand minute" id="m"></div>
        <div class="hand second" id="s"></div>
        <div class="center"></div>
    </div>
    <div class="digital" id="digital"></div>
</div>

<!-- WORLD CLOCK -->
<div class="section">
    <select id="tz" onchange="world()">
        <option value="Asia/Dhaka">Bangladesh</option>
        <option value="Europe/London">London</option>
        <option value="America/New_York">New York</option>
        <option value="Asia/Tokyo">Tokyo</option>
    </select>
    <div class="digital" id="world"></div>
</div>

<!-- STOPWATCH -->
<div class="section">
    <div class="time" id="sw">00:00:00</div>
    <button onclick="startSW()">Start</button>
    <button onclick="stopSW()">Stop</button>
    <button onclick="resetSW()">Reset</button>
</div>

<!-- TIMER -->
<div class="section">
    <input id="min" type="number" placeholder="Min">
    <input id="sec" type="number" placeholder="Sec">
    <div class="time" id="timer">00:00</div>
    <button onclick="startTimer()">Start</button>
    <button onclick="resetTimer()">Reset</button>
</div>

</div>

<script>
/* TAB SWITCH */
function show(i){
 document.querySelectorAll(".tab").forEach((t,x)=>t.classList.toggle("active",x===i));
 document.querySelectorAll(".section").forEach((s,x)=>s.classList.toggle("active",x===i));
}

/* THEME SWITCH */
function theme(){
 document.body.classList.toggle("light");
}

/* MAIN CLOCK */
function update(){
 let d=new Date();
 let s=d.getSeconds()*6;
 let m=d.getMinutes()*6 + d.getSeconds()*0.1;
 let h=d.getHours()*30 + d.getMinutes()*0.5;
 document.getElementById("s").style.transform=`translateX(-50%) rotate(${s}deg)`;
 document.getElementById("m").style.transform=`translateX(-50%) rotate(${m}deg)`;
 document.getElementById("h").style.transform=`translateX(-50%) rotate(${h}deg)`;
 document.getElementById("digital").innerText=d.toLocaleTimeString();
}
setInterval(update,1000);
update();

/* WORLD CLOCK */
function world(){
 let tz=document.getElementById("tz").value;
 document.getElementById("world").innerText =
   new Date().toLocaleTimeString("en-US",{timeZone:tz});
}
setInterval(world,1000);
world();

/* STOPWATCH */
let sw=0,swi=null;
function startSW(){
 if(!swi){
  swi=setInterval(()=>{
   sw++;
   let h=String(Math.floor(sw/3600)).padStart(2,"0");
   let m=String(Math.floor(sw%3600/60)).padStart(2,"0");
   let s=String(sw%60).padStart(2,"0");
   document.getElementById("sw").innerText=`${h}:${m}:${s}`;
  },1000);
 }
}
function stopSW(){clearInterval(swi);swi=null;}
function resetSW(){stopSW();sw=0;document.getElementById("sw").innerText="00:00:00";}

/* TIMER */
let ti=null,ts=0;
function startTimer(){
 ts=(+min.value||0)*60+(+sec.value||0);
 if(ti) clearInterval(ti);
 ti=setInterval(()=>{
  if(ts<=0){clearInterval(ti);alert("⏰ Time Up");return;}
  ts--;
  timer.innerText=
   String(Math.floor(ts/60)).padStart(2,"0")+":"+String(ts%60).padStart(2,"0");
 },1000);
}
function resetTimer(){clearInterval(ti);timer.innerText="00:00";}
</script>
</body>
</html>
