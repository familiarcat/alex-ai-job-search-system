# Alex AI API Documentation

## Overview
The Alex AI Superagent System provides a comprehensive API for job search and crew coordination functionality.

## Base URL
```
http://localhost:8000
```

## Authentication
All API endpoints require authentication via API key in the header:
```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### Health Check
```
GET /health
```
Returns the health status of the system.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-09-06T10:00:00Z",
  "uptime_seconds": 3600,
  "checks": {
    "database": {"status": "healthy"},
    "redis": {"status": "healthy"},
    "external_apis": {"status": "healthy"}
  }
}
```

### System Status
```
GET /status
```
Returns the current system status and configuration.

**Response:**
```json
{
  "version": "1.0.0",
  "status": "running",
  "crew_members": {
    "captain_picard": "Strategic Command",
    "commander_data": "Technical Implementation"
  }
}
```

### Job Search
```
POST /api/v1/jobs/search
```
Search for job opportunities.

**Request Body:**
```json
{
  "query": "software engineer",
  "location": "San Francisco",
  "filters": {
    "experience_level": "mid",
    "remote": true
  }
}
```

**Response:**
```json
{
  "query": "software engineer",
  "results": [
    {
      "id": "job_123",
      "title": "Senior Software Engineer",
      "company": "Tech Corp",
      "location": "San Francisco, CA",
      "remote": true,
      "salary_range": "$120k - $180k"
    }
  ],
  "total_results": 1
}
```

### Crew Coordination
```
POST /api/v1/crew/coordinate
```
Coordinate crew members for a specific task.

**Request Body:**
```json
{
  "task": "Implement new feature",
  "priority": "high",
  "crew_members": ["commander_data", "lt_la_forge"]
}
```

**Response:**
```json
{
  "task_id": "task_456",
  "assigned_crew": ["commander_data", "lt_la_forge"],
  "status": "assigned",
  "estimated_completion": "2025-09-06T12:00:00Z"
}
```

## Error Handling
All endpoints return appropriate HTTP status codes and error messages:

- `200 OK` - Success
- `400 Bad Request` - Invalid request
- `401 Unauthorized` - Invalid API key
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

Error response format:
```json
{
  "error": "Error message",
  "code": "ERROR_CODE",
  "timestamp": "2025-09-06T10:00:00Z"
}
```
