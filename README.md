# aiaxia-preview

Static HTML preview of the AiAxia onboarding flow. Mirrored from `aivalueprospector/AiAxia` (`public/onboarding-preview/` + `public/css/`) for visual review without running the Laravel backend.

**Live URL:** https://aivalueprospector.github.io/aiaxia-preview/

## What's here

- `index.html` redirects to the preview entry point.
- `onboarding-preview/welcome.html` ... `complete.html` are the five screens, with sample data baked in.
- `css/app.css` is the AiAxia v1 design system (OKLCH botanical palette, Source Serif 4 + Inter).

## How to update

This repo is a mirror. The source of truth lives in `aivalueprospector/AiAxia`:

```
public/onboarding-preview/*.html  ->  onboarding-preview/
public/css/app.css                ->  css/app.css
```

Manual sync until a workflow is added:

```bash
cd /path/to/AiAxia
cp public/onboarding-preview/*.html /path/to/aiaxia-preview/onboarding-preview/
cp public/css/app.css /path/to/aiaxia-preview/css/app.css
cd /path/to/aiaxia-preview
git add -A
git commit -m "sync from AiAxia <commit-sha>"
git push
```

Pages publishes the new content within a minute or two of push.

## License

For preview / review purposes only. Source belongs to the upstream AiAxia project.
