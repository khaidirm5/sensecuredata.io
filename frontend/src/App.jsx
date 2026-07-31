import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

import MainLayout from "./components/layout/MainLayout";

function App() {
  return (
    <MainLayout>
      <div className="flex items-center justify-center min-h-screen">
        <h1 className="text-4xl font-bold text-blue-600">
          Sentinel Secure Data Intelligence Platform
        </h1>
      </div>
    </MainLayout>
  );
}

export default App;