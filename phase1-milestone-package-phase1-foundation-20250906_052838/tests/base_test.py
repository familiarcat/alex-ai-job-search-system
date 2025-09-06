import pytest
import os
import sys
from unittest.mock import Mock, patch

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BaseTestCase:
    """Base test case with common setup and utilities"""
    
    @pytest.fixture(autouse=True)
    def setup_test_environment(self):
        """Set up test environment for each test"""
        # Set test environment variables
        os.environ['TESTING'] = 'true'
        os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
        os.environ['REDIS_URL'] = 'redis://localhost:6379/1'
        
        yield
        
        # Cleanup after test
        if 'TESTING' in os.environ:
            del os.environ['TESTING']
    
    def mock_api_response(self, status_code=200, data=None):
        """Create a mock API response"""
        mock_response = Mock()
        mock_response.status_code = status_code
        mock_response.json.return_value = data or {}
        return mock_response
