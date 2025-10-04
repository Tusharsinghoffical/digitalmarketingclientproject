# Digital Marketing Agency Website

A complete Django-based website for a digital marketing agency with multiple pages and services.

## Features

- Home page with services overview
- Services pages (SEO, PPC, Website Development, App Development, Video Marketing)
- Packages page with pricing tiers
- Blog section with posts
- About Us page with company information
- Contact page with form
- Responsive design using Bootstrap 5
- Premium, luxurious aesthetic with gold accents and gradient effects

## Technologies Used

- Django 5.2.6
- Python 3.13+
- Bootstrap 5.3
- Font Awesome 6.0
- HTML5 & CSS3

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd digitalmarketing
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Deployment

### Deploying to Render

This project includes a `render.yaml` file for one-click deployment to Render.

1. Fork this repository to your GitHub account
2. Sign up or log in to [Render](https://render.com)
3. Click the "New +" button and select "Web Service"
4. Connect your GitHub account and select your forked repository
5. Render will automatically detect the `render.yaml` file and configure the service:
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn digitalmarketing.wsgi:application`
   - Environment: Python 3.13.0
6. Add environment variables in the Render dashboard:
   - `SECRET_KEY` - A random secret key for Django (automatically created by Render)
   - `DEBUG` - Set to `False` for production
7. Click "Create Web Service" to deploy

The `render.yaml` file configures:
- Python version (3.13.0)
- Build process (install dependencies and collect static files)
- Start command (Gunicorn WSGI server)
- Environment variables

### Deployment Preparation Scripts

Several scripts are provided to help with deployment:

- `deploy_render.py` - Python script to prepare for deployment
- `prepare_deploy.bat` - Windows batch file for deployment preparation
- `deploy.bat` - Original deployment instructions

### Additional Documentation

See these files for more detailed deployment information:
- [DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md) - Complete deployment guide
- [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) - Step-by-step checklist

### Environment Variables

For production deployment, you should set these environment variables:
- `SECRET_KEY` - Django secret key (keep this secret!)
- `DEBUG` - Set to `False` in production
- `ALLOWED_HOSTS` - Comma-separated list of allowed domains

## Pages

- `/` - Home page
- `/services/` - Services overview
- `/services/seo/` - SEO services
- `/services/ppc/` - PPC advertising
- `/services/website-development/` - Website development
- `/services/apps/` - App development
- `/services/video-marketing/` - Video marketing
- `/packages/` - Pricing packages
- `/blog/` - Blog section
- `/about/` - About us
- `/contact/` - Contact page

## Customization

- Templates: All HTML templates are located in the `templates` directory
- Static files: CSS, JavaScript, and images are in the `static` directory
- Views: Each app has its own views in the `views.py` file
- URLs: URL routing is defined in each app's `urls.py` file

## License

This project is proprietary and confidential. All rights reserved.