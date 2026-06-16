# InterviewOS UI Design System

> Design philosophy: **Premium**, **Dark-first**, **Purposeful Motion**, **Glassmorphism** — inspired by Linear, Stripe, Vercel, Notion, and Arc Browser.

---

## 1. Design Principles

| Principle | Implementation |
|-----------|---------------|
| **Dark First** | Deep near-black backgrounds (#09090b base) with layered depth |
| **Glass Morphism** | Frosted glass cards with `backdrop-blur`, subtle borders |
| **Purposeful Motion** | Every animation has meaning — no decoration for its own sake |
| **Information Hierarchy** | Aggressive typographic scale for clear visual hierarchy |
| **Premium Feel** | Subtle gradients, refined spacing, micro-interactions everywhere |

---

## 2. Color Palette

### Base Colors (Zinc Scale — Dark Mode First)
```css
--background:        #09090b;  /* zinc-950 — deepest background */
--surface:           #0f0f12;  /* slightly lighter — card backgrounds */
--surface-raised:    #141418;  /* elevated cards */
--surface-overlay:   #1a1a20;  /* modals, dropdowns */
--border:            #27272a;  /* zinc-800 — subtle borders */
--border-strong:     #3f3f46;  /* zinc-700 — emphasized borders */
--muted:             #71717a;  /* zinc-500 — placeholder text */
--foreground:        #fafafa;  /* zinc-50 — primary text */
--foreground-muted:  #a1a1aa;  /* zinc-400 — secondary text */
```

### Accent Colors — Electric Palette
```css
/* Primary Accent: Violet/Purple (Interviews, CTAs) */
--accent-primary:    #7c3aed;  /* violet-600 */
--accent-primary-glow: rgba(124, 58, 237, 0.4);

/* Secondary Accent: Cyan (AI, Voice, Tech) */
--accent-cyan:       #06b6d4;  /* cyan-500 */
--accent-cyan-glow:  rgba(6, 182, 212, 0.3);

/* Success: Emerald */
--accent-emerald:    #10b981;  /* emerald-500 */
--accent-emerald-glow: rgba(16, 185, 129, 0.3);

/* Warning: Amber */
--accent-amber:      #f59e0b;  /* amber-500 */

/* Error: Rose */
--accent-rose:       #f43f5e;  /* rose-500 */

/* Info: Blue */
--accent-blue:       #3b82f6;  /* blue-500 */
```

### Gradient Definitions
```css
/* Hero gradient — text gradient */
--gradient-hero: linear-gradient(135deg, #7c3aed 0%, #06b6d4 50%, #10b981 100%);

/* Background mesh gradient */
--gradient-bg: radial-gradient(ellipse at 20% 50%, rgba(124, 58, 237, 0.15) 0%, transparent 50%),
               radial-gradient(ellipse at 80% 20%, rgba(6, 182, 212, 0.1) 0%, transparent 50%),
               radial-gradient(ellipse at 50% 80%, rgba(16, 185, 129, 0.08) 0%, transparent 50%);

/* Card gradient */
--gradient-card: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);

/* Glow gradient for buttons */
--gradient-button: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%);
```

### Score Color Scale
```css
/* Used for all scoring displays */
--score-excellent:  #10b981;  /* 90-100 */
--score-good:       #22c55e;  /* 75-89 */
--score-average:    #f59e0b;  /* 50-74 */
--score-poor:       #ef4444;  /* 25-49 */
--score-critical:   #f43f5e;  /* 0-24 */
```

---

## 3. Typography

### Font Families
```css
/* Sans-serif UI font */
font-family: 'Geist', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

/* Monospace for code, scores, IDs */
font-family: 'Geist Mono', 'JetBrains Mono', 'Fira Code', monospace;
```

### Type Scale
```css
/* Display — Hero headlines */
.text-display-2xl { font-size: 4.5rem; line-height: 1; font-weight: 700; letter-spacing: -0.03em; }
.text-display-xl  { font-size: 3.75rem; line-height: 1; font-weight: 700; letter-spacing: -0.02em; }
.text-display-lg  { font-size: 3rem; line-height: 1.1; font-weight: 700; letter-spacing: -0.02em; }

/* Heading */
.text-4xl { font-size: 2.25rem; line-height: 2.5rem; font-weight: 700; }
.text-3xl { font-size: 1.875rem; line-height: 2.25rem; font-weight: 600; }
.text-2xl { font-size: 1.5rem; line-height: 2rem; font-weight: 600; }
.text-xl  { font-size: 1.25rem; line-height: 1.75rem; font-weight: 600; }
.text-lg  { font-size: 1.125rem; line-height: 1.75rem; font-weight: 500; }

/* Body */
.text-base { font-size: 1rem; line-height: 1.5rem; font-weight: 400; }
.text-sm   { font-size: 0.875rem; line-height: 1.25rem; }
.text-xs   { font-size: 0.75rem; line-height: 1rem; }
```

---

## 4. Spacing System

Based on 4px base unit (0.25rem):
```
1  =  4px    (xs gaps, icon padding)
2  =  8px    (sm internal padding)
3  =  12px   (badge padding)
4  =  16px   (base unit, most common)
5  =  20px
6  =  24px   (card padding)
8  =  32px   (section gaps)
10 =  40px
12 =  48px   (large section padding)
16 =  64px   (hero padding)
20 =  80px
24 =  96px   (page sections)
32 = 128px   (hero section)
```

---

## 5. Component Specifications

### 5.1 Glassmorphism Card
```css
.glass-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  box-shadow: 
    0 4px 24px rgba(0, 0, 0, 0.4),
    inset 0 1px 0 rgba(255, 255, 255, 0.05);
  transition: all 0.2s ease;
}

.glass-card:hover {
  border-color: rgba(255, 255, 255, 0.12);
  box-shadow: 
    0 8px 40px rgba(0, 0, 0, 0.5),
    inset 0 1px 0 rgba(255, 255, 255, 0.08);
  transform: translateY(-2px);
}
```

### 5.2 Button Variants

#### Primary (Glow)
```css
.btn-primary {
  background: linear-gradient(135deg, #7c3aed, #5b21b6);
  color: white;
  border: none;
  border-radius: 10px;
  padding: 10px 20px;
  font-weight: 600;
  font-size: 0.875rem;
  box-shadow: 0 0 20px rgba(124, 58, 237, 0.4), 0 4px 12px rgba(0,0,0,0.3);
  transition: all 0.2s ease;
}

.btn-primary:hover {
  box-shadow: 0 0 30px rgba(124, 58, 237, 0.6), 0 6px 20px rgba(0,0,0,0.4);
  transform: translateY(-1px);
}
```

#### Ghost
```css
.btn-ghost {
  background: transparent;
  color: #a1a1aa;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px;
  padding: 10px 20px;
  font-weight: 500;
  transition: all 0.2s ease;
}

.btn-ghost:hover {
  background: rgba(255,255,255,0.05);
  color: #fafafa;
  border-color: rgba(255,255,255,0.15);
}
```

#### Cyan Accent (Voice/AI)
```css
.btn-cyan {
  background: rgba(6, 182, 212, 0.1);
  color: #06b6d4;
  border: 1px solid rgba(6, 182, 212, 0.3);
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(6, 182, 212, 0.15);
}

.btn-cyan:hover {
  background: rgba(6, 182, 212, 0.2);
  box-shadow: 0 0 30px rgba(6, 182, 212, 0.3);
}
```

### 5.3 Badge Variants
```css
/* Hiring Recommendation Badges */
.badge-strong-hire { background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); }
.badge-hire        { background: rgba(59, 130, 246, 0.15); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.3); }
.badge-no-hire     { background: rgba(244, 63, 94, 0.15); color: #f43f5e; border: 1px solid rgba(244, 63, 94, 0.3); }

/* Difficulty Badges */
.badge-easy   { background: rgba(16, 185, 129, 0.15); color: #10b981; }
.badge-medium { background: rgba(245, 158, 11, 0.15); color: #f59e0b; }
.badge-hard   { background: rgba(239, 68, 68, 0.15); color: #ef4444; }
.badge-faang  { background: rgba(124, 58, 237, 0.15); color: #a78bfa; border: 1px solid rgba(124, 58, 237, 0.4); }
```

### 5.4 Input Fields
```css
.input {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  color: #fafafa;
  padding: 10px 14px;
  font-size: 0.875rem;
  transition: all 0.2s ease;
  outline: none;
}

.input:focus {
  border-color: rgba(124, 58, 237, 0.5);
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
}

.input::placeholder {
  color: #52525b;
}
```

### 5.5 Progress Ring (SVG)
```tsx
// Animated SVG circle progress for scores
interface ProgressRingProps {
  score: number; // 0-100
  size?: number; // px
  strokeWidth?: number;
  color?: string; // CSS color
}

// Implementation: Use stroke-dasharray and stroke-dashoffset
// Animate from 0 to score value using Framer Motion
```

### 5.6 Audio Waveform Visualizer
```tsx
// Canvas-based real-time audio waveform
// Uses Web Audio API AnalyserNode
// 64 frequency bins rendered as animated bars
// Color: cyan gradient matching accent palette
```

### 5.7 Score Card
```tsx
interface ScoreCardProps {
  label: string;
  score: number; // 0-100
  icon: LucideIcon;
  trend?: number; // +/- change from last interview
  breakdown?: { label: string; score: number }[];
}
```

---

## 6. Animation Specifications

### Motion Principles
1. **Entrance animations**: `slide-up` + `fade-in` (200-400ms, ease-out)
2. **Staggered lists**: 50ms delay between each item
3. **Hover states**: 150-200ms ease transitions
4. **Page transitions**: Shared layout animations with Framer Motion
5. **Loading states**: Skeleton shimmer animations

### Keyframes
```css
@keyframes shimmer {
  0%   { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-10px); }
}

@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 10px var(--accent-cyan-glow); }
  50%       { box-shadow: 0 0 30px var(--accent-cyan-glow), 0 0 60px var(--accent-cyan-glow); }
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes gradient-shift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

@keyframes speaking-ring {
  0%   { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(1.8); opacity: 0; }
}
```

### Framer Motion Variants
```tsx
// Page entrance
const pageVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.4, ease: "easeOut" } },
  exit: { opacity: 0, y: -20, transition: { duration: 0.2 } }
};

// Staggered children
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.05, delayChildren: 0.1 }
  }
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.3, ease: "easeOut" } }
};

// Card hover
const cardHoverVariants = {
  rest: { scale: 1, y: 0 },
  hover: { scale: 1.02, y: -4, transition: { duration: 0.2, ease: "easeOut" } }
};

// Score counter animation
// Use Framer Motion's useMotionValue + useSpring for smooth number counting
```

---

## 7. Layout System

### Sidebar Layout (Dashboard)
```
┌──────────────────────────────────────────────────────┐
│  TOPBAR: Logo | Breadcrumb | Search | Notifications  │
├─────────────┬────────────────────────────────────────┤
│             │                                        │
│  SIDEBAR    │   MAIN CONTENT                        │
│  (240px)    │   (flex-1, max-w: 1200px, centered)   │
│             │                                        │
│  ⭐ Logo    │                                        │
│  ─────────  │                                        │
│  Dashboard  │                                        │
│  Interviews │                                        │
│  Progress   │                                        │
│  Resume     │                                        │
│  Reports    │                                        │
│  Settings   │                                        │
│             │                                        │
│  [User]     │                                        │
└─────────────┴────────────────────────────────────────┘
```

### Grid System
- Container max-width: `1280px`
- Gutter: `24px` (mobile), `32px` (desktop)
- Columns: 12-column grid
- Breakpoints: sm `640px`, md `768px`, lg `1024px`, xl `1280px`, 2xl `1536px`

---

## 8. Icon System

Use **Lucide React** exclusively. Key icons:
```
Brain           — AI/Intelligence
Mic / MicOff    — Voice recording
Volume2         — Audio/TTS
FileText        — Resume/Documents  
Briefcase       — Job/Career
BarChart3       — Analytics/Progress
Trophy          — Scores/Achievements
Zap             — Fast/AI processing
Target          — Goals/Accuracy
TrendingUp      — Improvement
Clock           — Timer/Duration
Shield          — Security
Star            — Favorites/Featured
ChevronRight    — Navigation
PlayCircle      — Start interview
PauseCircle     — Pause
StopCircle      — End interview
Loader2         — Loading (animated with spin)
CheckCircle2    — Success
XCircle         — Error
AlertTriangle   — Warning
```

---

## 9. Responsive Design

### Mobile First Breakpoints
```tsx
// Tailwind responsive classes usage:
// sm: 640px — show sidebar collapsed
// md: 768px — show stats in 2 columns  
// lg: 1024px — full sidebar expanded
// xl: 1280px — 3-column layouts
```

### Mobile Sidebar
- Hamburger menu icon in topbar
- Slides in from left as overlay
- Dark backdrop with blur
- Auto-closes on navigation

---

## 10. Loading States

### Skeleton Screens
```css
.skeleton {
  background: linear-gradient(90deg, 
    rgba(255,255,255,0.03) 25%, 
    rgba(255,255,255,0.07) 50%, 
    rgba(255,255,255,0.03) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 8px;
}
```

### Loading Overlay (Voice Interview)
- Animated concentric rings (cyan)
- "Connecting to AI Interviewer..." text
- Pulsing gradient background

---

## 11. Voice Interview UI

### AI Avatar Area
```
┌────────────────────────────────────┐
│                                    │
│    ╭──────────────────────╮        │
│    │  Animated AI Avatar  │        │
│    │  (pulsing rings when │        │
│    │   speaking)          │        │
│    ╰──────────────────────╯        │
│                                    │
│    "Tell me about yourself..."     │
│                                    │
│    [Transcript scroll area]        │
│                                    │
│  ┌─────────────────────────────┐   │
│  │  ████░░░░███░░░████░░░███  │   │
│  │  [User Audio Waveform]     │   │
│  └─────────────────────────────┘   │
│                                    │
│  [🎤 Unmute]  [⏱ 12:34]  [■ End] │
└────────────────────────────────────┘
```

### Speaking Indicator
```css
/* 3 expanding rings when AI is speaking */
.speaking-ring {
  position: absolute;
  border: 2px solid rgba(6, 182, 212, 0.6);
  border-radius: 50%;
  animation: speaking-ring 2s infinite;
}

.speaking-ring:nth-child(2) { animation-delay: 0.4s; }
.speaking-ring:nth-child(3) { animation-delay: 0.8s; }
```

---

## 12. Score Report UI

### Score Ring Colors
```
100 — #10b981 (Emerald) "Outstanding"
80  — #22c55e (Green)   "Excellent"  
65  — #f59e0b (Amber)   "Good"
50  — #ef4444 (Red)     "Needs Work"
<50 — #f43f5e (Rose)    "Critical"
```

### Hiring Recommendation Display
```
╭────────────────────────────────────╮
│  🟢 STRONG HIRE                   │
│                                    │
│  "This candidate demonstrated     │
│  exceptional technical depth..."  │
╰────────────────────────────────────╯
```

---

## 13. Design Tokens (Tailwind Extension)

```js
// tailwind.config.ts
theme: {
  extend: {
    colors: {
      zinc: { /* full scale */ },
      accent: {
        violet: '#7c3aed',
        cyan:   '#06b6d4',
        emerald:'#10b981',
        amber:  '#f59e0b',
        rose:   '#f43f5e',
      }
    },
    fontFamily: {
      sans: ['Geist', 'Inter', 'system-ui', 'sans-serif'],
      mono: ['Geist Mono', 'JetBrains Mono', 'monospace'],
    },
    boxShadow: {
      'glow-violet': '0 0 20px rgba(124, 58, 237, 0.4)',
      'glow-cyan':   '0 0 20px rgba(6, 182, 212, 0.3)',
      'glow-emerald':'0 0 20px rgba(16, 185, 129, 0.3)',
      'glass':       '0 4px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05)',
    },
    animation: {
      'shimmer':      'shimmer 1.5s infinite',
      'float':        'float 3s ease-in-out infinite',
      'pulse-glow':   'pulse-glow 2s ease-in-out infinite',
      'slide-up':     'slide-up 0.4s ease-out',
      'gradient-shift':'gradient-shift 4s ease infinite',
      'speaking-ring':'speaking-ring 2s ease-out infinite',
    },
    borderRadius: {
      'glass': '16px',
    },
    backdropBlur: {
      'glass': '12px',
    }
  }
}
```
