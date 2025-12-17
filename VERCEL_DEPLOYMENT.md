# Vercel Deployment Guide

Your weather app has been reorganized for Vercel deployment. Here's what was changed and how to deploy:

## Changes Made

1. **Created `api/index.py`** - Serverless function entry point for Vercel
2. **Created `vercel.json`** - Vercel configuration file
3. **Created `.vercelignore`** - Excludes unnecessary files from deployment
4. **Improved error handling** - Better error handling in both `api/index.py` and `src/weather.py`

## Project Structure

```
.
├── api/
│   └── index.py          # Vercel serverless function
├── src/
│   ├── app.py            # Original Flask app (kept for reference)
│   └── weather.py        # Weather API logic
├── templates/
│   └── index.html        # Frontend template
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
└── .vercelignore        # Files to ignore during deployment
```

## Deployment Steps

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm i -g vercel
   ```

2. **Set Environment Variable**:
   - Go to your Vercel project dashboard
   - Navigate to Settings → Environment Variables
   - Add `API_KEY` with your OpenWeatherMap API key
   - Make sure it's set for Production, Preview, and Development

3. **Deploy**:
   ```bash
   vercel
   ```
   
   Or connect your GitHub repository to Vercel for automatic deployments.

## Important Notes

- **Environment Variables**: Make sure to set `API_KEY` in Vercel's dashboard. The app uses `python-dotenv` for local development, but on Vercel, environment variables are set directly in the dashboard.
- **Original Files Preserved**: Your original `src/app.py` is still there and unchanged. The Vercel deployment uses `api/index.py` instead.
- **Website Functionality**: All features are preserved - city/state/country search and map coordinate selection both work the same way.

## Troubleshooting

If you encounter issues:
1. Check that `API_KEY` is set in Vercel's environment variables
2. Verify that `requirements.txt` includes all dependencies
3. Check Vercel's build logs for any import or path errors

