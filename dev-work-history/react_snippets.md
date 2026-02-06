## useState

```tsx
'use client';
import { useState } from 'react';

function Counter() {
  // 1. STATE IS READ-ONLY: Never do count = count + 1
  const [count, setCount] = useState(0);

  // 2. FUNCTION REFERENCE: No () means "run this later when clicked"
  const handleReset = () => setCount(0);
  
  // 2. ARRAY UPDATE: Create NEW array with [...] (Spread)
  // Logic: Unpack old items into a new "box", then add the new one
  const addItem = () => setItems(prev => [...prev, 'Banana']);
  
  // 3. OBJECT UPDATE: Create NEW object with {...} (Spread)
  // Logic: Copy all old fields first, then overwrite only what's changing
  const updateName = () => setUser(prev => ({ ...prev, name: 'Admin' }));

  return (
    <div>
      <p>Count: {count}</p>

      {/* 3. WRAPPER FUNCTION: Used to pass data without running immediately */}
      <button onClick={() => setCount(count + 5)}>+5</button>

      {/* 4. SNAPSHOT vs FUNCTIONAL:
          - count + 1: Uses value from "now" (can miss fast clicks) captures last rendered value
          - prev => prev + 1: Uses "live" latest value (bulletproof) */}
      <button onClick={() => setCount(count + 1)}>Snapshot</button> ❌
      
      <button onClick={() => setCount(prev => prev + 1)}>Functional</button> ✅
      <button onClick={updateName}>Change Object Name</button> ✅
      <button onClick={addItem}>Add Array Item</button> ✅

      {/* 5. REFERENCE CALL: No arguments needed, just pass the name */}
      <button onClick={handleReset}>Reset</button>

      {/* ❌ AVOID THIS: onClick={setCount(1)} 
          This runs during render -> updates state -> re-renders -> LOOP CRASH */}
    </div>
  );
}

// 6. OBJECT UPDATES: Always spread (...) to create a NEW object address
// ✅ Correct: setUser({ ...user, name: 'Bob' })
// ❌ Wrong: user.name = 'Bob'; setUser(user);
```

## useEffect

```tsx
'use client';
import { useEffect, useState } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  // Runs after EVERY render: if added setCount(+1) in this it's infinite render
  useEffect(() => {
    console.log('Rendered');
  });

  // Runs only on MOUNT (empty array): only 1st time
  useEffect(() => {
    console.log('Mounted');
  }, []); // include dependacy array have the states if those changes then add

  // Runs when `count` CHANGES
  useEffect(() => {
    console.log('Count changed:', count);
  }, [count]);

  // Cleanup function
  useEffect(() => {
    const timer = setInterval(() => console.log('tick'), 1000);
    
    return () => clearInterval(timer); // Cleanup on unmount
  }, []);

  return <div>{count}</div>;
}
```

- Axios automatically converts responses to JSON objects. Unlike `fetch`, it handles parsing for you. You simply access the data via `response.data`. No need for a `.json()` step.
    
    ```tsx
    const res = await fetch('/api/user');
    const data = await res.json(); // YOU must parse it manually
    ```
    
    ```tsx
    const res = await axios.get('/api/user');
    const data = res.data; // IT IS ALREADY AN OBJECT
    ```
    

## useRef:

**mutating (changing) its `.current` value does not trigger a re-render in React**

```tsx
'use client';
import { useRef } from 'react';

// Accessing DOM element
function TextInput() {
  const inputRef = useRef(null);

  const focusInput = () => {
	  inputRef.current = 'shome';
    inputRef.current.focus();
  };

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
}
```

## useContext

`useContext` is React’s way of avoiding **"Prop Drilling"** (passing data through 5 components just to reach the last one). It creates a "Global Broadcast" that any component can tune into.

### **The 3 Steps of Context**

1. **Create:** Make the "Context Object."
2. **Provide:** Wrap your app (or a section) in a Provider and give it a value.
3. **Consume:** Use the `useContext` hook in any child component to grab that value.

---

### **The Code Syntax (the ts would be more complex)**

```jsx
'use client';
import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext(null);

// Create a Provider component that accepts children
export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export default function App() {
  return (
    <ThemeProvider>
      <Page />
    </ThemeProvider>
  );
}

function Page() {
  return (
    <div>
      <h1>My App</h1>
      <ThemeButton />
    </div>
  );
}
```

```tsx
function ThemeButton() {
  // 3. CONSUME: No props needed! Just grab it from the "air"
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <button 
      onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
      style={{ background: theme === 'light' ? '#fff' : '#333', color: theme === 'light' ? '#000' : '#fff' }}
    >
      Toggle to {theme === 'light' ? 'Dark' : 'Light'} Mode
    </button>
  );
}
```

### **Important Notes for Next.js**

- **Context needs `'use client'`:** Because Context is a dynamic React feature that relies on hooks, the file where you create the Provider must be a Client Component.
- **Don't overdo it:** Context is great for global things like **User Authentication**, **Themes**, or **Cart Items**. Don't use it for every little piece of state, or your app will become hard to debug.
- **Provider Placement:** Usually, in Next.js, you create a dedicated "Providers" file and wrap the `{children}` in your `layout.tsx`.

---

## useMemo

**optimizes performance by memoizing (caching) the result of expensive calculations between re-renders**

```jsx
// Syntax: const value = useMemo(() => function, [dependencies])

const totalAmount = useMemo(() => {
  return price * quantity; // Yeh calculation sirf tab hogi jab price ya quantity badlegi
}, [price, quantity]);
```

---

## **`memo` + `useCallback` (The "Pair" for Functions)**

Yeh tab use hota hai jab tum Parent se Child mein function bhejte ho.

**Step A: Child ko `memo`** stops the Child from re-rendering. 

```jsx
import { memo } from 'react';

const MyChild = memo(({ onClick }) => {
  console.log("Child Rendered");
  return <button onClick={onClick}>Click Me</button>;
});
```

**Step B: Parent mein function ko `useCallback` do (The ID Card)**

```jsx
import { useCallback, useState } from 'react';

function Parent() {
  const [count, setCount] = useState(0);

  // Function ka address lock kar diya
  const handleClick = useCallback(() => {
    console.log("Button clicked!");
  }, []); // [] matlab address kabhi nahi badlega

  return (
    <>
      <MyChild onClick={handleClick} /> 
      <button onClick={() => setCount(count + 1)}>Re-render Parent</button>
    </>
  );
}
```

---

### **Simple Terms mein Difference Table**

| **Concept** | **Kya karta hai?** | **Simple Syntax** |
| --- | --- | --- |
| **`memo`** | Component ko "freeze" kar deta hai. | `memo(Component)` |
| **`useCallback`** | Function ka address "freeze" kar deta hai. | `useCallback(() => {...}, [])` |
| **`useMemo`** | Kisi calculation ka result "freeze" kar deta hai. | `useMemo(() => a + b, [])` |

---

### **Golden Rule Yaad Rakho:**

1. **Sirf Data (Array/Object) bachaana hai?** -> Use `useMemo`.
2. **Child Component ka re-render rokna hai?** -> Use `memo`.
3. **Child ko function bhej rahe ho aur re-render rokna hai?** -> Use **BOTH** (`memo` on child + `useCallback` on parent).

---