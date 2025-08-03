# Deployment Guide - Obesity Risk Prediction App

This guide will help you deploy your Obesity Risk Prediction App to Vercel so it's accessible to everyone.

## Prerequisites

1. **GitHub Account**: Make sure your code is pushed to a GitHub repository
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)

## Step-by-Step Deployment

### Method 1: Automatic Deployment (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for Vercel deployment"
   git push origin main
   ```

2. **Deploy on Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up/Login with your GitHub account
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect it's a Vite project
   - Click "Deploy"

3. **Your app will be live in minutes!**

### Method 2: Manual Deployment with Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

4. **Follow the prompts** to complete deployment

## Configuration Files

The project includes these configuration files for Vercel:

- `vercel.json` - Vercel deployment configuration
- `vite.config.js` - Vite build configuration
- `package.json` - Dependencies and build scripts

## What Happens After Deployment

1. **Automatic Build**: Vercel will run `npm run build`
2. **Static Files**: The `dist` folder will be served
3. **Custom Domain**: You'll get a `.vercel.app` URL
4. **Auto Updates**: Every push to GitHub triggers a new deployment

## Environment Variables

This app doesn't require any environment variables, so no additional configuration is needed.

## Troubleshooting

### Common Issues:

1. **Build Fails**
   - Check that all dependencies are in `package.json`
   - Ensure `npm install` works locally

2. **App Not Loading**
   - Check the build logs in Vercel dashboard
   - Verify the `vercel.json` configuration

3. **Styling Issues**
   - Make sure CSS is properly imported in `src/main.jsx`

## Post-Deployment

After successful deployment:

1. **Test the App**: Visit your Vercel URL and test all features
2. **Share the URL**: Share the live URL with your team
3. **Monitor**: Check Vercel dashboard for performance metrics

## Custom Domain (Optional)

1. Go to your Vercel project dashboard
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

## Performance Optimization

The app is optimized for:
- ✅ Fast loading with Vite
- ✅ Responsive design
- ✅ SEO-friendly
- ✅ Mobile-first approach

## Support

If you encounter issues:
1. Check Vercel documentation
2. Review build logs in Vercel dashboard
3. Test locally with `npm run build`

---

**Your app will be accessible to everyone worldwide once deployed!** 🌍 