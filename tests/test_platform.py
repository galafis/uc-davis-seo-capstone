import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.seo_audit import SEOAuditor
from src.keyword_research.keyword_researcher import KeywordResearcher
from src.content_optimization.content_optimizer import ContentOptimizer
from src.competitor_analysis.competitor_analyzer import CompetitorAnalyzer
from src.local_seo.local_seo_manager import LocalSEIManager
from src.international_seo.international_seo_manager import InternationalSEIManager

class TestSEOPlatform(unittest.TestCase):

    def test_seo_auditor(self):
        auditor = SEOAuditor()
        audit_results = auditor.full_audit("https://test.com")
        self.assertIn("status", audit_results)
        self.assertEqual(audit_results["status"], "audited")
        
        issues = auditor.identify_technical_issues(audit_results)
        self.assertIsInstance(issues, list)
        self.assertGreater(len(issues), 0)
        
        recommendations = auditor.generate_recommendations(issues)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

    def test_keyword_researcher(self):
        researcher = KeywordResearcher()
        keywords = researcher.discover_keywords("test_topic")
        self.assertIsInstance(keywords, list)
        self.assertGreater(len(keywords), 0)
        
        analysis = researcher.analyze_keywords(keywords)
        self.assertIsInstance(analysis, dict)
        self.assertIn("keyword1 for test_topic", analysis)
        
        opportunities = researcher.find_opportunities(analysis)
        self.assertIsInstance(opportunities, list)

    def test_content_optimizer(self):
        optimizer = ContentOptimizer()
        analysis = optimizer.analyze_content("This is test content.")
        self.assertIn("readability_score", analysis)
        self.assertIn("keyword_density", analysis)
        
        optimized_title = optimizer.optimize_title("Test Title")
        self.assertIn("Optimized:", optimized_title)

    def test_competitor_analyzer(self):
        analyzer = CompetitorAnalyzer()
        competitors = analyzer.identify_competitors("test.com")
        self.assertIsInstance(competitors, list)
        self.assertGreater(len(competitors), 0)
        
        gap_analysis = analyzer.content_gap_analysis(competitors)
        self.assertIn("gaps", gap_analysis)
        
        strategy = analyzer.create_strategy(gap_analysis)
        self.assertIsInstance(strategy, str)

    def test_local_seo_manager(self):
        manager = LocalSEIManager()
        result_optimize = manager.optimize_local_search({"name": "Test Business"})
        self.assertIn("Optimized local search", result_optimize)
        
        result_gmb = manager.analyze_gmb_profile("GMB123")
        self.assertIn("Analyzed GMB profile", result_gmb)

    def test_international_seo_manager(self):
        manager = InternationalSEIManager()
        urls = ["https://test.com/en", "https://test.com/fr"]
        result_hreflang = manager.implement_hreflang(urls)
        self.assertIn("Hreflang implemented", result_hreflang)
        
        result_targeting = manager.international_targeting("FR")
        self.assertIn("Targeting FR", result_targeting)

if __name__ == '__main__':
    unittest.main()

