#!/usr/bin/env python3
"""
Alex AI REST API
Comprehensive API endpoints for all functionality
"""

from flask import Flask, request, jsonify
from job_search_system import AlexAIJobSearchSystem
from crew_coordination_system import CrewCoordinationSystem
from n8n_integration import N8NIntegration
from supabase_integration import SupabaseMemoryIntegration

app = Flask(__name__)

# Initialize systems
job_search = AlexAIJobSearchSystem()
crew_coord = CrewCoordinationSystem()
n8n_integration = N8NIntegration()
supabase_integration = SupabaseMemoryIntegration()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '2.0.0'
    })

@app.route('/api/v1/jobs/search', methods=['POST'])
def search_jobs():
    """Job search endpoint"""
    data = request.get_json()
    results = job_search.search_jobs(
        query=data.get('query'),
        location=data.get('location'),
        filters=data.get('filters')
    )
    return jsonify(results)

@app.route('/api/v1/crew/coordinate', methods=['POST'])
def coordinate_crew():
    """Crew coordination endpoint"""
    data = request.get_json()
    coordination = crew_coord.coordinate_task(
        task=data.get('task'),
        priority=data.get('priority', 'medium')
    )
    return jsonify(coordination)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
