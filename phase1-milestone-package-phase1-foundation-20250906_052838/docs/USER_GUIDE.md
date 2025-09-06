# Alex AI User Guide

## Getting Started

### Prerequisites
- Python 3.13+
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/familiarcat/alex-ai-job-search-system.git
   cd alex-ai-job-search-system
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

3. **Start with Docker:**
   ```bash
   docker-compose up -d
   ```

4. **Or run locally:**
   ```bash
   pip install -r requirements.txt
   python main.py
   ```

### Basic Usage

#### Command Line Interface
```bash
# Start the system
python main.py

# Check system status
Alex AI> status

# Run health check
Alex AI> health

# Search for jobs
Alex AI> search software engineer

# Coordinate crew
Alex AI> crew implement new feature
```

#### API Usage
```bash
# Health check
curl http://localhost:8000/health

# Job search
curl -X POST http://localhost:8000/api/v1/jobs/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"query": "software engineer", "location": "San Francisco"}'
```

### Configuration

#### Environment Variables
- `OPENAI_API_KEY` - OpenAI API key
- `ANTHROPIC_API_KEY` - Anthropic API key
- `SUPABASE_URL` - Supabase project URL
- `SUPABASE_KEY` - Supabase API key
- `N8N_WEBHOOK_URL` - N8N webhook URL
- `DATABASE_URL` - Database connection string
- `REDIS_URL` - Redis connection string

#### Docker Configuration
The system uses Docker Compose for easy deployment:
- `alex-ai-app` - Main application
- `postgres` - Database
- `redis` - Cache and session storage

### Monitoring

#### Health Checks
The system provides comprehensive health monitoring:
- Database connectivity
- Redis connectivity
- External API availability
- Disk space monitoring
- Memory usage monitoring

#### Logs
Logs are available in the Docker container:
```bash
docker-compose logs -f alex-ai-app
```

### Troubleshooting

#### Common Issues

1. **Port already in use:**
   ```bash
   # Change ports in docker-compose.yml
   ports:
     - "8001:8000"  # Use port 8001 instead
   ```

2. **Database connection failed:**
   ```bash
   # Check if postgres container is running
   docker-compose ps
   
   # Restart database
   docker-compose restart postgres
   ```

3. **API key errors:**
   ```bash
   # Verify environment variables
   docker-compose exec alex-ai-app env | grep API_KEY
   ```

### Support

For support and questions:
- GitHub Issues: https://github.com/familiarcat/alex-ai-job-search-system/issues
- Documentation: https://github.com/familiarcat/alex-ai-job-search-system/tree/main/docs
