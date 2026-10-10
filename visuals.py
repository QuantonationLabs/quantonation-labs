"""Local visual scenes. Schematic animations carry explicit provenance labels."""
import base64
from pathlib import Path
import streamlit.components.v1 as components

ROOT=Path(__file__).parent

def logo(name):
    path=ROOT/'assets'/name
    mime='image/svg+xml' if path.suffix=='.svg' else 'image/png'
    return f'data:{mime};base64,'+base64.b64encode(path.read_bytes()).decode()

def quantum_stage():
    components.html('''<!doctype html><html><head><style>
    *{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;background:#0b1027;color:#edf5ff;border-radius:22px;overflow:hidden}
    .stage{position:relative;height:350px;background:radial-gradient(ellipse at 24% 50%,#143e6666,transparent 55%),radial-gradient(ellipse at 80% 50%,#592ca955,transparent 55%)}
    .title{position:absolute;top:24px;left:26px;font-size:12px;letter-spacing:2px;color:#7ce5ff}.label{position:absolute;bottom:40px;left:26px;font-size:18px;font-weight:bold}.label.right{left:auto;right:26px;text-align:right}
    .caption{font-size:11px;color:#99afd1;margin-top:8px;font-weight:normal;max-width:310px}.chip{position:absolute;left:45%;top:43%;width:10%;text-align:center;font-size:11px;color:#bcb4ff;letter-spacing:2px}
    canvas{width:100%;height:350px}.legend{position:absolute;bottom:14px;left:26px;font-size:10px;color:#9faecb;letter-spacing:.6px}
    @media(max-width:650px){.caption{max-width:180px}.label{font-size:14px}.chip{display:none}}
    </style></head><body><div class="stage"><div class="title">TWO QUANTUM LANGUAGES · ONE RESEARCH DESK</div><canvas id="c"></canvas><div class="chip">SCIENCE<br>↔<br>HARDWARE</div><div class="label">Neutral-atom arrays<div class="caption">PASQAL · programmable geometry and interactions</div></div><div class="label right">Quantum circuits<div class="caption">qBraid / IQM · gates, compilation and measurements</div></div><div class="legend">ANIMATED SCHEMATIC · NO DEVICE TELEMETRY OR MEASURED STATE</div></div><script>
    const c=document.getElementById('c'),ctx=c.getContext('2d');let last=0;
    function frame(t){requestAnimationFrame(frame);if(t-last<35)return;last=t;let w=c.clientWidth,h=350;c.width=w*2;c.height=h*2;ctx.scale(2,2);ctx.clearRect(0,0,w,h);
    let s=Math.min(w*.038,27),ox=w*.24-4.5*s,oy=83;
    for(let r=0;r<7;r++)for(let k=0;k<10;k++){let x=ox+k*s+r%2*s/2,y=oy+r*s*.82,p=.5+.5*Math.sin(t/900+k*.5+r*.4);if(k<9){ctx.strokeStyle='#4bc8ee19';ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+s,y);ctx.stroke()};ctx.beginPath();ctx.arc(x,y,3.5+2*p,0,7);ctx.fillStyle=`rgba(80,${140+Math.round(90*p)},255,1)`;ctx.shadowBlur=12*p+4;ctx.shadowColor='#53dfff';ctx.fill();ctx.shadowBlur=0;}
    let x0=w*.57,x1=w*.95,y0=92,dy=35;ctx.font='11px Arial';
    for(let q=0;q<5;q++){let y=y0+q*dy;ctx.strokeStyle='#9c87ec88';ctx.beginPath();ctx.moveTo(x0,y);ctx.lineTo(x1,y);ctx.stroke();ctx.fillStyle='#b0a7df';ctx.fillText('q'+q,x0-23,y+4);}
    for(let k=0;k<4;k++){let x=x0+(k+.6)*(x1-x0)/4;for(let q=0;q<5;q++){let y=y0+q*dy;if((k+q)%3===0){ctx.fillStyle='#392265';ctx.fillRect(x-11,y-11,22,22);ctx.strokeStyle='#a47bff';ctx.strokeRect(x-11,y-11,22,22);ctx.fillStyle='#dfcdff';ctx.fillText(k%2?'Rz':'Rx',x-8,y+4);}}let a=k%4,b=a+1;ctx.strokeStyle='#66dcff';ctx.beginPath();ctx.moveTo(x,y0+a*dy);ctx.lineTo(x,y0+b*dy);ctx.stroke();for(let q of [a,b]){ctx.beginPath();ctx.arc(x,y0+q*dy,4,0,7);ctx.fillStyle='#66dcff';ctx.fill();}}
    let px=x0+((t/4500)%1)*(x1-x0);ctx.strokeStyle='#72e6ff66';ctx.beginPath();ctx.moveTo(px,75);ctx.lineTo(px,250);ctx.stroke();}requestAnimationFrame(frame);
    </script></body></html>''',height=355)

def agent_topology():
    icons=[logo('openai.svg'),logo('claude.png'),logo('grok.svg')]
    cards=''.join(f'<div class="node n{i}"><img src="{icon}"><b>{model}</b><span>{role}</span></div>' for i,(icon,model,role) in enumerate(zip(icons,['GPT','Claude','Grok'],['Experiment designer','Scientific auditor','Sceptical reviewer'])))
    components.html('''<!doctype html><html><head><style>
    body{margin:0;font-family:Arial,sans-serif;color:#ecf3ff;background:#10172f;border-radius:20px;overflow:hidden}.map{height:250px;position:relative;background:radial-gradient(ellipse at center,#37287666,transparent 70%)}
    .node{position:absolute;top:65px;width:21%;height:112px;border:1px solid #8ba7e655;border-radius:16px;background:#ffffff09;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:7px}.n0{left:4%}.n1{left:39.5%}.n2{right:4%}.node img{height:30px;width:30px;object-fit:contain;background:white;border-radius:8px;padding:5px}.node span{font-size:11px;color:#bbc9e5}.node b{font-size:15px}.title{text-align:center;font-size:11px;color:#7ce5ff;letter-spacing:2px;padding-top:22px}.line{position:absolute;top:120px;height:1px;background:linear-gradient(90deg,#66dcff,#9b72ff);width:14%;}.l0{left:25%}.l1{right:25%}.dot{width:5px;height:5px;border-radius:50%;background:#66dcff;box-shadow:0 0 12px #66dcff;position:absolute;top:-2px;animation:travel 2.5s infinite}.footer{position:absolute;bottom:22px;width:100%;text-align:center;color:#acbce0;font-size:11px}@keyframes travel{from{left:0}to{left:100%}}
    </style></head><body><div class="map"><div class="title">SHARED EVIDENCE → PARALLEL REVIEWS → SYNTHESIS</div><div class="line l0"><i class="dot"></i></div><div class="line l1"><i class="dot"></i></div>'''+cards+'''<div class="footer">Architecture illustration · actual task states and response provenance appear below</div></div></body></html>''',height=255)
