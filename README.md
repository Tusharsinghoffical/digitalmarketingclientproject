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

This project is configured for deployment on Render. Simply connect your GitHub repository to Render and it will automatically deploy.

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