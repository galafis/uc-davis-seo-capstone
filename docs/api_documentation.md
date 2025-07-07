# Documentação da API - SEO Platform

## 🔍 Endpoints de Auditoria

### Site Audit
- `POST /api/audit/full` - Auditoria completa do site
- `GET /api/audit/technical` - Problemas técnicos
- `GET /api/audit/content` - Análise de conteúdo
- `GET /api/audit/performance` - Métricas de performance

### Keyword Research
- `POST /api/keywords/research` - Pesquisa de palavras-chave
- `GET /api/keywords/difficulty` - Análise de dificuldade
- `GET /api/keywords/suggestions` - Sugestões relacionadas
- `POST /api/keywords/track` - Monitoramento de posições

### Competitor Analysis
- `POST /api/competitors/analyze` - Análise competitiva
- `GET /api/competitors/keywords` - Keywords dos concorrentes
- `GET /api/competitors/backlinks` - Perfil de backlinks
- `GET /api/competitors/content` - Gaps de conteúdo

## 📝 Exemplos de Uso

### Auditoria Completa
```python
import requests

response = requests.post('/api/audit/full', json={
    'url': 'https://example.com',
    'depth': 'full',
    'include_images': True
})

audit_results = response.json()
```

### Pesquisa de Keywords
```python
response = requests.post('/api/keywords/research', json={
    'seed_keywords': ['seo', 'marketing digital'],
    'location': 'Brazil',
    'language': 'pt-BR'
})

keywords = response.json()
```

## 🔐 Autenticação

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -X POST /api/audit/full
```
