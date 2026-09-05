# Link Shrink — URL Shortener Frontend

A simple static frontend for the [Serverless URL Shortener](https://github.com/Harsh-Oraon/Serverless-Url-Shortener) API — paste a long URL, get a short one back.

## Live site
_Add your CloudFront URL here once deployed._

## Architecture

```
Browser
   |
   v
CloudFront (CDN + HTTPS)
   |
   v
S3 bucket (private, static files only)
   |
   v (calls, via JS fetch)
API Gateway -> Lambda -> DynamoDB
(the URL shortener backend, deployed separately)
```

This site is just the frontend — plain HTML/CSS/JS, no framework, no build step. It calls the existing URL shortener API directly from the browser.

## Files
- `index.html` — page structure
- `style.css` — styling
- `script.js` — calls the API and handles the form

## Deploy steps
1. Create an S3 bucket (block public access ON)
2. Upload `index.html`, `style.css`, `script.js`
3. Create a CloudFront distribution pointing at the bucket, using Origin Access Control
4. Set `index.html` as the default root object
5. Visit the CloudFront domain to test

## Status
- [x] Site built
- [ ] Deployed to S3
- [ ] CloudFront distribution live
