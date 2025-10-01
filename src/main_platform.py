import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

from src.seo_audit import SEOAuditor
from src.keyword_research.keyword_researcher import KeywordResearcher
from src.content_optimization.content_optimizer import ContentOptimizer
from src.competitor_analysis.competitor_analyzer import CompetitorAnalyzer
from src.local_seo.local_seo_manager import LocalSEIManager
from src.international_seo.international_seo_manager import InternationalSEIManager

def main():
    st.set_page_config(layout="wide")
    st.title("📊 Google Search Engine Optimization (SEO) Platform")
    st.markdown("**Professional Capstone Project by Gabriel Demetrios Lafis**")
    st.markdown("---")

    st.sidebar.title("Navegação")
    selection = st.sidebar.radio("Ir para", ["Visão Geral", "Auditoria SEO", "Pesquisa de Palavras-chave", "Otimização de Conteúdo", "Análise de Concorrentes", "SEO Local", "SEO Internacional"])

    if selection == "Visão Geral":
        st.header("Bem-vindo à Plataforma de SEO")
        st.write("Esta plataforma oferece um conjunto completo de ferramentas para análise, auditoria e otimização de SEO.")
        
        # Demo data (can be replaced with real data from tools later)
        data = pd.DataFrame({
            'Date': pd.date_range('2024-01-01', periods=30),
            'Organic Traffic': np.random.randint(1000, 5000, 30).cumsum(),
            'Keyword Rankings': np.random.randint(1, 50, 30)
        })
        
        st.subheader("Métricas de Desempenho (Exemplo)")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tráfego Orgânico Total", f"{data['Organic Traffic'].iloc[-1]:,.0f}")
        with col2:
            st.metric("Média de Posição de Palavras-chave", f"{data['Keyword Rankings'].mean():.1f}")
        with col3:
            st.metric("Última Atualização", data['Date'].iloc[-1].strftime('%Y-%m-%d'))

        st.subheader("Gráfico de Tráfego Orgânico (Exemplo)")
        fig_traffic = px.line(data, x='Date', y='Organic Traffic', title='Tráfego Orgânico ao Longo do Tempo')
        st.plotly_chart(fig_traffic, use_container_width=True)

    elif selection == "Auditoria SEO":
        st.header("🔍 Auditoria Técnica de SEO")
        auditor = SEOAuditor()
        url_to_audit = st.text_input("Insira a URL para auditoria", "https://www.example.com")
        if st.button("Executar Auditoria"): 
            with st.spinner('Executando auditoria...'):
                audit_results = auditor.full_audit(url_to_audit)
                st.success(f"Auditoria concluída para {url_to_audit}!")
                st.json(audit_results)
                
                issues = auditor.identify_technical_issues(audit_results)
                st.subheader("Problemas Técnicos Identificados")
                for issue in issues:
                    st.warning(f"- {issue}")
                
                recommendations = auditor.generate_recommendations(issues)
                st.subheader("Recomendações")
                for rec in recommendations:
                    st.info(f"- {rec}")

    elif selection == "Pesquisa de Palavras-chave":
        st.header("🔑 Pesquisa de Palavras-chave")
        researcher = KeywordResearcher()
        topic = st.text_input("Insira um tópico para pesquisa de palavras-chave", "SEO")
        if st.button("Pesquisar Palavras-chave"): 
            with st.spinner('Pesquisando palavras-chave...'):
                keywords = researcher.discover_keywords(topic)
                st.subheader("Palavras-chave Descobertas")
                st.write(keywords)
                
                analysis = researcher.analyze_keywords(keywords)
                st.subheader("Análise de Palavras-chave")
                st.json(analysis)
                
                opportunities = researcher.find_opportunities(analysis)
                st.subheader("Oportunidades de Palavras-chave")
                st.write(opportunities)

    elif selection == "Otimização de Conteúdo":
        st.header("📝 Otimização de Conteúdo")
        optimizer = ContentOptimizer()
        content_input = st.text_area("Cole o conteúdo para otimização", "Seu conteúdo aqui...")
        if st.button("Otimizar Conteúdo"): 
            with st.spinner('Otimizando conteúdo...'):
                analysis = optimizer.analyze_content(content_input)
                st.subheader("Análise de Conteúdo")
                st.json(analysis)
                
                title_input = st.text_input("Insira um título para otimização", "Título do Artigo")
                optimized_title = optimizer.optimize_title(title_input)
                st.subheader("Título Otimizado")
                st.success(optimized_title)

    elif selection == "Análise de Concorrentes":
        st.header("📈 Análise de Concorrentes")
        analyzer = CompetitorAnalyzer()
        domain_input = st.text_input("Insira seu domínio para análise de concorrentes", "example.com")
        if st.button("Analisar Concorrentes"): 
            with st.spinner('Analisando concorrentes...'):
                competitors = analyzer.identify_competitors(domain_input)
                st.subheader("Concorrentes Identificados")
                st.write(competitors)
                
                gap_analysis = analyzer.content_gap_analysis(competitors)
                st.subheader("Análise de Lacunas de Conteúdo")
                st.json(gap_analysis)
                
                strategy = analyzer.create_strategy(gap_analysis)
                st.subheader("Estratégia Sugerida")
                st.info(strategy)

    elif selection == "SEO Local":
        st.header("🌍 SEO Local")
        local_seo_manager = LocalSEIManager()
        business_name = st.text_input("Nome do Negócio", "Minha Empresa Local")
        gmb_id = st.text_input("ID do Google My Business", "GMB12345")
        if st.button("Otimizar SEO Local"): 
            with st.spinner('Otimizando SEO Local...'):
                st.success(local_seo_manager.optimize_local_search({"name": business_name}))
                st.info(local_seo_manager.analyze_gmb_profile(gmb_id))

    elif selection == "SEO Internacional":
        st.header("🌐 SEO Internacional")
        international_seo_manager = InternationalSEIManager()
        urls_input = st.text_area("URLs para implementação de Hreflang (uma por linha)", "https://example.com/en\nhttps://example.com/pt")
        country_code = st.text_input("Código do País para Segmentação (ex: BR, US)", "BR")
        if st.button("Otimizar SEO Internacional"): 
            with st.spinner('Otimizando SEO Internacional...'):
                urls = urls_input.split('\n')
                st.success(international_seo_manager.implement_hreflang(urls))
                st.info(international_seo_manager.international_targeting(country_code))

if __name__ == "__main__":
    main()

