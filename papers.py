"""Verified public references; optional local preprint copies for the laptop demo."""
from pathlib import Path
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
    st.markdown('<div style="background:linear-gradient(115deg,#172046,#5335a8,#087f98);padding:26px 30px;border-radius:22px;color:white"><span style="font-size:12px;letter-spacing:2px;color:#a3ebff">QUANTONATION LABS · RESEARCH LIBRARY</span><h1 style="color:white;margin:10px 0;font-size:2.5rem">Papers & perspectives</h1><p style="color:#dbe5ff;margin:0">The published trail behind the experiments: literary structures, agentic quantum workflows and Nature coverage.</p></div>',unsafe_allow_html=True)
    st.write('Three references to open during the presentation or share with the team.')
    for col,p in zip(st.columns(3),PAPERS):
        with col,st.container(border=True):
            st.markdown(f'<div style="height:105px;padding:20px;border-radius:14px;background:linear-gradient(120deg,#151d3b,{p["colour"]});color:white"><span style="font-size:10px;letter-spacing:1.5px">{p["kind"].upper()}</span><div style="font-size:25px;font-weight:700;margin-top:12px">{p["name"]}</div></div>',unsafe_allow_html=True)
            st.caption(p['date']+' · '+p['id'])
            st.markdown('### '+p['title'])
            st.caption(p['authors'])
            st.write(p['summary'])
            st.link_button('Open '+('Nature article ↗' if p['name']=='Nature' else 'paper on arXiv ↗'),p['url'],width='stretch')
            if p.get('pdf_url'):st.link_button('Read the PDF ↗',p['pdf_url'],width='stretch')
    st.markdown('### Read & connect to the demo')
    index=st.selectbox('Choose a reference',range(len(PAPERS)),format_func=lambda i:PAPERS[i]['name'],key='paper_selection')
    p=PAPERS[index]
    st.write(p['connection'])
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
        for p in PAPERS:st.markdown(f'[{p["title"]}]({p["url"]})')
