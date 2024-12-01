"use client";

import { useState, useEffect } from "react";

function useTheme() {
  const [theme, setTheme] = useState("dark");

  useEffect(() => {
    setTheme(window.localStorage.getItem("theme") || "dark");
  }, []);

  useEffect(() => {
    if (theme === "dark") {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
    window.localStorage.setItem("theme", theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
  };

  return {
    theme,
    toggleTheme,
  };
}

export default useTheme;
