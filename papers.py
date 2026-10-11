"""Verified public references; optional local preprint copies for the laptop demo."""
from pathlib import Path
import base64
import streamlit as st

ROOT=Path(__file__).parent
PAPERS=[
    {'name':'QOuLiPo','title':'QOuLiPo: What a quantum computer sees when it reads a book',
     'authors':'Christophe Jurczak','date':'13 May 2026','kind':'arXiv preprint','id':'2605.14188',
     'url':'https://arxiv.org/abs/2605.14188','pdf_url':'https://arxiv.org/pdf/2605.14188',
     'file':'qoulipo_2605.14188.pdf','cover':'qoulipo_cover.png','colour':'#8b68ef',
     'summary':'From Renaissance texts to graphs and neutral-atom experiments. Natural and engineered literary structures become a hardware benchmark, including registers up to 100 atoms.',
     'connection':'Shows how one researcher can combine an agentic coding environment with cloud quantum hardware. An application and benchmark, without a speedup claim.'},
    {'name':'PASQAL × AI agents','title':'Lowering the implementation barrier of neutral-atom quantum computing with agentic workflows',
     'authors':'Constantin Dalyac · Alexandre Dauphin · Loïc Henriet · Christophe Jurczak',
     'date':'28 July 2026','kind':'arXiv preprint','id':'2607.25834',
     'submission':'Submitted to Quantum Machine Intelligence','journal_url':'https://link.springer.com/journal/42484',
     'url':'https://arxiv.org/abs/2607.25834','pdf_url':'https://arxiv.org/pdf/2607.25834',
     'file':'pasqal_agents_2607.25834.pdf','cover':'pasqal_agents_cover.png','colour':'#03aabc',
     'summary':'An agentic workflow takes scientific papers and patents through protocol design, simulation and experiments on two cloud PASQAL processors.',
     'connection':'The scientific foundation for this demo: automation accelerates experiments, while domain-expert review catches incorrect observables and plausible but wrong diagnoses.'},
    {'name':'Nature','title':'AI tool lets researchers ‘vibe code’ in the quantum realm',
     'authors':'Davide Castelvecchi','date':'19 August 2026','kind':'News / coverage','id':'Nature 656, 800–801',
     'url':'https://www.nature.com/articles/d41586-026-02495-4','colour':'#d05c70',
     'summary':'Nature coverage of the PASQAL agentic-workflows research and the move from natural-language requests to quantum code and execution.',
     'connection':'A bridge from the research to the wider audience. The publisher classifies this as news coverage; full text may require your Nature or institutional access.'},
]

def render():
    st.markdown('<div style="background:linear-gradient(115deg,#172046,#5335a8,#087f98);padding:20px 26px;border-radius:22px;color:white"><span style="font-size:12px;letter-spacing:2px;color:#a3ebff">QUANTONATION LABS · RESEARCH LIBRARY</span><h1 style="color:white;margin:10px 0;font-size:2rem">Papers & perspectives</h1><p style="color:#dbe5ff;margin:0">The published trail behind the experiments: literary structures, agentic quantum workflows and Nature coverage.</p></div>',unsafe_allow_html=True)
    st.write('Three references to open during the presentation or share with the team.')
    for col,p in zip(st.columns(3),PAPERS):
        with col,st.container(border=True):
            st.markdown(f'<div style="min-height:105px;padding:16px;display:flex;flex-direction:column;gap:10px;border-radius:14px;background:linear-gradient(120deg,#151d3b,{p["colour"]});color:white"><span style="font-size:10px;line-height:1.3;letter-spacing:1px">{p["kind"].upper()}</span><div style="font-size:20px;line-height:1.25;font-weight:700">{p["name"]}</div></div>',unsafe_allow_html=True)
            st.caption(p['date']+' · '+p['id'])
            if p.get('submission'):
                journal_brand(p)
            st.markdown(f'<h3 style="font-size:17px;line-height:1.4;margin:14px 0;overflow-wrap:normal">{p["title"]}</h3>',unsafe_allow_html=True)
            st.caption(p['authors'])
            st.write(p['summary'])
            st.link_button('Open '+('Nature article ↗' if p['name']=='Nature' else 'paper on arXiv ↗'),p['url'],width='stretch')
            if p.get('pdf_url'):st.link_button('Read the PDF ↗',p['pdf_url'],width='stretch')
    st.markdown('### Read & connect to the demo')
    index=st.selectbox('Choose a reference',range(len(PAPERS)),format_func=lambda i:PAPERS[i]['name'],key='paper_selection')
    p=PAPERS[index]
    st.write(p['connection'])
    if p.get('submission'):
        journal_brand(p)
        st.link_button('Quantum Machine Intelligence ↗',p['journal_url'])
    if p.get('file'):
        pdf=ROOT/'assets/papers'/p['file'];cover=ROOT/'assets/papers'/p['cover']
        if pdf.exists():st.download_button('Download the local preprint PDF',pdf.read_bytes(),p['file'],'application/pdf',key='paper_pdf_'+str(index))
        if cover.exists():
            with st.expander('Preview the first page',expanded=True):st.image(str(cover),width=560)
    else:
        st.link_button('Read on Nature ↗',p['url'])
        st.caption('DOI · 10.1038/d41586-026-02495-4 · Publisher access applies.')
    with st.expander('Source details'):
        st.write('Titles, dates and author information checked against arXiv and Nature on 11 October 2026. The two scientific papers are preprints; the Nature item is journalistic coverage.')
        st.caption('PASQAL paper submission to Quantum Machine Intelligence: confirmed by Christophe Jurczak on 11 October 2026. Status: submitted.')
        for p in PAPERS:st.markdown(f'[{p["title"]}]({p["url"]})')

def journal_brand(p):
    path=ROOT/'assets/springer-journal-logo.svg'
    mark=''
    cover=ROOT/'assets/quantum-machine-intelligence.webp'
    if cover.exists():
        src='data:image/webp;base64,'+base64.b64encode(cover.read_bytes()).decode()
        mark=f'<img src="{src}" alt="Quantum Machine Intelligence journal cover" style="width:42px;float:right;margin:0 0 8px 8px">'
    if path.exists():
        src='data:image/svg+xml;base64,'+base64.b64encode(path.read_bytes()).decode()
        mark+=f'<img src="{src}" alt="Springer journal logo" style="width:100px;height:auto;margin-bottom:10px">'
    st.markdown('<div style="padding:14px;background:#10263a;border-radius:12px;color:white">'+mark+'<div style="font-size:11px;letter-spacing:1px;color:#78dedb">SUBMITTED TO</div><div style="font-size:14px;line-height:1.4;margin-top:6px">Quantum Machine Intelligence</div></div>',unsafe_allow_html=True)
