# URL Shortener

A serverless URL shortener built on AWS — submit a long URL, get back a short code, and visiting the short link redirects to the original URL.

## Architecture
Browser
|
v
API Gateway (HTTP endpoint)
|
v
Lambda (create_link.py / redirect_link.py)
|
v
DynamoDB (stores short_code -> long_url mappings)


- **API Gateway** exposes two HTTP routes and forwards requests to Lambda
- **Lambda** runs the actual logic — no server managed or running continuously
- **DynamoDB** stores the short_code -> long_url mapping

## Endpoints
- `POST /links` — create a short link. Body: `{"url": "https://example.com"}`
- `GET /links/{code}` — redirects to the original URL

## Tech
- Python 3.13
- boto3 (AWS SDK)

## Status
- [x] Lambda functions written
- [x] DynamoDB table created
- [x] Lambda functions deployed
- [ ] API Gateway configured
- [ ] Live and tested