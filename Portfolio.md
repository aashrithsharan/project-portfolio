# Portfolio Site

A modern, performant portfolio website built with **Next.js 14** (App Router), **TypeScript**, and **Tailwind CSS**.

## Features

- ✅ Multi-page architecture with Home, About, Case Studies, Blog, Contact, 404
- ✅ File-based blog system (Markdown) — add a file, get a post
- ✅ Syntax highlighting with Shiki (dual theme)
- ✅ Auto-generated table of contents on blog posts
- ✅ Previous/Next post navigation
- ✅ RSS feed at `/rss.xml`
- ✅ Auto-generated `sitemap.xml` and `robots.txt`
- ✅ SEO metadata per page (Open Graph, Twitter cards)
- ✅ Contact form with Slack webhook or Resend email integration
- ✅ Honeypot spam protection + rate limiting
- ✅ Responsive and accessible
- ✅ Modern typography with `next/font` (Inter + Outfit + JetBrains Mono)
- ✅ Smooth scroll on homepage with active section highlighting
- ✅ Sticky navigation with mobile menu

## Getting Started

### Prerequisites

- **Node.js** 18.17 or later
- **npm**, **yarn**, or **pnpm**

### Installation

```bash
# Clone the repository
git clone <your-repo-url> portfolio-site
cd portfolio-site

# Install dependencies
npm install

# Copy environment variables
cp .env.example .env.local

# Start development server
npm run dev
```

Open [URL_REMOVED]

### Environment Variables

Copy `.env.example` to `.env.local` and configure:

| Variable | Description | Required |
|----------|-------------|----------|
| `SLACK_WEBHOOK_URL` | Slack incoming webhook URL for contact form | One of Slack or Resend |
| `RESEND_API_KEY` | Resend API key for email delivery | One of Slack or Resend |
| `CONTACT_EMAIL` | Email address to receive contact form submissions | Only with Resend |
| `NEXT_PUBLIC_SITE_URL` | Your deployed site URL (used for RSS, sitemap, OG) | Recommended |

> **Note:** If neither Slack nor Resend is configured, contact form submissions are logged to the server console.

#### Setting up Slack Webhook

1. Go to Slack API → Create New App → From scratch
2. Enable **Incoming Webhooks** → Add New Webhook to Workspace
3. Copy the webhook URL to `SLACK_WEBHOOK_URL`

#### Setting up Resend

1. Sign up at resend.com
2. Create an API key
3. Set `RESEND_API_KEY` and `CONTACT_EMAIL` in `.env.local`

## Project Structure

```
portfolio-site/
├── content/
│   └── blog/                    # Blog posts (Markdown files)
│       ├── building-performant-react-apps.md
│       ├── modern-css-reset.md
│       ├── nextjs-app-router-migration.md
│       └── designing-accessible-components.md
├── public/
│   ├── og-default.png           # Default Open Graph image
│   ├── resume.pdf               # Downloadable resume
│   └── favicon.svg              # Site favicon
├── src/
│   ├── app/
│   │   ├── layout.tsx           # Root layout (nav + footer)
│   │   ├── page.tsx             # Home page
│   │   ├── globals.css          # Global styles
│   │   ├── not-found.tsx        # 404 page
│   │   ├── sitemap.ts           # Auto-generated sitemap
│   │   ├── robots.ts            # robots.txt
│   │   ├── about/page.tsx
│   │   ├── blog/
│   │   │   ├── page.tsx         # Blog index
│   │   │   └── [slug]/page.tsx  # Blog post detail
│   │   ├── case-studies/
│   │   │   ├── page.tsx         # Case studies index
│   │   │   └── [slug]/page.tsx  # Case study detail
│   │   ├── contact/page.tsx
│   │   ├── api/contact/route.ts # Contact form API
│   │   └── rss.xml/route.ts     # RSS feed
│   ├── components/
│   │   ├── Nav.tsx
│   │   ├── Footer.tsx
│   │   ├── TableOfContents.tsx
│   │   └── sections/            # Home page sections
│   │       ├── Hero.tsx
│   │       ├── AboutSection.tsx
│   │       ├── ExperienceSection.tsx
│   │       ├── CaseStudiesSection.tsx
│   │       ├── SkillsSection.tsx
│   │       ├── BlogSection.tsx
│   │       ├── ContactSection.tsx
│   │       └── index.ts
│   ├── content/
│   │   ├── profile.ts           # All portfolio content
│   │   └── caseStudies.ts       # Case study data
│   └── lib/
│       ├── blog.ts              # Blog file system utilities
│       ├── markdown.ts          # Markdown → HTML processor
│       └── seo.ts               # SEO metadata builder
├── .env.example
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

## Content Management

### Editing Portfolio Content

All personal content is centralized in **`src/content/profile.ts`**:
- Name, title, tagline, contact info, social links
- About text (short + long)
- Work experience timeline
- Skills grouped by category
- Testimonials

### Editing Case Studies

Case studies are in **`src/content/caseStudies.ts`**. Each case study has:
- Title, subtitle, description
- Cover image URL
- Tags, metrics, outcomes
- Challenge → Approach → Result narrative

### Adding a New Blog Post

1. Create a new `.md` file in `content/blog/`:

```
content/blog/my-new-post.md
```

2. Add frontmatter at the top:

```markdown
---
title: "My New Post Title"
date: "2026-03-01"
excerpt: "A brief description that appears in the blog index and RSS feed."
tags: ["React", "TypeScript"]
ogImage: "[URL_REMOVED]
---

# My New Post Title

Your content here. Supports full Markdown:
- Headers (h2–h4 auto-generate table of contents)
- Code blocks with syntax highlighting (use ```language)
- Images, tables, blockquotes, lists
- GFM (GitHub Flavored Markdown) features
```

3. That's it! The post will automatically appear in:
   - `/blog` (index page, sorted by date)
   - `/blog/my-new-post` (detail page)
   - Homepage blog section (if among the 3 latest)
   - RSS feed (`/rss.xml`)
   - Sitemap (`/sitemap.xml`)

**No code changes needed.**

### Supported Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | ✅ | Post title |
| `date` | string | ✅ | Publication date (YYYY-MM-DD) |
| `excerpt` | string | ✅ | Short description for index/RSS |
| `tags` | string[] | ❌ | Array of tag labels |
| `ogImage` | string | ❌ | Open Graph image URL |

### Supported Code Languages

Syntax highlighting supports: TypeScript, TSX, JavaScript, JSX, CSS, HTML, JSON, Bash, Python, Markdown, YAML, SQL.

## Deployment to Vercel

### Option A: One-Click Deploy

![Deploy with Vercel]([URL_REMOVED])

1. Import your Git repository
2. Add environment variables in the Vercel dashboard
3. Deploy

### Option B: Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Set environment variables
vercel env add SLACK_WEBHOOK_URL
vercel env add NEXT_PUBLIC_SITE_URL
```

### Environment Variables on Vercel

In your Vercel project dashboard → Settings → Environment Variables, add:

- `NEXT_PUBLIC_SITE_URL` = `[URL_REMOVED]
- `SLACK_WEBHOOK_URL` = your Slack webhook (or Resend keys)

## Development

```bash
npm run dev     # Start dev server
npm run build   # Production build
npm run start   # Start production server
npm run lint    # Run ESLint
```

## Tech Stack

- **Framework:** Next.js 14 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Fonts:** Inter, Outfit, JetBrains Mono (via `next/font`)
- **Markdown:** unified + remark + rehype
- **Syntax Highlighting:** Shiki
- **RSS:** rss package
- **Contact:** Slack Webhook or Resend API

## License

MIT
