---

## **React & DOM Fundamentals**

- The DOM (Document Object Model) is an object representation of the HTML elements.
- **imperative** **programming:** writing the steps for **how** the user interface should be updated
- pieces of information as properties to React components. These are called `props`

---

## **Server Components vs Client Components**

- **Server Components** are for **Data and Structure**
    
    **Client Components** are for **Interactivity and Events**
    
- just move that component using useState etc. to client side

---

## **Next.js Pre-rendering & Hydration**

- **Pre-rendering Mechanism:** Next.js generates HTML for every page in advance on the server, replacing client-side construction to boost performance and SEO.
- **The Hydration Lifecycle:** The browser first delivers static HTML for instant visibility, then "hydrates" it with JavaScript to transform "dry" UI into a functional, "living" React application.

### **Two Forms of Pre-rendering**

- **Static Generation (SSG):** Generates HTML once at **build time**, reusing the same file for every request to ensure maximum speed.
    
    **The "Snapshot" Rule:** By default, Next.js captures your UI at build time. Since the code doesn't re-run, the content remains "frozen" even if your backend data changes.
    
- **Server-side Rendering (SSR):** Generates fresh HTML on **each request**, ideal for data that changes constantly.
    
    **Bypassing the Cache:** To serve fresh data instead of a snapshot, you must use `cache: 'no-store'` or `force-dynamic`, forcing the server to re-run functions on every visit.
    

---

### `getStaticProps` (static rendering with data): ❌ old way

Once `getStaticProps` fetches the data at build time for static content, Next.js does two specific things with it to make the page work:

### 1. The HTML "Bake"

Next.js renders your React component into a **static HTML file**.

### 2. The JSON "Snapshot"

This is the part most people miss. Next.js also saves a small **JSON file** containing the result of `getStaticProps`.

---

### What if the data changes?

Since the data is "frozen," if you update your database, your website **will not change** until one of two things happens:

| **Method** | **What Happens** |
| --- | --- |
| **Rebuild** | You manually trigger a new deployment (e.g., redeploying on Vercel). This runs `getStaticProps` again and "re-freezes" the new data. |
| **ISR** | You use **Incremental Static Regeneration**. You tell Next.js: "Re-fetch this data in the background at most once every 60 seconds." |

> The Bottom Line: For standard Static Generation, once the build is done, the data is set in stone. It's perfect for things that don't change every second, like blog posts, documentation, or product listings.
> 

Would you like to see how to add the `revalidate` property to make your "static" data update automatically without a full rebuild?

---

## **SWR (Stale-While-Revalidate)**

### **What is SWR?**

**SWR (Stale-While-Revalidate)** is a client-side strategy that:

- **Stale:** Displays cached data immediately for an instant UI.
- **While:** Background-fetches fresh data.
- **Revalidate:** Updates the UI once new data arrives.

### **SWR vs. Server Components**

While **Server Fetching** is best for SEO and initial page loads, **SWR** is used for interactive, user-specific data that updates after the page is open:

- **Real-time updates:** Notification bells or live counts.
- **Interactivity:** Search-as-you-type results.
- **Focus:** Refreshing data whenever the user returns to the tab.

---

## **React Vs Next.js Comparison**

| **Feature** | **Traditional React SPA** | **Next.js (Framework)** |
| --- | --- | --- |
| **Code Splitting** | **Manual:** You have to manually set up `React.lazy` and `Suspense` for every route. | **Automatic:** Every file in your `app` or `pages` folder is automatically its own chunk. |
| **Initial Load** | **Large:** The browser usually downloads the *entire* app before showing the first page. | **Small:** Only the code needed for the current page is loaded. |
| **Navigation** | **Reactionary:** It starts loading the next page *only after* you click the link. | **Proactive (Prefetching):** It loads the next page in the background *before* you even click. |
| **SEO** | **Poor:** Search engines see a "blank" HTML page until the JavaScript runs. | **Excellent:** Pages are pre-rendered on the server into full HTML. |
| **Routing** | Requires a library like `react-router-dom`. | **Built-in:** File-system based routing (no extra library needed). |
| **Performance** | Slower "Time to Interactive" as the bundle grows. | Near-instant page transitions due to prefetching and partial loading. |

| **Feature** | **React (Standard)** | **Next.js (The Points you mentioned)** |
| --- | --- | --- |
| **Code Splitting** | Manual (Hard to do) | **Automatic** (By route) |
| **Error Handling** | Whole app crashes | **Isolated Routes** |
| **Loading Speed** | Loads everything at once | **Only loads what's needed** |
| **Prefetching** | None (Wait for click) | **Background Loading** |

---

## **Why Node.js When Next.js Can Do Frontend and Backend**

### 1. Multi-Platform Support

A separate Node.js backend acts as a "Single Source of Truth," allowing one API to serve Web, Mobile, and third-party apps simultaneously, whereas Next.js logic is often coupled only to the web frontend.

### 2. Background Workers

Next.js is designed for quick cycles and often times out. A dedicated backend uses workers (like Celery/BullMQ) to handle heavy, long-running tasks—such as batch OCR processing—without interrupting the user experience.

### 3. Connection Pooling

Unlike serverless Next.js functions that can overwhelm a database with individual requests, a persistent Node.js server manages a "pool" of connections, ensuring database stability during high traffic.

### 4. Stateful Real-time Features

Next.js functions are short-lived and terminate after a response. Real-time tools like [**Socket.io**](http://socket.io/) require a persistent, "always-on" Node.js server to maintain the constant open connections necessary for live chat and updates.

---

## **Reserved Filenames**

| Filename | Type | Purpose |
| --- | --- | --- |
| `page.tsx` | UI | The unique content for a URL. |
| `layout.tsx` | UI | Shared UI (Sidebar, Navbar) that persists across navigation. |
| `loading.tsx` | UI | Show a spinner while `page.tsx` loads data. |
| `error.tsx` | UI | Show a friendly error message if `page.tsx` crashes. It needs to be a Client Component. |
| `not-found.tsx` | UI | Custom 404 page. |
| `template.tsx` | UI | Wrapper that remounts on every navigation (rare). |
| `route.ts` | API | Backend logic (Database, Auth) returning JSON. |

---

## **Layouts & Partial Rendering**

- One benefit of using layouts in Next.js is that on navigation, only the page components update while the layout won't re-render. This is called [partial rendering](https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating#4-partial-rendering)

```jsx
export default function RootLayout
({ children }: { children: React.ReactNode })
```

since in JavaScript, the pattern is **`{ oldName: newName }`**.  for destructuring, we have to use above code: for destructuring children property and it should be of type: { children: React.ReactNode } as their key value should be of this type…

---

## **Routing & Dynamic Segments**

- Dynamic segment:

```tsx
// app/blog/[slug]/page.js
export default function BlogPost({ params }) {
  // params will be { slug: 'post-1' } for the URL /blog/post-1
  const { slug } = params;
	...
}
```

**multiple segments:** **`app/blog/[year]/[month]/[day]/page.js`**

```tsx
export default function Page({ params }) {
// params is { year: '2023', month: '10', day: '15' }
const { year, month, day } = params;
}
```

### **Catch-all Routes** `app/posts/[...id]/page.js`

**`[...id]`** handles multiple URL levels like `/posts/a/b/c` in one file.

- **Params:** `id` is an **array**: `['a', 'b', 'c']`
- **Static Generation:** `generateStaticParams` returns array of strings for the key

```jsx
export async function generateStaticParams() {
  return [{ id: ['a', 'b', 'c'] }]; // Pre-renders /posts/a/b/c
}
export default async function Page({ params }) {
  const { id } = await params; // id is ['a', 'b', 'c']
  return <h1>Path: {id.join('/')}</h1>;
}
```

- https://nextjs.org/learn/dashboard-app/streaming#streaming-a-component

Route groups in picture:

route-group.avif

---

## **route.js (API Routes)**

creates RESTful endpoints that handle multiple HTTP methods (GET, POST, DELETE) for one URL, keeping APIs organized.

**One URL, Multiple Actions**
Use one folder `app/api/user/` with single `route.js` instead of separate folders per action.

```jsx
// app/api/user/route.js
import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({ name: "John Doe" });
}

export async function POST(req) {
  const data = await req.json();
  return NextResponse.json({ message: `User ${data.name} saved!` });
}

export async function DELETE() {
  return NextResponse.json({ message: "User deleted" });
}
```

**Key Points:**

- Method-Based Routing: Next.js calls function matching request type
- Must name it `route.js` : API Endpoints (Data) - can't coexist with `page.js` : UI Pages (Components)
- Uses standard Web Request/Response APIs
- Server-side only - safe for secrets

**Using in Client Components:**

```jsx
'use client'

// GET
const loadData = async () => {
  const res = await fetch('/api/user');
  const data = await res.json();
};

// POST
const saveUser = async () => {
  await fetch('/api/user', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: "Alice" }),
  });
};
```

**Summary:**

- `method` in `fetch()` determines which function runs
- URL matches folder path (`app/api/auth/route.js` → `/api/auth`)
- Server-side execution keeps API keys secure

---

## **Navigation (Link, useRouter, redirect)**

### **Imports Summary Table**

| **Feature** | **Import Path** | **Context** | **Common Use Case** |
| --- | --- | --- | --- |
| **`<Link>`** | `next/link` | Client & Server | Clicking a navigation menu or anchor. |
| **`useRouter`** | `next/navigation` | **Client Only** | Navigating after an `onClick` or logic. |
| **`redirect`** | `next/navigation` | **Server Only** | Moving users after a Server Action (e.g., Save). |

### **Code Example**

**1. Client Side (`useRouter` & `Link`)**

```tsx
'use client';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

export default function ClientNav() {
  const router = useRouter();

  return (
    <div>
      <Link href="/dashboard">Go to Dashboard</Link>
      <button onClick={() => router.push('/settings')}>Settings</button>
    </div>
  );
}
```

**2. Server Side (`redirect`)**

```tsx
import { redirect } from 'next/navigation';

export async function createInvoice(formData: FormData) {
  // Logic to save to database...

  redirect('/invoices'); // Moves user after server logic is done: 
}
```

- `redirect` to redirect the user to a new page (absolute path NOT relative to current path or file)
- What does Next.js do when a <Link> component appears in the browser's viewport in a production environment?
    
    Next.js automatically prefetches the code for the linked route in the background. By the time the user clicks the link, the code for the destination page will already be loaded in the background, and this is what makes the page transition near-instant!
    

---

## **Suspense & Streaming**

fallback: jab tak RevenueChart load ni hota tab rak fallback ka saaman dikha

```tsx
<Suspense fallback={<RevenueChartSkeleton/>}>
  <RevenueChart />
</Suspense>
```

A `<Suspense>` wrapper around multiple components works like `Promise.all`: the fallback UI remains visible until **all** nested async components have finished loading, regardless of whether some are ready sooner than others.

Move data fetching down to the specific components that use it to create granular Suspense boundaries. This enables individual component streaming and prevents UI blocking.

---

## **Code Splitting**

in Next.js automatically breaks your application into smaller "chunks" (JavaScript bundles) instead of one massive file.

### How it Works

- **Route-Based:** By default, Next.js only loads the code required for the current page. Navigating to `/dashboard` won't load the code for `/settings`.
- **Component-Based:** You can manually split large or "heavy" components using **Dynamic Imports** (`next/dynamic`).

### Why it Matters

- **Faster Loads:** Users download significantly less JavaScript on the initial visit.
- **Better Performance:** Reduces browser parsing and execution time, improving your Core Web Vitals (like LCP and TBT).

### Manual Implementation

To split a specific component (e.g., a heavy map or editor):

```tsx
import dynamic from 'next/dynamic';

const HeavyChart = dynamic(() => import('@/components/HeavyChart'), {
  loading: () => <p>Loading...</p>,
});
```

---

## **Error Handling (error.tsx, not-found.tsx)**

**`not-found.tsx`** handles intentional cases where data is missing (via `notFound()`), while **`error.tsx`** is a safety net for unintentional code crashes.

If both exist, `notFound()` takes precedence, ensuring a specific "missing" message appears instead of a generic "application error."

The `error.tsx` file serves as a catch-all for unexpected errors and allows you to display a fallback UI to your users.

---

## **Server Actions & Data Mutation**

- `React Server Actions` allow you to run asynchronous code directly on the server. They eliminate the need to create API endpoints to mutate your data. https://nextjs.org/learn/dashboard-app/mutating-data

---

## **Performance Concepts**

- A `request waterfall` is a web performance issue where network requests, such as API calls or asset loads, execute in a serial, sequential chain rather than in parallel.
- Debouncing prevents a new database query on every keystroke, thus saving resources.

---

## **Image & Link Components**

- <Image /> instead of <img /> from html from the next/image optimize, lazy loading, automatic sizing, responsive image, aspect ration, auto layout shifting, `<Image .../>`

---

## **CSS & Styling**

- benefit of using CSS modules: **Provide a way to make CSS classes locally scoped to components by default, reducing the risk of styling conflicts.**
- const pathname = usePathname();

```jsx
className={clsx(
  'flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-2 md:px-3',
  {
    'bg-sky-100 text-blue-600': pathname === link.href,
  },
)}
```

---

## **Event Handlers**

### When to Use `onClick={handleClick}` vs `onClick={() => handleClick()}`

1. **Use the function name directly:**

`onClick={handleClick}  // ✅ Preferred`

- More efficient - doesn't create a new function on every render
- Use when you don't need to pass arguments
1. **Use arrow function when:**

```jsx
onClick={() => handleClick(id)}  // Pass arguments
onClick={() => console.log('hi')} // Inline simple logic
onClick={(e) => handleClick(e, id)} // Pass event + arguments
```

| **Code** | **Action** | **Result** |
| --- | --- | --- |
| **`{handleSubmit}`** | Passing a reference | Works perfectly on submission. |
| **`{handleSubmit()}`** | Immediate execution | ❌ Crashes or runs at the wrong time as soon as the component is rendered. |

```tsx
<input
    className="..."
    placeholder={placeholder}
    onChange={(e) => {handleSearch(e.target.value);}}
/>
```

---

## **Seeding & Database**

- Seeding: **the process of populating a database or application with initial, sample, or dummy data**

---

## **Syntax & Imports**

- syntax:
    - export default function RootLayout({ children })
    - import { useState } from 'react';
    - import Image from 'next/image';
    - import Link from 'next/link'; `<Link href="…"> </Link>`
    - ***import*** { *usePathname* } ***from*** '*next/navigation*'; `const pathname = usePathname();`
    - import type { User } from '@/app/lib/definitions';
    - import Script from 'next/script'; (**Loading third-party scripts)**

---

## **TypeScript Basics**

- **`:` (Colon)**: Labels a variable (e.g., `name: string`).
- **`{}` (Curly Braces)**: Defines an object's structure (e.g., `{ id: number }`).
- **`<>` (Angle Brackets)**: Used for "containers" (Generics) to describe what's inside a wrapper like a `Promise` or `Array` (e.g., `Promise<string>`).

**Summary:** Use `:` to define **what** a variable is, and `<>` to define what a container **holds**.

- `?` is for the optional

```tsx
export default async function Page(props: {
  searchParams?: Promise<{
    query?: string;
    page?: string;
  }>;
}) {
```

**The pattern is:** `({ destructured, params }: { type: definition })`

e.g.

```tsx
function greet({ name, age }: { name: string; age: number }) {
  console.log(name, age);
}
```

---

## **TypeScript Generics**

```tsx
// T is a generic type variable
function identity<T>(arg: T): T {
  return arg;
}
let output = identity<string>("myString"); // Explicitly sets T to string
let output2 = identity(123); // TypeScript infers T as number
```

### **TypeScript generics** - a way to write reusable code that works with multiple types while maintaining type safety.

**Breaking it down:**

```tsx
function identity<T>(arg: T): T
```

- `<T>` declares a **type variable** (placeholder for any type)
- `arg: T` means the parameter will be of type T
- `: T` means the function returns the same type T

**The function simply returns whatever you pass in, but preserves the type.**

```tsx
let output = identity<string>("myString");
```

- Explicitly tells TypeScript that `T = string`
- Returns a string

---

## **TypeScript Type Definitions**

```tsx
export type State = {
  errors?: {
    customerId?: string[]; ...
  };
  message?: string | null;
};
```

---

## **TypeScript Union Types & JavaScript Operators**

**`|` - Type Union (TypeScript only)**

```tsx
// Means the variable can be EITHER a number OR a string
const createPageURL = (pageNumber: number | string) => {
  // pageNumber can be 1 or "1"
}
```

| **Feature** | **Syntax** | **Context** | **Meaning** |
| --- | --- | --- | --- |
| **TS Union (OR)** | `string | number` | Type Definition |
| **JS Logical OR** | `a |  | b` |
| **JS Logical AND** | `a && b` | Logic/Code | "If **a** is true, then do/use **b**." |

---

## **JavaScript Functions & Hoisting**

### "Hoisting" (The Main Difference)

- **`function createPageURL(...)`**: These are "hoisted." You can call the function at the top of your file even if it is defined at the bottom.
- **`const createPageURL = ...`**: These are not. You must define the variable **before** you try to use it.

---

## **External Resources**

https://next-auth.js.org/getting-started/example

http://zod.dev/

https://nextjs.org/learn