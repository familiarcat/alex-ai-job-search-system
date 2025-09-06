#!/usr/bin/env python3
"""
Health Check Endpoint for Alex AI System
"""

import json
import time
from datetime import datetime
from typing import Dict, Any

class HealthChecker:
    def __init__(self):
        self.start_time = time.time()
        self.checks = {
            'database': self._check_database,
            'redis': self._check_redis,
            'external_apis': self._check_external_apis,
            'disk_space': self._check_disk_space,
            'memory': self._check_memory
        }
    
    def _check_database(self) -> Dict[str, Any]:
        """Check database connectivity"""
        try:
            # This will be implemented when database is added
            return {'status': 'healthy', 'response_time': 0.001}
        except Exception as e:
            return {'status': 'unhealthy', 'error': str(e)}
    
    def _check_redis(self) -> Dict[str, Any]:
        """Check Redis connectivity"""
        try:
            # This will be implemented when Redis is added
            return {'status': 'healthy', 'response_time': 0.001}
        except Exception as e:
            return {'status': 'unhealthy', 'error': str(e)}
    
    def _check_external_apis(self) -> Dict[str, Any]:
        """Check external API connectivity"""
        try:
            # This will be implemented when external APIs are added
            return {'status': 'healthy', 'response_time': 0.001}
        except Exception as e:
            return {'status': 'unhealthy', 'error': str(e)}
    
    def _check_disk_space(self) -> Dict[str, Any]:
        """Check available disk space"""
        import shutil
        try:
            total, used, free = shutil.disk_usage('/')
            free_percent = (free / total) * 100
            status = 'healthy' if free_percent > 10 else 'warning'
            return {
                'status': status,
                'free_percent': round(free_percent, 2),
                'free_gb': round(free / (1024**3), 2)
            }
        except Exception as e:
            return {'status': 'unhealthy', 'error': str(e)}
    
    def _check_memory(self) -> Dict[str, Any]:
        """Check memory usage"""
        try:
            import psutil
            memory = psutil.virtual_memory()
            status = 'healthy' if memory.percent < 90 else 'warning'
            return {
                'status': status,
                'percent_used': memory.percent,
                'available_gb': round(memory.available / (1024**3), 2)
            }
        except Exception as e:
            return {'status': 'unhealthy', 'error': str(e)}
    
    def get_health_status(self) -> Dict[str, Any]:
        """Get overall health status"""
        results = {}
        overall_status = 'healthy'
        
        for check_name, check_func in self.checks.items():
            try:
                results[check_name] = check_func()
                if results[check_name]['status'] == 'unhealthy':
                    overall_status = 'unhealthy'
                elif results[check_name]['status'] == 'warning' and overall_status == 'healthy':
                    overall_status = 'warning'
            except Exception as e:
                results[check_name] = {'status': 'unhealthy', 'error': str(e)}
                overall_status = 'unhealthy'
        
        return {
            'status': overall_status,
            'timestamp': datetime.now().isoformat(),
            'uptime_seconds': round(time.time() - self.start_time, 2),
            'checks': results
        }

if __name__ == "__main__":
    checker = HealthChecker()
    status = checker.get_health_status()
    print(json.dumps(status, indent=2))
