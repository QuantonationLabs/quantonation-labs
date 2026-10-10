"""Public scientific showcase: local calculations and labelled architecture only."""
from pathlib import Path
import base64
import numpy as np
import plotly.graph_objects as go
import streamlit as st
from scipy.linalg import eigh
from visuals import quantum_stage
from architecture_view import architecture
from science import model

ROOT=Path(__file__).parent
st.set_page_config(page_title='Quantonation Labs',page_icon='✦',layout='wide')
st.markdown('''<style>.block-container{max-width:1300px;padding-top:2rem}h1,h2,h3{color:#2e346c;letter-spacing:-.03em}[data-testid="stSidebar"]{background:#f2f5ff}.hero{padding:25px 30px;border-radius:22px;background:linear-gradient(110deg,#111638,#352b87,#0000b8);color:white;margin:18px 0}.hero h1{color:white;margin:8px 0;font-size:2.5rem}.hero p{color:#d2e7ff}.platform{display:flex;gap:12px;align-items:center;padding:13px;margin:9px 0;border-radius:13px;text-decoration:none!important;color:#2e346c!important;font-weight:bold}.platform img{width:28px;height:28px;object-fit:contain;background:white;padding:4px;border-radius:8px}</style>''',unsafe_allow_html=True)
with st.sidebar:
    st.image(str(ROOT/'assets/quantonation-labs.svg'),width=220)
    st.caption('PUBLIC SHOWCASE · LOCAL SCIENCE')
    for title,asset,url,bg in [
        ('Theo','theo-icon.png','https://firstprinciples.com/','#e8e6ff'),
        ('PASQAL','pasqal-icon.png','https://portal.pasqal.cloud/','#e3faff'),
        ('qBraid','qbraid-icon.png','https://lab.qbraid.com/','#ebe5ff'),
        ('OpenRouter','openrouter.png','https://openrouter.ai/','#e2edff'),
        ('ChatGPT','openai.svg','https://chatgpt.com/','#def7ef'),
        ('Claude','claude.png','https://claude.ai/','#ffeadc'),
        ('Grok','grok.svg','https://grok.com/','#e7eaf0')]:
        p=ROOT/'assets'/asset;mime='image/svg+xml' if p.suffix=='.svg' else 'image/png';data=base64.b64encode(p.read_bytes()).decode()
        st.markdown(f'<a class="platform" href="{url}" target="_blank" rel="noopener noreferrer" style="background:{bg}"><img src="data:{mime};base64,{data}" alt="{title} logo">{title}<span style="margin-left:auto">↗</span></a>',unsafe_allow_html=True)
    st.caption('External services use their own accounts. This showcase submits no job or model request.')
st.image(str(ROOT/'assets/quantonation-labs.svg'),width=340)
st.markdown('<div class="hero"><span>SCIENCE · MACHINES · COLLECTIVE INTELLIGENCE</span><h1>Quantum research, orchestrated.</h1><p>Explore quantum control, exact predictions and the architecture of a coordinated research desk.</p></div>',unsafe_allow_html=True)
quantum_stage()
tabs=st.tabs(['Quantum control','Exact science','Quantonation OS'])
with tabs[0]:
    area=st.slider('Pulse area / π',0.0,2.0,1.0,.05)
    p=float(np.sin(np.pi*area/2)**2)
    dots=''.join(f'<i style="background:rgb({int(50+60*p)},{int(80+140*p)},255);box-shadow:0 0 {4+18*p}px #66dcff"></i>' for _ in range(100))
    st.markdown('<div style="background:#10172f;border-radius:20px;padding:26px;color:#c6e6ff"><b>100-site conceptual array · isolated-atom reference</b><div class="quantum-dots" style="display:grid;grid-template-columns:repeat(10,14px);gap:14px;margin:28px auto;width:max-content">'+dots+'</div><style>.quantum-dots i{width:14px;height:14px;border-radius:50%;display:block}</style></div>',unsafe_allow_html=True)
    st.metric('Analytical excitation',f'{100*p:.1f}%')
    x=np.linspace(0,2,201);fig=go.Figure(go.Scatter(x=x,y=np.sin(np.pi*x/2)**2,line=dict(color='#00bad6',width=4)));fig.add_vline(x=area,line_dash='dot',line_color='#7855e8');fig.update_layout(xaxis_title='Pulse area / π',yaxis_title='Excitation probability',height=300);st.plotly_chart(fig,width='stretch')
    st.caption('H = ΩX/2, Δ = 0. This is a calculated isolated-atom reference and a conceptual array illustration. It is not a full interacting 100-atom simulation or a hardware result.')
with tabs[1]:
    time=st.slider('Dimensionless evolution time',0.0,2.0,.75,.05)
    xy,J,fields,nn,z,H=model();values,vectors=eigh(H)
    probabilities=abs(vectors@(np.exp(-1j*values*time)*vectors[0,:].conj()))**2
    excitation=(1-probabilities@z)/2
    fig=go.Figure(go.Scatter(x=xy[:,0],y=xy[:,1],mode='markers+text',text=[f'Site {i}' for i in range(6)],textposition='top center',marker=dict(size=36,color=excitation,cmin=0,cmax=1,colorscale=[[0,'#2e346c'],[.5,'#7855e8'],[1,'#66dcff']],colorbar=dict(title='Excitation'))))
    fig.update_layout(height=350,yaxis=dict(scaleanchor='x',scaleratio=1),xaxis_title='Lattice units',yaxis_title='Lattice units');st.plotly_chart(fig,width='stretch')
    st.caption('Exact 64-state six-spin local model, with interaction tails retained. Model parameters define this example; no measurements are included in the public edition.')
with tabs[2]:
    architecture()
    st.write('The proposed system coordinates scientific tools and specialist agents through Prefect and durable task records. GitHub holds reviewed specifications and knowledge; runtime state belongs in the registry.')
    st.caption('Architecture illustration. The fund-owned implementation, evidence and credentials belong in a separate private deployment and repository.')
